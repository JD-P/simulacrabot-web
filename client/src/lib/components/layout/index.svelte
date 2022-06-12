<script lang="ts">
  import DefaultMetaTags from "./DefaultMetaTags.svelte";
  import Header from "./Header.svelte";
  import Footer from "./Footer.svelte";
</script>

<DefaultMetaTags />

<div class="min-h-screen">
  <Header />
  <main class="layout px-4 py-8">
    <slot />
  </main>
  <Footer />
</div>
