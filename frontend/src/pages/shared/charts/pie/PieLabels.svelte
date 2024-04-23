<script lang='ts'>
    export let labels: string[];
    export let colorPool: string[];
    export let header: string;

    function colorIndex(index: number): number {
        let validIndex = index;
        while (validIndex > colorPool.length - 1) {
            validIndex -= colorPool.length;
        }
        return validIndex;
    }
</script>

<div class="parentContainer">
    <h4>
        {header}
    </h4>
    <ul class="listContainer">
        {#each labels as label, index}
            <li class="labelContainer">
                <div class="colorContainer"
                    style="background-color: {colorPool[colorIndex(index)]}">
                </div>
                <div class="nameContainer" title={label}>
                    {label}
                </div>
            </li>
        {/each}
    </ul>
</div>

<style>
    .parentContainer {
        display: flex;
        flex-direction: column;
        margin-top: auto;
        margin-bottom: auto;
        /* border: 1px solid red; */
        /* height: 100%; */
    }
    .listContainer {
        display: flex;
        /* border: 1px solid blue; */
        flex-wrap: wrap;
        row-gap: 10px;
        column-gap: 15px;
        max-width: 100%;
        overflow: hidden;
        box-sizing: border-box;
        margin-top: auto;
        margin-bottom: auto;
    }
    h4 {
        margin: 0;
        padding: 0;
        margin-bottom: 20px;
        text-align: center;
        /* border: 1px solid red; */
    } 
    .labelContainer {
        display: flex;
        /* border: 1px solid green; */
        align-items: center;
        overflow: hidden;
        box-sizing: border-box;
        height: max-content;
    }
    .colorContainer {
        width: 30px;
        height: 10px;
        flex-shrink: 0;
        filter: brightness(90%);
    }
    .nameContainer {
        font-family: "Montserrat";
        height: max-content;
        margin-left: 5px;
        overflow: hidden;
        text-overflow: ellipsis;
        color: rgb(230, 230, 230);
        max-width: 100%;
        white-space: nowrap;
    }
</style>