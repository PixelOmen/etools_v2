<script lang="ts">
  import { Router, Route } from "svelte-routing";
  import Home from "./pages/home/Home.svelte";
  import Another from "./pages/another/Another.svelte";
  import KDM from "./pages/kdm/KDM.svelte"

  export let url = "";
</script>

<Router {url}>
  <Route path="/kdm" component={KDM}></Route>
  <Route path="/" component={Home}></Route>
</Router>