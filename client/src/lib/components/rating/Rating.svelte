<script lang="ts">
  import Selection from "./Selection.svelte";
  const sels = [...Array(10).keys()].map((n) => "sel_" + n.toString());
  let num: number;
  const submit = (res: number) => {
    num = undefined;
    const tmp: HTMLInputElement = document.createElement("input");
    document.body.appendChild(tmp);
    tmp.focus();
    document.body.removeChild(tmp);
  };
  const handleKeydown = (event: KeyboardEvent) => {
    switch (event.key) {
      case "Enter":
        if (num !== undefined) {
          submit(num);
        }
        break;
      case "a":
      case "1":
        if (num == 1) {
          submit(num);
        } else {
          num = 1;
        }
        break;
      case "s":
      case "2":
        if (num == 2) {
          submit(num);
        } else {
          num = 2;
        }
        break;
      case "d":
      case "3":
        if (num == 3) {
          submit(num);
        } else {
          num = 3;
        }
        break;
      case "f":
      case "4":
        if (num == 4) {
          submit(num);
        } else {
          num = 4;
        }
        break;
      case "g":
      case "5":
        if (num == 5) {
          submit(num);
        } else {
          num = 5;
        }
        break;
      case "h":
      case "6":
        if (num == 6) {
          submit(num);
        } else {
          num = 6;
        }
        break;
      case "j":
      case "7":
        if (num == 7) {
          submit(num);
        } else {
          num = 7;
        }
        break;
      case "k":
      case "8":
        if (num == 8) {
          submit(num);
        } else {
          num = 8;
        }
        break;
      case "l":
      case "9":
        if (num == 9) {
          submit(num);
        } else {
          num = 9;
        }
        break;
      case ";":
      case "0":
        if (num == 0) {
          submit(num);
        } else {
          num = 0;
        }
        break;
    }
    if (num !== undefined) {
      document.getElementById(sels[num]).focus();
    }
  };
</script>

<svelte:window on:keydown={handleKeydown} />

<div>
  <h2 class="text-xl font-black">SimulacraBot Aesthetic Captions</h2>
  <br />
  <p>Please rate images according to how attractive you feel the image is.</p>
  <p><i>Consider rating images that contain text (such as watermarks) lower.</i></p>
  <br />
  <br />
  <p><b>Prompt:</b> filler for now.</p>
  <br />
  <br />
  <img
    alt=""
    class="mx-auto"
    style="height:300px"
    src="https://i.pinimg.com/736x/33/0b/96/330b96ac230146d5df366da858a00c80.jpg"
  />
  <br />
  <div class="inline-flex rounded-md shadow-sm" role="group">
    <p class="text-xl font-black p-4">Ugly.</p>
    <Selection num={1} letter="a" />
    <Selection num={2} letter="s" />
    <Selection num={3} letter="d" />
    <Selection num={4} letter="f" />
    <Selection num={5} letter="g" />
    <Selection num={6} letter="h" />
    <Selection num={7} letter="j" />
    <Selection num={8} letter="k" />
    <Selection num={9} letter="l" />
    <Selection num={0} letter=";" />
    <p class="text-xl font-black p-4">Wow!</p>
  </div>
  <br />
  <br />
  <div>
    <button
      id="submit"
      class="py-2 px-4 text-m font-medium text-white bg-gray-700 border-gray-600 hover:bg-gray-600 focus:bg-gray-600"
      >Submit</button
    >
    <br />
    <br />
    Or hit Enter.
    <br />
    Or double-tap your selection.
  </div>
</div>
