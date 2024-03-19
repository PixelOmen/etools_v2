<script lang='ts'>
    import logo from '../../../assets/logo.ico';
    import NavSection from './NavSection.svelte';
    import type { SectionData } from './NavSection.svelte';

    let test: SectionData = [
        {
            url: "/another",
            displayName: "Some Section"
        }
    ]
</script>

<header class="container">
    <img src={logo} alt="Main Logo" width="75" height="75">
    <nav>
        <ul>
            <NavSection displayText="SomeButton" sectionData={test}></NavSection>
        </ul>
    </nav>
</header>

<style>
    .container {
        display: flex;
        justify-content: space-between;
        align-items: center;
        width: 90%;
        border: solid 1px blue;
        margin-left: auto;
        margin-right: auto;
    }
    nav {
        margin-right: 3%;
    }
</style>