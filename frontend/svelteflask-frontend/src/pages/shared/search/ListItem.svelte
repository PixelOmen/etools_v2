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
    .container:hover {
        background-color: grey;
    }
</style>