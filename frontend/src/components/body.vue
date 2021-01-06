<template>
  <div id="bodyinner">
    <!-- 对话框主体 -->
    <div id="content">
      <ul
        id="aaul"
        v-for="QA in qa"
        v-bind:key="QA.counter"
        style="list-style: none; margin: 0; padding: 0; width: 100%"
      >
        <li class="msgcontent right">{{ QA.questions }}</li>
        <div style="clear: both"></div>
        <li v-if="QA.answers" class="msgcontent left">{{ QA.answers }}</li>
        <div style="clear: both"></div>
      </ul>
    </div>

    <!-- 输入框 -->
    <div class="inputbox">
      <div id="inpute">
        <textarea
          v-model="question"
          @keyup="messageSendlisten"
          id="mytextarea"
          placeholder="请输入内容..."
        ></textarea>
      </div>

      <div id="voiceshake">
        <div
          class="recallingWrod animate__animated animate__swing animate__infinite infinite animate__slower 0.1s"
        >
          正
        </div>
        <div
          class="recallingWrod animate__animated animate__swing animate__infinite infinite animate__slower 0.2s"
        >
          在
        </div>
        <div
          class="recallingWrod animate__animated animate__swing animate__infinite infinite animate__slower 0.1s"
        >
          录
        </div>
        <div
          class="recallingWrod animate__animated animate__swing animate__infinite infinite animate__slower 0.2s"
        >
          音
        </div>
        <div
          class="recallingWrod animate__animated animate__swing animate__infinite infinite animate__slower 0.1s"
        >
          ...
        </div>
      </div>
    </div>

    <!-- 发送和录音按钮 -->
    <div id="sendandvoice">
      <button @click="sendquestion()" class="sendbutton">发送</button>
      <!-- <el-button type="primary" class="sendbutton" @click="voice()" plain>录音</el-button> -->
      <button @click="voice()" class="sendbutton" id="startvoice">说话</button>
      <button @click="getmypost()" class="sendbutton" id="endvoice">
        结束
      </button>
    </div>
  </div>
</template>
<script>
import axios from "axios";
import Qs from "qs";
import Recorder from "js-audio-recorder";

const recorder = new Recorder({
  sampleBits: 16, // 采样位数，支持 8 或 16，默认是16
  sampleRate: 16000, // 采样率，支持 11025、16000、22050、24000、44100、48000，根据浏览器默认值，我的chrome是48000
  numChannels: 1, // 声道，支持 1 或 2， 默认是1
  // compiling: false,(0.x版本中生效,1.x增加中) // 是否边录边转换，默认是false
});

