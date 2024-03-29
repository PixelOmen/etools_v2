<script context="module" lang="ts">
    import type { SvelteComponent } from 'svelte';
    import type { ListItemData } from '../shared/search/ListItem.svelte'
    import * as coms from '../../libs/coms';
</script>

<script lang="ts">
    import HeroSection from "../shared/sections/HeroSection.svelte";
    import SearchList from "../shared/search/SearchList.svelte";
    import Selected from "./Selected.svelte";
    import DateSelect from '../shared/dates/DateSelect.svelte';
    import FsInput from '../shared/filesystem/FSInput.svelte';
    import ImportantBtn from '../shared/ui/ImportantBtn.svelte';
    import FooterLinks from '../shared/sections/FooterLinks.svelte';

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

    let startDateComp: SvelteComponent;
    let endDateComp: SvelteComponent;
    let timezoneComp: SvelteComponent;
    let outputDirComp: SvelteComponent;

    async function submit() {
        startDateComp.clearError();
        endDateComp.clearError();
        outputDirComp.clearError();

        let start = startDateComp.getValue();
        if (!start) {
            startDateComp.setError();
        }

        let end = endDateComp.getValue();
        if (!end) {
            endDateComp.setError();
        }

        let outputDir = outputDirComp.getValue();
        if (!outputDir) {
            outputDirComp.setError();
        }

        if (!(start && end && outputDir)) {
            return;
        }
        let tz = timezoneComp.getValue();

        let data = {
            "startDate": start,
            "endDate": end,
            "timezone": tz,
            "outputDir": outputDir
        }

        let res = coms.submitJSON('/api/submit', data);
        res.then(jsonres => console.log(jsonres));

    }
</script>

<main>
    <HeroSection>
        <div class="certSection">
            <div style="width: 40%">
                {#if {certData}}
                    <SearchList listData={certData}
                        bind:selected={selectedCert}
                        header="Certificate"
                        boxHeight="200px"
                        searchPlaceholder="Search Certs"/>
                {/if}
                <Selected selected={selectedCert}/>
            </div>
            <div style="width: 40%">
                {#if {dkdmData}}
                    <SearchList listData={dkdmData}
                        bind:selected={selectedDKDM}
                        header="CPL DKDM"
                        boxHeight="200px"
                        searchPlaceholder="Search CPLs"/>
                {/if}
                <Selected selected={selectedDKDM}/>
            </div>
        </div>
    </HeroSection>
    <section class="dateSection">
        <div class="sectionContainer">
            <div class="dateContainer">
                <DateSelect bind:this={startDateComp}/>
                <DateSelect bind:this={endDateComp} header="End"/>
                <DateSelect bind:this={timezoneComp} isTimezone={true} header="Timezone"/>
            </div>
            <div class="fileContainer">
                <FsInput bind:this={outputDirComp} header="Output"/>
                <ImportantBtn on:click={submit} content="Submit"/>
            </div>
        </div>
    </section>
    <footer class="footerSection">
        <div class="footerContainer">
            <hr>
            <FooterLinks/>
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
        display: flex;
        justify-content: center;
        width: 100%;
        gap: 4%;
        margin-left: auto;
        margin-right: auto;
    }

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