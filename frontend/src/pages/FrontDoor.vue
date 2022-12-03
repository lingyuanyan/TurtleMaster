<template>
    <div>
        <TopLine />
        <InformationBar />
        <DataList />
    </div>
</template>

<script>

import TopLine from "../components/topline.vue";
import InformationBar from "../components/information.vue";
import DataList from "../components/datalist.vue";
export default {
    name: "FrontDoor",
    props: {},

    data() {
        return {
        };
    },

    components: {
        TopLine,
        InformationBar,
        DataList,
    },

    created() { },
    mounted() {
    },
    methods: {
    },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">

</style>
