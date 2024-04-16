<script>
    import NavBar from '../nav/NavBar.svelte'
    export let paddingTop = "60px";
    export let paddingBottom = "30px";
</script>

<main>
    <NavBar/>
    <section class="container" style="
      padding-top: {paddingTop};
      padding-bottom: {paddingBottom};
    ">
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
  }
</style>
  