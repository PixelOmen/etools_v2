<script context="module" lang='ts'>
    import type { BrowserItemData } from "./BrowserItem.svelte";
    import * as coms from "../../../../libs/coms"

    interface DirResponse {
        dirPath: string;
        contents: BrowserItemData[];
        status: string;
        error: string;
    }
</script>

<script lang='ts'>
    import { createEventDispatcher } from "svelte";
    import CloseBtn from "../../ui/CloseBtn.svelte";
    import backarrow from "../../../../assets/backarrow.png";
    import BrowserItem from "./BrowserItem.svelte";
    import ImportantBtn from "../../ui/ImportantBtn.svelte";

    export let startDir = "ROOT";
    export let apiURL = "/api/webfs";
    let dirContents: BrowserItemData[] = [];
    let selectedItem: BrowserItemData | null = null;
    let errormsg = "";
    let pathInput: HTMLInputElement;


    function getDir(path: string): void {
        errormsg = "";
        
        coms.submitJSON(apiURL, {
            "path": path
        })
        .then(res => res.json())
        .then(resjson => {
            if (resjson.status != "ok") {
                errormsg = resjson.error;
                dirContents = [];
            } else {
                pathInput.value = resjson.dirPath;
                dirContents = resjson.contents;
            }
        });
    }

    function setSelected(e: CustomEvent): void {
        selectedItem = e.detail;
    }

    const dispatch = createEventDispatcher();
    function close(): void {
        dispatch("browserClose", {
            "path": pathInput.value,
            "selected": selectedItem
        });
    }

    function select(): void {
        dispatch("browserSelect", {
            "path": pathInput.value,
            "selected": selectedItem
        });
    }


    getDir(startDir);
    // dirContents = [
    //     {
    //         displayName: "Some_Folder",
    //         isDir: true,
    //         filePath: "some/path/to/Some_Folder"
    //     },
    //     {
    //         displayName: "Some_file.xml",
    //         isDir: false,
    //         filePath: "some/path/to/Some_file.xml"
    //     }        
    // ];    
</script>


<div class="container">
    <div class="closeBtnContainer">
        <CloseBtn on:click={close} size="22px"/>
    </div>
    <div class="headerContainer">
        <img id="backArrow" src={backarrow} alt="Browse Back" width="25px">
        <input bind:this={pathInput} type="text">
    </div>
    <hr>
    <div class="fileContainer">
        {#if errormsg}
            <div class="errorContainer">
                {errormsg}
            </div>            
        {/if}
        {#each dirContents as item}
            <BrowserItem data={item} on:browserItemClicked={setSelected}/>        
        {/each}
    </div>
    <div class="footerContainer">
        <div class="btnContainer">
            <ImportantBtn
                on:click={select}
                content="Select"
                padding="5px 10px"
                fontSize="11pt"
                hasShadow={false}
            />
        </div>
    </div>
</div>


<style>
    .container {
        z-index: 100;
        display: flex;
        flex-direction: column;
        position: fixed;
        top: 10%;
        left: 10%;
        width: 80%;
        height: 80%;
        background-color: rgba(37, 37, 37, 0.9);
        filter: drop-shadow(5px 20px 10px rgba(0, 0, 0, 0.5));
        border-radius: 10px;
        border: 1px solid rgb(63, 63, 63);
        padding-bottom: 10px;
    }
    @supports (backdrop-filter: blur(15px)) {
        .container {
            background-color: rgba(37, 37, 37, 0.6);
            backdrop-filter: blur(10px);
        }
    }
    .closeBtnContainer {
        margin-left: auto;
        margin-right: 20px;
        margin-top: 8px;
        width: max-content;
    }

    .headerContainer {
        display: flex;
        margin-top: 10px;
        margin-left: 20px;
        margin-right: 20px;
    }
    #backArrow {
        margin-right: 10px;
        cursor: pointer;
    }
    #backArrow:hover {
        filter: brightness(110%);
    }
    #backArrow:active {
        filter: brightness(80%);
    }

    .headerContainer > input {
        font-family: inherit;
        font-size: 12pt;
        font-weight: bold;
        color: inherit;
        width: 100%;
        box-sizing: border-box;
        border: none;
        outline: none;
        padding: 3px 10px;
        background-color: rgba(0, 0, 0, 0);
        border-radius: 5px;
    }
    .headerContainer > input:focus {
        background-color: rgb(62, 61, 64);
    }

    hr {
        margin-top: 10px;
        border: none;
        border-top: 1px solid rgb(0, 0, 0);
        width: 100%;
    }

    .fileContainer {
        padding: 10px 10px;
        margin: 20px 30px;
        height: 75%;
        border: 1px solid black;
        background-color: rgba(37, 37, 37, 0.94);
    }

    .errorContainer {
        position: relative;
        margin-left: auto;
        margin-right: auto;
        top: 30%;
        border: 1px solid yellow;
        text-align: center;
        white-space: pre-line;
        overflow-wrap: break-word;
    }

    .footerContainer {
        margin-bottom: 10px;
    }
    .btnContainer {
        width: max-content;
        margin-left: auto;
        margin-right: 20px;
    }
</style>