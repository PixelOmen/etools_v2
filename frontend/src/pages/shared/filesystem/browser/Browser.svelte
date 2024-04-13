<script context="module" lang='ts'>
    import type { BrowserItemData } from "./BrowserItem.svelte";
    import * as coms from "../../../../libs/coms"

    interface DirResponse {
        dirPath: string;
        parentPath: string;
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
    import LoadingIcon from "../../ui/LoadingIcon.svelte";

    export let startDir = "ROOT";
    export let apiURL = "/api/webfs";
    export let dirOnly = false;

    const dispatch = createEventDispatcher();

    let pathInput: HTMLInputElement;
    let dirContents: BrowserItemData[] = [];
    let selectedItem: BrowserItemData | null = null;
    let currentDir: DirResponse | null = null;
    let errormsg = "";
    let isLoading = false;
    let showLoading = false;

    $: {
        dirContents = dirContents.filter((item) => {
            if (dirOnly) {
                return item.isDir;
            } else {
                return true;
            }
        });
        dirContents.sort((a, b) => {
            if (a.isDir === b.isDir) return 0;
            if (a.isDir) return -1;
            return 1;
        });
    }

    $: {
        if (pathInput) {
            pathInput.addEventListener("keydown", (e) => {
                if (e.key == "Enter" || e.keyCode === 13) {
                    getDir(pathInput.value);
                }
            })
        }
    }


    function getDir(path: string): void {
        errormsg = "";
        isLoading = true;
        setTimeout(() => {
            if (isLoading) {
                showLoading = true;
            }
        }, 150);
        dirContents = [];
        
        coms.submitJSON(apiURL, {
            "path": path
        })
        .then(res => res.json())
        .then(resjson => {
            isLoading = false;
            showLoading = false;
            if (resjson.status != "ok") {
                errormsg = resjson.error;
                dirContents = [];
            } else {
                currentDir = resjson;
                pathInput.value = resjson.dirPath;
                dirContents = resjson.contents;
            }
        });
    }

    function setSelected(e: CustomEvent): void {
        selectedItem = e.detail;
    }

    function enterFolder(e: CustomEvent): void {
        getDir(e.detail.filePath);
        pathInput.focus();
        pathInput.blur();
    }

    function back(): void {
        if (currentDir) {
            getDir(currentDir.parentPath);
        }
    }
    
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
</script>


<div class="container">
    <div class="closeBtnContainer">
        <CloseBtn on:click={close} size="22px"/>
    </div>
    <div class="headerContainer">
        <button id="backBtn" on:click={back}>
            <img id="backArrow" src={backarrow} alt="Browse Back" width="25px">
        </button>
        <input bind:this={pathInput} type="text">
    </div>
    <hr>
    <div class="fileContainer">
        {#if showLoading}
            <div class="loadingContainer">
                <LoadingIcon/>
            </div>            
        {/if}
        {#if errormsg}
            <div class="errorContainer">
                {errormsg}
            </div>            
        {/if}
        {#each dirContents as item}
            <BrowserItem
                data={item}
                on:browserItemClick={setSelected}
                on:browserItemDblClick={enterFolder}
            />        
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
        justify-content: flex-end;
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

    #backBtn {
        cursor: pointer;
        border: none;
        outline: none;
        background: none;
        margin-right: 5px;
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
        text-overflow: ellipsis;
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
        margin-top: 10px;
        height: 75%;
        border: 1px solid black;
        background-color: rgba(37, 37, 37, 0.94);
        overflow: auto;
    }

    .errorContainer, .loadingContainer {
        position: relative;
        margin-left: auto;
        margin-right: auto;
        top: 30%;
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