<template>
    <div>
        <el-menu default-active="1-4-1" 
        class="el-menu-vertical-demo"
        @open="handleOpen" 
        @close="handleClose" 
        background-color=""
        :collapse="isCollapse"
        :default-openeds="openeds"
        >
            <el-submenu index="1">
                  <template slot="title">
                  <i class="el-icon-location"></i>
                  <span slot="title">基本功能</span>
                  </template>
                  <el-menu-item index="1-1" onclick="sendmsg1()" title="可以通过 疾病名称+病因、预防进行查询
如：
感冒的原因有哪些？
你好，我最近有一点发烧，还有一点咳嗽，还有一点头痛。
如何预防感冒？">问病情</el-menu-item>
                  <el-menu-item index="1-2" title="可以通过 疾病名称 + 科室进行查询
如：
感冒该挂哪科？">问科室</el-menu-item>
                  <el-menu-item index="1-3" title="问注意事项
可以通过 疾病名称+方向+注意事项进行查询
如：
感冒饮食有哪些注意事项">问注意事项</el-menu-item>
                  <el-menu-item index="1-4" title="
开始聊天
你好，开始聊天吧">开始聊天</el-menu-item>        
            </el-submenu>

            <el-submenu index="2">
                  <template slot="title">
                      <i class="el-icon-location"></i>
                      <span slot="title">拓展功能</span>
                  </template>
                  <el-menu-item index="1-3">有待开发</el-menu-item>
            </el-submenu>
        </el-menu>
    </div>
</template>

<style>
  .el-menu-vertical-demo:not(.el-menu--collapse) {
    width: 100%;
    height:100%;
  }
</style>

<style scoped>
</style>

<script>
  export default {
    data() {
      return {
         openeds: ['1','2'],
        isCollapse: false
      };
    },
    methods: {

      handleOpen(key, keyPath) {
        console.log(key, keyPath);
      },
      handleClose(key, keyPath) {
        console.log(key, keyPath);
      }
    }
  }
</script>