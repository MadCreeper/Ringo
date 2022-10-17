<template>
  <div class="common-layout">
    <el-container>
      <el-header>Header</el-header>
      <el-main>
      <p>Main</p>
      <Grid></Grid>
      </el-main>
      <el-footer>Footer</el-footer>
    </el-container>
  </div>
</template>
<script>
    import Grid from './HelloWorld.vue'
    export default {
    components: {Grid},
  }
</script>