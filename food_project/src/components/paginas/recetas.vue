<template>
<div>
    <div>
        <h1 class="title">RECETAS FIT</h1>
        <div class="recetasFit">
            <tarjetaReceta v-for="receta in recetasFit" :key="receta.titulo" :imagen="receta.imagen" :titulo="receta.titulo" :tiempo="receta.tiempo" :dificultad="receta.dificultad" :parrafo="receta.parrafo" :link="receta.id_receta"/>
        </div>
    </div>

    <div>
        <h1 class="title">RECETAS FAT</h1>
        <div class="recetasFat">
            <tarjetaReceta v-for="receta in recetasFat" :key="receta.titulo" :imagen="receta.imagen" :titulo="receta.titulo" :tiempo="receta.tiempo" :dificultad="receta.dificultad" :parrafo="receta.parrafo" :link="receta.id_receta"/>
        </div>
    </div>
</div>
</template>

<script>
import axios from 'axios';
import tarjetaReceta from '../tarjetaReceta.vue';

export default {
    components: {
        tarjetaReceta,
    },
    data() {
        return {
        recetasFit: [],
        recetasFat: [],
        }
    },
    async mounted() {
        this.recetasFit = await this.getRecetasFit();
        console.log(this.recetasFit)
        this.recetasFat = await this.getRecetasFat();
        // console.log(sqlClient);
    },
    methods:{
        async getRecetasFit(){
            const recetasFit = await axios.get('//localhost:5000/recetas?categoria=Fit');
            return recetasFit.data
        },
        async getRecetasFat(){
            const recetasFat = await axios.get('//localhost:5000/recetas?categoria=Fat');
            return recetasFat.data
        }
        
    }
}
</script>

<style scoped>

div.recetasFit, div.recetasFat{
    margin: 2cm 3cm 2cm;
    display: grid;
    grid-template-columns: auto auto auto auto;
    grid-gap: 24px;
    justify-content: center;
}

h1.title {
   margin: 1cm 3cm 1cm; 
   color: #e01304;
   font-family:Cambria, Cochin, Georgia, Times, 'Times New Roman', serif;
}
</style>