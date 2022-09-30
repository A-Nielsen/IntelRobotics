<script setup lang="ts">
defineProps<{
  productId: string;
}>();
</script>

<template>
  <div class="product">
    <img class="Image" src="https://media.istockphoto.com/vectors/thumbnail-image-vector-graphic-vector-id1147544807?k=20&m=1147544807&s=612x612&w=0&h=pBhz1dkwsCMq37Udtp9sfxbjaMl27JUapoyYpQm0anc="/>
    <p class="product-name">{{productId}}</p>
    <p class="product-text">wwwwwwwwwww wafsd adsf asdfadslæfkqewfj pgmåsdfnhåjfåg jzåfnvaåodsnåak dmvåoxkgfåzpdjgskon  </p>
  </div>
</template>
 
<style scoped>
  .product{
    width: 30vw;
    margin-top: var(--margin-default);
    padding: 20px;
    background-color: var(--color-background-soft);
    border-radius: 8px;

    /* stops image from having space at bottom */
    display:flex;
    align-items: left;
    justify-content: center;
    flex-direction: column;
  }

  .Image{
    border-radius: 8px;
  }

  .product-name{
    font-size: xx-large;
    color: var(--color-heading)
  }
</style>
