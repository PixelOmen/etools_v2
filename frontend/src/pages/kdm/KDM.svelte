<script context="module" lang="ts">
    import type { ListItemData } from '../shared/search/ListItem.svelte'
</script>

<script lang="ts">
    import HeroSection from "../shared/sections/HeroSection.svelte";
    import SearchList from "../shared/search/SearchList.svelte";
    import DateSelect from '../shared/dates/DateSelect.svelte';
    import FsInput from '../shared/filesystem/FSInput.svelte';
    import Timezone from '../shared/dates/Timezone.svelte';
    import Selected from "./Selected.svelte";
    import Footer from '../shared/sections/Footer.svelte';

    let certData: ListItemData[] = [];
    fetch('/api/certs')
        .then(res => res.json())
        .then(data => {certData = data});

    let dkdmData: ListItemData[] = [];
    fetch('/api/dkdms')
        .then(res => res.json())
        .then(data => {dkdmData = data});

    let selectedCert: ListItemData | null = null; 
    let selectedDKDM: ListItemData | null = null;
    function itemSelected(e: CustomEvent) {
        if (e.detail.header == "Certificate") {
            selectedCert = e.detail.data;
        } else {
            selectedDKDM = e.detail.data;
        }
    }
</script>

<main>
    <HeroSection>
        <div class="certSection">
            <div style="width: 40%">
                {#if {certData}}
                    <SearchList listData={certData}
                        header="Certificate"
                        boxHeight="200px"
                        searchPlaceholder="Search Certs"
                        on:searchItemSelected={itemSelected}/>
                {/if}
                <Selected selected={selectedCert}/>
            </div>
            <div style="width: 40%">
                {#if {certData}}
                    <SearchList listData={dkdmData}
                        header="CPL DKDM"
                        boxHeight="200px"
                        searchPlaceholder="Search CPLs"
                        on:searchItemSelected={itemSelected}/>
                {/if}
                <Selected selected={selectedDKDM}/>
            </div>
        </div>
    </HeroSection>
    <section class="dateSection">
        <div class="sectionContainer">
            <div class="dateContainer">
                <DateSelect/>
                <DateSelect header="End"/>
                <Timezone/>
            </div>
            <div class="fileContainer">
                <FsInput header="Output"/>
                <button class="submitBtn">
                    Submit
                </button>
            </div>
        </div>
    </section>
    <footer class="footerSection">
        <div class="footerContainer">
            <hr>
            <Footer/>
        </div>
    </footer>
</main>

<style>
    main {
        min-width: 950px;
    }

    .certSection {
        /* border: 1px solid blue; */
        display: flex;
        justify-content: space-around;
        gap: 20px;
        max-width: 80%;
        margin-left: auto;
        margin-right: auto;
        overflow: hidden;
    }

    .sectionContainer {
        display: flex;
        justify-content: space-around;
        flex-wrap: wrap;
        /* border: 1px solid yellow; */
        width: 80%;
        margin-left: auto;
        margin-right: auto;
        gap: 20px;
    }

    .dateSection {
        padding: 20px 0px;
        width: 100%;
        background: linear-gradient(310deg, #197a87 0%, #652a6f 99%);
    }
    .dateContainer {
        /* border: 1px solid green; */
        /* margin-left: 5%; */
        /* flex-direction: row; */
        display: flex;
        justify-content: center;
        width: 100%;
        gap: 4%;
        margin-left: auto;
        margin-right: auto;
    }
    /* @media (min-width: 1000px) {
        .dateContainer {
            margin-left: 0;
            flex-direction: column;
            width: 30%;
            gap: 15px;
        }
        .sectionContainer {
            gap: 0px;
        }
    } */

    .fileContainer {
        /* border: 1px solid green; */
        display: flex;
        align-items: flex-end;
        width: 90%;
        padding: 5px;
        gap: 10px
    }
    @media (min-width: 1200px) {
        .fileContainer {
            max-width: 60%;
        }
    }
    .submitBtn {
        cursor: pointer;
        padding: 3px 15px;
        /* border: 4px solid rgb(71, 71, 71); */
        border: none;
        outline: none;
        border-radius: 5px;
        font-size: 13pt;
        filter: drop-shadow(1px 5px 5px rgba(0, 0, 0, 0.3));
        background: linear-gradient(45deg, #923214, #ce4820 99%);
        color: rgb(228, 228, 228);
        font-family: inherit;
        font-weight: 900;
    }
    .submitBtn:hover {
        background: linear-gradient(45deg, #ce4820, #ce4820 99%);
    }
    .submitBtn:active {
        background: #ad3e1c;
        filter: drop-shadow(1px 5px 5px rgba(0, 0, 0, 0.0));
    }

    .footerSection {
        /* border: 1px solid yellow; */
        background: radial-gradient(ellipse at 10% -10%, #163139 0%, #12232E 40%, transparent),
                    radial-gradient(ellipse at 90% 120%, #163139 0%, #12232E 40%);
    }
    
    .footerContainer {
        width: 80%;
        padding-top: 50px;
        margin-left: auto;
        margin-right: auto;
    }
    hr {
        width: 100%;
        margin-top: 0px;
        margin-bottom: 20px;
    }
</style>