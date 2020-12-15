<template>
    <div id="robotbox" class="inner">
        <div id="dialogbox">
            <div id="content">
                <div id="content_top">
                    <div id="nowDiv"></div>
                    <div id="state"></div>
                </div>
                <div id="content_main" style="max-width:474">
                    <div class="infinite-list" v-infinite-scroll="load" style="overflow:auto;max-width:100%;">
                        <div v-for="QA in qa" v-bind:key="QA" class="infinite-list-item">
                           <div style="display:flex;padding:10px;width:100 padding-left:50px;float:right">
                               <div class="talk_content">{{QA.questions}}</div>
                               <div class="head"></div>
                           </div>
                           <div style="display:flex; padding:10px;padding-right:50px;float:left">
                               <div class="head"></div>
                               <div class="talk_content">{{QA.answers}}</div>
                           </div>
                        </div>
                    </div>
                </div>   
            </div>
            <div id="functionbuttons">
                <b-button @click="clickMe($event)" class="fbutton" value="问症状">问症状</b-button>
                <b-button @click="clickMe($event)" class="fbutton" value="开始聊天">开始聊天</b-button>
                <b-button @click="clickMe($event)" class="fbutton" value="更多功能">更多功能</b-button>
            </div>
            <div id="inputbox">
                <div style="width:450px;"><input v-model="question" type="text" id="input"></div>
                <b-button @click="clickMe" id="voice"></b-button>
            </div>
        </div>
        <div>
            <button  @click="sendquestion()" id="sendbutton">发送</button>
        </div>
    </div>
</template>

<style scoped>
#robotbox {
    background-color: var(--box-background-color);
    border-top-left-radius: 3px;
    border-top-right-radius: 3px;
}

.inner {
    padding-left: 50px;
    padding-right: 50px;
    padding-bottom: 10px;
    font-size: 14px;
    line-height: 150%;
    text-align: left;
}

#dialogbox{
    border: 1px solid black;
    height: 720px;
    padding-top:5px;
}

#content{
    margin-left: 5px;
    margin-right: 5px;
    height: 86%;
    border:1px solid black;
    overflow:auto;
}

#content_top{
    display:flex;
    height:40px;
}

.infinite-list-item{
     margin-top: 10px;
     display:block;
}

.head{
    border:1px solid black;
    border-radius: 50%;
    height: 50px;
    width: 50px;
    /* position: relative;;
    right:5px; */
}

.talk_content{
    border:1px solid black;
    width:fit-content;
    border-radius: 10px;
    margin-left: 10px;
    margin-right:10px;
    /* font-size: 25px; */
    padding:10px;
    /* position: relative;;
    right:60px; */
}


#functionbuttons{
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding-top:5px;
    margin-left:5px;
    margin-right:5px;
    height: 7%;
}

.fbutton{
    border: 2px solid black; /* Green */
    width: 150px;
    border-radius:25px;
}

#inputbox{
    margin-left: 5px;
    margin-right: 5px;
    padding-top:5px;
    padding-bottom :5px;
    display: flex;
    height: 7%;
}

#input{
    display:block;
    height:100%;
    width:97%;
    border-radius:25px;
    outline:none
}

#voice{
    width:100px;
    border: 2px solid black;
    margin-left:7px;
    display:block;
    height:100%;
    border-radius:25px;
    outline:none;
}

#sendbutton{
    display:block;
    margin-top: 5px;
    width:100%;
    height:50px;
}

#nowDiv{
    font-size:20px;
    font-weight:bold;
    width:60%;
    padding: 10px;
    height:30px;
}

#state{
    padding:10px;
    font-size:20px;
    font-weight:bold;
    height:30px;
}

</style>


<script> 
import axios from "axios";
import Qs from 'qs';

 export default {
    components:{
        
    },
    data(){
        return{
            qa:[],
            respond:"",
            question:"",
            answer:""
        }
    },
    methods: {
        clickMe(event) {
             document.getElementById("state").innerHTML = "当前状态："+ event.currentTarget.value;
        } ,

        sendquestion() {
            axios({
                method:"post",
                url:"http://server.kingfish404.cn/msgAsk",
                data:Qs.stringify({
                    question:this.question
                }),
            }).then((res)=>{
                 this.respond = Qs.parse(res.data);
                 this.answer = this.respond.data.answer;
                 this.qa.push({questions:this.question,answers:this.answer});
            })
        }
    }

 }

window.onload = function(){
    show();
}

function show(){ 
    var date = new Date(); //日期对象 
    var now = ""; 
    now = date.getFullYear()+"年"; //读英文就行了 
    now = now + (date.getMonth()+1)+"月"; //取月的时候取的是当前月-1如果想取当前月+1就可以了 
    now = now + date.getDate()+"日"; 
    document.getElementById("nowDiv").innerHTML = now; //div的html是now这个字符串 
    setTimeout("show()",1000); //设置过1000毫秒就是1秒，调用show方法 
}


</script> 
