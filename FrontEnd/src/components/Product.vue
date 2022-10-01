<script setup lang="ts">
defineProps<{
  productName: string;
  productDesc: string;
  imageURL: string;
}>();
</script>

<template>
  <div class="product">
    <img class="Image" :src="imageURL"/>
    <p class="product-name">{{productName}}</p>
    <p class="product-text">{{productDesc}}</p>
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
