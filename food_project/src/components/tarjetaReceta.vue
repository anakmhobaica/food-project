<template>
    <div class="cuadro1">
        <div class="imagen" :style="{ backgroundImage: `url(${imagen})`, backgroundSize: 'cover' }">
            <!-- <img :src="imagen" alt="Imagen" class="fotito"> -->
        </div>
        <div class="infor">
            <h2>{{titulo}}</h2>
            <div class="letras">
                <div><b><font-awesome-icon icon="hourglass-half"/> {{tiempo}}</b></div>
                <div><b><font-awesome-icon icon="clipboard-check"/> {{dificultad}}</b></div>
            </div>
            <p class="par"> 
                {{parrafo}}
            </p>        
            <div class="buttonT">
                <button class="buttonT" @click="navigate()">Seguir Leyendo</button>
            </div>
        </div>

    </div>
</template>

<script>

import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
export default{
    components: {
        FontAwesomeIcon,
    },
    props: {
        imagen: String,
        titulo: String,
        tiempo: String,
        dificultad: String,
        parrafo: String,
        link: String,
        receta: Object,
    },
    methods: {
        navigate() {
            this.$router.push({ path: `/receta/${this.link}`});
            // console.log(this.link)
        }
    }, 
    created() {
        console.log(this.receta)
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

div.buttonT {
    text-align: left;
}

button.buttonT{
    background-color: white;
    color: grey;
    border: 1px solid grey;
    width: 150px;
    height: 45px;
    cursor: pointer;
    font-size: 14px;
    margin: auto;
}
button.buttonT:hover {
    color: white;
    background-color: #e01304;
    border: 1px solid #e01304;
}


</style>