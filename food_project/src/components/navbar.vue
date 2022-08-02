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
                <li class="dropdown1" v-if="usuario.tipo_usuario === 'admin'"><router-link to='/admin'>ADMIN</router-link></li>
                <!-- <li class="dropdown1">{{ $route.path }}</li> -->
                <!-- <li class="dropdown1"><router-link to='/login'>Login</router-link></li> -->
                <!--<li><router-link to='/admin'>Admin</router-link></li>-->
            </ul>
        </div>
        <div class="field" id="searchfrom">
          <!-- <input type="text" name="search" placeholder="¿Qué estás buscando?"  v-model="busqueda"> -->
          <button type="button" id="buscar" @click="salir" >CERRAR SESIÓN</button>
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
    usuario: [],
    }
  },
  mounted() {
    this.getUsuario();
  },
  methods : {
    salir(){
      localStorage.removeItem('user');
      window.location.href = "/login";
    },
    getUsuario(){
      const usuario = localStorage.getItem('user');
      this.usuario = JSON.parse(usuario);
    },
  }
}
import './estilos/mystyle.css';
import imagen from './imagenes/fitANDfat.png'
</script>
