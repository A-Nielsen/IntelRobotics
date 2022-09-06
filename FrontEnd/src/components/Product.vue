<script setup lang="ts">
defineProps<{
  productId: string;
}>();
</script>

<template>
  <div class="Product">
    <img class="Image" src="https://media.istockphoto.com/vectors/thumbnail-image-vector-graphic-vector-id1147544807?k=20&m=1147544807&s=612x612&w=0&h=pBhz1dkwsCMq37Udtp9sfxbjaMl27JUapoyYpQm0anc="/>
  </div>
</template>

<style scoped>
  .Image{
    border-radius: 8px;
    width: 100%;
  }

 @media screen and (max-width: 750px) {
  .Image{
    border-radius: 8px;
    width: 50%;
  }

}

</style>
