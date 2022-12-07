<!-- This is for ManagePage -->
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
            <el-card v-bind:class="{ 'box-card': fill, 'box-card-fold': !fill }" v-for="need in needs" :key="need">
              <template #header>
                <div v-bind:class="{ 'card-header': fill, 'card-header-fold': !fill }">
                  <!-- switch styles for fill or not fill -->
                  <div class="name">
                    <span>{{ need.name }}</span>
                  </div>
                  <div class="line-break"></div>

                  <div class="tags">
                    <el-tag class="ml-2" type="success">{{ categories[need.category] }}</el-tag>
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
                    用户：{{ need.user}}
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
                <el-icon><House /></el-icon> {{ "地址: " + "test" }}
              </div>
              <div class="submit-time">
                {{need.add_time}}
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
import { ref } from 'vue'

const fill = ref(true)
</script>
<script>
import foo from './components/FooterGrid.vue'
import Navigator from './components//NavigationBar.vue'
import { getGoods } from '../api/api';
import { categories, emergency_levels } from './dataTypes'
// import { useRouter } from 'vue-router'
// const router = useRouter()


export default {
  components: { foo, Navigator },
  data() {
    return {
      ButtonLeft: "求助",
      ButtonRight: "我的提供",
      needs: [
      ],
      test_tags: ["tag1", "tag2", "tag3"],
      requests_test: [
        {
          name: '矿泉水喝完了',
          tags: ['饮用品', '水', '较紧急'],
          desc: "饮水机坏了，被封着快没水了。",
          address: "东3"
        },
        {
          name: '急需N95口罩',
          tags: ['医疗', '口罩', '非常紧急'],
          desc: "口罩用完了，需要口罩，谢谢！",
          address: "东上院123"
        },
        {
          name: '有没有薯片',
          tags: ['食品', '零食', '普通'],
          desc: "被封了无聊，想吃薯片🤤",
          address: "西11"
        },
        {
          name: 'Song From Pippa Passes',
          tags: ['Robert', 'Browning'],
          desc: "The year’s at the spring, And day’s at the morn; Morning’s at seven; The hill-side’s dew-pearl’d; The lark’s on the wing; The snail’s on the thorn; God’s in his heaven -All’s right with the world!",
          address: "测试多行内容"
        },
        {
          name: 'Song From Pippa Passes',
          tags: ['Robert', 'Browning'],
          desc: "The year’s at the spring, And day’s at the morn; Morning’s at seven; The hill-side’s dew-pearl’d; The lark’s on the wing; The snail’s on the thorn; God’s in his heaven -All’s right with the world!",
          address: "测试多行内容"
        },
        {
          name: '纯真的空气',
          tags: ['义乌', 'DJ'],
          desc: "有一种纯真的美",
          address: "四川理塘"
        },
        {
          name: '矿泉水喝完了',
          tags: ['饮用品', '水', '较紧急'],
          desc: "饮水机坏了，被封着快没水了。",
          address: "东3"
        },
        {
          name: '急需N95口罩',
          tags: ['医疗', '口罩', '非常紧急'],
          desc: "口罩用完了，需要口罩，谢谢！",
          address: "东上院123"
        },
        {
          name: '有没有薯片',
          tags: ['食品', '零食', '普通'],
          desc: "被封了无聊，想吃薯片🤤",
          address: "西11"
        },
      ]

    }
  },
  methods: {
    loadNeeds() {
      getGoods().then(response => {
        this.needs = response.data.results
        console.log(this.needs)
      })
    }
  },
  created: function () {
    console.log("hello")
    this.loadNeeds()
  },
  provide() {
    return {
      message: '/info',
      messageFooLeft: '/request',
      messageFooRight: '/offer'
    }
  }
}
</script>
<style scoped>
.el-container {
  height: 100vh;
}

.box-card {
  width: 80vw;
  text-overflow: ellipsis;
}

.box-card-fold {
  width: 40vw;
  height: 200px;
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
  color:dimgray;
}

.submit-time {
  text-align: right;
  font-size: smaller;
  color:dimgray;
}

#headerBack {
  margin-bottom: 20px;
  background: #fff url("https://uploadfile.bizhizu.cn/up/cc/d0/87/ccd08766b03deca06263f0d8e0013dec.jpg") no-repeat;
  background-size: cover;
}

#MainBack {
  background: linear-gradient(120deg, yellow 0%, silver 100%);
  background-size: cover;
}

#FooterBack {
  background: #fff url("https://th.bing.com/th/id/OIP.Oc9mYdpG25SBa-pRljEXwAHaEK?pid=ImgDet&w=1500&h=844&rs=1") no-repeat;
  background-size: cover;
}
</style>