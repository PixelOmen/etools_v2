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
            console.log("test")
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
    <!-- <ul bind:this={sectionUL} style="display: {sectionVisible ? 'flex' : 'none'}"> -->
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
        display: flex;
        flex-direction: column;
        position: absolute;
        top: 35px;
        left: 10px;
        justify-content: space-between;
        min-width: 60%;
        padding: 10px;
        gap: 5px;
        background-color: #88dfef1e;
        border-radius: 5px;
        transition: gap 0.3s;
        overflow: hidden;
    }
    .hidden {
        top: -600px;
        gap: 0px;
    }
</style>