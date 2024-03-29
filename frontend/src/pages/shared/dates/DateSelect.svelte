<script lang='ts'>
    export let header = "Start";
    export let width = "auto";
    export let isTimezone = false;

    let tzOffsets = Array.from({length: 24}, (_, i) => {
        let hroffset = i - 11;
        return hroffset < 0 ? hroffset : `+${hroffset}`
    });
    
    let inputElem: HTMLInputElement;
    let selectElem: HTMLSelectElement;


    export function getValue(): string {
        return isTimezone? selectElem.value: inputElem.value;
    }
</script>

<div style="width: {width}">
    <h3>
        {header}
    </h3>
    {#if isTimezone}
        <select bind:this={selectElem} name="Timezone" class="inputBox tzbox">
            {#each tzOffsets as tzoffset}
                <option value={tzoffset}>{`UTC${tzoffset}`}</option>
            {/each}
        </select>
    {:else}
        <input bind:this={inputElem} class="inputBox"
            type="datetime-local" id="dateInput-from"
            min="2022-01-01" max="2099-01-01">
    {/if}
</div>

<style>
    h3 {
        margin-top: 0;
        margin-bottom: 10px;
    }
    .inputBox {
        color: inherit;
        cursor: pointer;
        border-radius: 10px;
        border: none;
        padding: 3px 10px;
        font-size: 12pt;
        background-color: #162a37;
        border: 2px solid transparent;
        background: linear-gradient(#12232E, #12232E) padding-box,
                    linear-gradient(45deg, #1c9bab 0%, #0e6764) border-box;
        filter: drop-shadow(0px 10px 5px rgba(0, 0, 0, 0.3));                    
    }
    .inputBox:focus {
        outline: none;
        border: 2px solid #ce4820;
    }

    .tzbox {
        background: linear-gradient(#12232E, #12232E) padding-box,
                    linear-gradient(270deg, #1c9bab 0%, #0e6764) border-box;
    }

    option {
        background-color: #12232E;
    }
</style>