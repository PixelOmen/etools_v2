<script lang="ts">
    import * as coms from "../../libs/coms"
    import type { SvelteComponent } from 'svelte';
    import HeroSection from "../shared/sections/HeroSection.svelte";
    import DateSelect from "../shared/dates/DateSelect.svelte";
    import ImportantBtn from "../shared/ui/ImportantBtn.svelte";
    import PieChart from "../shared/charts/pie/PieChart.svelte";
    import FooterLinks from "../shared/sections/FooterLinks.svelte";

    let dateSelect: SvelteComponent;
    let tomorrowString = "";

    fetch("http://10.0.30.24:8080/api/nextdate")
    .then(res => res.json())
    .then((jsoninfo) => {
        tomorrowString = jsoninfo.standardDate;
    });

    function test() {
        console.log(dateSelect.getValue());
    }
</script>

<main>
    <HeroSection paddingBottom="0px" paddingTop="100px">
        <section class="sectionContainer topSection">
            <div class="summaryContainer">
                <div class="summaryHeaderContainer">
                    <h3 class="summaryHeaderText">
                        Schedule Summary for {tomorrowString}
                    </h3>
                    <div class="inputContainer">
                        <div class="dateSelectContainer">
                            <DateSelect bind:this={dateSelect}
                                padding="3px 15px"
                                header=""
                                dateOnly={true}
                            />
                        </div>
                        <div class="btnContainer">
                            <ImportantBtn on:click={test}
                                content="Generate"
                                fontSize="11pt"
                                padding="5px 10px"
                            />
                        </div>
                    </div>
                </div>
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
<FooterLinks paddingTop="30px" showBorder={false}/>


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
        box-sizing: border-box;
        align-items: center;
        flex-direction: column;
    }
    .bottomSection {
        padding: 50px 0px;
        border-bottom: 2px solid #cbcbcb;
    }

    .summaryHeaderContainer {
        display: flex;
        align-items: center;
    }
    h3 {
        margin: 0;
        padding: 0;
        font-family: "Montserrat";
    }
    .inputContainer {
        margin-left: auto;
        margin-right: 20px;
        width: max-content;
        height: max-content;
        display: flex;
        align-items: flex-end;
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
        background-color: rgba(85, 85, 85, 0.124);
        border: 2px solid rgb(122, 122, 122);
        border-radius: 20px;
        padding: 10px;
        max-width: 1000px;
        font-family: "Montserrat";
    }
    .summaryHeaderText {
        margin: 0;
        margin: 10px;
        margin-left: 20px;
        padding: 0;
        font-family: "Montserrat";
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
