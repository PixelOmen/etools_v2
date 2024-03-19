<script context="module", lang="ts">
    export interface AnchorData {
        displayName: string;
        url: string;
    }
</script>

<script lang='ts'>
    export let data: AnchorData
</script>


<li>
    <a href={data.url}>
        {data.displayName}
    </a>
</li>


<style>
    a {
        text-decoration: none;
        color: rgb(225, 225, 225);
    }
    a:hover {
        text-decoration: underline;
    }
</style>