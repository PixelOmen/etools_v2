<script lang="ts">
  import svelteLogo from './assets/svelte.svg'
  import viteLogo from '/vite.svg'
  import Navbar from './components/navbar/Navbar.svelte'

  fetch('/api/test')
    .then(response => response.text())
    .then(data => console.log(data))
</script>

<main>
  <Navbar/>
  <div class="main-section-container">
  </div>
</main>

<style>
  .main-section-container {
    /* display: flex; */
    border: solid 1px red;
    /* background-image: url('./assets/Hero_BG.png');
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat; */
    width: 100%;
    height: 200px;
    background-image: radial-gradient(ellipse 50% 100% at 50% -10%, #7889df50, #778ae800)
  }
</style>
