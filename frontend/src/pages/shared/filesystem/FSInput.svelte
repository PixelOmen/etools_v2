<script lang='ts'>
    export let header: string;
    export let placeholder = "Output Directory";
</script>

<div class="container">
    <h3>
        {header}
    </h3>
    <input type="text" placeholder={placeholder}>
</div>

<style>
    .container {
        /* border: 1px solid blue; */
        width: 100%;
    }
    h3 {
        margin-top: 0px;
        margin-bottom: 10px;
    }
    input {
        color: inherit;
        border-radius: 10px;
        border: none;
        padding: 3px 10px;
        font-size: 12pt;
        background-color: #162a37;
        border: 2px solid transparent;
        background: linear-gradient(#12232E, #12232E) padding-box,
                    linear-gradient(45deg, #1c9bab 0%, #0e6764) border-box;
        filter: drop-shadow(0px 10px 5px rgba(0, 0, 0, 0.3));
        width: 100%;
        box-sizing: border-box;
    }
    input:focus {
        outline: none;
        border: 2px solid #ce4820;
    }
    input::placeholder {
        color: grey;
    }
</style>