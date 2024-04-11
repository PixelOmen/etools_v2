<script context="module" lang="ts">
    import type { SvelteComponent } from 'svelte';
    import type { ListItemData } from '../shared/search/ListItem.svelte'
    import type { KDMHistory } from './kdmHistory'
    import * as coms from '../../libs/coms';
</script>

<script lang="ts">
    import Browser from '../shared/filesystem/browser/Browser.svelte';
    import LoadingIcon from '../shared/ui/LoadingIcon.svelte';
    import ErrorModal from '../shared/ui/ErrorModal.svelte';
    import HeroSection from "../shared/sections/HeroSection.svelte";
    import CertificateIcon from "../../assets/certificate.svg";
    import FolderIcon from "../../assets/folderIcon.svg"
    import SearchList from "../shared/search/SearchList.svelte";
    import Selected from "./Selected.svelte";
    import DateSelect from '../shared/dates/DateSelect.svelte';
    import FsInput from '../shared/filesystem/FSInput.svelte';
    import ImportantBtn from '../shared/ui/ImportantBtn.svelte';
    import DataTable from '../shared/tables/DataTable.svelte';
    import { historyHeaders } from './tableHeaders';
    import FooterLinks from '../shared/sections/FooterLinks.svelte';

    let certData: ListItemData[] = [];
    fetch('/api/certs')
        .then(res => res.json())
        .then(data => {certData = data});

    let dkdmData: ListItemData[] = [];
    fetch('/api/dkdms')
        .then(res => res.json())
        .then(data => {dkdmData = data});

    let historyData: KDMHistory[] = [];
    function updateHistory(): void {
        fetch('api/kdm/history')
            .then(res => res.json())
            .then(data => {
                historyData = data;
            });
    }
    updateHistory();
    $: tableData = historyData;

    let showLoading = false;

    let errorModal: SvelteComponent;
    let selectedCertElem: SvelteComponent;
    let selectedDKDMElem: SvelteComponent;
    let selectedCertValue: ListItemData | null = null; 
    let selectedDKDMValue: ListItemData | null = null;

    let startDateComp: SvelteComponent;
    let endDateComp: SvelteComponent;
    let timezoneComp: SvelteComponent;
    let outputDirComp: SvelteComponent;

    function showError(e: CustomEvent): void {
        errorModal.setError(e.detail);
        errorModal.show();
    }

    function closeError() {
        errorModal.hide();
    }

    async function submit() {
        startDateComp.clearError();
        endDateComp.clearError();
        outputDirComp.clearError();
        selectedCertElem.clearError();
        selectedDKDMElem.clearError();

        if (!selectedCertValue) {
            selectedCertElem.setError();
        }

        if (!selectedDKDMValue) {
            selectedDKDMElem.setError();
        }        

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

        if (!(
            selectedCertValue &&
            selectedDKDMValue &&
            start && end && outputDir
        )) {
            return;
        }
        
        let tz = timezoneComp.getValue();

        let data = {
            "cert": selectedCertValue,
            "dkdm": selectedDKDMValue.displayName,
            "startDate": start,
            "endDate": end,
            "timezone": tz,
            "outputDir": outputDir
        }

        showLoading = true;
        coms.submitJSON('/api/kdm/submit', data).then(res => {
            console.log(res.status);
            updateHistory();
            showLoading = false;
        });
    }
</script>


<main id="main">
    <Browser/>
    <ErrorModal bind:this={errorModal} on:click={closeError}/>
    <HeroSection>
        <div class="certSection">
            <div style="width: 40%">
                {#if {certData}}
                    <SearchList listData={certData}
                        bind:selected={selectedCertValue}
                        header="Certificate"
                        boxHeight="200px"
                        searchPlaceholder="Search Certs"
                        fileIcon={CertificateIcon}
                        dirIcon={FolderIcon}
                    />
                {/if}
                <Selected bind:this={selectedCertElem} selected={selectedCertValue}/>
            </div>
            <div style="width: 40%">
                {#if {dkdmData}}
                    <SearchList listData={dkdmData}
                        bind:selected={selectedDKDMValue}
                        header="CPL DKDM"
                        boxHeight="200px"
                        searchPlaceholder="Search CPLs"/>
                {/if}
                <Selected bind:this={selectedDKDMElem} selected={selectedDKDMValue}/>
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
                <div style="width: 130px; margin-right: auto; margin-left: auto;">
                {#if showLoading}
                    <LoadingIcon width="18px" height="18px"/>
                {:else}
                    <ImportantBtn on:click={submit} content="Submit"/>
                {/if}
                </div>
            </div>
        </div>
    </section>
    {#if historyData.length > 0}
        <section class="historySection">
            <div class="sectionContainer">
                <h3 id="historyHeader">
                    History
                </h3>
                <DataTable
                    headers={historyHeaders}
                    tableData={tableData}
                    on:tableCellClick={showError}/>
            </div>
        </section>
    {/if}
    <footer class="footerSection">
        <div class="footerContainer">
            <hr>
            <FooterLinks/>
        </div>
    </footer>
</main>

<style>
    main {
        position: relative;
        min-width: 950px;
    }

    .certSection {
        display: flex;
        justify-content: space-around;
        gap: 20px;
        max-width: 80%;
        margin-left: auto;
        margin-right: auto;
    }

    .sectionContainer {
        display: flex;
        justify-content: space-around;
        flex-wrap: wrap;
        width: 80%;
        margin-left: auto;
        margin-right: auto;
        gap: 20px;
    }

    .dateSection {
        padding: 20px 0px;
        width: 100%;
        background: linear-gradient(310deg, #197a87 0%, #652a6f 99%);
        color: #45c2b7;
        color: #0d4149;
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

    .historySection {
        padding: 20px 0px;
        width: 100%;
        background: radial-gradient(ellipse at 50% -10%, #16323a 0%, #12232E 50%, transparent), 
                    linear-gradient(0deg, #12232E 10%, #5a2251 99%);
        
    }
    #historyHeader {
        margin: 0;
    }

    .footerSection {
        background: linear-gradient(#12232E 0%, #0e1f25 100%, transparent);   
    }
    
    .footerContainer {
        width: 80%;
        padding-top: 50px;
        padding-bottom: 10px;
        margin-left: auto;
        margin-right: auto;
    }
    hr {
        width: 100%;
        margin-top: 0px;
        margin-bottom: 20px;
    }
</style>