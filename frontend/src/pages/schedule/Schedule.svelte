<script lang="ts">
    import HeroSection from "../shared/sections/HeroSection.svelte";
    import FooterLinks from "../shared/sections/FooterLinks.svelte";
    import PieChart from "../shared/charts/pie/PieChart.svelte";
</script>

<main>
    <HeroSection paddingBottom="0px" paddingTop="70px">
        <section class="sectionContainer topSection">
            Test info
        </section>
        <section class="sectionContainer bottomSection">
            <div class="contentContainer">
                <h3>
                    Summary for 04/23/2024
                </h3>
                <div class="summaryContainer">
                    <div class="statsContainer">
                        <div>
                            Jobs: 10
                        </div>
                        <div>
                            Rooms: 10
                        </div>
                        <div>
                            Resources: 20
                        </div>
                    </div>
                    <div class="chartContainer">
                        <PieChart pieHeight="150px" header="Clients"/>
                    </div>
                </div>
            </div>
        </section>
    </HeroSection>
</main>
<FooterLinks paddingTop="0px"/>


<style>
    main {
        min-width: 900px;
    }
    .sectionContainer {
        position: relative;
        display: flex;
        width: 100%;
        margin-left: auto;
        margin-right: auto;
        justify-content: center;
        overflow: hidden;
        /* border-bottom: 2px solid #a46d39; */
    }
    .topSection {
        /* border-top: 2px solid #a46d39; */
        height: 200px;
    }
    .bottomSection {
        border-bottom: 2px solid #a46d39;
        padding: 20px 0px;
    }

    .contentContainer {
        background-color: rgba(0, 77, 79, 0.124);
        border: 2px solid rgb(86, 86, 86);
        border-radius: 20px;
        padding: 10px;
        width: 80%;
        font-family: "Montserrat";
    }
    h3 {
        margin: 0;
        margin: 10px;
        padding: 0;
        width: 100%;
        font-family: "Montserrat";
        /* text-align: center; */
    }
    .summaryContainer {
        margin-top: 20px;
    }
    .statsContainer {
        /* border: 2px solid blue; */
        font-size: 12pt;
        width: 100%;
        flex-grow: 3;
        flex-shrink: 1;
        display: flex;
        justify-content: space-evenly;
        font-weight: bold;
        border-bottom: 1px solid grey;
        border-top: 1px solid grey;
    }
    .chartContainer {
        /* border: 2px solid green; */
        border-radius: 20px;
    }
</style>
