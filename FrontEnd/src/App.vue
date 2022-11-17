<script setup lang="ts">
import { RouterLink, RouterView } from "vue-router";
</script>

<template>
  <div class="flex-wrapper">
    
    <div class="nav">
      <div class="logo">
        <RouterLink to="/" class><img class="navlogo" src="/Robot.png"/></RouterLink>
      </div>
      <div class="navlink">
        <RouterLink to="/">Home</RouterLink>
      </div>
      <div class="navlink" >
        <RouterLink to="/products">Products</RouterLink>
      </div>
      <div class="navlink" >
        <RouterLink to="/about">About</RouterLink>
      </div>
    </div>
  

    <!-- Where content will be displayed -->
    <div id="main">
      <RouterView />
    </div>
  </div>
  
  <div id="footer">
      <div class="footer-row">
        <img class="navlogo" src="/Robot.png"/>
      </div>  
      <div class="footer-row">
        <p>&#169; 2022 - IntelRobotics</p>
      </div>
      <div class="footer-row">
        <div class="footer-text">
          <p>Useful links</p>
        </div>
        <div class="footer-text">
          <p>Other info</p>
        </div>
      </div>
      <div class="footer-row">
        <div class="footer-text">
          <a href="https://vuejs.org/">Vue</a>
        </div>
        <div class="footer-text">
          <p>Contact info</p>
        </div>
      </div>
    </div>
</template>

<style scoped>
body {
  height: 100vh;
  margin: 0;
  padding: 0;
}

#main{
  flex:1;
}

.flex-wrapper {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

.navlogo{
  height: 60px;
  border-radius: 8px;
  margin: 0 5px 0 5px;
}

.logo{
  margin: 0;
  padding: 0;
  line-height: 0;
  border-radius: 8px;
}

.navlink a{
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
}

.nav{
  display: flex;
  margin: 0;
  padding: 5px 0 5px 0;
  align-items: center;
  justify-content: left;
  background-color: var(--vt-c-black-mute);
}

.navlink{
  height: 60px;
  width: 100px;
  font-size: larger;
}

#footer{
  margin-top: var(--margin-default);
  margin-bottom: var(--margin-default);
  display: flex;
  flex-direction: column;
}

.footer-row{
  display: flex;
  flex-direction: row;
  justify-content: space-around;
}

.footer-text{
  width: 100px;
  display: flex;
  justify-content: left;
}

nav a.router-link-exact-active {
  color: var(--color-text);
}

nav a.router-link-exact-active:hover {
  background-color: transparent;
}

@media (max-width: 1024px) {

}
</style>
