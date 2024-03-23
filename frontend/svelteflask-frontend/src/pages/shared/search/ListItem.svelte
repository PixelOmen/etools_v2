<script context="module" lang="ts">
    export interface ListItemData {
        displayName: string;
        filePath: string;
    }
</script>

<script lang='ts'>
    export let listdata: ListItemData;

    let isSelected = false;
</script>

<li>
    <div class="container">
            {listdata.displayName}
    </div>
</li>

<style>
    .container {
        padding: 3px;
        padding-left: 5px;
        background-color: #162a37;
        border: 1px solid black;
        border-radius: 5px;
    }
    .container:hover {
        /* color: black; */
        cursor: pointer;
        border-radius: 5px;
        background-color: rgb(77, 122, 147);
        filter: drop-shadow(0px 10px 10px rgba(0, 0, 0, 0.472));
        font-weight: 900;
        
    }
</style>