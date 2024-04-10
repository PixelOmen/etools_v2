<script lang='ts'>
    export let content = "MyButton";
    export let fontSize = "13pt";
    export let fontWeight = "900";
    export let padding = "3px 15px";
    export let hasShadow = true;
    export let isClose = false;
    export let hasBG = true;

    let shadowSpec = hasShadow? "drop-shadow(1px 5px 5px rgba(0, 0, 0, 0.3))" : "";
    let bgSpec: string;
    if (hasBG) {
        bgSpec = "background: linear-gradient(45deg, #923214, #ce4820 99%);";
    } else {
        bgSpec = "background: rgba(0,0,0,0);";
    }
    let paddingBottom = isClose? "padding-bottom: 6px;" : "";
</script>

<button 
    on:click 
    style="font-size: {fontSize};
    font-weight: {fontWeight};
    padding: {padding};
    {paddingBottom}
    filter: {shadowSpec};
    {bgSpec}
    "
>
    {content}
</button>

<style>
    button {
        cursor: pointer;
        border: none;
        outline: none;
        border-radius: 5px;
        color: rgb(228, 228, 228);
        font-family: inherit;
    }
    button:hover {
        background: linear-gradient(45deg, #ce4820, #ce4820 99%) !important;
    }
    button:active {
        background: #ad3e1c !important;
        filter: drop-shadow(1px 5px 5px rgba(0, 0, 0, 0.0));
    }
</style>