<template>
  {{needs}}
<div v-for="need in needs" :key="need">
  {{need}}
</div>
<el-card v-for="need in needs" :key="need">
  {{need.title}}
  {{need.author}}
</el-card>
<el-switch
    v-model="value6"
    class="ml-2"
    width="60"
    inline-prompt
    active-text="超出省略"
    inactive-text="超出省略"
  />
</template>

<script setup>
</script>
<script>
import { getNeeds } from '../api/index';
import { onMounted, ref } from 'vue';
const value6 = ref(true);
export default {
  setup () {
     onMounted(() => {
       console.log('mounted in the composition api!')
     })
   },
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
