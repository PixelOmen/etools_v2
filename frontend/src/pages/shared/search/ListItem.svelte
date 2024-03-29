<script context="module" lang="ts">
    export interface ListItemData {
        displayName: string;
        filePath: string;
    }
</script>

<script lang='ts'>
    import { createEventDispatcher } from 'svelte';
    export let listdata: ListItemData;

    const dispatch = createEventDispatcher();
    function searchItemSelected() {
        dispatch("searchItemSelected", listdata);
    }

</script>

<li>
    <button class="container"
        title={listdata.displayName}
        on:click="{searchItemSelected}">
            {listdata.displayName}
    </button>
</li>

<style>
    .container {
        padding: 10px;
        padding-left: 10px;
        background-color: #162a37;
        border: 1px solid black;
        border-radius: 5px;
        font-family: inherit;
        color: inherit;
        width: 100%;
        text-align: left;
        overflow: hidden;
        text-overflow: ellipsis;
        white-space: nowrap;
    }
    .container:hover {
        cursor: pointer;
        border-radius: 5px;
        background-color: #1a7c89;
        /* filter: drop-shadow(0px 10px 20px rgba(0, 0, 0, 0.7)); */
        font-weight: 900;        
    }
</style>