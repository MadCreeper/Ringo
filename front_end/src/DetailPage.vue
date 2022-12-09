<template>
    <div class="common-layout">
        <el-container>
            <el-header id="headerBack" height="200px">


            </el-header>
            <el-main id="MainBack">
                <div class="need-title">
                    <div>
                        {{ item_type[this.need.property_type] + ": " + this.need.name }}
                    </div>
                    <div class="tags" v-if="this.need.category">
                        <el-tag class="ml-2" type="success">{{ this.need.category.name }}</el-tag>
                        <el-tag class="ml-2" type="danger">{{ emergency_levels[need.emergency] }}</el-tag>
                    </div>
                </div>
                <div class="body">

                
                <div class="user-display">
                    <div>
                        <AvaterUsr></AvaterUsr>
                    </div>
                    <div>
                        {{ this.need.user }}
                    </div>
                </div>

                <div v-if="this.need.goods_brief">
                    {{this.need.goods_brief}}
                </div>
                
                <div v-if="this.need.goods_desc">
                    {{ this.need.goods_desc }}
                </div>


                

                <div>
                    <el-icon>
                        <House />
                    </el-icon> {{ "地址: " + need.address }}
                </div>

                <div class="need-time" v-if="this.need.add_time && this.need.expected_end_time">
                    {{formatDateTime(this.need.add_time)}} ~ {{formatDateTime(this.need.expected_end_time)}}
                </div>
            </div>
            </el-main>
            <el-footer id="FooterBack">
                Looking at good ID: {{ this.$route.query.id }} <br>
            </el-footer>
        </el-container>
    </div>
</template>

<script>
/* eslint-disable */
import { onMounted } from 'vue'

import { getGoodsDetail } from '../api/api';
import { emergency_levels, item_type } from './dataTypes'
import { formatDateTime } from './utils'
import AvaterUsr from './components/AvaterUser.vue'

export default {
    data() {
        return {
            itemId: -1,
            ButtonLeft: "求助",
            ButtonRight: "我的提供",
            need: {},
            need_test: {
                name: '矿泉水喝完了',
                tags: ['饮用品', '水', '较紧急'],
                desc: "饮水机坏了，被封着快没水了。",
                address: "东3"
            },
            emergency_levels: emergency_levels,
            item_type: item_type
        }
    },
    methods: {
        getGoodById(goodId) {
            getGoodsDetail(goodId).then(response => {
                console.log(response.data)
                this.need = response.data
                console.log(this.need.category.name)
            })
        },
        formatDateTime,
    },
    created() {
        onMounted(() => {
            console.log("aaaaa")
            this.getGoodById(this.$route.query.id)
            console.log(emergency_levels)
            // console.log(this.$route.query.id)
        })
    },
    provide() {
        return {
            message: '/info',
            messageFooLeft: '/request',
            messageFooRight: '/offer'
        }
    },
    components: { AvaterUsr },
}
</script>
<style scoped>
.el-container {
    height: 100vh;
}

.body {
    line-height: 3ch;
    text-indent: 2ch;
}

.need-title {
    /* align-self: flex-end; */
    font-size: xx-large;
    /* background-color: lightgrey; */
    display: flex;
    flex-direction: row;
}

.need-title .tags {
    display: flex;
    margin-left: auto;
    align-items: center;
    gap: 10px;
}

.user-display {
    display: flex;
    flex-direction: row;
    justify-items: right;
    align-items: center;
    font-size: large;
}

.need-time {
  text-align: right;
  font-size: smaller;
  color: dimgray;
}
#headerBack {
    display: flex;
    margin-bottom: 20px;
    background: #fff url("https://uploadfile.bizhizu.cn/up/cc/d0/87/ccd08766b03deca06263f0d8e0013dec.jpg") no-repeat;
    background-size: cover;
}

#MainBack {
    /* background: linear-gradient(120deg, yellow 0%, silver 100%); */
    background-size: cover;
}

#FooterBack {
    background: #fff url("https://th.bing.com/th/id/OIP.Oc9mYdpG25SBa-pRljEXwAHaEK?pid=ImgDet&w=1500&h=844&rs=1") no-repeat;
    background-size: cover;
}
</style>