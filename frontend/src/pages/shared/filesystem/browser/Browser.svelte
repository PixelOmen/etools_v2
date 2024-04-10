<script lang='ts'>
    import { createEventDispatcher } from "svelte";
    import CloseBtn from "../../ui/CloseBtn.svelte";
    import backarrow from "../../../../assets/backarrow.png";

    export let rootPath = "ROOT";
    let pathInput: HTMLInputElement;

    const dispatch = createEventDispatcher();
    function close(e: Event): void {
        dispatch("browserClose", {
            "path": pathInput.value
        });
    }

    $: {
        if (pathInput) {
            pathInput.value = rootPath;
        }
    }
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
</div>


<style>
    .container {
        z-index: 100;
        position: fixed;
        top: 10%;
        left: 10%;
        height: 80%;
        width: 80%;
        background-color: rgba(37, 37, 37, 0.9);
        border-radius: 10px;
        filter: drop-shadow(5px 20px 10px rgba(0, 0, 0, 0.5));
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
        /* background-color: rgba(0, 0, 0, 0.3); */
        border-radius: 5px;
    }
    .headerContainer > input:focus {
        background-color: rgb(62, 61, 64);
    }

    hr {
        margin-top: 20px;
        border: none;
        border-top: 1px solid rgb(0, 0, 0);
        width: 100%;
    }
</style>