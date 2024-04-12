<script lang='ts'>
    import LoadingIcon from "../../../assets/LoadingIcon.png"
    export let width = "30px";
    export let height = "30px";
</script>

<!-- <div style="width: {width}; height: {height}"></div> -->
<div>
    <img src={LoadingIcon} alt="Loading Icon" width={width} height={height}>
</div>

<style>
    div {
        line-height: 0;
    }
    img {
        margin: 0;
        padding: 0;
        margin-left: 35px;
        margin-right: auto;
        /* border-top: 4px solid #cf6208;
        border-left: 4px solid #cf6208;
        border-bottom: 4px solid #08cfb5;
        border-right: 4px solid #08cfb5;
        border-radius: 90%; */
        animation: spin 3s linear infinite;
    }

    @keyframes spin {
        0% { transform: rotate(0deg) }
        100% { transform: rotate(360deg) }
    }
</style>