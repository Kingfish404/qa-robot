<template>
    <b-navbar>
        <template slot="brand">
        </template>
        <template slot="start">
            <b-navbar-item href="#">
                QARobot
            </b-navbar-item>
            <b-navbar-item href="#">
                文档
            </b-navbar-item>
            <b-navbar-dropdown label="更多">
                <b-navbar-item href="#">
                    关于
                </b-navbar-item>
                <b-navbar-item href="#">
                    联系
                </b-navbar-item>
            </b-navbar-dropdown>
        </template>

        <template slot="end">
            <b-navbar-item tag="div">
                <h1>健康问答机器人</h1>

            </b-navbar-item>
        </template>
    </b-navbar>
</template>