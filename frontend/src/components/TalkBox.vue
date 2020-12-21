<template>
  <div id="robotbox" class="inner">
    <div id="dialogbox">
      <div id="content">
        <div id="content_top">
          <div id="nowDiv">{{ this.date }}</div>
          <div id="state">当前状态：</div>
        </div>
        <div class="content_main">
          <ul
            v-for="QA in qa"
            v-bind:key="QA.questions"
            style="list-style: none; margin: 0"
          >
            <li class="head right"></li>
            <li class="msgcontent right">{{ QA.questions }}</li>
            <div style="clear: both"></div>
            <li v-if="QA.answers" class="head left"></li>
            <li v-if="QA.answers" class="msgcontent left">{{ QA.answers }}</li>
            <div style="clear: both"></div>
          </ul>
        </div>
      </div>
      <div id="functionbuttons">
        <el-button type="primary" round plain @click="clickMe($event)">问症状</el-button>
        <el-button type="primary" round plain @click="clickMe($event)">开始聊天</el-button>
        <el-button type="primary" round plain @click="clickMe($event)">更多功能</el-button>
      </div>
      <div id="inputbox">
        <div class="inputPlace">
          <el-input
            id="input"
            placeholder="请输入内容"
            v-model="question"
            clearable
          >
          </el-input>
          <!-- <input type="file" @change="onChange($event)"> -->
        </div>
        <!-- <b-button @click="gettoken()" id="voice"></b-button> -->
         <el-button round @click="gettoken()" id="voice">
            <svg t="1608094125767" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="1319" width="200" height="200"><path d="M779.202 472.798c-15.464 0-28 12.536-28 28C751.202 633.246 643.447 741 511 741S270.798 633.246 270.798 500.798c0-15.464-12.536-28-28-28s-28 12.536-28 28c0 79.118 30.811 153.501 86.755 209.446 46.403 46.402 105.495 75.492 169.447 84.073A300.628 300.628 0 0 0 511 797c13.495 0 26.848-0.918 40-2.683 63.953-8.581 123.044-37.67 169.446-84.073 55.945-55.945 86.756-130.328 86.756-209.446 0-15.464-12.536-28-28-28zM471 803.317v77.389c0 18.446 17.909 33.399 40 33.399s40-14.953 40-33.399v-77.389a359.352 359.352 0 0 1-40 2.24c-13.495 0-26.848-0.766-40-2.24z" p-id="1320"></path><path d="M511 672c106.972 0 194-87.028 194-194V292c0-106.972-87.028-194-194-194s-194 87.028-194 194v186c0 106.972 87.028 194 194 194zM373 433V292c0-7.138 0.545-14.151 1.595-21 10.144-66.163 67.45-117 136.405-117 76.094 0 138 61.907 138 138v186c0 76.094-61.906 138-138 138-76.093 0-138-61.906-138-138v-45z" p-id="1321"></path><path d="M569 299c0-15.464-12.536-28-28-28H384.595A138.514 138.514 0 0 0 383 292v35h158c15.464 0 28-12.536 28-28zM569 405c0-15.464-12.536-28-28-28H383v56h158c15.464 0 28-12.536 28-28z" p-id="1322"></path></svg>
         </el-button>
      </div>
    </div>
    <div>
      <el-button type="primary" id="sendbutton" @click="sendquestion" plain>发送</el-button>
      <!-- <button @click="sendquestion" id="sendbutton">发送</button> -->
    </div>
  </div>
</template>

<style scoped>
#robotbox {
  height:90%;
  padding-top:2.5em;
  padding-bottom: 2em;
  background-color: var(--box-background-color);
  border-top-left-radius: 3px;
  border-top-right-radius: 3px;
}

.inner {
  /* padding-left: 50px;
  padding-right: 50px; */
  padding-bottom: 10px;
  font-size: 14px;
  line-height: 150%;
  text-align: left;
}

#dialogbox {
  border-bottom: 1px solid black;
  padding-top: 5px;
}

#content {
  margin-left: 5px;
  margin-right: 5px;
  height: 81%;
  border: 1px solid black;
}

#content_top {
  display: flex;
  height: 40px;
}

