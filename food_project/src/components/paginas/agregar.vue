<template>
    <section id="contacto">
        <div class="warpper">
            <input class="radio" id="one" name="group" type="radio" checked>
            <input class="radio" id="two" name="group" type="radio">
            <div class="tabs">
                <label class="tab" id="one-tab" for="one">Recetas</label>
                <label class="tab" id="two-tab" for="two">Curiosidades</label>
            </div>
            <div class="panels">
                <div class="panel" id="one-panel">
                    <div class="title"><h1>Nueva Receta</h1></div>
                    <form>
                        <div class="tituloR">
                            <p>Título de la Receta:</p>
                            <input type="text" placeholder="Título" v-model="nombre">
                        </div>
                        <div class="tiempo">
                            <p>Tiempo:</p>
                            <input type="number" placeholder="Tiempo" v-model="tiempo" min="0">
                        </div>
                        <div class="dificultad">
                            <p>Dificultad:</p>
                            <select name="dificultad" v-model="dificultad">
                                <option value="Facil">Facil</option>
                                <option value="Media">Media</option>
                                <option value="Dificil">Dificil</option>
                                <option value="Muy Dificil">Muy Dificil</option>
                            </select>
                        </div>
                        <div class="parrafo">
                            <p>Información:</p>
                            <textarea v-model="parrafo" placeholder="Información de la receta" rows="4" cols="40" style="resize: none"/>
                        </div>
                        <div class="categoria">
                            <p>Categoría:</p>
                            <select name="categoria" v-model="categoria">
                                <option value="Fit">Fit</option>
                                <option value="Fat">Fat</option>
                            </select>
                        </div>
                        <div class="ingrediente">
                            <p>Ingredientes:</p>
                            <ckeditor :editor="editor" v-model="ingredientes"></ckeditor>
                        </div>
                        <div class="procedimiento">
                            <p>Procedimiento:</p>
                            <ckeditor :editor="editor" v-model="procedimiento"></ckeditor>
                        </div>
                        <div class="imagen">
                            <p>Ruta de la imágen:</p>
                            <input type="text" placeholder="Ruta de la imagen" v-model="link">
                        </div>
                    </form>
                    <div class="boton"><button @click="crearReceta" class="bReceta">Crear Receta</button></div> 
                </div>
            <div class="panel" id="two-panel">
                <div>
            <div class="title"><h1>Nueva Curiosidad</h1></div>
            <form>
                <div class="tituloC">
                    <p>Título de la Curiosidad:</p>
                    <input type="text" placeholder="Título" v-model="titulo">
                </div>
                <div class="parrafo">
                    <p>Información:</p>
                    <textarea v-model="info" placeholder="Información de la curiosidad" rows="4" cols="40" style="resize: none"/>
                </div>
                <div class="imagen">
                    <p>Ruta de la imágen:</p>
                    <input type="text" v-model="imagen" placeholder="Ruta de la imagen">
                </div>
            </form>
            <div class="boton">
                <button @click="crearCuriosidad" class="bCuriosidad">Crear Curiosidad</button>
            </div>
                </div>
            </div>
            </div>
        </div>
    </section>
</template>

<script>
import axios from 'axios'
import CKEditor from '@ckeditor/ckeditor5-vue';
import ClassicEditor from '@ckeditor/ckeditor5-build-classic';
export default {
    components: {
        ckeditor: CKEditor.component
    },
    data() {
        return {
            nombre: '',
            tiempo: '',
            dificultad: 'Facil',
            parrafo: '',
            categoria: 'Fit',
            ingredientes: '',
            procedimiento: '',
            link: '',
            rawHtml: null,
            editor: ClassicEditor,
            titulo: '',
            info: '',
            imagen: '',
            }
    },
    methods: {
        crearReceta() {
            const id = this.nombre.toLowerCase().normalize("NFD").replaceAll(/\p{Diacritic}/gu, "").replaceAll(' ', '-');
            const tiempoString = `${this.tiempo} min`;
            const usuario = localStorage.getItem('user');
            this.usuario = JSON.parse(usuario);
            axios.post('//localhost:5000/recetas', {
                id_receta: id, titulo: this.nombre, tiempo: tiempoString, dificultad: this.dificultad, parrafo: this.parrafo, categoria: this.categoria, ingredientes: this.ingredientes, procedimiento: this.procedimiento, imagen: this.link, usuario: this.usuario.nombre
            }).then(response => {
                console.log(response);
                window.location.href = '/admin'
            })
        },
        crearCuriosidad() {
            const id = this.titulo.toLowerCase().normalize("NFD").replaceAll(/\p{Diacritic}/gu, "").replaceAll(' ', '-');
            const usuario = localStorage.getItem('user');
            this.usuario = JSON.parse(usuario);
            axios.post('//localhost:5000/curiosidades', {
                id_curiosidad: id, titulo: this.titulo, parrafo: this.info, imagen: this.imagen, usuario: this.usuario.nombre
            }).then(response => {
                console.log(response);
                window.location.href = '/admin'
            })
        },
    }   
}
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