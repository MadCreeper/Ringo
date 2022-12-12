<template>
    <el-container>
        <el-page-header @back="goBack">
            <template #content>
                <span class="text-large font-600 mr-3"> 提交需求 </span>
            </template>
        </el-page-header>
        <el-main>
            <el-form :model="form" label-width="120px">
                <el-form-item label="需求物品名称">
                    <el-input v-model="form.name" />
                </el-form-item>
                <el-form-item label="位置">
                    <el-select v-model="form.region" placeholder="please select your zone">
                        <el-option label="上海" value="shanghai" />
                        <el-option label="北京" value="beijing" />
                    </el-select>
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
                    <el-cascader-panel :options="this.categories" v-model="form.type"/>
                </el-form-item>
                <el-form-item label="备注">
                    <el-input v-model="form.desc" type="textarea" />
                </el-form-item>
                <el-form-item>
                    <el-alert v-if="show" title="success alert" type="success" effect="dark" />
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
export default {
    data() {
        return {
            show: false,
            form: form,
            categories: [],
            typesData : [],
        }
    },
    created: async function () {
        console.log("hello submitneed");

        let res = await getCategory({ "page": 1 });
        console.log(res.data)
        
        this.typesData = res.data.results;


        console.log(this.typesData)
        for (let i = 0; i < this.typesData.length; i++) {
            this.categories.push({ 'value': i, 'label': this.typesData[i].name })
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
                "category" : (this.typesData[form.type[0]]),
                "property_type" : 0,
                "emergency" : form.priority,
                "expected_end_time" : form.date[1],
                "name" : form.name,
                "address" : form.region,
                "goods_brief" : form.desc,
            }
            console.log("submitted info:")
            console.log(needInfo)
            addNeeds(needInfo);
            // console.log(form);
            // setTimeout(() => {
            //     this.$router.push('/')
            // }, 10000)
        },
        goBack (){
            history.back();
        },

    }
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
</style>