<script context='module' lang='ts'>
    export interface ClientInfo {
        name: string;
        count: number;
    }
</script>

<script lang='ts'>
    import Chart from "chart.js/auto";
    import PieLabels from "./PieLabels.svelte";

    
    export let header: string;
    export let clientInfo: ClientInfo[]
    export let pieHeight = "200px";
    export let colorPool = [
        '#ff7675', // Tomato
        '#74b9ff', // Sky Blue
        '#a29bfe', // Plum
        '#ffeaa7', // Light Goldenrod
        '#55efc4', // Turquoise
        '#fab1a0', // Sandy Brown
        '#81ecec', // Turquoise Blue
        '#a55eea', // Purple
        '#ff8c00', // Dark Orange
        '#2e8b57', // Sea Green
        '#fd79a8', // Deep Pink
        '#e17055', // Chocolate
        '#00cec9', // Dark Turquoise
        '#fdcb6e', // Light Salmon
        '#6c5ce7', // Cornflower Blue
        '#ffa07a', // Light Salmon
        '#8b008b', // Dark Magenta
        '#add8e6', // Light Blue
        '#e9967a', // Dark Salmon
        '#9370db'  // Medium Slate Blue
    ];
    
    let pieCanvas: HTMLCanvasElement;

    $: {
        if (pieCanvas) {
            new Chart(pieCanvas, {
                type: 'doughnut',
                data: {
                    labels: clientInfo.map((i) => i.name),
                    datasets: [{
                        data: clientInfo.map((i) => i.count),
                        backgroundColor: colorPool,
                        borderColor: "black"
                    }]
                },
                options: {
                    cutout: "40%",
                    animation: {
                        animateRotate: true,
                        animateScale: false
                    },
                    plugins: {
                        legend: {
                            display: false
                        }
                    }
                }
            });
        }
    }
</script>

<div class="parentContainer">
    <div class="canvasContainer" style="height: {pieHeight}">
        <canvas bind:this={pieCanvas}></canvas>
    </div>
    <div class="labelContainer">
        <PieLabels labels={clientInfo.map((i) => i.name)} {colorPool} {header}/>
    </div>
</div>


<style>
    .parentContainer {
        display: flex;
        margin-top: 10px;
        padding: 5px 20px;
        border-radius: 10px;
        align-items: center;
    }
    .canvasContainer {
        margin-left: auto;
        filter: brightness(90%);
        width: max-content;
        margin-right: 20px;
    }
    .labelContainer {
        margin-right: auto;
        margin-left: 20px;
        padding: 0px 0px;
        /* border: 1px solid red; */
    }
</style>