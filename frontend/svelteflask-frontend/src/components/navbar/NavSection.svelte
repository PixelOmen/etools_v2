<script context="module" lang='ts'>
    interface AnchorData {
        displayName: String;
        url: String;
    }
    
    export type SectionData = AnchorData[];
</script>

<script lang="ts">

    let sectionVisible: boolean = false;

    export let sectionData: SectionData;
    export let displayText: String;
</script>

<button>
    {displayText}
    
</button>