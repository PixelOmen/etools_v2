<script lang="ts">
  import { Router, Link, Route } from "svelte-routing";
  import Home from "./pages/home/Home.svelte";
  import Another from "./pages/another/Another.svelte";

  export let url = "";
</script>

<Router {url}>
  <Route path="/another" component={Another}></Route>
  <Route path="/" component={Home}></Route>
</Router>