<script lang="ts">
import Product from "./Product.vue";
import axios from 'axios'
import Product from './Product.vue'

export default({
    data() {
        return {
            products: [] as Array<object>
        };
    },
    mounted: function () {
        this.$nextTick(function () {
            axios.get("http://localhost:5000/api/product").then((response) => {
                let data = response.data;
                data.forEach((product: object) => {
                  console.log(product.imagePath);
                    if(product.imagePath === undefined)
                    {
                      product.imagePath = "https://media.istockphoto.com/vectors/thumbnail-image-vector-graphic-vector-id1147544807?k=20&m=1147544807&s=612x612&w=0&h=pBhz1dkwsCMq37Udtp9sfxbjaMl27JUapoyYpQm0anc="
                    }
                    this.products.push(product);
                });
            });
        });
    },
    components: { Product }
})



</script>
<template>
  <div id="products" v-for="product in products">
    <Product :productName="product.name" :productPrice=product.price :imageURL=product.imagePath></Product>
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



