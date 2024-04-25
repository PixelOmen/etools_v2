<script lang="ts">
    import * as coms from "../../libs/coms"
    import type { SvelteComponent } from 'svelte';
    import type { ClientInfo } from "../shared/charts/pie/PieChart.svelte";
    import LoadingIcon from '../shared/ui/LoadingIcon.svelte';
    import HeroSection from "../shared/sections/HeroSection.svelte";
    import DateSelect from "../shared/dates/DateSelect.svelte";
    import ImportantBtn from "../shared/ui/ImportantBtn.svelte";
    import PieChart from "../shared/charts/pie/PieChart.svelte";
    import FooterLinks from "../shared/sections/FooterLinks.svelte";

    let dateSelect: SvelteComponent;
    let tomorrowString = "";
    let summaryLoading = true;
    let generateLoading = false;
    let summaryError = false;
    let summaryClients: ClientInfo[] = [];
    let summaryEquipment = "";
    let summaryRooms = "";
    let summaryJobs = "";
    let noJobs = false;

    fetch("/api/nextdate")
    .then(res => res.json())
    .then((jsoninfo) => {
        tomorrowString = jsoninfo.standardDate;
    });

    fetch("/api/schedulestats")
    .then(res => res.json())
    .then((jsoninfo) => {
        if (jsoninfo.err) {
            summaryError = true;
        } else {
            summaryLoading = false;
            if (jsoninfo.clients.length < 1) {
                noJobs = true;
                summaryEquipment = "N/A";
                summaryRooms = "N/A";
                summaryJobs = "N/A";
                
            } else {
                summaryClients = jsoninfo.clients;
                summaryEquipment = jsoninfo.equipment;
                summaryRooms = jsoninfo.rooms;
                summaryJobs = jsoninfo.jobs;
            }
        }
    });

    function submit() {
        let dateValue = dateSelect.getValue();
        if (!dateValue) return;
        
        generateLoading = true;

        const payload = {
            date: {
                from: dateValue,
                to: ""
            },
            type: "scheduling"
        }
        
        coms.submitJSON('/api/callsheet_query', payload)
        .then(res => res.json())
        .then((jsoninfo) => {
            generateLoading = false;
            if (jsoninfo.err) {
                console.error(jsoninfo.err);
            } else {
                window.open(`/api/callsheet_pdf/${jsoninfo.pdfurl}`, '_blank');
            }
        });
    }

  
</script>

<main>
    <HeroSection paddingBottom="0px" paddingTop="100px">
        <section class="sectionContainer topSection">
            <div class="summaryContainer">
                <div class="summaryHeaderContainer">
                    <h3 class="summaryHeaderText">
                        {#if summaryLoading}
                            Loading Summary...
                        {:else}
                            Schedule Summary for {tomorrowString}
                        {/if}
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
                            {#if generateLoading}
                                <LoadingIcon
                                    width="30px"
                                    height="30px"
                                    offsetLeft="30px"
                                />                            
                            {:else}
                                <ImportantBtn on:click={submit}
                                    content="Generate"
                                    fontSize="11pt"
                                    padding="5px 10px"
                                />
                            {/if}
                        </div>
                    </div>
                </div>
                <div class="summaryContentContainer">
                    <div class="statsContainer">
                        {#if summaryLoading}
                            Loading...
                        {:else}
                            <div>
                                Rooms: {summaryRooms}
                            </div>
                            <div>
                                Jobs: {summaryJobs}
                            </div>
                            <div>
                                Equipment: {summaryEquipment}
                            </div>
                        {/if}
                    </div>
                    <div class="chartContainer">
                        {#if summaryLoading}
                            <div class="summaryLoadingContainer">
                                <LoadingIcon
                                    width="60px"
                                    height="60px"
                                    offsetLeft="0px"
                                />
                            </div>
                        {:else if !noJobs}
                            <PieChart header="Clients"
                                clientInfo={summaryClients} pieHeight="150px"
                            />
                        {:else}
                            <div class="noJobsContainer">
                                No Jobs
                            </div>
                        {/if}                        
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
        border-bottom: 2px solid #a46d39;   
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
        padding: 40px 0px;     
        /* border-bottom: 2px solid #cbcbcb; */
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
        width: 95px;
    }

    .summaryContainer {
        background-color: rgba(85, 85, 85, 0.124);
        border: 2px solid rgb(122, 122, 122);
        border-radius: 20px;
        padding: 10px;
        max-width: 1000px;
        font-family: "Montserrat";
        min-height: 250px;
        min-width: 730px;
        display: flex;
        flex-direction: column;
    }
    .summaryHeaderText {
        margin: 0;
        margin: 10px;
        margin-left: 20px;
        padding: 0;
        font-family: "Montserrat";
    }
    .summaryContentContainer {
        margin-top: 20px;
        /* border: 1px solid red; */
    }
    .statsContainer {
        /* border: 2px solid blue; */
        font-size: 12pt;
        width: 100%;
        display: flex;
        justify-content: space-evenly;
        font-weight: bold;
        border-bottom: 1px solid grey;
        border-top: 1px solid grey;
    }
    .summaryLoadingContainer {
        width: max-content;
        margin: auto;
        margin-top: 40px;
    }
    .noJobsContainer {
        margin: auto;
        margin-top: 50px;
        font-family: "Montserrat";
        font-size: 14pt;
        width: max-content;
    }
    .chartContainer {
        /* border: 2px solid green; */
        border-radius: 20px;
        box-sizing: border-box;
    }
</style>
