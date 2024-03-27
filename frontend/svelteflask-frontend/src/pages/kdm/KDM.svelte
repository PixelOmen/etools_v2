<script context="module" lang="ts">
    import type { ListItemData } from '../shared/search/ListItem.svelte'
</script>

<script lang="ts">
    import HeroSection from "../shared/sections/HeroSection.svelte";
    import SearchList from "../shared/search/SearchList.svelte";
    import DateSelect from '../shared/dates/DateSelect.svelte';
    import Selected from "./Selected.svelte";
    import { listData } from "../../TestData";

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
        <div class="fileSelect">
            <div style="width: 40%">
                <SearchList {listData}
                    header="Certificate"
                    boxHeight="200px"
                    searchPlaceholder="Search Certs"
                    on:searchItemSelected={itemSelected}/>
                <Selected selected={selectedCert}/>
            </div>
            <div style="width: 40%">
                <SearchList {listData}
                    header="CPL DKDM"
                    boxHeight="200px"
                    searchPlaceholder="Search CPLs"
                    on:searchItemSelected={itemSelected}/>
                <Selected selected={selectedDKDM}/>
            </div>
        </div>
    </HeroSection>
    <section class="dateSection">
        <div class="formContainer">
            <div class="dateContainer">
                <DateSelect width=300px/>
                <DateSelect width=300px header="To"/>
            </div>
        </div>
    </section>
    <footer>

    </footer>
</main>

<style>
    main {
        min-width: 950px;
    }
    .fileSelect {
        /* border: 1px solid blue; */
        display: flex;
        justify-content: space-around;
        gap: 20px;
        max-width: 80%;
        margin-left: auto;
        margin-right: auto;
        overflow: hidden;
    }
    .dateSection {
        padding-top: 20px;
        /* padding-left: 4%; */
        width: 100%;
        height: 200px;
        background: linear-gradient(310deg, #197a87 0%, #652a6f 99%);
    }
    .dateContainer {
        border: 1px solid blue;
        display: flex;
        justify-content: space-around;
        max-width: 80%;
        margin-left: auto;
        margin-right: auto;
    }

    footer {
        height: 200px;
    }
</style>