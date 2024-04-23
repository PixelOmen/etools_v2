<script lang="ts">
    import HeroSection from "../shared/sections/HeroSection.svelte";
    import DateSelect from "../shared/dates/DateSelect.svelte";
    import ImportantBtn from "../shared/ui/ImportantBtn.svelte";
    import PieChart from "../shared/charts/pie/PieChart.svelte";
    import FooterLinks from "../shared/sections/FooterLinks.svelte";
</script>

<main>
    <HeroSection paddingBottom="0px" paddingTop="70px">
        <section class="sectionContainer topSection">
            <div class="inputContainer">
                <div class="dateSelectContainer">
                    <DateSelect header="Select Date"/>
                </div>
                <div class="btnContainer">
                    <ImportantBtn content="Generate" fontSize="11pt" padding="5px 10px"/>
                </div>
            </div>
            <div class="summaryContainer">
                <h3>
                    Report Summary for 04/23/2024
                </h3>
                <div class="summarySubContainer">
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
        <section class="sectionContainer bottomSection">
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
    }
    .topSection {
        width: 80%;
        padding-top: 0px;
        /* border: 1px solid yellow; */
        box-sizing: border-box;
        flex-wrap: wrap;
    }
    .bottomSection {
        padding: 40px 0px;
        border-bottom: 2px solid #a46d39;
    }

    .inputContainer {
        width: max-content;
        height: max-content;
        display: flex;
        align-items: flex-end;
        margin-bottom: 40px;
        /* border: 1px solid blue; */
    }
    .dateSelectContainer {
        /* border: 1px solid yellow; */
        height: max-content;
    }
    .btnContainer {
        /* border: 1px solid red; */
        margin-left: 20px;
        margin-right: auto;
        height: max-content;
        width: max-content;
    }

    .summaryContainer {
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
    .summarySubContainer {
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
