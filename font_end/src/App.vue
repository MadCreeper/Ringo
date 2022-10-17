
<template>
  <el-button>I am ElButton</el-button>
  <container></container>
  <container_2></container_2>
</template>
<script>
  import container from './components/ContainerOne.vue'
  import container_2 from'./components/ContainerTwo.vue'
  import { ElButton } from 'element-plus'
  export default {
    components: {ElButton,container,container_2},
  }

</script>
