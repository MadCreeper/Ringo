<template>
  {{needs}}
<div v-for="need in needs" :key="need">
  {{need}}
</div>
<el-card v-for="need in needs" :key="need">
  {{need.title}}
  {{need.author}}
</el-card>

</template>

<script setup>
</script>
<script>
import { getNeeds } from '../api/index';
export default {
  data() {
    return {
      ButtonLeft: "求助",
      ButtonRight: "我的提供",
      needs : [
        {'title': "Help", 'author': "tom"}
      ],
    }
  },
  methods: {
    loadNeeds () {
      getNeeds().then(response => {
        this.needs = response.data
        console.log(this.needs)
      })
    }
  },
  created: function () {
    console.log("hello")
    this.loadNeeds()
  },
  
}
</script>
<style scoped>
</style>
