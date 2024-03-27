<script>
    import NavBar from '../navbar/NavBar.svelte'
</script>

<main>
    <NavBar/>
    <section class="container">
      <slot></slot>
    </section>
</main>
  
<style>
  main {
    background: radial-gradient(ellipse at 80% -10%, #163139 0%, #12232E 40%, transparent),
                radial-gradient(ellipse at 10% 100%, #163139 0%, #12232E 40%);
    padding-top: 30px;
  }
  section {
    margin-left: auto;
    margin-right: auto;
    padding-top: 50px;
    padding-bottom: 30px;
  }
</style>
  