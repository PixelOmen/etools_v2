<script>
    import NavBar from '../navbar/NavBar.svelte'
</script>

<main>
    <NavBar/>
    <slot></slot>
</main>
  
  <style>
    main {
      border: solid 1px red;
      background: radial-gradient(ellipse at 80% -10%, #163139 0%, #12232E 40%, transparent),
      radial-gradient(ellipse at 10% 100%, #163139 0%, #12232E 40%);
      background-size: cover;
      background-position: center;
      background-repeat: no-repeat;
    }
  </style>
  