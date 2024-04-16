<script lang="ts">
  import HeroSection from "../shared/sections/HeroSection.svelte";
  import LoadingIcon from '../shared/ui/LoadingIcon.svelte';
  import FooterLinks from '../shared/sections/FooterLinks.svelte';
  import HomeCard from "./HomeCard.svelte";
  import onyx from "../../assets/onyx.jpg"
</script>

<main>
  <div class="hidden">
    <LoadingIcon width="30px" height="30px"/>
  </div>
  <HeroSection>
      <div class="sectionContainer" id="mainSection">
        <HomeCard header="Welcome to Our Toolkit" imgURL={onyx}>
            Here you'll find many essential tools in one convenient place. Adjust timecodes, validate Dolby Vision XMLs, 
            create KDMs for DCPs, and more. This platform is here to support your worlflow with straightforward solutions.
        </HomeCard>
      </div>
  </HeroSection>
  <footer class="footerSection">
      <div class="footerContainer">
          <hr>
          <FooterLinks/>
      </div>
  </footer>    
</main>

<style>
  .hidden {
    display: none;
  }
  .sectionContainer {
    position: relative;    
    display: flex;
    width: 80%;
    margin-left: auto;
    margin-right: auto;
    justify-content: center;
  }


  .footerSection {
      background: linear-gradient(#12232E 0%, #0e1f25 100%, transparent);   
  }

  .footerContainer {
      width: 80%;
      padding-top: 50px;
      padding-bottom: 10px;
      margin-left: auto;
      margin-right: auto;
  }    
</style>