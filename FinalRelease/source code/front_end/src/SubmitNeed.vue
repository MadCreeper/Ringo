<template>
    <el-container>
        <el-page-header @back="goBack" @title="返回">
            <template #content>
                <span class="text-large font-600 mr-3"> 提交需求 </span>
            </template>
        </el-page-header>
        <el-main>
            <el-form :model="form" label-width="120px">
                <el-form-item label="需求物品名称">
                    <el-input v-model="form.name" />
                </el-form-item>
                <!-- <el-form-item label="位置">
                    <el-select v-model="form.region" placeholder="please select your zone">
                        <el-option label="上海" value="shanghai" />
                        <el-option label="北京" value="beijing" />
                    </el-select>
                </el-form-item> -->
                <el-form-item label="位置">
                    <elui-china-area-dht @change="this.locationChoose"></elui-china-area-dht>
                </el-form-item>
                <el-form-item label="需求日期段">
                    <el-col :span="11">
                        <el-date-picker v-model="form.date" type="daterange" range-separator="To"
                            start-placeholder="Start date" end-placeholder="End date" size="small"
                            style="width: 200%" />
                    </el-col>
                </el-form-item>
                <el-form-item label="紧急程度（1-5）">
                    <el-slider v-model="form.priority" :step="1" :min="1" :max="5" :show-tooltip="false" :marks="marks"
                        show-stops />
                </el-form-item>
                <el-form-item label="物品类型">
                    <el-cascader-panel :options="this.categories" v-model="form.type" />
                </el-form-item>
                <el-form-item label="备注">
                    <el-input v-model="form.desc" type="textarea" />
                </el-form-item>
                <el-form-item>
                    <el-alert v-if="show" title="提交成功" type="success" effect="dark" />
                    <el-button type="primary" @click="submit">提交</el-button>
                    <el-button>取消</el-button>
                </el-form-item>
            </el-form>
        </el-main>
        <!-- Footer -->
        <el-footer>

        </el-footer>
    </el-container>
</template>




<script>

import { reactive } from 'vue'
let form = reactive({
    name: '',
    region: '',
    date: '',
    priority: '',
    type: [],
    desc: '',
})

// const marks = {
//     1: '不急',
//     2: '普通',
//     3: '较为紧急',
//     4: '非常紧急',
//     5: '十万火急'
// }
import { addNeeds, getCategory } from '../api/api'
import { EluiChinaAreaDht } from 'elui-china-area-dht'
const chinaData = new EluiChinaAreaDht.ChinaArea().chinaAreaflat
export default {
    components: {
        EluiChinaAreaDht,
    },
    data() {
        return {
            show: false,
            form: form,
            categories: [],
            typesData: [],
        }
    },
    created: async function () {
        console.log("hello submitneed");

        let res = await getCategory({ "page": 1 });
        console.log(res.data)

        this.typesData = res.data.results;


        console.log("categories", this.typesData)
        for (let i = 0; i < this.typesData.length; i++) {
            
            if (this.typesData[i].category_type == 1) {
                this.categories.push({ 'value': i, 'label': this.typesData[i].name, children:[] })
            }
        }

        for (let i = 0; i < this.typesData.length; i++) {
            if (this.typesData[i].category_type == 2) {
                
                for (let j = 0; j < this.typesData.length; j++) { // find parent category
                    if (this.typesData[j].category_type == 1 && this.typesData[i].parent_category == this.typesData[j].code) {
                        for(let k = 0; k < this.categories.length; k++){
                            if(this.categories[k].label == this.typesData[j].name){
                                this.categories[k].children.push({ 'value': i, 'label': this.typesData[i].name, children:[] })
                            }
                        }
                    }
                }
            }
        }
        console.log("categories:");
        console.log(this.categories);

    },
    methods: {
        submit() {
            console.log('submit!')
            this.show = true;
            // this.$emit('submit', this.form);

            let needInfo = {
                "category": (1 in form.type ? this.typesData[form.type[1]] : this.typesData[form.type[0]]),
                "property_type": 0,
                "emergency": form.priority,
                "expected_end_time": form.date[1],
                "name": form.name,
                "address": form.region,
                "goods_brief": form.desc,
            }
            console.log("submitted info:")
            console.log(needInfo)
            addNeeds(needInfo);
            console.log(form);
            setTimeout(() => {
                history.back();
            }, 3000)
        },
        goBack() {
            history.back();
        },
        locationChoose : function (e) {
            const one = chinaData[e[0]]
            const two = chinaData[e[1]]
            const three = chinaData[e[2]]
            console.log(one, two, three)
            this.form.region = one.label + '-' + two.label + '-' + three.label;
        }
    }
}


</script>
<script setup>
// do not use same name with ref
const goBack = () => {
    history.back();
}
</script>

<style scoped>
.el-row {
    margin-bottom: 20px;
}

.el-row:last-child {
    margin-bottom: 0;
}

.el-col {
    border-radius: 4px;
}

.el-slider {
    /* fix slider last mark not breaking properly */
    word-break: keep-all;
    width: 90%;
}

.grid-content {
    border-radius: 4px;
    min-height: 36px;
}

.el-form {
    height: 90vh;
    width: 100%;
    overflow: hidden;
    background-image: lightblue;
    background-size: 100%;
    font-family: "montserrat";
    animation: bganimation 15s infinite;
}

.el-container {
    height: 100vh;
    background-image: linear-gradient(125deg, rgb(213, 241, 251), white);
}

.el-form h1 {
    margin-top: 0;
    font-weight: 200;
}

.el-form-item {
    border: 2px solid #aaa;
    margin: 8px 0;
    padding: 12px 18px;
    border-radius: 10px;
    color: #fff;
    font-size: 30px;
}

.el-form-item el-input {
    width: 100%;
    background: none;
    border: none;
    outline: none;
    margin-top: 6px;
    font-size: 18px;
    color: #fff;
}

.el-form-item label {
    font-size: 100px;
}

#selectForm>>>.el-form-item__label {
    font-size: 18px;
}

.file {
    position: relative;
    display: inline-block;
    background: #D0EEFF;
    border: 1px solid #99D3F5;
    border-radius: 4px;
    padding: 4px 12px;
    overflow: hidden;
    color: #1E88C7;
    text-decoration: none;
    text-indent: 0;
    line-height: 20px;
}

.file input {
    position: absolute;
    font-size: 100px;
    right: 0;
    top: 0;
    opacity: 0;
}

.file:hover {
    background: #AADFFD;
    border-color: #78C3F3;
    color: #004974;
    text-decoration: none;
}
.el-header{
    title:'返回';
}
</style>