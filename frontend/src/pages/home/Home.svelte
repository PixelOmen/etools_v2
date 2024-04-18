<script lang="ts">
    import HeroSection from "../shared/sections/HeroSection.svelte";
    import FooterLinks from "../shared/sections/FooterLinks.svelte";
    import HomeCard from "./HomeCard.svelte";
    import onyx from "../../assets/onyx.jpg";
</script>

<main>
    <HeroSection paddingBottom="60px">
        <div class="sectionContainer" id="mainSection">
        </div>
    </HeroSection>
    <section class="secondarySection sectionContainer">
        <div id="imgContainer" style="background-image: url({onyx});"></div>
        <div id="mainCard">
            <HomeCard header="Post-Production Tools">
                Here you'll find many essential tools in one convenient place.
                Adjust timecodes, validate Dolby Vision XMLs, create KDMs for
                DCPs, and more. This platform is here to support you and your
                worlflow.
            </HomeCard>
        </div>
    </section>
</main>
<FooterLinks />


<style>
    main {
        min-width: 900px;
    }
    .sectionContainer {
        position: relative;
        display: flex;
        width: 100%;
        margin-left: auto;
        margin-right: auto;
        padding-bottom: 10px;
        justify-content: center;
        overflow: hidden;
    }
    .secondarySection {
        border-top: 2px solid #a46d39;
        border-bottom: 2px solid #a46d39;
        height: 250px;
    }

    #mainCard {
        margin-top: 20px;
    }

    #imgContainer {
        z-index: 0;
        position: absolute;
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        width: 100%;
        height: 100%;
        filter: blur(10px) brightness(65%);
    }
</style>
