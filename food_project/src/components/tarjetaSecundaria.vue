<template>
<div class="hacks-home">
    <div class="imagen-home" :style="{ backgroundImage: `url(${imagen})`, backgroundSize: 'cover' }"></div> 
    <div class="info-home">
        <p class="parrafo-home">
            {{parrafo}}
        </p>
    </div>
    <br> 
</div>
</template>

<script> 
    export default{
        props : {
            imagen:String,
            titulo:String,
            parrafo:String,
        }
    }
</script>

<style scoped>
.imagen-home{
    height: 200px;
}

</style>