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
                  <el-menu-item index="1-1">问病情</el-menu-item>
                  <el-menu-item index="1-2">问科室</el-menu-item>
                  <el-menu-item index="1-3">问注意事项</el-menu-item>
                  <el-menu-item index="1-4">开始聊天</el-menu-item>        
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