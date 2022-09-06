<script setup lang="ts">
import { RouterLink, RouterView } from "vue-router";
import Product from "./components/Product.vue";
</script>

<template>
  <div class="nav">
    <img class="navlogo" src="src/components/icons/Robot.png"/>
    <navlink class="navlink">
      <RouterLink to="/">Home</RouterLink>
    </navlink>
    <navlink class="navlink" >
      <RouterLink to="/products">Products</RouterLink>
    </navlink>
    <navlink class="navlink" >
      <RouterLink to="/about">About</RouterLink>
    </navlink>
  </div>
  
  <!-- Where content will be displayed -->
  <RouterView />
</template>

<style scoped>

.navlogo{
  height: 60px;
  border-radius: 8px;
  margin: 0 5px 0 5px;
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

nav a.router-link-exact-active {
  color: var(--color-text);
}

nav a.router-link-exact-active:hover {
  background-color: transparent;
}

@media (max-width: 1024px) {
  .nav{
    justify-content: center;
  }

  .navlogo{
    position: absolute; 
    left: 5px;
  }
}
</style>
