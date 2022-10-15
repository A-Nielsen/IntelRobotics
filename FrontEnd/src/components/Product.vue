<script setup lang="ts">
defineProps<{
  productName: string;
  productPrice: number;
  imageURL: string;
}>();
</script>

<template>
  <div class="product">
    <img style="background-image: url('https://media.istockphoto.com/vectors/thumbnail-image-vector-graphic-vector-id1147544807?k=20&m=1147544807&s=612x612&w=0&h=pBhz1dkwsCMq37Udtp9sfxbjaMl27JUapoyYpQm0anc=')" class="Image" :src="imageURL"/>
    <p class="product-name">{{productName}}</p>
    <p class="product-text">indicative price: <br/>{{productPrice}} $USD</p>
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

  
  @media only screen and (max-width: 1024px) {
    .product{
    width: 80vw;
    }
  }
</style>
