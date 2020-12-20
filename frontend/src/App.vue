<template>
  <div id="app">
      <div id="Wrapper">
          <div class="content">
            <div id="Leftbar"></div>
            <div id="Rightbar"></div>
            <div id="Main">    
              <div class="sep20"></div>
              <div class="box" id="BOX">
                  <TalkBox></TalkBox>
              </div>
              <div class="sep20"></div>
          </div>
      </div>
    </div>  
  </div>
</template>

<script>
import TalkBox from './components/TalkBox.vue'

export default {
  name: 'App',
  components: {
    TalkBox
  }
}
</script>

<style>
html, body{
    widows: 100%;
    height: 100%;
}
#app{
    width: 100%;
    height: 100%;
    background-image: url(/static/img/shadow_light.png);
    background-color: #e2e2e2;
}
#Top{
  padding-right:300px;
  padding-left:300px;
  background-color: white;
}

#Wrapper {
    text-align: center;
    background-repeat: repeat-x;
}

.content {
    min-width: 600px;
    max-width: 1100px;
    margin: 0 auto;
}

#Leftbar {
    width: 0;
    float: left;
}

#Rightbar {
    width: 270px;
    float: right;
    margin-right: 20px;
}

#Main {
    margin: 0 auto;
    width: auto;
    max-width: 760px;
}

.sep20 {
    height: 20px;
}

.box {
    background-color: var(--box-background-color);
    border-radius: var(--box-border-radius);
    box-shadow: 0 2px 3px rgba(0,0,0,.1);
    border-bottom: 1px solid var(--box-border-color);
    width:33em;
}

#BOX{
  padding:0;
}
</style>
