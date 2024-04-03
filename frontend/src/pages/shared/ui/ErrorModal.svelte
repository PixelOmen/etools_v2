<script lang='ts'>
    import ImportantBtn from "./ImportantBtn.svelte";

    let errMsg = "No error set";
    let container: HTMLDivElement;

    export function setError(err: string): void {
        errMsg = err;
    }

    export function show(): void {
        container.classList.remove("hidden");
    }

    export function hide(): void {
        container.classList.add("hidden");
    }
</script>

<div bind:this={container} class="container hidden">
    <div class="header">
        <h4>
            Error Details:
        </h4>
        <div class="btn">
            <ImportantBtn on:click content="X" fontSize="10pt" padding="3px 8px"/>
        </div>
    </div>
    <p>
        {errMsg}
    </p>
</div>

<style>
    .container {
        position: fixed;
        top: 40%;
        left: 50%;
        transform: translate(-50%, -50%);
        border: 3px solid black;
        padding: 20px 20px;
        min-width: 400px;
        max-width: 80%;
        z-index: 100;
        background-color: #16323a;
        border-radius: 20px;
        filter: drop-shadow(5px 20px 10px rgba(0, 0, 0, 0.5));
    }
    .header {
        display: flex;
        margin-bottom: 15px;
        margin-right: 5px;
    }
    h4 {
        margin: 0;
    }
    p {
        border: 1px solid black;
        margin: 0;
        margin-left: 10px;
        margin-bottom: 10px;
        margin-right: 10px;
        padding: 0px 10px;
        background-color: #18262a;
        color: orange;
        white-space: pre-line;
        overflow-wrap: break-word;
    }
    .btn {
        margin-left: auto;
        margin-right: right;
    }
    .hidden {
        display: none;
    }
</style>