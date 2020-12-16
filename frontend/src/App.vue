<template>
  <div id="app">
    <div if="Top"><NavMenu></NavMenu></div>
    <div id="Wrapper">
      <div class="content">
        <div id="Leftbar"></div>
        <div id="Rightbar"></div>
        <div id="Main">
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
import NavMenu from "./components/NavMenu.vue";
import TalkBox from "./components/TalkBox.vue";

export default {
  name: "App",
  components: {
    NavMenu,
    TalkBox,
  },
};
</script>

<style>
html,
body {
  width: 100%;
  height: 100%;
  position: fixed;
}
#app {
  width: 100%;
  height: 100%;
}
#Top {
  padding-right: 300px;
  padding-left: 300px;
  background-color: white;
}

#Wrapper {
  width: 50%;
  height: 100%;
  text-align: center;
  background-repeat: repeat-x;
  float: right;
}

.content {
  max-width: 1100px;
  margin: 0 auto;
  height:100%;
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
  width: auto;
  height:100%;
  max-width: 760px;
}

.box {
  background-color: var(--box-background-color);
  border-radius: var(--box-border-radius);
  box-shadow: 0 2px 3px rgba(0, 0, 0, 0.1);
  border-bottom: 1px solid var(--box-border-color);
}

#BOX {
  padding: 0;
  height: 90%;
}

@media screen and (max-width: 960px) {
  #Wrapper {
    width:100%;
    position: absolute;
  }
}
</style>
