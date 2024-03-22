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
        }        
    ]
</script>

<main>
    <HeroSection>
        <SearchList {listData} header="Certificates"/>
    </HeroSection>
</main>