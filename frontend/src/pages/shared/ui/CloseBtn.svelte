<script lang='ts'>
    import img_closeBtn from "../../../assets/img_closeBtn.png";
    export let size = "25px";
    let svgSize = `${Number(size.slice(0, 2)) - 10}px`;
</script>

<button on:click style="width:{size};height:{size};">
    <img src={img_closeBtn} alt="" width={size} height={size}>
</button>

<style>
    button {
        cursor: pointer;
        outline: none;
        border: none;
        background-color: rgba(0, 0, 0, 0);
        padding: 0;
        margin: 0;
    }
    button:hover {
        filter: brightness(110%);
    }
    button:active {
        filter: brightness(80%);
    }
</style>