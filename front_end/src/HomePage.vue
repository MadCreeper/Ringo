<template>
  <div class="common-layout">
    <el-container>
      <el-header id="headerBack" height="200px">
        <Navigator :msg="redirect" />
      </el-header>
      <el-main id="MainBack">
        <div>
          <div style="margin-bottom: 15px">Switch:
            <el-switch v-model="fill" />
          </div>
          <el-space :fill="fill" wrap>
            <el-card @click="gotoDetails(need.goods_sn)" v-bind:class="{ 'box-card': fill, 'box-card-fold': !fill }"
              v-for="need in needs" :key="need">
              <template #header>
                <div v-bind:class="{ 'card-header': fill, 'card-header-fold': !fill }">
                  <!-- switch styles for fill or not fill -->
                  <div class="name">
                    <span>{{ need.name }}</span>
                  </div>
                  <div class="line-break"></div>

                  <div class="tags">
                    <el-tag class="ml-2" type="success" v-if="need.category">{{ need.category.name }}</el-tag>
                    <el-tag class="ml-2" type="danger">{{ emergency_levels[need.emergency] }}</el-tag>
                  </div>

                  <div class="line-break"></div>


                  <!-- <div class="tags">
                    <div v-for="tag in need.tags" :key="tag">
                      <el-tag class="ml-2" type="success">{{ tag }}</el-tag>
                    </div>
                  </div> -->

                </div>
                <div class="username-display">
                  用户：{{ need.user }}
                </div>
              </template>
              <!-- user name -->
              <div>

              </div>

              <!-- 简介 -->
              <div v-snip:js="3">
                {{ need.goods_brief }}
              </div>
              <div>
                <el-icon>
                  <House />
                </el-icon> {{ "地址: " + need.address }}
              </div>
              <div class="submit-time">
                {{ formatDateTime(need.add_time) }}
                <div v-if="need.expected_end_time">
                  {{ formatDateTime(need.expected_end_time)}}
                </div>
              </div>
            </el-card>
          </el-space>
        </div>
      </el-main>
      <el-footer id="FooterBack">
        <foo :ButtonLeft="ButtonLeft" :ButtonRight="ButtonRight"></foo>
      </el-footer>
    </el-container>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
const fill = ref(true)
onMounted(() => {
    console.log("hello mainpage")
})
</script>
<script>
import foo from './components/FooterGrid.vue'
import Navigator from './components//NavigationBar.vue'
import { getGoods } from '../api/api';
import { emergency_levels } from './dataTypes'
import { formatDateTime } from './utils'



export default {
  components: { foo, Navigator },
  data() {
    return {
      ButtonLeft: "求助",
      ButtonRight: "我的提供",
      needs: [
      ],
      test_tags: ["tag1", "tag2", "tag3"],
    }
  },
  mounted: function (){
    this.loadNeeds()
  },
  methods: {
    loadNeeds() {
      getGoods().then(response => {
        this.needs = response.data.results;
        console.log("needs:")
        console.log(this.needs);
      })
      .catch(
        err => {
          console.log(err)
          this.$router.push('/login')
        }
      )
    },
    gotoDetails(need_id) {
      this.$router.push({
        path: '/details',
        query: {
          id: need_id
        }
      })
      console.log("test details")
    },
    formatDateTime,
  },
  provide() {
    return {
      message: '/info',
      messageFooLeft: '/request',
      messageFooRight: '/offer',
      messageFooMid: '/request',
    }
  }
}
</script>
<style scoped>
.el-container {
  height: 95vh;
}

.box-card {
  width: 80vw;
  text-overflow: ellipsis;
}

.box-card-fold {
  width: 40vw;
  height: fit-content;
  text-overflow: ellipsis;
}

.card-header {
  display: flex;
  flex-direction: row;
}

.card-header .name {
  display: flex;
  justify-content: flex-start;
  align-items: center;
}

.card-header .tags {
  display: flex;
  margin-left: auto;
  align-items: center;
  gap: 10px;
}

.card-header-fold {
  display: flex;
  flex-direction: column;
}

.card-header-fold .name {
  width: 100%;
  display: flex;
  justify-content: flex-start;
  align-items: center;
}

.card-header-fold .tags {
  width: 100%;
  display: flex;
  margin-left: auto;
  align-items: flex-start;
  gap: 5px;
}

.username-display {
  font-size: small;
  color: dimgray;
}

.submit-time {
  text-align: right;
  font-size: smaller;
  color: dimgray;
}

#headerBack {
  margin-bottom: 20px;
  background: #fff url("https://uploadfile.bizhizu.cn/up/cc/d0/87/ccd08766b03deca06263f0d8e0013dec.jpg") no-repeat;
  background-size: cover;
}

#MainBack {
  background: linear-gradient(0deg, rgb(213, 255, 216) 0%, rgb(240, 240, 240) 100%);
  background-size: cover;
}

#FooterBack {
  /* background: #fff url("https://th.bing.com/th/id/OIP.Oc9mYdpG25SBa-pRljEXwAHaEK?pid=ImgDet&w=1500&h=844&rs=1") no-repeat; */
  background-size: cover;
}
</style>