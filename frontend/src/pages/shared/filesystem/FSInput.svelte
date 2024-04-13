<script lang='ts'>
    import type { SvelteComponent } from 'svelte';
    import ErrorCard from '../ui/ErrorCard.svelte';
    import Browser from './browser/Browser.svelte';

    export let header: string = "";
    export let placeholder = "Output Directory";
    export let dironly = false;

    let inputElem: HTMLInputElement;
    let errorCard: SvelteComponent;
    let browserOpen = false;

    function browseClick(): void {
        browserOpen = true;
    }

    function browserClose(): void {
        browserOpen = false;
    }

    function browserSelect(e: CustomEvent): void {
        if (e.detail.selected) {
            inputElem.value = e.detail.selected.filePath;
        }
        browserOpen = false;
    }    

    export function setError(): void {
        errorCard.setError();
    }

    export function clearError(): void {
        errorCard.clearError();
    }

    export function getValue(): string {
        return inputElem.value;
    }
</script>

<div class="container">
    {#if browserOpen}
        <Browser
            on:browserClose={browserClose}
            on:browserSelect={browserSelect}
            dironly={dironly}
        />
    {/if}
    {#if header}
        <h3>
            {header}
        </h3>
    {/if}
    <ErrorCard bind:this={errorCard}>
        <div class="inputContainer">
            <button on:click={browseClick} class="browseBtn">
                Browse
            </button>
            <input bind:this={inputElem} type="text" placeholder={placeholder}>
        </div>
    </ErrorCard>
</div>

<style>
    .container {
        position: relative;
        width: 100%;
    }
    h3 {
        margin-top: 0px;
        margin-bottom: 10px;
    }
    .inputContainer {
        position: relative;
        display: flex;
        background-color: #162a37;
        border: 2px solid transparent;
        background: linear-gradient(#12232E, #12232E) padding-box,
                    linear-gradient(45deg, #1c9bab 0%, #0e6764) border-box;
        filter: drop-shadow(0px 10px 5px rgba(0, 0, 0, 0.3));
        width: 100%;
        box-sizing: border-box;
        border-radius: 10px;
        overflow: hidden;
    }
    input {
        border-radius: 10px;
        color: inherit;
        border: none;
        padding: 0px 10px;
        font-size: 11pt;
        font-family: inherit;
        background-color: #12232E;
        width: 100%;
        border: 2px solid #00000000;
        min-height: 100%;
        box-sizing: border-box;
    }
    input:focus {
        outline: none;
        border: 2px solid #ce4820;
        border-top-left-radius: 0;
        border-bottom-left-radius: 0;
    }
    input::placeholder {
        color: grey;
    }
    .browseBtn {
        padding: 0px 15px;
        cursor: pointer;
        border-radius: 0px;
        min-height: 100%;
        border: none;
        border-top-right-radius: 0;
        border-bottom-right-radius: 0;
        background: linear-gradient(90deg, #1c9bab, #12232E 99%);
        filter: none;
        color: rgb(227, 227, 227);
        font-family: inherit;
        font-weight: bold;
        font-size: 11pt;
    }
    .browseBtn:hover {
        filter: brightness(120%);
    }
    .browseBtn:active {
        filter: brightness(80%);
    }    
</style>