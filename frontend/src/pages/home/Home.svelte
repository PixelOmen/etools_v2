<script lang="ts">
    import HeroSection from "../shared/sections/HeroSection.svelte";
    import LoadingIcon from "../shared/ui/LoadingIcon.svelte";
    import FooterLinks from "../shared/sections/FooterLinks.svelte";
    import HomeCard from "./HomeCard.svelte";
    import onyx from "../../assets/onyx.jpg";
</script>

<main>
    <div class="hidden">
        <LoadingIcon width="30px" height="30px" />
    </div>
    <HeroSection paddingBottom="0px">
        <div class="sectionContainer" id="mainSection">
        </div>
    </HeroSection>
    <section class="secondarySection sectionContainer">
        <div id="imgContainer" style="background-image: url({onyx});"></div>
        <HomeCard header="Post-Production Tools">
            Here you'll find many essential tools in one convenient place.
            Adjust timecodes, validate Dolby Vision XMLs, create KDMs for
            DCPs, and more. This platform is here to support you and your
            worlflow.
        </HomeCard>
    </section>
    <footer class="footerSection">
        <div class="footerContainer">
            <hr />
            <FooterLinks />
        </div>
    </footer>
</main>

<style>
    .hidden {
        display: none;
    }
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
        border-bottom: 2px solid #a46d39;
        overflow: hidden;
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

    .secondarySection {
        height: 200px;
    }

    .footerSection {
        background: radial-gradient(
                ellipse at 40% -400%,
                rgb(36, 51, 78) 0%,
                #0e1f25 70%,
                transparent 100%
        ), linear-gradient(#12232e 0%, #0e1f25 10%);
    }

    .footerContainer {
        width: 80%;
        padding-top: 50px;
        padding-bottom: 10px;
        margin-left: auto;
        margin-right: auto;
    }
</style>
