<template>
    <el-container>
        <el-page-header @back="goBack" content="提供物品">
        </el-page-header>
        <el-main>
            <el-form :model="form" label-width="120px">
                <el-form-item label="提供物品">
                    <el-input v-model="form.name" />
                </el-form-item>
                <el-form-item label="位置">
                    <el-select v-model="form.region" placeholder="please select your zone">
                        <el-option label="上海" value="shanghai" />
                        <el-option label="北京" value="beijing" />
                    </el-select>
                </el-form-item>
                <el-form-item label="提供日期段">
                    <el-col :span="11">
                        <el-date-picker v-model="form.date" type="daterange" range-separator="To"
                            start-placeholder="Start date" end-placeholder="End date" size="small"
                            style="width: 200%" />
                    </el-col>
                </el-form-item>
                <el-form-item label="物品类型">
                    <el-cascader-panel :options="this.categories" v-model="form.type" />
                </el-form-item>
                <el-form-item label="图片url">
                    <el-input v-model="form.imageurl" type="textarea" />
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
import { addOffering, getCategory } from '../api/api'
let form = reactive({
    name: '',
    region: '',
    date: '',
    priority: '',
    type: [],
    desc: '',
    imageurl: '',
})

const OFFERING = 1
// const marks = {
//     1: '不急',
//     2: '普通',
//     3: '较为紧急',
//     4: '非常紧急',
//     5: '十万火急'
// }
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
        console.log("hello submitOffering");

        // get category data
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

            let offerInfo = {
                "category" : (this.typesData[form.type[0]]),
                "property_type" : OFFERING, // 1 = offering
                // "expected_end_time" : form.date[1].toDateString(),
                "name" : form.name,
                "address" : form.region,
                "goods_brief" : form.desc,
                "goods_desc" : form.imageurl
            }
            console.log("submitted offering info:")
            console.log(offerInfo)
            addOffering(offerInfo);
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