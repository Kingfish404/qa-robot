<template>
  <div id="app">
    <!-- 头部信息 -->
    <div id="head">
      <div>
        <button id="headbutton" @click="hiddeleftbar()">
          <span id="headimg"><svg t="1608562305853" class="icon" viewBox="0 0 1305 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="3135" width="2.7em" height="2.7em"><path d="M0.837818 75.218317c0 19.642164 8.098902 39.191237 21.969435 53.06177 13.963624 13.963624 33.512697 22.062525 53.247951 22.062525a76.055204 76.055204 0 0 0 53.06177-21.969434c13.963624-13.963624 22.062525-33.512697 22.062526-53.154861A76.055204 76.055204 0 0 0 129.303156 21.970365 76.055204 76.055204 0 0 0 76.055204 0.000931a76.055204 76.055204 0 0 0-53.247951 21.969434A76.706839 76.706839 0 0 0 0.837818 75.218317M0.837818 476.160498c0 19.642164 8.005811 39.377419 21.969435 53.247952 13.963624 13.963624 33.419606 21.969435 53.247951 21.969434a76.241385 76.241385 0 0 0 53.154861-21.969434 75.962113 75.962113 0 0 0 21.969435-53.247952 76.241385 76.241385 0 0 0-21.969435-53.154861 75.962113 75.962113 0 0 0-53.154861-21.969434 76.241385 76.241385 0 0 0-53.247951 21.969434 75.962113 75.962113 0 0 0-21.969435 53.154861M0.837818 877.19577c0 19.642164 8.005811 39.284328 21.969435 53.247951 13.963624 13.963624 33.419606 21.969435 53.247951 21.969435a76.241385 76.241385 0 0 0 53.154861-21.969435 75.962113 75.962113 0 0 0 21.969435-53.247951 76.241385 76.241385 0 0 0-21.969435-53.247952 75.962113 75.962113 0 0 0-53.154861-21.969434 76.241385 76.241385 0 0 0-53.247951 21.969434 76.520658 76.520658 0 0 0-21.969435 53.247952M1304.109361 75.218317c0 41.518508-32.395607 75.124295-72.331571 75.124295H373.945843c-40.029055 0-72.331571-33.512697-72.331571-75.124295C301.521181 33.513628 333.916788 0.000931 373.945843 0.000931h857.831947c40.029055 0 72.331571 33.605788 72.331571 75.217386M1231.77779 551.377884H373.945843c-40.029055 0-72.331571-33.605788-72.331571-75.217386 0-41.518508 32.302516-75.124295 72.331571-75.124295h857.831947c40.029055-0.186182 72.331571 33.512697 72.331571 75.124295 0 41.425417-32.395607 75.217386-72.331571 75.217386zM1304.109361 877.102679c0 41.611599-32.395607 75.310477-72.331571 75.310477H373.945843c-40.029055 0-72.331571-33.698878-72.331571-75.310477 0-41.425417 32.302516-75.124295 72.331571-75.124295h857.831947c40.029055-0.093091 72.331571 33.698878 72.331571 75.124295" p-id="3136" fill="white"></path></svg></span>
        </button>
      </div>
      <div id="headname">QARobot</div>
    </div>

    <!-- 左侧导航 -->
    <div id="leftbar">
      <leftbar></leftbar>
    </div>

    <!-- 聊天框主体 -->
    <div id="talkbody">
      <Body></Body>
    </div>
    
  </div>
</template>

<script>
import leftbar from './components/leftbar'
import Body from './components/body'

export default {
  name: 'App',
  components: {
    leftbar,
    Body
  },
  methods:{
    hiddeleftbar(){
      var el = document.getElementById("leftbar");
      var el2 = document.getElementById("talkbody");
      if(el.style.display != "none"){
        el.style.display = "none";
        el2.style.width = "100%";
      }else{
        el.style.display = "block";
         el2.style.width = "80%";
      }
    }
  }
}
</script>

<style>
html,body{
  height:100%;
  width:100%;
  margin:0;
  padding:0;
}

#app{
  height: 100%;
  margin:0;
  padding:0;
}

#head{
  height:10%;
  border-bottom: 1px solid black;
  align-items: center;
  background-color:rgb(63, 81, 181);
  display: flex;
  align-items: center;
}

#headbutton{
  float: left;
  height:4em;
  width:4em;
  background-color:rgb(63, 81, 181);
  border:0;
  margin-left: 1em;
}

#headbutton:focus{
  border:0;
  outline:none;
  box-shadow: none;
}

#headimg{
  color:white;
}

#headbutton:hover{
  float: left;
  height:4em;
  width:4em;
  border-radius: 50%;

  background-color: rgb(78,95,187);
}

#headname{
  color:white;
  font-size:20px;
  margin-left:1em;
}

#leftbar{
    height: 88%;
    width: 20%;
    float: left;
    display:block;
}

#talkbody{
  height: 88%;
  width: 80%;
  float:left;
}

@media screen and (max-width: 760px) {
  #leftbar{
    display: none;
  }
  #talkbody{
    width: 100%;
  }
}
</style>
