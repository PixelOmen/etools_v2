<script lang="ts">
  import HeroSection from "./components/sections/HeroSection.svelte";

  fetch('/api/test')
    .then(response => response.text())
    .then(data => console.log(data))
</script>

<main>
  <HeroSection>
    <div class="test"></div>
  </HeroSection>
</main>

<style>
  .test {
    height: 300px;
  }
</style>