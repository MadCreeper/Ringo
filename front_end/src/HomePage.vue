<template>
  <div class="common-layout">
    <el-container>
      <el-header id="headerBack" height="220px">
        <el-row>
        <el-col :span=6>
          <div v-if="titleImgUrl">
            <img src="http://127.0.0.1:8000/media_url/ringo_new.png" width="90" />
          </div>
        </el-col>
        <el-col :span=16>
        </el-col>
        <el-col :span=2>
       <div class="container">
        <div class="sunny"></div>
        </div>
        </el-col>
        </el-row>
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
            <el-col :span="12">
              <el-switch v-model="fill" class="ml-2" inline-prompt
                style="--el-switch-on-color: #13ce66; --el-switch-off-color: #339933" active-text="展开"
                inactive-text="折叠" /> <span style="font-size:small">切换展示模式</span>
            </el-col>
            <el-col :span="3" type="flex" id="avatar">
              <div class="x-right">
                <div class="block">
                  <el-avatar class="avater" size=80 :src=this.info.avatar @click="redirect"></el-avatar>
                </div>
              </div>
            </el-col>

          </el-row>
        </div>

      </el-header>

      <el-main id="MainBack">
        <div>
          <el-space :fill="fill" wrap :size=30>
            <el-card  @mouseenter="play" @click="gotoDetails(need.goods_sn)" :class="{ 'box-card': fill, 'box-card-fold': !fill }"
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
                简介：{{ need.goods_brief }}
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
import { getGoods, getRecommendation } from '../api/api';
import { getUserDetail } from '../api/api'
import { emergency_levels, sort_options } from './dataTypes'
import { formatDateTime } from './utils'
import { Search } from '@element-plus/icons-vue'
import { titleImgUrl } from './resources'
import { reactive } from 'vue'
export default {
  components: { foo },
  data() {
    return {
      
      showAnimate: false,

      ButtonLeft: "求助",
      ButtonRight: "我的提供",
      needs: [
      ],
      test_tags: ["tag1", "tag2", "tag3"],
      sort_options,
      sort_method: "默认排序",
      search_text: "",
      info: reactive({
        owner: "",
        nickname: "",
        avater: "",
        address: "",
        signature: ""
      }),
    }
  },
  mounted: function () {
    this.loadNeeds();
    this.loadinfo();
  },
  methods: {
    play() {
    this.showAnimate = true
    console.log(this.showAnimate);
    },
    redirect(){
      this.$router.push('/info')
    },
    loadNeeds(params) {
      if (params && params.ordering == "best_match") {
        getRecommendation().then(response => {
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
      }
      else {
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
      }
    },
    gotoDetails(need_id){
      setTimeout(() =>{
      this.$router.push({
        path: '/details',
        query: {
          id: need_id
        }
      })},600)
      console.log("test details")
    },
    getSorted(sort_method) {
      console.log("sort method:" + sort_method)
      this.loadNeeds({
        "search": this.search_text,
        "ordering": sort_method
      })
    },
    loadinfo() {
      getUserDetail().then(response => {
        this.info = response.data;
        this.info.avatar = "http://127.0.0.1:8000" + response.data.avatar;
        console.log("info:")
        console.log(this.info.avatar)
      })
        .catch(
          err => {
            console.log(err)
            this.$router.push('/login')
          }
        )
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
  width: 38vw;
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

.el-card ::v-deep .el-card__header {
  padding: 10px 10px;
  background-color: rgb(189, 246, 200);
}

.el-card ::v-deep .el-card__body {
  padding: 10px;
  background-color: white;

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

.el-card {
  position: relative;
    /*子溢出父元素隐藏 这样hover子元素的时候 不算hover父元素*/
  overflow: hidden;
}
.el-card::after{
    content: "";
    position: absolute;
    /*首先隐藏子元素*/
    left: -100%;
    top: 0;
    /*设置和父元素一样大*/
    width: 100%;
    height: 100%;
    /*添加从左往右的渐变 即模仿光照效果*/
    background-image: -webkit-linear-gradient(0deg,hsla(0,0%,100%,0),hsla(0,0%,100%,.5),hsla(0,0%,100%,0));
    background-image: linear-gradient(to right,hsla(0,0%,100%,0),hsla(0,0%,100%,.5),hsla(0,0%,100%,0));
    /*光照是斜着的更好看*/
    -o-transform: skewx(-25deg);
    -moz-transform: skewx(-25deg);
    -webkit-transform: skewx(-25deg);
    transform: skewx(-25deg);
    /*添加动画效果*/
    transition: all .3s ease;
    &:active {
      left: 100%;
    }
}
.el-card:active{
  -moz-transform: translateY(-6px);
  -webkit-transform: translateY(-6px);
  transform: translateY(-6px);
  /*添加一个淡一点的阴影*/
  -moz-box-shadow: 0 26px 40px -24px rgba(0,36,100,.5);
  -webkit-box-shadow: 0 26px 40px -24px rgba(0,36,100,.5);
  box-shadow: 0 26px 40px -24px rgba(0,36,100,.5);
}
.el-card:hover::after {
    /*鼠标放在父元素上 移动子元素*/
    left: 100%;
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

.container{
    width: 70px;
    height: 70px;
}
.sunny{
    width: 10px;
    height: 70px;
    position: absolute;
    background: -webkit-linear-gradient(top, rgba(255,255,255,0) 0%, rgba(255,255,255,0.8) 50%, rgba(255,255,255,0) 100%);
    animation: sunny 15s linear infinite;
}

@keyframes sunny {
    0%{
        transform: rotate(0deg);
    }
    100%{
        transform: rotate(360deg);
    }
}
.sunny::before{
    content: '';
    width: 10px;
    height: 70px;
    position: absolute;
    bottom: 0;
    left: 0;
    background: -webkit-linear-gradient(top, rgba(255,255,255,0) 0%, rgba(255,255,255,0.8) 50%, rgba(255,255,255,0) 100%);
    transform: rotate(90deg)
}

.sunny::after{
    content: '';
    width: 40px;
    height: 40px;
    position: absolute;
    top: 15px;
    left: -15px;
    background: #ffee44;
    border-radius: 50%;
    box-shadow: rgba(255,255,0,0.2) 0 0 0 15px;
}

</style>



<style src="./css/header.css"  lang="css" scoped />