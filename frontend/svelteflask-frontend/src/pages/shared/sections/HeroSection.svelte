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
      /* border: solid 1px red; */
      background: radial-gradient(ellipse at 80% -10%, #163139 0%, #12232E 40%, transparent),
                  radial-gradient(ellipse at 10% 100%, #163139 0%, #12232E 40%);
      background-size: cover;
      background-position: center;
      background-repeat: no-repeat;
      box-sizing: content-box;
      padding-top: 30px;
    }
    section {
      /* border: solid 1px blue; */
      width: 90%;
      margin-left: auto;
      margin-right: auto;
      padding-top: 50px;
      padding-bottom: 30px;
    }
  </style>
  