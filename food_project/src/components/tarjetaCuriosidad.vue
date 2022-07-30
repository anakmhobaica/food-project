<template>
    <div class="cuadro1">
        <div class="imagen" :style="{ backgroundImage: `url(${imagen})`, backgroundSize: 'cover' }">
            <!-- <img :src="imagen" alt="Imagen" class="fotito"> -->
        </div>
        <div class="infor">
            <h2>{{titulo}}</h2>
            <p class="par">
                {{parrafo}}
            </p>        
        </div>

    </div>
</template>

<script>
export default{
    props: {
        imagen: String,
        titulo: String,
        parrafo: String,
    }
}
</script>

<style scoped>
div.cuadro1 {
    width: 275px;
    height: 100%;
    background-color: white ;
}
h3 {
    font-size: 16px;
}
.imagen{
    height: 180px;
    background-size: cover;
    background: grey;
}
div.infor {
    font-family: Arial, Helvetica, sans-serif;
    padding: 4px 12px 12px 12px;
    font-size: 14px;
}

p.par {
    color: rgb(56, 56, 56);
}

div.letras {
    color: #e01304; 
    display: flex;
    justify-content: space-evenly;
}

</style>