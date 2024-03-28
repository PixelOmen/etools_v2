<script lang="ts">
  import { Router, Route } from "svelte-routing";
  import Home from "./pages/home/Home.svelte";
  import Another from "./pages/another/Another.svelte";
  import KDM from "./pages/kdm/KDM.svelte"

  export let url = "";
</script>

<Router {url}>
  <Route path="/another" component={Another}></Route>
  <Route path="/" component={KDM}></Route>
</Router>