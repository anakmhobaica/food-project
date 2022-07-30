<template>
      <div class="barra"  v-if="($route.path!='/login')">
      <nav>
        <div class="options">
          <header>
              <img class="logo" :src="logo" alt="Logo">
          </header>
            <ul id="u01">
                <li><router-link to='/'>HOME</router-link></li>  
                <li class="dropdown1"><router-link to='/recetas'>RECETAS</router-link></li>
                <li class="dropdown1"><router-link to='/curiosidades'>CURIOSIDADES</router-link></li>
                <!-- <li class="dropdown1">{{ $route.path }}</li> -->
                <!-- <li class="dropdown1"><router-link to='/login'>Login</router-link></li> -->
                <!--<li><router-link to='/admin'>Admin</router-link></li>-->
            </ul>
        </div>
        <div class="field" id="searchfrom">
          <input type="text" name="search" placeholder="¿Qué estás buscando?"  v-model="busqueda">
          <button type="button" id="buscar">Buscar</button>
        </div>
      </nav>
  </div>
  <div>
    <!-- Two Way Binding:
    {{busqueda}} -->
  </div>
  <router-view/>
</template>

<script>
export default {
  name: 'App',
  data() {
  return {
    logo: imagen,
    busqueda: '',
  }
},

        // computed: {
        // currentRouteName() {
        //     return this.$route.name;
        // }
        // }
}
import './estilos/mystyle.css';
import imagen from './imagenes/fitANDfat.png'
</script>
