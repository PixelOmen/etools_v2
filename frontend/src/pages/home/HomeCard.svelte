<script lang='ts'>
    export let header = "";
</script>

<div class="container">
    <div class="textContainer">
        <h4 class="header">
            {header}
        </h4>
        <p>
            <slot/>
        </p>
    </div>
</div>

<style>
    .container {
        padding: 30px 0px;
        border-radius: 20px;
        font-family: "Montserrat";
        display: flex;
        flex-wrap: nowrap;
        justify-content: space-around;
        max-width: 900px;
        position: relative;
    }
    .header {
        font-size: 20pt;
        margin: 0;
        font-weight: bold;
    }
    .textContainer {
        z-index: 1;
        padding: 10px 60px;
        width: 70%;
        border-radius: 30px;
        font-weight: bold;
        font-size: 11pt;
        text-align: center;
        color:rgb(230, 230, 230);
    }
</style>