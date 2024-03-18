<script context="module" lang='ts'>
    interface AnchorData {
        displayName: string;
        url: string;
    }
    export type SectionData = AnchorData[];
</script>

<script lang="ts">
    let sectionVisible: boolean = false;

    function toggleSection(): void {
        sectionVisible = sectionVisible ? false : true;
    }

    export let sectionData: SectionData;
    export let displayText: string;
</script>

<li class="navSection">
    <button on:click={toggleSection}>{displayText}&#9207;</button>
    <ul style="display: {sectionVisible ? 'flex' : 'none'}">
        {#each sectionData as data}
            <li>
                <a href={data.url}>{data.displayName}</a>
            </li>
        {/each}
    </ul>
</li>

<style>
    a {
        text-decoration: none;
        color: rgb(225, 225, 225);
    }
    a:hover {
        text-decoration: underline;
    }

    button {
        cursor: pointer;
        border: none;
        outline: none;
        background: none;
        color: rgb(225, 225, 225);
        font-size: inherit;
        font-family: inherit;
        transition: color 0.3s;
    }
    button:hover {
        color: rgb(179, 179, 179);
    }

    .navSection {
        position: relative;
    }

    ul {
        position: absolute;
        border: solid 1px purple;
        width: max-content;
        padding: 10px;
    }
</style>