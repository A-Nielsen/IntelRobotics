<script setup lang="ts">
import Product from "./Product.vue";
</script>

<template>
  <div id="products">
      <Product productId="test"/>
      <Product productId="test2"/>
  </div>
</template>

<style scoped>

  #products{
    width: 100vw;
    display: flex;
    align-items: center;
    flex-direction: column;
  } 
</style>