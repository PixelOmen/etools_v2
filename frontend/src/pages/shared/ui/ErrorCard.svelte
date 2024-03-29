<script lang='ts'>
    export let errMsg = "Required";
    let errorCard: HTMLDivElement;

    export function setError(): void {
        errorCard.classList.remove("hidden");
        errorCard.classList.remove("errorCardEnd");
        setTimeout(() => {
            errorCard.classList.add("errorCardEnd");
        }, 100);
    }

    export function clearError(): void {
        errorCard.classList.add("hidden");
    }
</script>


<div bind:this={errorCard} class="hidden errorCardStart errorCardEnd">
    {errMsg}
</div>
<slot></slot>


<style>
    .errorCardStart {
        position: absolute;
        z-index: 0;
        top: 38px;
        left: 10%;
        width: 80%;
        text-align: center;
        color: rgb(255, 0, 0);
        font-family: inherit;
        font-weight: bold;
        background-color: #183549;
        border-radius: 10px 10px 0px 0px;
        transition: top 0.5s;
    }

    .errorCardEnd {
        top: 15px;
    }

    .hidden {
        display: none;
    }
</style>