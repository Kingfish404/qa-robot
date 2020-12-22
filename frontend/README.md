# frontend

## 项目设置
### 环境配置
1. vue 2.6.12
2. vue/cli 4.5.9
注意：vue/cli最新版本安装的先要条件在[官网](https://cli.vuejs.org/guide/installation.html)可查

### 安装依赖
```
npm install
npm install axios
npm install qs
npm install element-ui
npm install vue-happy-scroll
```

### 编译和重新加载
```
npm run serve
```

### 编译和缩小用于生产
```
npm run build
```

### Lints和修复文件
```
npm run lint
```

### 自定义配置项
查看 [Configuration Reference](https://cli.vuejs.org/config/).

## 文档说明
 frontend目录规范

---

    frontend >
    |- node_modules                               # npm 加载的项目依赖模块
    |- public	                              # 静态文件夹                   
         |- index.htmll                           # 首页入口文件，你可以添加一些 meta 信息或统计代码啥的。
    |- src                                        # 这里是我们要开发的目录，基本上要做的事情都在这个目录里。里面包含了几个目录及文件：
         |- components                            # 目录里面放了一个组件文件
             |- body.vue                          # 聊天主体组件
             |- leftbar.vue                       # 左侧导航组件
         |- App.vue                               # 项目入口文件
         |- main.js                               # 项目的核心文件
         |- router.js                             # 路由的设置文件
    |- babel.config.js                            # babel语法编译
    |- package.json                               # 项目配置文件。
    |- package-lock.json                          # 记录当前状态下实际安装的各个npm package的具体来源和版本号
    |- README.md                                  # 项目的说明文档
