<script context="module" lang='ts'>
    import type { BrowserItemData } from "./BrowserItem.svelte";
</script>

<script lang='ts'>
    import { createEventDispatcher } from "svelte";
    import CloseBtn from "../../ui/CloseBtn.svelte";
    import backarrow from "../../../../assets/backarrow.png";
    import BrowserItem from "./BrowserItem.svelte";
    import ImportantBtn from "../../ui/ImportantBtn.svelte";

    export let rootPath = "ROOT";
    // export let dirOnly = false;

    let pathInput: HTMLInputElement;

    const dispatch = createEventDispatcher();
    function close(e: Event): void {
        dispatch("browserClose", {
            "path": pathInput.value
        });
    }

    function select(e: Event): void {
        dispatch("browserSelect", {
            "path": pathInput.value
        });
    }    

    $: {
        if (pathInput) {
            pathInput.value = rootPath;
        }
    }

    let testData = [
        {
            displayName: "Test_item.xml",
            isDir: true,
            filePath: "some/path/"
        },
        {
            displayName: "Test_item.xml",
            isDir: false,
            filePath: "some/path/"
        }        
    ]
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
        <BrowserItem data={testData[0]}/>
        <BrowserItem data={testData[1]}/>
    </div>
    <div class="footerContainer">
        <div class="btnContainer">
            <ImportantBtn
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

    .footerContainer {
        margin-bottom: 10px;
    }
    .btnContainer {
        width: max-content;
        margin-left: auto;
        margin-right: 20px;
    }
</style>