<script context='module' lang='ts'>
</script>

<script lang='ts'>
    export let header: string;
    export let data: string[];
    export let minwidth = "10px";
</script>

<div class="container" style="min-width: {minwidth}">
    <h3>
        {header}
    </h3>
    <ul>
        {#each data as item}
            <li title="{item}">{item}</li>
        {/each}
    </ul>
</div>

<style>
    .container {
        flex-grow: 1;
        overflow: hidden;
        font-size: 11pt;
        box-sizing: content-box;
        border: 1px solid #197a87;
        background-color: #12232E;
    }
    h3 {
        padding: 0;
        margin: 5px 5px;
    }
    li {
        padding: 2px 10px;
        border-top: 1px solid #197a87;
        overflow: hidden;
        text-overflow: ellipsis;
        border-radius: 2px;
    }
</style>