<template>
<div class="parr">
    <h1 class="title">CURIOSIDADES</h1>
    <div class="curiosidades">
        <tarjetaCuriosidad v-for="receta in curiosidades" :key="receta.titulo" :imagen="receta.imagen" :titulo="receta.titulo" :tiempo="receta.tiempo" :dificultad="receta.dificultad" :parrafo="receta.parrafo" :link="receta.link"/>
    </div>
</div>  
</template>

<script>
import axios from 'axios';
import tarjetaCuriosidad from '../tarjetaCuriosidad.vue';
export default {
    components: {
        tarjetaCuriosidad,
    },
    data() {
    return {
        curiosidades: [],
    } 
    },
    mounted() {
        this.getCuriosidades();
    },
    methods:{
        getCuriosidades(){
            axios.get('//localhost:5000/curiosidades').then(response => {
                this.curiosidades = response.data;
            });
        },
    }
}
</script>

<style scoped>
div.curiosidades{
    margin: 2cm 3cm 2cm;
    display: grid;
    grid-template-columns: auto auto auto auto;
    grid-gap: 24px;
    grid-auto-rows: 1fr;
    justify-content: center;
}

h1.title {
   margin: 1cm 3cm 1cm; 
   font: 'Montserrat Alternates';
   color: #e01304;
   font-family:Cambria, Cochin, Georgia, Times, 'Times New Roman', serif;
}
</style>>
