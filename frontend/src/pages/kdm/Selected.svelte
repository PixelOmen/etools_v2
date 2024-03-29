<script context="module" lang="ts">
    import type { ListItemData } from '../shared/search/ListItem.svelte'
</script>

<script lang='ts'>
    export let selected: ListItemData | null = null;

    let displayName: string;
    $: {
        if (selected === null) {
            displayName = "None";
        } else {
            displayName = selected.displayName;
        }
    }
</script>

<div>
    <h4>
        Selected:
    </h4>
    <div class="displayBox" title={displayName}>
        {displayName}
    </div>
</div>


<style>
    h4 {
        margin-top: 10px;
        margin-bottom: 10px;
    }
    .displayBox {
        cursor: default;
        font-size: 11pt;
        font-weight: bold;
        border: 1px solid rgb(52, 51, 51);
        padding-left: 10px;
        padding-right: 10px;
        border-radius: 5px;
        background-color: #1a333a;
        border: 2px solid transparent;
        background: linear-gradient(#12232E, #12232E) padding-box,
                    linear-gradient(270deg, #1c9bab 10%, #0e6764) border-box;
        overflow: hidden;
        text-overflow: ellipsis;
        text-wrap: nowrap;
    }
</style>