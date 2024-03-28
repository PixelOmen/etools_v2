<script lang='ts'>
    import NavAnchor from "../nav/NavAnchor.svelte";
    import type { AllNavSections } from "../nav/NavBar.svelte"

    let allsections: AllNavSections = [];
    fetch("/api/nav")
        .then(res => res.json())
        .then(output => allsections = output);
</script>

<nav>
    {#each allsections as footerSection}
        <section>
            <h3>
                {footerSection.sectionName}
            </h3>
            <ul>
                {#each footerSection.contents as data}
                    <NavAnchor {data}/>
                {/each}
            </ul>
        </section>
    {/each}
</nav>

<style>
    nav {
        display: flex;
        justify-content: space-around;
        width: 100%;
        margin-left: auto;
        margin-right: auto;
    }
    h3 {
        font-weight: bold;
        margin: 10px 0px;
    }
    ul {
        font-size: 10pt;
    }
</style>