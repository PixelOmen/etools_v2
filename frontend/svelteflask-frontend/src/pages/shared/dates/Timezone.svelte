<script lang='ts'>
    let offsets = Array.from({length: 24}, (_, i) => {
        let hroffset = i - 11;
        return hroffset < 0 ? hroffset : `+${hroffset}`
    });
</script>

<div>
    <h3>
        Timezone
    </h3>
    <select name="Timezone" id="timezone">
        {#each offsets as tzoffset}
            <option value={tzoffset}>{`UTC${tzoffset}`}</option>
        {/each}
    </select>
</div>

<style>
    /* div {
        border: 1px solid red;
    } */
    h3 {
        margin-top: 0;
        margin-bottom: 10px;
    }
    select {
        width: 150px;
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
    select:focus {
        outline: none;
        border: 2px solid #ce4820;
    }
    option {
        background-color: #12232E;
    }
</style>