<template>
    <div id="bodyinner">
        <!-- 对话框主体 -->
        <div id="content">
          <happy-scroll 
          color="black" 
          size="5" 
          style="width:100%"
          hide-horizontal
          @vertical-end="yourHandler"
           >
            <ul
            v-for="QA in qa"
            v-bind:key="QA.questions"
            style="list-style: none; margin: 0;padding:0;width:100%"
            >
            <li class="msgcontent right">{{ QA.questions }}</li>
            <div style="clear: both"></div>
            <li v-if="QA.answers" class="msgcontent left">{{ QA.answers }}</li>
            <div style="clear: both"></div>
          </ul>
          </happy-scroll>
            
        </div>

        <!-- 输入框 -->
        <div class="inputbox">
            <div id="inpute">
                <!-- <el-input
                  type="textarea"
                  :rows="5"
                  placeholder="请输入内容"
                  @keyup.enter.native="sendquestion()"
                  v-model="question">
                </el-input> -->
                <textarea v-model="question"  @keyup="messageSendlisten" id="mytextarea" placeholder="请输入内容..."></textarea>
            </div>
        </div>

        <!-- 发送和录音按钮 -->
         <div id="sendandvoice">
                <button @click="sendquestion()" class="sendbutton">发送</button>
                <!-- <el-button type="primary" class="sendbutton" @click="voice()" plain>录音</el-button> -->
                <button @click="voice()" class="sendbutton">录音</button>
                <button @click="play()" class="sendbutton">播放</button>
                <button @click="download()" class="sendbutton">下载pcm</button>
                <button @click="getmypost()" class="sendbutton">post请求</button>
         </div>

    </div>
</template>

<script>
import axios from "axios";
import Qs from "qs";
import Recorder from 'js-audio-recorder';

const recorder = new Recorder({
sampleBits: 16, // 采样位数，支持 8 或 16，默认是16
sampleRate: 16000, // 采样率，支持 11025、16000、22050、24000、44100、48000，根据浏览器默认值，我的chrome是48000
numChannels: 1, // 声道，支持 1 或 2， 默认是1
// compiling: false,(0.x版本中生效,1.x增加中) // 是否边录边转换，默认是false
})


export default {
  data() {
    return {
      qa:[],
      question:"",
      pcm:''
    }
  },
  methods:{
      sendquestion() {
      var q=this.question;
      this.qa.push({questions:q,answers:""});
      this.question=""
      axios({
        method: "post",
        url: "https://pi.kingfish404.cn/robot/msgAsk",
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

    messageSendlisten(event) {
      if (event.keyCode === 13) {
        this.sendquestion(); // 发送文本
        event.preventDefault(); // 阻止浏览器默认换行操作
        return false;
      }
    },

    voice(){
      recorder.start().then(() => {
        console.log("success");
      }, (error) => {
      // 出错了
      console.log(`${error.name} : ${error.message}`);
      });
    },

    play(){
      recorder.play();
    },

    download(){
      this.pcm=recorder.getPCMBlob();
      console.log("get pcm success")
    },

    getmypost(){
      axios({
          method: 'post',
          url: "https://pi.kingfish404.cn/robot/sendPcm",
          data : this.pcm
      }).then((res)=>{
        console.log(res);
      })
    }
  },
  
watch: {
    Talk() {
      this.$nextTick(() => {
        var container = this.$el.querySelector('#talk')
        container.scrollTop = container.scrollHeight
      })
    }
  },
}
</script>

<style>
.happy-scroll-container{
  width: 100% !important; 
  height:100% !important;
}

.happy-scroll-container .happy-scroll-content {
    width: 100%;
}

.happy-scroll-bar{
  height:40px !important;
}


</style>

<style scoped>
button{
    display: inline-block;
    line-height: 1;
    white-space: nowrap;
    cursor: pointer;
    background: #FFF;
    border: 1px solid #DCDFE6;
    color: #606266;
    -webkit-appearance: none;
    text-align: center;
    box-sizing: border-box;
    outline: 0;
    margin: 0;
    transition: .1s;
    font-weight: 500;
    padding: 12px 20px;
    font-size: 14px;
    border-radius: 4px;
}


#bodyinner{
  width:100%;
  height:100%;
  background-color: #eeeeee;
}

#content{
    width:100%;
    height:80%;
    /* background-color:white; */
}

.msgcontent {
  width: auto;
  min-width: 30px;
  min-height: 30px;
  max-width: 50%;
  height: auto;
  word-break: break-all;
  margin: 5px;
  padding: 8px 16px;
  
}

.left {
  float: left;
  text-align: left;
  background-color: white;
  border-radius: 15px 15px 15px 5px;
}

.right {
  float: right;
  text-align: left;
  color:white;
  background-color:black;
  border-radius: 15px 15px 5px 15px;
}

.inputbox{
    width:100%;
    height:15%;
    border-left:1px solid  #eeeeee;
}

#inpute{
  width:100%;
  height:100%;
  display: flex;
  align-items: center;
  float: left;
}

#mytextarea{
  width:100%;
  height:100%;
  padding:0;
  border:0;
  resize: none;
  outline: none;
  font-size:15px;
}



#sendandvoice{
  height:5%;
  width:100%;
  border-left:1px solid  #eeeeee;
  background-color: white;
}

.sendbutton{
  margin:0 5px 0 5px;
  float: right;
}


</style>