<script context="module" lang="ts">
    import type { ListItemData } from './ListItem.svelte';
    type ListData = ListItemData[];
</script>

<script lang="ts">
    import { createEventDispatcher } from 'svelte';
    import SearchBox from './SearchBox.svelte';
    import ListItem from './ListItem.svelte';

    export let boxWidth = "auto";
    export let boxHeight = "auto";
    export let listData: ListData;
    export let header: string;
    export let searchPlaceholder = "Search";

    $: filteredData = listData;

    let searchInput: HTMLInputElement;
    $: {
        if (searchInput) {
            searchInput.addEventListener('change', () => {
                if (!searchInput.value) {
                    filteredData = listData;
                } else {
                    filteredData = listData.filter((item) => {
                        let lowerName = item.displayName.toLowerCase();
                        let lowerValue = searchInput.value.toLowerCase();
                        return lowerName.includes(lowerValue)
                    })
                }
            });
        }
    }

    const dispatch = createEventDispatcher();
    function searchItemSelected(e: CustomEvent) {
        dispatch("searchItemSelected", {header: header, data: e.detail});
    }
</script>

<div class="container" style="width: {boxWidth}">
    <h3 style="margin-bottom: 10px">
        {header}
    </h3>
    <SearchBox bind:searchInput={searchInput} boxWidth="auto" placeholder="{searchPlaceholder}"/>
    <ul style="height: {boxHeight}">
        {#each filteredData as item}
            <ListItem listdata={item} on:searchItemSelected={searchItemSelected}/>
        {/each}
    </ul>
</div>

<style>
    ::-webkit-scrollbar {
        width: 8px;
    }
    ::-webkit-scrollbar-track {
        background-color: #334c5d;
        border-radius: 10px;
    }
    ::-webkit-scrollbar-thumb {
        background-color: #5fa2ae;
        border-radius: 20px;
    }
    ::-webkit-scrollbar-thumb:hover {
        background-color: #71becc;
    }    

    .container {
        flex-direction: column;
    }

    h3 {
        margin: 0;
    }

    ul {
        margin-top: 5px;
        border: 3px solid transparent;
        background: linear-gradient(#12232E, #12232E) padding-box,
                    linear-gradient(90deg, #923214, #ce4820 90%) border-box;
        border-radius: 10px;
        display: flex;
        flex-direction: column;
        padding: 5px 5px;
        overflow: auto;
    }
</style>