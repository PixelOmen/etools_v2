<script context="module" lang='ts'>
    export interface BrowserItemData {
        displayName: string;
        isDir: boolean;
        filePath: string;
    }
</script>

<script lang='ts'>
    import { createEventDispatcher } from "svelte";
    import FolderIcon from "../../../../assets/folderIcon.svg";
    import FileIcon from "../../../../assets/fileIcon.svg";

    export let data: BrowserItemData;
    const dispatch = createEventDispatcher();
    function clicked(): void {
        dispatch("browserItemClick", data);
    }
    function dblclicked(): void {
        dispatch("browserItemDblClick", data);
    }
</script>

<button class="container" on:click={clicked} on:dblclick={dblclicked}>
    <div class="icon">
        {#if data.isDir}
            <img src={FolderIcon} alt="Folder Icon" width="30px">
        {:else}
            <img src={FileIcon} alt="Folder Icon" width="30px">
        {/if}
    </div>
    <div class="itemName">
        {data.displayName}
    </div>
</button>

<style>
    .container {
        outline: none;
        border: 1px solid rgba(0, 0, 0, 0);
        background: none;
        font-family: inherit;
        padding-top: 5px;
        cursor: pointer;
        display: flex;
        align-items: center;
        border-radius: 5px;
        min-width: 100%;
        color: inherit;
    }
    .container:hover {
        background-color: #495c5f0f;
        border: 1px solid rgb(93, 93, 93);
    }
    .container:focus {
        background-color: #1a7c89b1;
    }

    .itemName {
        margin-left: 10px;
        height: max-content;
        width: max-content;
        text-align: center;
        color: inherit;
    }
</style>