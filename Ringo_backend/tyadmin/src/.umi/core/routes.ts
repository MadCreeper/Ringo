// @ts-nocheck
import { ApplyPluginsType, dynamic } from 'D:/Ringo/Ringo/tyadmin/node_modules/@umijs/runtime';
import { plugin } from './plugin';

const routes = [
  {
    "path": "/xadmin/login",
    "component": dynamic({ loader: () => import(/* webpackChunkName: 'layouts__UserLayout' */'D:/Ringo/Ringo/tyadmin/src/layouts/UserLayout'), loading: require('@/components/PageLoading/index').default}),
    "routes": [
      {
        "name": "login",
        "path": "/xadmin/login",
        "component": dynamic({ loader: () => import(/* webpackChunkName: 'p__TyAdminBuiltIn__UserLogin' */'D:/Ringo/Ringo/tyadmin/src/pages/TyAdminBuiltIn/UserLogin'), loading: require('@/components/PageLoading/index').default}),
        "exact": true
      }
    ]
  },
  {
    "path": "/xadmin/",
    "component": dynamic({ loader: () => import(/* webpackChunkName: 'layouts__SecurityLayout' */'D:/Ringo/Ringo/tyadmin/src/layouts/SecurityLayout'), loading: require('@/components/PageLoading/index').default}),
    "routes": [
      {
        "path": "/xadmin/",
        "component": dynamic({ loader: () => import(/* webpackChunkName: 'layouts__BasicLayout' */'D:/Ringo/Ringo/tyadmin/src/layouts/BasicLayout'), loading: require('@/components/PageLoading/index').default}),
        "authority": [
          "admin",
          "user"
        ],
        "routes": [
          {
            "name": "Home",
            "path": "/xadmin/index",
            "icon": "dashboard",
            "component": dynamic({ loader: () => import(/* webpackChunkName: 'p__TyAdminBuiltIn__DashBoard' */'D:/Ringo/Ringo/tyadmin/src/pages/TyAdminBuiltIn/DashBoard'), loading: require('@/components/PageLoading/index').default}),
            "exact": true
          },
          {
            "path": "/xadmin/",
            "redirect": "/xadmin/index",
            "exact": true
          },
          {
            "name": "认证和授权",
            "icon": "BarsOutlined",
            "path": "/xadmin/auth",
            "routes": [
              {
                "name": "权限",
                "path": "/xadmin/auth/permission",
                "component": dynamic({ loader: () => import(/* webpackChunkName: 'p__AutoGenPage__PermissionList' */'D:/Ringo/Ringo/tyadmin/src/pages/AutoGenPage/PermissionList'), loading: require('@/components/PageLoading/index').default}),
                "exact": true
              },
              {
                "name": "组",
                "path": "/xadmin/auth/group",
                "component": dynamic({ loader: () => import(/* webpackChunkName: 'p__AutoGenPage__GroupList' */'D:/Ringo/Ringo/tyadmin/src/pages/AutoGenPage/GroupList'), loading: require('@/components/PageLoading/index').default}),
                "exact": true
              }
            ]
          },
          {
            "name": "用户管理",
            "icon": "BarsOutlined",
            "path": "/xadmin/users",
            "routes": [
              {
                "name": "用户信息",
                "path": "/xadmin/users/user_profile",
                "component": dynamic({ loader: () => import(/* webpackChunkName: 'p__AutoGenPage__UserProfileList' */'D:/Ringo/Ringo/tyadmin/src/pages/AutoGenPage/UserProfileList'), loading: require('@/components/PageLoading/index').default}),
                "exact": true
              },
              {
                "name": "短信验证",
                "path": "/xadmin/users/verify_code",
                "component": dynamic({ loader: () => import(/* webpackChunkName: 'p__AutoGenPage__VerifyCodeList' */'D:/Ringo/Ringo/tyadmin/src/pages/AutoGenPage/VerifyCodeList'), loading: require('@/components/PageLoading/index').default}),
                "exact": true
              }
            ]
          },
          {
            "name": "物品管理",
            "icon": "BarsOutlined",
            "path": "/xadmin/goods",
            "routes": [
              {
                "name": "物品类别",
                "path": "/xadmin/goods/goods_category",
                "component": dynamic({ loader: () => import(/* webpackChunkName: 'p__AutoGenPage__GoodsCategoryList' */'D:/Ringo/Ringo/tyadmin/src/pages/AutoGenPage/GoodsCategoryList'), loading: require('@/components/PageLoading/index').default}),
                "exact": true
              },
              {
                "name": "物品信息",
                "path": "/xadmin/goods/goods",
                "component": dynamic({ loader: () => import(/* webpackChunkName: 'p__AutoGenPage__GoodsList' */'D:/Ringo/Ringo/tyadmin/src/pages/AutoGenPage/GoodsList'), loading: require('@/components/PageLoading/index').default}),
                "exact": true
              }
            ]
          },
          {
            "name": "操作管理",
            "icon": "BarsOutlined",
            "path": "/xadmin/user_operation",
            "routes": [
              {
                "name": "用户收藏",
                "path": "/xadmin/user_operation/user_fav",
                "component": dynamic({ loader: () => import(/* webpackChunkName: 'p__AutoGenPage__UserFavList' */'D:/Ringo/Ringo/tyadmin/src/pages/AutoGenPage/UserFavList'), loading: require('@/components/PageLoading/index').default}),
                "exact": true
              },
              {
                "name": "收货地址",
                "path": "/xadmin/user_operation/user_address",
                "component": dynamic({ loader: () => import(/* webpackChunkName: 'p__AutoGenPage__UserAddressList' */'D:/Ringo/Ringo/tyadmin/src/pages/AutoGenPage/UserAddressList'), loading: require('@/components/PageLoading/index').default}),
                "exact": true
              },
              {
                "name": "用户留言",
                "path": "/xadmin/user_operation/user_leaving_message",
                "component": dynamic({ loader: () => import(/* webpackChunkName: 'p__AutoGenPage__UserLeavingMessageList' */'D:/Ringo/Ringo/tyadmin/src/pages/AutoGenPage/UserLeavingMessageList'), loading: require('@/components/PageLoading/index').default}),
                "exact": true
              }
            ]
          },
          {
            "name": "TyadminBuiltin",
            "icon": "VideoCamera",
            "path": "/xadmin/sys",
            "routes": [
              {
                "name": "TyAdminLog",
                "icon": "smile",
                "path": "/xadmin/sys/ty_admin_sys_log",
                "component": dynamic({ loader: () => import(/* webpackChunkName: 'p__TyAdminBuiltIn__TyAdminSysLogList' */'D:/Ringo/Ringo/tyadmin/src/pages/TyAdminBuiltIn/TyAdminSysLogList'), loading: require('@/components/PageLoading/index').default}),
                "exact": true
              },
              {
                "name": "TyAdminVerify",
                "icon": "smile",
                "path": "/xadmin/sys/ty_admin_email_verify_record",
                "component": dynamic({ loader: () => import(/* webpackChunkName: 'p__TyAdminBuiltIn__TyAdminEmailVerifyRecordList' */'D:/Ringo/Ringo/tyadmin/src/pages/TyAdminBuiltIn/TyAdminEmailVerifyRecordList'), loading: require('@/components/PageLoading/index').default}),
                "exact": true
              }
            ]
          },
          {
            "name": "passwordModify",
            "path": "/xadmin/account/change_password",
            "hideInMenu": true,
            "icon": "dashboard",
            "component": dynamic({ loader: () => import(/* webpackChunkName: 'p__TyAdminBuiltIn__ChangePassword' */'D:/Ringo/Ringo/tyadmin/src/pages/TyAdminBuiltIn/ChangePassword'), loading: require('@/components/PageLoading/index').default}),
            "exact": true
          },
          {
            "component": dynamic({ loader: () => import(/* webpackChunkName: 'p__404' */'D:/Ringo/Ringo/tyadmin/src/pages/404'), loading: require('@/components/PageLoading/index').default}),
            "exact": true
          }
        ]
      },
      {
        "component": dynamic({ loader: () => import(/* webpackChunkName: 'p__404' */'D:/Ringo/Ringo/tyadmin/src/pages/404'), loading: require('@/components/PageLoading/index').default}),
        "exact": true
      }
    ]
  },
  {
    "component": dynamic({ loader: () => import(/* webpackChunkName: 'p__404' */'D:/Ringo/Ringo/tyadmin/src/pages/404'), loading: require('@/components/PageLoading/index').default}),
    "exact": true
  }
];

// allow user to extend routes
plugin.applyPlugins({
  key: 'patchRoutes',
  type: ApplyPluginsType.event,
  args: { routes },
});

export { routes };
