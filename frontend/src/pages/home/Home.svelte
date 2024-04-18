<script lang="ts">
    import HeroSection from "../shared/sections/HeroSection.svelte";
    import FooterLinks from "../shared/sections/FooterLinks.svelte";
    import CenteredBanner from "../shared/sections/CenteredBanner.svelte";
    import onyx from "../../assets/onyx.jpg";
</script>

<main>
    <HeroSection paddingBottom="0px" paddingTop="120px">
        <CenteredBanner header="Post-Production Tools" bgimg={onyx}>
            Here you'll find many essential tools in one convenient place.
            Adjust timecodes, validate Dolby Vision XMLs, create KDMs for
            DCPs, and more. This platform is here to support you and your
            worlflow.
        </CenteredBanner>
    </HeroSection>
</main>
<FooterLinks />


<style>
    main {
        min-width: 900px;
    }
</style>
