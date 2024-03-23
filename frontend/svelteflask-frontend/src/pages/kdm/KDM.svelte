<script lang="ts">
    import HeroSection from "../shared/sections/HeroSection.svelte";
    import SearchList from "../shared/search/SearchList.svelte";

    let listData = [
        {
            displayName: "Item1.pem",
            filePath: "Fake/file/path/item1.pem"
        },
        {
            displayName: "Item2.pem",
            filePath: "Fake/file/path/item1.pem"
        },
        {
            displayName: "Item3.pem",
            filePath: "Fake/file/path/item1.pem"
        },
        {
            displayName: "Item1.pem",
            filePath: "Fake/file/path/item1.pem"
        },
        {
            displayName: "Item2.pem",
            filePath: "Fake/file/path/item1.pem"
        },
        {
            displayName: "Item3.pem",
            filePath: "Fake/file/path/item1.pem"
        },
        {
            displayName: "Item1.pem",
            filePath: "Fake/file/path/item1.pem"
        },
        {
            displayName: "Item2.pem",
            filePath: "Fake/file/path/item1.pem"
        },
        {
            displayName: "Item3.pem",
            filePath: "Fake/file/path/item1.pem"
        },                
    ]
</script>

<main>
    <HeroSection>
        <div class="fileSelect">
            <SearchList {listData} header="Certificates" searchPlaceholder="Search Certs"/>
            <SearchList {listData} header="CPL DKDM" searchPlaceholder="Search CPLs"/>
        </div>
    </HeroSection>
</main>

<style>
    main {
        /* border: 1px solid red; */
        min-width: 950px;
    }
    .fileSelect {
        max-width: 70%;
        margin-left: auto;
        margin-right: auto;
        display: flex;
        justify-content: space-around;
        gap: 20px;
    }
</style>