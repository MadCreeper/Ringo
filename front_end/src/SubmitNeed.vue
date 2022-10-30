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
                    <el-cascader-panel :options="itemTypes" />
                </el-form-item>
                <el-form-item label="备注">
                    <el-input v-model="form.desc" type="textarea" />
                </el-form-item>
                <el-form-item>
                    <el-button type="primary" @click="onSubmit">提交</el-button>
                    <el-button>取消</el-button>
                </el-form-item>
            </el-form>
        </el-main>
        <!-- Footer -->
        <el-footer>

        </el-footer>
    </el-container>
</template>

<script setup>

import { reactive } from 'vue'



const form = reactive({
    name: '',
    region: '',
    date: '',
    priority: '',
    type: [],
    desc: '',
})

const marks = {
    1: '不急',
    2: '普通',
    3: '较为紧急',
    4: '非常紧急',
    5: '十万火急'
}

const itemTypes = [
    {
        value: 'medical',
        label: '医疗用品',
        children: [
            {
                value: 'mask',
                label: '口罩',
                children: [
                    {
                        value: 'normal',
                        label: '普通口罩',
                    },
                    {
                        value: 'n95',
                        label: 'N95口罩',
                    },
                    {
                        value: 'surgical',
                        label: '外科口罩',
                    },
                ],
            },
            {
                value: 'disinfectant',
                label: '消毒用品',
                children: [
                    {
                        value: 'ethanol',
                        label: '医用酒精',
                    },
                    {
                        value: 'bleach',
                        label: '84消毒液',
                    },
                ],
            },
        ],
    },
    {
        value: 'edible',
        label: '食品和饮用品',
        children: [
            {
                value: 'water',
                label: '饮用水',
                children: [
                    {
                        value: 'mineral_water',
                        label: '矿泉水',
                    },
                    {
                        value: 'pure_water',
                        label: '纯净水',
                    },
                ],
            },

            {
                value: 'instant',
                label: '即食',
                children: [
                    {
                        value: 'instant_noodles',
                        label: '方便面',
                    },
                    {
                        value: 'self_heat_meal',
                        label: '自热饭',
                    },
                ],
            },
            {
                value: 'snack',
                label: '零食',
                children: [
                    {
                        value: 'chips',
                        label: '薯片',
                    },
                    {
                        value: 'biscuit',
                        label: '饼干',
                    },
                ],
            },
        ],
    },
    {
        value: 'daily_use',
        label: '日用品',
        children: [
            {
                value: 'sanitation',
                label: '卫浴',
                children: [
                    {
                        value: 'shampoo',
                        label: '洗发水',
                    },
                    {
                        value: 'body_soap',
                        label: '沐浴露',
                    },
                ],
            },
            {
                value: 'electronics',
                label: '电子设备',
                children: [
                    {
                        value: 'powerbank',
                        label: '充电宝',
                    },
                    {
                        value: 'usb_cord',
                        label: 'USB数据线',
                    },
                ],
            },
        ],
    },
]

const onSubmit = () => {
    console.log('submit!')
}

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
.el-slider{
    /* fix slider last mark not breaking properly */
    word-break: keep-all; 
    width: 90%;
}
.grid-content {
    border-radius: 4px;
    min-height: 36px;
}
</style>