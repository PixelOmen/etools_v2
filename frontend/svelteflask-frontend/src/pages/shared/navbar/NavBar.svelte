<script lang='ts'>
    import { onMount, onDestroy } from 'svelte';
    import logo from '../../../assets/logo.ico';
    import NavSection from './NavSection.svelte';
    import type { SectionLinks } from './NavSection.svelte';

    type AllNavSections = {
        sectionName: string;
        contents: SectionLinks;
    }[];

    let allsections: AllNavSections = [];
    fetch("/api/nav")
        .then(res => res.json())
        .then(output => allsections = output)

    let openSection: string|null = null;
    function setOpenSection(e: CustomEvent): void {
        openSection = openSection === e.detail ? null : e.detail;
    }

    let navElement: HTMLElement;
    function clickOutside(e: Event): void {
        if (navElement && !navElement.contains(e.target as Node)) {
            openSection = null;
        }
    }

    onMount(() => {
        window.addEventListener('click', clickOutside)
    })
    onDestroy(() => {
        window.removeEventListener('click', clickOutside)
    })
</script>

<header class="container">
    <a href="/">
        <img src={logo} alt="Main Logo" width="75" height="75">
    </a>
    <nav bind:this={navElement}>
        <ul>
            {#each allsections as navsection}
                <NavSection
                    displayText={navsection.sectionName}
                    sectionData={navsection.contents}
                    sectionVisible={openSection === navsection.sectionName}
                    on:navSectionOpen={setOpenSection}
                />
            {/each}
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
    ul {
        display: flex;
    }
</style>