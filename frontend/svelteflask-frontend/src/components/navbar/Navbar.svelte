<script lang='ts'>
    import logo from '../../assets/logo.ico';
    import NavSection from './NavSection.svelte';
    import type { SectionData } from './NavSection.svelte';

    let test: SectionData = [
        {
            url: "test",
            displayName: "Some Section"
        }
    ]
</script>

<nav class="container">
    <img src={logo} alt="Main Logo" width="75">
    <NavSection displayText="SomeButton" sectionData={test}></NavSection>
</nav>

<style>
    .container {
        display: flex;
        width: 90%;
        border: solid 1px blue;
        margin-left: auto;
        margin-right: auto;
    }
</style>