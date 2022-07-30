<template>
    <div class="cuadro">
        <div class="fotito">
            <img :src="receta.imagen" alt="Foto" class="image">
        </div>
        <div class="titulo"><h1 v-html="receta.titulo" class="nReceta"></h1></div>
        <div class="allInfo">
            <div class="ingr">
                <h1 class="titulos">Ingredientes:</h1>
                <div v-html="receta.ingredientes" class="parraf1"></div>

            </div>
            <div class="proced">
                <h1 class="titulos">Procedimiento:</h1>
                <div v-html="receta.procedimiento" class="parraf2"></div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
// import imagen from './imagenes/3-2.png'
export default {
    data() {
    return {
        //foto: imagen,
        receta: {},
    } 
    },
    mounted() {
        this.getReceta(this.$route.params.id);
        console.log(this.$route.params.id);
    },
    methods: {
        getReceta(id) {
            axios.get(`//localhost:5000/recetas/${id}`).then(response => {
                this.receta = response.data[0];
                console.log(this.response);
            })
        }
    },
}
</script>

<style scoped>
div.cuadro { 
    margin: 0cm 4cm;
}

.image {
    width: 100%;
}

.nReceta {
    font-family:Cambria, Cochin, Georgia, Times, 'Times New Roman', serif;
    font-size: 50px;

}

.titulo {
    text-align: center;
}

.allInfo {
    display: flex;
    justify-content: space-evenly;
    margin: 1cm 0cm 0cm 0cm;
    font-family:Cambria, Cochin, Georgia, Times, 'Times New Roman', serif;
}

.ingr {
    width: 15cm;

}

.parraf1 {
    border: 0.05cm solid #e01304;
    font-family:Arial, Helvetica, sans-serif;
    margin: 0cm 1cm 0cm 0cm;;
}

.parraf2 {
    font-family:Arial, Helvetica, sans-serif;
    margin: 0cm 1cm 0cm 0cm;;
}

.proced {
    width: 25cm;
}

.titulos {
    color: #e01304;
}

</style>>
