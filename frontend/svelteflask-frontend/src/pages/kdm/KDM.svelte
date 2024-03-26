<script context="module" lang="ts">
    import type { ListItemData } from '../shared/search/ListItem.svelte'
</script>

<script lang="ts">
    import HeroSection from "../shared/sections/HeroSection.svelte";
    import SearchList from "../shared/search/SearchList.svelte";
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
</main>

<style>
    main {
        min-width: 950px;
    }
    .fileSelect {
        max-width: 80%;
        margin-left: auto;
        margin-right: auto;
        display: flex;
        justify-content: space-around;
        gap: 20px;
        overflow: hidden;
    }
</style>