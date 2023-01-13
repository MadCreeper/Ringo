export const categories = {
    0:"食品",
    1: "药品",
    2: "生活用品",
    3: "娱乐",
    4: "器械",
    5: "其他物品",
 };

export const emergency_levels = {
    1: "啥时候都行",
    2: "最好尽快",
    3: "比较紧急",
    4: "很急",
    5: "十万火急",
};

export const item_type = {
    0: "需求物品",
    1: "提供物品",
};


export const sort_options = [
  {'value': '-emergency',
   'label': "按紧急度排序"
  },
  {'value': 'add_time',
   'label': "按时间排序"
  },
  { 'value' : 'best_match',
    'label' : "按匹配度排序"  
  },
]


export const requests_test = [
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