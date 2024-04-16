<script lang='ts'>
    export let header = "";
    export let imgURL = "";
</script>

<div class="container">
    <div id="imgContainer" style="background-image: url({imgURL});"></div>
    <div class="textContainer">
        <h4>
            {header}
        </h4>
        <p>
            <slot/>
        </p>
    </div>
</div>

<style>
    .container {
        padding: 10px 0px;
        border-radius: 20px;
        font-family: "Montserrat";
        display: flex;
        flex-wrap: nowrap;
        justify-content: space-around;
        max-width: 900px;
        position: relative;
        /* margin-left: auto; */
        /* margin-right: auto; */
    }
    .textContainer {
        width: 80%;
        z-index: 1;
        font-weight: bold;
        background-color: rgba(19, 9, 0, 0.4);
        border: 2px solid rgba(156, 73, 0, 0.776);
        /* border: 2px solid rgba(128, 128, 128, 0.4); */
        /* background: linear-gradient(to bottom, rgba(0, 0, 0, 0.1) 0%, rgba(0, 0, 0, 0.26) 100%); */
        padding: 20px 40px;
        border-radius: 40px;
        color:rgb(230, 230, 230);

    }
    #imgContainer {
        z-index: 0;
        position: absolute;
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        top: -20px;
        /* right: 20px; */
        width: 120%;
        height: 120%;
        mask-image: radial-gradient(ellipse 55% 50%, white 0%, transparent 100%);
        border-radius: 20px;
    }
</style>