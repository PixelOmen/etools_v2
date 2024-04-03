<script lang='ts'>
    export let content = "MyButton";
    export let fontSize = "13pt";
    export let padding = "3px 15px";
</script>

<button 
    on:click 
    style="font-size: {fontSize};
    padding: {padding}"
>
    {content}
</button>

<style>
    button {
        cursor: pointer;
        border: none;
        outline: none;
        border-radius: 5px;
        font-size: 13pt;
        filter: drop-shadow(1px 5px 5px rgba(0, 0, 0, 0.3));
        background: linear-gradient(45deg, #923214, #ce4820 99%);
        color: rgb(228, 228, 228);
        font-family: inherit;
        font-weight: 900;
    }
    button:hover {
        background: linear-gradient(45deg, #ce4820, #ce4820 99%);
    }
    button:active {
        background: #ad3e1c;
        filter: drop-shadow(1px 5px 5px rgba(0, 0, 0, 0.0));
    }
</style>