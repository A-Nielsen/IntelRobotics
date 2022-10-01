<script setup lang="ts">
import Product from "./Product.vue";
</script>

<template>
  <div id="products">
      <Product productName="test" productDesc="safgatga" imageURL="https://media.istockphoto.com/vectors/thumbnail-image-vector-graphic-vector-id1147544807?k=20&m=1147544807&s=612x612&w=0&h=pBhz1dkwsCMq37Udtp9sfxbjaMl27JUapoyYpQm0anc="/>
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