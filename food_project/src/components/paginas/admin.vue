<template>
    <div class="container">
        <div class="title-add">
            <h1>Recetas</h1>
            <button type="button" class="agregar" @click="goToForm">Agregar</button>
        </div>
        <div class="row">
            <br><br>
            <table class="table-hover">
            <thead>
                <tr>
                <th scope="col" class="info-title">Título</th>
                <th scope="col" class="info-cat">Categoría</th>
                <th></th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="(receta) in recetas" :key="receta.id_receta">
                <td class="titulos">{{ receta.titulo }}</td>
                <td class="categorias">{{ receta.categoria }}</td>
                <td>
                    <div class="btn-group" role="group">
                        <button type="button" class="delete-button" @click="deleteReceta(receta.id_receta)"><b><font-awesome-icon icon="trash-can" style="width:20px; height:20px"/></b></button>
                    </div>
                </td>
                </tr>
            </tbody>
            </table>
        </div>
        <div class="title-add">
            <h1>Curiosidades</h1>
            <button type="button" class="agregar" @click="goToForm">Agregar</button>
        </div>
        <div class="row">
            <br><br>
            <table class="table-hover">
            <thead>
                <tr>
                <th scope="col" class="info-title">Título</th>
                <th></th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="(curiosidad) in curiosidades" :key="curiosidad.id_curiosidad">
                <td class="titulos">{{ curiosidad.titulo }}</td>
                <td>
                    <div class="btn-group" role="group">
                        <button type="button" class="delete-button" @click="deleteCuriosidad(curiosidad.id_curiosidad)"><b><font-awesome-icon icon="trash-can" style="width:20px; height:20px"/></b></button>
                    </div>
                </td>
                </tr>
            </tbody>
            </table>
        </div>
  </div>
</template>

<script>
import axios from 'axios';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
export default {
    components :{
        FontAwesomeIcon,
    },
    data(){
        return{
            recetas: [],
            curiosidades: [],
        }
    },
    async mounted() {
        await this.getRecetas();
        await this.getCuriosidades();
    },
    methods: {
        async getRecetas(){
            const recetas = await axios.get('//localhost:5000/recetas');
            this.recetas = recetas.data;
        },
        async deleteReceta(id){
            const usuario = localStorage.getItem('user');
            this.usuario = JSON.parse(usuario);
            await axios.delete(`//localhost:5000/eliminar-receta/${id}?usuario=${this.usuario.nombre}`);
            const recetas = await axios.get('//localhost:5000/recetas');
            this.recetas = recetas.data;
            // console.log(this.recetas)
        },
        async getCuriosidades(){
            const curiosidades = await axios.get('//localhost:5000/curiosidades');
            this.curiosidades = curiosidades.data;
        },
        async deleteCuriosidad(id){
            const usuario = localStorage.getItem('user');
            this.usuario = JSON.parse(usuario);
            await axios.delete(`//localhost:5000/eliminar-curiosidad/${id}?usuario=${this.usuario.nombre}`);
            const curiosidades = await axios.get('//localhost:5000/curiosidades');
            this.curiosidades = curiosidades.data;
            // console.log(this.recetas)
        },
        goToForm(){
            window.location.href = '/admin-agregar';
        },
    }
} 
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@600&display=swap');
h1{
    font-size: 38px;
    font-family: 'Quicksand', sans-serif;
    /* margin-bottom: 40px;
    margin-left: 30px; */
}

.title-add {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin: 20px 50px 20px 50px
}

.agregar {
    height: 50px;
    font-size: 16px;
    border: none;
    cursor: pointer;
    font-family: 'Quicksand', sans-serif;
    background-color: rgb(8, 164, 8);
    color: #fff;
    padding: 7px 10px 7px;
    border-radius: 10px;
}

.agregar:hover {
    background-color: black;
}

.info-title{
    width: 340px;
    background-color: black;
    color: #fff;
    padding: 20px 0 20px; 
    font-family: 'Quicksand', sans-serif;
}

.info-cat {
    width: 240px;
    background-color: black;
    color: #fff;
    padding: 20px 0 20px; 
    font-family: 'Quicksand', sans-serif;
}

.titulos{
    width: 340px;
    height: auto;
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 20px 0 20px; 
    font-family: 'Quicksand', sans-serif;
    border: 1px solid gray;
}

.categorias{
    width: 240px;
    height: auto;
    text-align: center;
    padding: 20px 0 20px; 
    font-family: 'Quicksand', sans-serif;
    border: 1px solid gray;
}

.row {
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
}

.btn-group {
    width: 50px;
    display: flex;
    justify-content: center;
}

.delete-button {
    border: none;
    background: none;
    cursor: pointer;
    color: red;
    width: 50px;
    height: 50px;
}

.delete-button:hover{
    color: black;
}

</style>