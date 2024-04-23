<script lang="ts">
  import { Router, Route } from "svelte-routing";
  import Home from "./pages/home/Home.svelte";
  import KDM from "./pages/kdm/KDM.svelte"
  import Scheduele from "./pages/schedule/Schedule.svelte"

  export let url = "";
</script>

<Router {url}>
  <Route path="/" component={Home}></Route>
  <Route path="/kdm" component={KDM}></Route>
  <Route path="/schedule" component={Scheduele}></Route>
</Router>