export default {
  data() {
    return {
      qa: [],
      counter: 0,
      question: "",
      pcm: "",
    };
  },
  methods: {
    sendquestion() {
      var q = this.question;
      this.counter++;
      this.qa.push({ questions: q, answers: "", counter: this.counter });
      this.question = "";
      axios({
        method: "post",
        url: "https://pi.kingfish404.cn/robot/msgAsk",
        data: Qs.stringify({
          question: q,
        }),
      })
        .then((res) => {
          this.respond = Qs.parse(res.data);
          this.answer = this.respond.data.answer;
          this.qa[this.qa.length - 1].answers = this.answer;
          console.log(this.answer);

          // 文字转语音写在这里
          function btts(param, options) {
            var url = "https://tsn.baidu.com/text2audio";
            var opt = options || {};

            // 如果浏览器支持，可以设置autoplay，但是不能兼容所有浏览器
            var audio = document.createElement("audio");
            if (opt.autoplay) {
              audio.setAttribute("autoplay", "autoplay");
            }

            // 隐藏控制栏
            if (!opt.hidden) {
              audio.setAttribute("controls", "controls");
            } else {
              audio.style.display = "none";
            }

            // 设置音量
            if (typeof opt.volume !== "undefined") {
              audio.volume = opt.volume;
            }

            // 调用onInit回调
            isFunction(opt.onInit) && opt.onInit(audio);

            // 默认超时时间60秒
            var DEFAULT_TIMEOUT = 60000;
            var timeout = opt.timeout || DEFAULT_TIMEOUT;

            // 创建XMLHttpRequest对象
            var xhr = new XMLHttpRequest();
            xhr.open("POST", url);

            // 创建form参数
            var data = {};
            for (var p in param) {
              data[p] = param[p];
            }

            // 赋值预定义参数
            data.cuid = data.cuid || data.tok;
            data.ctp = 1;
            data.lan = data.lan || "zh";
            data.aue = data.aue || 3;

            // 序列化参数列表
            var fd = [];
            for (var k in data) {
              fd.push(k + "=" + encodeURIComponent(data[k]));
            }

            // 用来处理blob数据
            var frd = new FileReader();
            xhr.responseType = "blob";
            xhr.send(fd.join("&"));

            // 用timeout可以更兼容的处理兼容超时
            var timer = setTimeout(function () {
              xhr.abort();
              isFunction(opt.onTimeout) && opt.onTimeout();
            }, timeout);

            xhr.onreadystatechange = function () {
              if (xhr.readyState == 4) {
                clearTimeout(timer);
                if (xhr.status == 200) {
                  if (xhr.response.type === "audio/mp3") {
                    // 在body元素下apppend音频控件
                    document.body.appendChild(audio);

                    audio.setAttribute(
                      "src",
                      URL.createObjectURL(xhr.response)
                    );

                    // autoDestory设置则播放完后移除audio的dom对象
                    if (opt.autoDestory) {
                      audio.onended = function () {
                        document.body.removeChild(audio);
                      };
                    }

                    isFunction(opt.onSuccess) && opt.onSuccess(audio);
                  }

                  // 用来处理错误
                  if (xhr.response.type === "application/json") {
                    frd.onload = function () {
                      var text = frd.result;
                      isFunction(opt.onError) && opt.onError(text);
                    };
                    frd.readAsText(xhr.response);
                  }
                }
              }
            };

            // 判断是否是函数
            function isFunction(obj) {
              if (Object.prototype.toString.call(obj) === "[object Function]") {
                return true;
              }
              return false;
            }
          }

          // 调用语音合成接口
          // 参数含义请参考 https://ai.baidu.com/docs#/TTS-API/41ac79a6
          let audio = btts(
            {
              tex: this.answer,
              tok:
                "24.ee8f6c336da1e847cb9e8c1a9da348b3.2592000.1611415416.282335-23183171",
              spd: 5,
              pit: 5,
              vol: 15,
              per: 4,
            },
            {
              volume: 0.3,
              autoDestory: true,
              timeout: 10000,
              hidden: false,
              onInit: function (htmlAudioElement) {
                audio = htmlAudioElement;
              },
              onSuccess: function (htmlAudioElement) {
                audio = htmlAudioElement;
                audio.play();
              },
              onTimeout: function () {
              },
            }
          );
          this.answer = "";
        })
        .then(() => {
          var textArea = document.getElementById("content");
          textArea.scrollTop = textArea.scrollHeight;
        });
    },

    messageSendlisten(event) {
      if (event.keyCode === 13) {
        this.sendquestion(); // 发送文本
        event.preventDefault(); // 阻止浏览器默认换行操作
        return false;
      }
    },

    voice() {
      recorder.start().then(
        () => {
          console.log("success");
          document.getElementById("voiceshake").style.display = "block";
          document.getElementById("startvoice").style.display = "none";
          document.getElementById("endvoice").style.display = "block";
          document.getElementById("inpute").style.display = "none";
        },
        (error) => {
          // 出错了
          console.log(`${error.name} : ${error.message}`);
        }
      );
    },

    getmypost() {
      //保存pcm格式
      this.pcm = recorder.getPCMBlob();
      console.log("get pcm success");
      axios({
        method: "post",
        url: "https://pi.kingfish404.cn/robot/sendPcm",
        data: this.pcm,
      }).then((res) => {
        console.log(res);
        this.question = res.data.data.answer[0];
      });
      document.getElementById("voiceshake").style.display = "none";
      document.getElementById("endvoice").style.display = "none";
      document.getElementById("startvoice").style.display = "block";
      document.getElementById("inpute").style.display = "block";
    },
  },

  watch: {
    Talk() {
      this.$nextTick(() => {
        var container = this.$el.querySelector("#talk");
        container.scrollTop = container.scrollHeight;
      });
    },
  },
};
</script>

<style>
.happy-scroll-container {
  width: 100% !important;
  height: 100% !important;
}

.happy-scroll-container .happy-scroll-content {
  width: 100%;
}

.happy-scroll-bar {
  height: 40px !important;
}
</style>

<style scoped>
button {
  display: inline-block;
  line-height: 1;
  white-space: nowrap;
  cursor: pointer;
  background: #fff;
  border: 1px solid #dcdfe6;
  color: #606266;
  -webkit-appearance: none;
  text-align: center;
  box-sizing: border-box;
  outline: 0;
  margin: 0;
  transition: 0.1s;
  font-weight: 500;
  padding: 12px 20px;
  font-size: 14px;
  border-radius: 4px;
}

#bodyinner {
  width: 100%;
  height: 100%;
  background-color: #eeeeee;
}

#content {
  width: 100%;
  height: 80%;
  margin: auto auto 1em;
  overflow: auto;
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

.recallingWrod {
  display: inline-block;
}

.left {
  clear: both;
  float: left;
  text-align: left;
  background-color: white;
  border-radius: 15px 15px 15px 5px;
}

.right {
  clear: both;
  float: right;
  text-align: left;
  color: white;
  background-color: rgb(80, 75, 75);
  border-radius: 15px 15px 5px 15px;
}

.inputbox {
  width: 100%;
  height: 12%;
  background-color: white;
  border-left: 1px solid #eeeeee;
  position: relative;
}

#inpute {
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  float: left;
  display: block;
}

#voiceshake {
  margin: 0 auto;
  width: 100%;
  text-align: center;
  position: absolute;
  font-size: xx-large;
  top: 40%;
  display: none;
}

#mytextarea {
  width: 100%;
  height: 100%;
  padding: 0;
  border: 0;
  resize: none;
  outline: none;
  font-size: 15px;
}

#sendandvoice {
  height: 7%;
  width: 100%;
  border-left: 1px solid #eeeeee;
  background-color: white;
}

.sendbutton {
  margin: 0 5px 0 5px;
  float: right;
}

#startvoice {
  display: block;
}

#endvoice {
  display: none;
}
</style>