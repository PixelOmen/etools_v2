<script lang='ts'>
    import { createEventDispatcher } from "svelte";
    import ImportantBtn from "../../ui/ImportantBtn.svelte";
    import backarrow from "../../../../../public/backarrow.png";

    const dispatch = createEventDispatcher();
    function close(e: Event): void {
        dispatch("browserClose");
    }
</script>


<div class="container">
    <div class="closeBtn">
        <ImportantBtn
            on:click={close}
            hasBG={true}
            content="X"
            isClose={true}
            hasShadow={false}
            padding = "2px 15px"
            fontWeight = "normal"
            fontSize = "8pt"
        />
    </div>
    <div class="headerContainer">
        <img id="backArrow" src={backarrow} alt="Browse Back" width="25px">
        <input type="text">
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
        background: rgb(37, 37, 37);
        border-radius: 10px;
        filter: drop-shadow(5px 20px 10px rgba(0, 0, 0, 0.5));
    }
    .closeBtn {
        margin-left: auto;
        margin-right: 10px;
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