<script context="module" lang='ts'>
    import type { AnchorData } from './NavAnchor.svelte'
    export type SectionData = AnchorData[];
</script>

<script lang="ts">
    import NavAnchor from './NavAnchor.svelte';
    let sectionVisible: boolean = false;

    function toggleSection(): void {
        sectionVisible = sectionVisible ? false : true;
    }

    export let sectionData: SectionData;
    export let displayText: string;
</script>

<li class="navSection">
    <button on:click={toggleSection}>{displayText}&#9207;</button>
    <ul style="display: {sectionVisible ? 'flex' : 'none'}">
        {#each sectionData as data}
            <NavAnchor {data}></NavAnchor>
        {/each}
    </ul>
</li>

<style>
    button {
        cursor: pointer;
        border: none;
        outline: none;
        background: none;
        color: rgb(225, 225, 225);
        font-size: inherit;
        font-family: inherit;
        transition: color 0.3s;
    }
    button:hover {
        color: rgb(179, 179, 179);
    }

    .navSection {
        position: relative;
    }

    ul {
        position: absolute;
        border: solid 1px purple;
        width: max-content;
        padding: 10px;
    }
</style>