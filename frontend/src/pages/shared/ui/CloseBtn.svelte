<script lang='ts'>
    export let size = "20px";
    let fontSize = Number(size.slice(0,2))/3;
</script>

<button on:click style="width:{size};height:{size};font-size:{fontSize}pt">
    X
</button>

<style>
    button {
        cursor: pointer;
        border: none;
        outline: none;
        color: rgb(228, 228, 228);
        height: 20px;
        width: 20px;
        border-radius: 50%;
        background: linear-gradient(45deg, #923214, #ce4820 99%);
        color: rgb(208, 208, 208);
        font-weight: bold;
        padding-bottom: 2px;
    }
    button:hover {
        background: linear-gradient(45deg, #ce4820, #ce4820 99%);
    }
    button:active {
        background: #ad3e1c;
        filter: drop-shadow(1px 5px 5px rgba(0, 0, 0, 0.0));
    }
</style>