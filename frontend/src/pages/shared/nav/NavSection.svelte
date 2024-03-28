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
    
    let sectionUL: HTMLUListElement;
    $: {
        if (sectionUL) {
            if (sectionVisible) {
                sectionUL.classList.remove('hidden');
            } else {
                sectionUL.classList.add('hidden')
            }
        }
    }
</script>

<li class="navSection">
    <button on:click={toggleSection}>{displayText}&#9207;</button>
    <ul bind:this={sectionUL} class="hidden">
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
        color: rgb(225, 225, 225);
        font-size: inherit;
        font-family: inherit;
        transition: color 0.3s;
        transition: background-color 0.3s;
        font-size: 14pt;
    }
    button:hover {
        border-radius: 10px;
        background-color: #88dfef1e;
    }
    button:focus {
        background-color: rgba(225, 225, 225, 0);
    }

    .navSection {
        position: relative;
    }

    ul {
        z-index: 100;
        display: flex;
        flex-direction: column;
        position: absolute;
        top: 35px;
        left: 5px;
        justify-content: space-between;
        width: max-content;
        min-width: 60%;
        padding: 20px;
        gap: 5px;
        background-color: #1d3a43;
        border-radius: 5px;
        transition: gap 0.3s;
        overflow: hidden;
        box-shadow: 5px 5px 20px rgba(0, 0, 0, 0.345);
    }
    .hidden {
        top: -600px;
        gap: 0px;
    }
</style>