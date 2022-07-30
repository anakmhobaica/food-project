<template>
    <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Recetas</h1>
        <hr><br><br>
        <button type="button" class="btn-agregar">Add receta</button>
        <br><br>
        <table class="table-hover">
          <thead>
            <tr>
              <th scope="col">Título</th>
              <th scope="col">Categoría</th>
              <!-- <th scope="col">Read?</th> -->
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(receta, id_receta) in recetas" :key="id_receta">
              <td>{{ receta.titulo }}</td>
              <td>{{ receta.categoria }}</td>
              <td>
                <div class="btn-group" role="group">
                  <button type="button" class="btn-update">Update</button>
                  <button type="button" class="btn-delete">Delete</button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
export default {
    data(){
        return{
            recetas: [],
            curiosidades: [],
        }
    },
    async mounted() {
        this.recetas = await this.getRecetas();
        this.curiosidades = await this.getCuriosidades();
    },
    methods: {
        async getRecetas(){
            const recetas = await axios.get('//localhost:5000/recetas');
            this.recetas = recetas;
        },
        async getCuriosidades(){
            const curiosidades = axios.get('//localhost:5000/curiosidades');
            return curiosidades.data;
        },
    }
}
// import axios from 'axios'
// import CKEditor from '@ckeditor/ckeditor5-vue';
// import ClassicEditor from '@ckeditor/ckeditor5-build-classic';
// export default {
//     components: {
//         ckeditor: CKEditor.component
//     },
//     data() {
//         return {
//             nombre: '',
//             tiempo: '',
//             dificultad: 'Facil',
//             parrafo: '',
//             categoria: 'Fit',
//             ingredientes: '',
//             procedimiento: '',
//             link: '',
//             rawHtml: null,
//             editor: ClassicEditor,
//             titulo: '',
//             info: '',
//             imagen: '',
//             }
//     },
//     methods: {
//         crearReceta() {
//             const id = this.nombre.toLowerCase().normalize("NFD").replaceAll(/\p{Diacritic}/gu, "").replaceAll(' ', '-');
//             const tiempoString = `${this.tiempo} min`;
//             axios.post('//localhost:5000/recetas', {
//                 id_receta: id, titulo: this.nombre, tiempo: tiempoString, dificultad: this.dificultad, parrafo: this.parrafo, categoria: this.categoria, ingredientes: this.ingredientes, procedimiento: this.procedimiento, imagen: this.link
//             }).then(response => {
//                 console.log(response);
//             })
//         },
//         crearCuriosidad() {
//             const id = this.titulo.toLowerCase().normalize("NFD").replaceAll(/\p{Diacritic}/gu, "").replaceAll(' ', '-');
//             axios.post('//localhost:5000/curiosidades', {
//                 id_curiosidad: id, titulo: this.titulo, parrafo: this.info, imagen: this.imagen
//             }).then(response => {
//                 console.log(response);
//             })
//         },
//     }   
</script>

<style scoped>
.subtitulo-contact{
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
    margin-top: 70px;
    text-align: center;
    font-size: 40px;
    font-weight: 300;
}

.firma {
    font-family: Verdana, Geneva, Tahoma, sans-serif;
    color: #fff;
    font-size: 12px;
    margin: 15px;
    text-align: center;
}

.warpper{
    display:flex;
    flex-direction: column;
    align-items: start;
    margin: auto; 
    max-width: 800px;
    font-family: Verdana, Geneva, Tahoma, sans-serif;
    margin-top: 50px;
    margin-bottom: 90px;
}
  
.tab{
    cursor: pointer;
    padding:10px 20px;
    margin:0px 2px;
    background:#e01304;
    display:inline-block;
    color:#fff;
    border-radius:3px 3px 0px 0px;
    box-shadow: 0 0.5rem 0.8rem #00000080;
}
.panels{
    background:#fffffff6;
    box-shadow: 0 2rem 2rem #00000080;
    min-height:400px;
    width: 100%;
    border-radius:3px;
    overflow:hidden;
    padding: 40px;
}
.panel{
    display:none;
    animation: fadein .8s;
}
.panel-title{
    font-size:1.5em;
    font-weight:bold
}
.radio{
    display:none;
}
  #one:checked ~ .panels #one-panel,
  #two:checked ~ .panels #two-panel,
  #three:checked ~ .panels #three-panel{
    display:block
}
  #one:checked ~ .tabs #one-tab,
  #two:checked ~ .tabs #two-tab{
    background:#fffffff6;
    color:#e01304;
    border-top: 3px solid #e01304;
}
  
.direccion {
    display: flex;
    justify-content: space-between;
    z-index: 0;
}
.dir {
    height: 450px;
    position: relative;
    background-position: right;
    width: 600px;
    margin-left: 24px;
    display: flex;
    align-items: center;
    z-index: 3;
} 
textarea{
    background-color: #fbfbfb; 
    width: 405px; 
    height: 100px; 
    border-radius: 5px;  
    border-style: solid; 
    border-width: 1px; 
    border-color: #02a352; 
    margin-top: 5px;  
    padding-left: 5px;
    margin-bottom: 15px; 
    padding-top: 10px; 
    font-family: Verdana, Geneva, Tahoma, sans-serif;
    font-size: 14px;
}
  
form p {
    margin: 0px;
    margin-bottom: 12px;
}
  
.title{
    margin: 0.5cm 0.5cm 0.5cm 0cm; 
    font-size: 28px;   
    /* color: #e01304; */
    color: black;
}
.receta, .curiosidad {
    /* margin: 0.5cm; */
    padding: 1cm;
    width: 15cm;
}

.tituloR>input, .tiempo>input, .imagen>input, .tituloC>input{
    flex:1;
    padding:0.6em;
    border:0.2em solid #e01304;
    background-color: whitesmoke;
    width:50%;
    margin: 0cm 0.5cm 0.5cm 0cm;
}

.dificultad, .categoria {
    display: flex;
    font-family:Verdana, Geneva, Tahoma, sans-serif;
    font-size: 17px;
    color: #e01304;
    align-items: center
}

.dificultad>select, .categoria>select {
    padding:0.6em;
    border:0.2em solid #e01304;
    background-color: whitesmoke;
    width: 3cm;
    margin: 0.5cm;
    font-family:Verdana, Geneva, Tahoma, sans-serif;
}

.parrafo>textarea{
    border:0.2em solid #e01304;
    background-color: whitesmoke;
    width: 13cm;
    margin: 0cm 0.5cm 0.5cm 0cm;
    font-family:Verdana, Geneva, Tahoma, sans-serif;
    border-radius: 0px;
}

.ingrediente, .procedimiento, .parrafo, .tituloR, .tiempo, .imagen, .tituloC {
    padding: 0cm 0.5cm 0.5cm 0cm;
    display: flex;
    font-family:Verdana, Geneva, Tahoma, sans-serif;
    font-size: 17px;
    color: #e01304;
    flex-direction: column;
    width: 510px;
}

.bReceta, .bCuriosidad {
    font-family:Verdana, Geneva, Tahoma, sans-serif;
    font-size: 17px;
    padding: 0.5cm;
    background-color: #e01304;
    color: white;
    margin-bottom: 10px;
    cursor: pointer;
}

.boton{
    width: 21.2cm;
    text-align: center;
}

</style>