.content_main {
  min-height: 400px;
  height: 80%;
  /* overflow-y: scroll; */
  overflow: auto;
}

#userhead {
  width: 50px;
  height: 50px;
  border-radius: 50%;
  padding: 3px;
  margin: 5px;
}

.msgcontent {
  width: auto;
  min-width: 30px;
  min-height: 30px;
  max-width: 500px;
  height: auto;
  word-break: break-all;
  margin: 5px;
  padding: 3px;
  border-radius: 5px;
}

.left {
  float: left;
  text-align: left;
  background-color: lightgrey;
}

.right {
  float: right;
  text-align: right;
  background-color: yellowgreen;
}

.head {
  border: 1px solid black;
  border-radius: 50%;
  height: 30px;
  width: 30px;
  padding: 3px;
  margin: 5px;
  background-color: white;
}

.infinite-list-item {
  display: block;
  height: 500px;
  margin-top: 10px;
}

.talk_content {
  border: 1px solid black;
  width: fit-content;
  border-radius: 10px;
  margin-left: 10px;
  margin-right: 10px;
  /* font-size: 25px; */
  padding: 10px;
  /* position: relative;;
    right:60px; */
}

#functionbuttons {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin: 5px 1em;
  height: 7%;
}

.fbutton {
  border: 2px solid black; /* Green */
  width: 150px;
  border-radius: 25px;
}

#inputbox {
  margin-left: 5px;
  margin-right: 5px;
  padding-top: 5px;
  padding-bottom: 5px;
  display: flex;
  height: 7%;
}

#input {
  display: block;
  height: 100%;
  width:80%;
  border-radius: 25px;
  padding-left: 20px;
  outline: none;
}

#voice{
  margin-left:1.5em;
}


#sendbutton {
  display: block;
  margin:5px 5px 5px 5px;
  width: 98%;
}

#nowDiv {
  font-size: 20px;
  font-weight: bold;
  width: 60%;
  padding: 10px;
  height: 30px;
}

#state {
  padding: 10px;
  font-size: 20px;
  font-weight: bold;
  height: 30px;
}

.inputPlace{
    width:80%;
}
</style>


<script>
import axios from "axios";
import Qs from "qs";


export default {
  components: {},
  data() {
    return {
      qa: [],
      respond: "",
      question: "",
      answer: "",
      speech:""
    };
  },
  computed: {
    date: function () {
      var date = new Date(); //日期对象
      var now = "";
      now = date.getFullYear() + "年"; //读英文就行了
      now = now + (date.getMonth() + 1) + "月"; //取月的时候取的是当前月-1如果想取当前月+1就可以了
      now = now + date.getDate() + "日";
      return now;
    },
  },
  methods: {
    clickMe(event) {
      document.getElementById("state").innerHTML =
        "当前状态：" + event.currentTarget.value;
    },

   sendquestion() {
      var q=this.question;
      this.qa.push({questions:q,answers:""});
      this.question="";
      axios({
        method: "post",
        url: "http://server.kingfish404.cn/msgAsk",
        data: Qs.stringify({
          question: q,
        }),
      }).then((res) => {
        this.respond = Qs.parse(res.data);
        this.answer = this.respond.data.answer;
        this.qa[this.qa.length - 1].answers = this.answer;
        this.answer = "";
      });
    },

    gettoken(){
      axios({
        method: "post",
        url: "https://vop.baidu.com/pro_api",
        headers:{"Content-Type":"application/json"},
        data:{
           "format":"m4a",
           "rate":16000,
           "dev_pid":80001,
           "channel":1,
           "token":"25.ae1d54b6eb6644c8318c25a2664fafd4.315360000.1923800218.282335-23182636",
           "cuid":"baidu_workshop",
           "len":77883,
           "speech":this.speech
        },
      }).then((res) => {
        alert("ok");
        console.log(res);
      });

    },



    onChange(e) {
      var file = e.target.files[0];
      var reader = new FileReader();
      reader.onload = function (e) {
        //console.log(e.target.result)
        let Base64 = require('js-base64').Base64
        var result = Base64.encode(e.target.result)
        this.speech= result;
        console.log(this.speech);

      };

      reader.readAsBinaryString(file);
    }




  },
};

</script> 


