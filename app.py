from flask import Flask, send_from_directory, redirect, url_for
from flask_cors import CORS, cross_origin
from flask_discord import DiscordOAuth2Session, requires_authorization, Unauthorized
import apsw
import random
"""
users(id INT PRI KEY, admin INT, banned INT, verified INT, name TEXT)
survey(uid INT, qid INT, rating INT, uid REFS users(id), PRI KEY(uid, qid))
images(id INT PRI KEY, gid INT, idx INT, gid REFS generations(id), UNIQUE(gid,idx))
ratings(uid INT, iid INT, rating INT, uid REFS users(id), iid REFS images(id), PRI KEY(uid, iid))

get_next_batch() -> [(img_id, img_url)]
set_rating(img_id, int) -> confirmation
"""

app = Flask(__name__)
cors = CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"
app.config["DISCORD_CLIENT_ID"] = 490732332240863233  # Discord client ID.
app.config["DISCORD_CLIENT_SECRET"] = ""  # Discord client secret.
app.config["DISCORD_REDIRECT_URI"] = ""  # URL to your callback endpoint.
app.config["DISCORD_BOT_TOKEN"] = ""  # Required to access BOT resources.

app.secret_key = b"random bytes representing flask secret key"

discord = DiscordOAuth2Session(app)

con = apsw.Connection("dump.db")
cur = con.cursor()


def to_file(g, p, i):
  return f"""{g}_{p.replace(" ","_").replace("/","_")}_{i}.png"""


def get():
  uid = 914036802438975538
  ids_and_files = []
  with con:
    iids = tuple(map(lambda x: x[0], con.cursor().execute(f"select iid from ratings where uid = {uid}").fetchall()))
    for id, gid, idx in con.cursor().execute(
        f"select * from images where id not in {iids} order by random() limit 100"):
      (p,) = con.cursor().execute(f"select prompt from generations where id = {gid}").fetchone()
      ids_and_files.append((id, to_file(gid, p, idx)))
  return ids_and_files


#for id, file in get():
#  print(id, file)


def welcome_user(user):
  dm_channel = discord.bot_request("/users/@me/channels", "POST", json={"recipient_id": user.id})
  return discord.bot_request(
      f"/channels/{dm_channel['id']}/messages", "POST", json={"content": "Thanks for authorizing the app!"})


@app.route("/login/")
def login():
  return discord.create_session()


@app.route("/callback/")
def callback():
  discord.callback()
  user = discord.fetch_user()
  welcome_user(user)
  return redirect(url_for(".me"))


@app.errorhandler(Unauthorized)
def redirect_unauthorized(e):
  return redirect(url_for("login"))


@app.route("/me/")
@requires_authorization
def me():
  user = discord.fetch_user()
  return f"""
    <html>
        <head>
            <title>{user.name}</title>
        </head>
        <body>
            <img src='{user.avatar_url}' />
        </body>
    </html>"""


@app.route("/")
def base():
  return send_from_directory("./client/dist", "index.html")


@app.route("/rand")
@cross_origin()
def rand():
  return str(random.randint(0, 100))


@app.route("/<path:path>")
def home(path):
  return send_from_directory("./client/dist", path)
