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
      background-image: url('../../assets/Hero_BG.png');
      background-size: cover;
      background-position: center;
      background-repeat: no-repeat;
      /* height: 300px; */
    }
  </style>
  