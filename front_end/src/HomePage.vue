<template>
  <div class="common-layout">
    <el-container>
      <el-header id="headerBack" height="200px">
        <div >
          <div v-if="titleImgUrl">
                <!-- {{offering.goods_desc}} -->
                
              <img src="src/assets/L.png" width="100" />
              Our logo / app name text here 
          </div>
        </div>
        <div class="header-searchbar">
          <el-input v-model="search_text" placeholder="请输入搜索内容" class="input">
            <template #append>
              <el-button :icon="Search" @click="getBySearch(search_text)" />
            </template>
          </el-input>
        </div>
        <div class="header-bottom">
          <el-row :gutter="20" type="flex">
            <el-col :span="8">
              <el-select v-model="sort_method" class="m-2" placeholder="默认排序" size="small"
                @change="getSorted(sort_method)">
                <el-option v-for="item in sort_options" :key="item.value" :label="item.label" :value="item.value" />
              </el-select>
            </el-col>
            <el-col :span="3">
              <el-switch v-model="fill" class="ml-2" inline-prompt
                style="--el-switch-on-color: #13ce66; --el-switch-off-color: #339933" active-text="展开"
                inactive-text="折叠" />
            </el-col>
            <el-col :span="1" :offset="10" type="flex">
              <div class="x-right">
              <AvaterUsr></AvaterUsr>
            </div>
            </el-col>

          </el-row>
        </div>

      </el-header>

      <el-main id="MainBack">
        <div>

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
                  {{ formatDateTime(need.expected_end_time) }}
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
// import Navigator from './components//NavigationBar.vue'
import { getGoods } from '../api/api';
import { emergency_levels, sort_options } from './dataTypes'
import { formatDateTime } from './utils'
import AvaterUsr from './components/AvaterUser.vue'
import { Search } from '@element-plus/icons-vue'
import {titleImgUrl} from './resources'

export default {
  components: { foo, AvaterUsr },
  data() {
    return {
      ButtonLeft: "求助",
      ButtonRight: "我的提供",
      needs: [
      ],
      test_tags: ["tag1", "tag2", "tag3"],
      sort_options,
      sort_method: "默认排序",
      search_text: ""
    }
  },
  mounted: function () {
    this.loadNeeds()
  },
  methods: {
    loadNeeds(params) {
      getGoods(params).then(response => {
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
    getSorted(sort_method) {
      console.log("sort method:" + sort_method)
      this.loadNeeds({
        "search": this.search_text,
        "ordering": sort_method
      })
    },
    getBySearch(search_text) {
      this.loadNeeds({
        "search": search_text,
        "ordering": this.sort_method
      })
    },
    formatDateTime,
  },
  provide() {
    return {
      message: '/info',
      messageFooLeft: '/',
      messageFooRight: '/offer',
      messageFooMid: '/request',
    }
  }
}
</script>
<style scoped>
.el-header {
  display: flex;
  flex-direction: column;
}

.el-container {
  height: 100vh;
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
  margin-bottom: 5px;
  background: #a1d9ea url("https://i.328888.xyz/2022/12/29/UPVpL.png") center center no-repeat;
  background-position: center;
  background-size: cover;
  background-size: auto 100%;
}

#MainBack {
  background: rgb(229, 250, 231);
  background-size: cover;
}

#FooterBack {
  /* background: #fff url("https://th.bing.com/th/id/OIP.Oc9mYdpG25SBa-pRljEXwAHaEK?pid=ImgDet&w=1500&h=844&rs=1") no-repeat; */
  background: rgb(229, 250, 231);
  background-size: cover;
}
</style>





<style src="./css/header.css"  lang="css" scoped />