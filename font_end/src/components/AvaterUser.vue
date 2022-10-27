 <template>
    <div class="demo-basic--circle">
    <div class="block">
        <el-avatar class="avater" :size="AvaterSize" :src="circleUrl" @click="redirect"></el-avatar>
    </div>
    <div>
    </div>
    </div>
</template>

<script setup>
import { reactive, toRefs } from 'vue'

const state = reactive({
  circleUrl:
    'https://cube.elemecdn.com/3/7c/3ea6beec64369c2642b92c6726f1epng.png',
})
const {circleUrl} = toRefs(state)

</script>
<script>
export default {
  inject: ['message'],
  props:{
    AvaterSize:[Number, String],
  },
  methods: {
    redirect(){
      this.$router.push(this.message)
    },
    CheckProps(){
      this.Check=!this.Check
    },
  },
}
</script>
<style scoped>
.demo-basic {
  text-align: center;
}
.demo-basic .demo-basic--circle{
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.demo-basic .block:not(:last-child) {
  border-right: 10px solid var(--el-border-color);
}
.demo-basic .el-col:not(:last-child) {
  border-right: 10px solid var(--el-border-color);
}
</style>