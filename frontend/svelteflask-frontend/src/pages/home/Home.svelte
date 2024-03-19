<script lang="ts">
  import HeroSection from "../shared/sections/HeroSection.svelte";
  
  fetch('/api')
    .then(response => response.text())
    .then(data => console.log(data))
</script>

<main>
  <HeroSection>
    <div class="test">This is the main</div>
  </HeroSection>
</main>

<style>
  .test {
    height: 300px;
  }
</style>