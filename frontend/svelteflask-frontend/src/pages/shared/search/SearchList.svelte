<script context="module" lang="ts">
    import type { ListItemData } from './ListItem.svelte';
    type ListData = ListItemData[];
</script>

<script lang="ts">
    import SearchBox from './SearchBox.svelte';
    import ListItem from './ListItem.svelte';

    export let boxWidth = "500px";
    export let boxHeight = "200px";
    export let listData: ListData;
    export let header: string;
</script>

<div class="container" style="width: {boxWidth}">
    <h3 style="margin-bottom: 10px">
        {header}
    </h3>
    <SearchBox boxWidth="auto" placeholder="Search Certs"/>
    <ul style="height: {boxHeight}">
        {#each listData as item}
            <ListItem listdata={item}/>
        {/each}
    </ul>
</div>

<style>
    .container {
        flex-direction: column;
        /* border: solid 1px blue; */
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
        padding: 10px;
    }
</style>