<template>
    <section class="content">
        <div class="column1">
            <tarjeta-principal v-for="receta in recetas" :key="receta.titulo" :imagen="receta.imagen" :titulo="receta.titulo" :parrafo="receta.parrafo" :link="receta.id_receta"/>

            <!-- <h1>Pie de Limón</h1>
                <p>Aprende a preparar Pie de Limón con esta rica y fácil receta. El Pie de limón es una de las recetas mas demandadas en las reuniones.
                    Normalmente, por comodidad, acostumbramos a encargarlo en la pastelería más cercana, pero ¿Por qué no preparar tu propio Pie de Limón? 
                    Como resultado tendrás una receta con un sabor único basado en tus gustos personales. 
                </p>
                <img :src="foto1" alt="Pie de Limón">  
                <br> 
                <button class="button1" @click="navigate('/receta/pie-de-limon')">Leer más</button>
                <br><br><br>
                <hr>
                <br>

                <h1>Café Dalgona</h1>
                <p>Aprende a hacer el café del momento, esta receta que llegó a nosotros gracias a la red social TikTok y y que ahora es lo más TOP. 
                Es fácil, delicioso y parece hecho en una cafetería. Te vamos a enseñar 3 formas distintas de hacer este famoso café, para todos los gustos.
                </p>
                <img :src="foto2" alt="Café Dalgona">
                <br>
                <button class="button1" @click="navigate('/receta/cafe-dalgona')">Leer más</button>
                <br><br><br>
                <hr>
                <br>

                <h1>Pasticho de Carne</h1>
                <p>El pasticho es la versión venezolana de la lasaña, es muy parecido pero tiene su propia receta. No hay una receta en especifico para el 
                pasticho, este puede ser adaptado a cualquier gusto.     
                </p>
                <img :src="foto3" alt="Pasticho de Carne">
                <br>
                <button class="button1" @click="navigate('/receta/pasticho-de-carne')">Leer más</button>
                <br><br><br>
                <hr>
                <br>

                <h1>Panquecas de Avena Fitness</h1>
                <p>Ser saludables no te impide comer rico. Esta receta de Panquecas de Avena es perfecta para cuando quieres tener un desayuno rico sin tener 
                que pecar. Un plato delicioso y saludable.     
                </p>
                <img :src="foto4" alt="Panquecas de Avena">
                <br>
                <button class="button1" @click="navigate('/receta/panquecas-de-avena-fitness')">Leer más</button>
                <br><br> -->
        </div>
        
        <div class="column2">
            <h2>ALGUNOS HACKS</h2>
            <tarjeta-secundaria v-for="curiosidad in curiosidades" :key="curiosidad.titulo" :imagen="curiosidad.imagen" :titulo="curiosidad.titulo" :parrafo="curiosidad.parrafo" :link="curiosidad.id_curiosidad"/>
            <!-- <img :src="foto5" alt="Recipientes de aderezos">  
            <br>
            <p>
                Los recipientes de aderezos como kétchup o mostaza pueden tener otro uso útil. Cuando estén vacíos, puedes usarlos para colocar la mezcla 
                de panqueques y facilitar la tarea de prepararlos cuando viertes la mezcla en la sartén.
            </p> 
            <br><br>
            <img :src="foto6" alt="Aguacate">   
            <br>
            <p>
                Para cortar el aguacate en cubos cuando quieras preparar guacamole, la mejor alternativa es usar un pisa papas.
            </p>     
            <br><br>
            <img :src="foto7" alt="Migas de pan">
            <br>
            <p>
                Utilizando un procesador de comidas, puedes obtener tus propias migas de pan libres de gluten, licuando cereales de arroz integral. 
            </p>
            <br><br>
            <img :src="foto8" alt="Chocolate Caliente">
            <br>
            <p>
                Para preparar una taza de chocolate caliente extremadamente deliciosa, agrega trufas a una taza llena de leche caliente. 
            </p>
            <br> -->

            <a class="link1" @click="navigate('/curiosidades')">Más Life Hacks</a>
        </div>
    </section>
</template>

<script>
import axios from 'axios';
import imagen1 from '../imagenes/RFB-2502-3-piedelimonconlicor.jpg';
import imagen2 from '../imagenes/como-hacer-cafe-dalgona.jpg';
import imagen3 from '../imagenes/pasticho-de-carne-750x466.jpg';
import imagen4 from '../imagenes/tortitas-avena-iStock-.jpg';
import imagen5 from '../imagenes/hacks-07.png';
import imagen6 from '../imagenes/hacks-11.png';
import imagen7 from '../imagenes/hacks-35.png';
import imagen8 from '../imagenes/hacks-36.png';
import tarjetaPrincipal from '../tarjetaPrincipal.vue'
import tarjetaSecundaria from '../tarjetaSecundaria.vue';
export default {
    name: 'Home',
    components: {
        tarjetaPrincipal,
        tarjetaSecundaria,
    },
    data(){
        return{
            foto1: imagen1,
            foto2: imagen2,
            foto3: imagen3, 
            foto4: imagen4,
            foto5: imagen5,
            foto6: imagen6,
            foto7: imagen7,
            foto8: imagen8,
            recetas: [],
            curiosidades: [],
        }
    },
    mounted() {
        this.getRecetas();
        this.getCuriosidades();
        // document.addEventListener('DOMContentLoaded', () => {
        //     const title = this.getElementByXpath("//div[@class='info-home']/h1");
        //     console.log(title);
        // })
    },
    methods: {
        getRecetas(){
            axios.get('//localhost:5000/recetas').then(response => {
                this.recetas = response.data.slice(-4).reverse();
            });
        },
        getCuriosidades(){
            axios.get('//localhost:5000/curiosidades').then(response => {
                this.curiosidades = response.data.slice(-4).reverse();
            });
        },
        navigate(path) {
            this.$router.push({path});
        },
        
        // getElementByXpath(path) {
        //         return document.evaluate(path, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
        //     },
        // getElementsByXpath(path) {
        //     const snapshot = document.evaluate(path, document, null, XPathResult.ORDERED_NODE_SNAPSHOT_TYPE, null);
        //     const list = [];
        //     for (let i = 0; i < snapshot.snapshotLength; i++) {
        //         list.push(snapshot.snapshotItem(i));
        //     }
        //     return list;
       // }
    }
}
</script>

<style>
.content {
    display: flex;
    justify-content: space-between;
}
.column1{
    width: 70%;
}
.column2{
    width: 30%;
}
</style>