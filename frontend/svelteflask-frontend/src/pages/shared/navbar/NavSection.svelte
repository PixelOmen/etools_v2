<script context="module" lang='ts'>
    import type { AnchorData } from './NavAnchor.svelte'
    export type SectionLinks = AnchorData[];
</script>

<script lang="ts">
    import { createEventDispatcher } from 'svelte';
    import NavAnchor from './NavAnchor.svelte';

    export let sectionVisible: boolean = false;
    export let sectionData: SectionLinks;
    export let displayText: string;

    const dispatch = createEventDispatcher();

    function toggleSection(): void {
        dispatch('navSectionOpen', displayText)
    }
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
        padding: 5px 10px;
        cursor: pointer;
        border: none;
        outline: none;
        background: none;
        background-color: rgba(225, 225, 225, 0);
        border-radius: 20px;
        color: rgb(225, 225, 225);
        font-size: inherit;
        font-family: inherit;
        transition: color 0.3s;
        transition: background-color 0.3s;
        font-size: 14pt;
    }
    button:hover {
        border-radius: 20px;
        background-color: #88dfef1e;
    }
    button:focus {
        background-color: rgba(225, 225, 225, 0);
    }

    .navSection {
        position: relative;
    }

    ul {
        position: absolute;
        min-width: 80%;
        padding: 10px;
        background-color: #88dfef1e;
        border-radius: 5px;
        flex-direction: column;
        justify-content: space-between;
        gap: 10px;
    }
</style>