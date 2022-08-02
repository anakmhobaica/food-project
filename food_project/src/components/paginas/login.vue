<template >
<body>
    <div class="bigContainer">
        <div class="main">  	
            <input type="checkbox" id="chk" aria-hidden="true">
                <div class="signup">
                    <form v-on:submit.prevent="registrarse">
                        <label for="chk" aria-hidden="true">Registro</label>
                        <input type="text" name="nombre_usuario" v-model="username" placeholder="Nombre de usuario" required="">
                        <input type="email" name="email" v-model="email" placeholder="Correo electrónico" required="">
                        <input type="password" name="pswd" v-model="pswd" placeholder="Contraseña" required="">
                        <button type="submit">Registrarse</button>
                    </form>
					<p v-if="respuesta.codigo == 400" style="color:red; text-align: center; padding: 5px;">{{ respuesta.mensaje }}</p>
					<p v-else-if="respuesta.codigo == 401" style="color:red; text-align: center; padding: 0 5px 0;">{{ respuesta.mensaje }}</p>
                </div>
                <div class="login">
                    <form v-on:submit.prevent="ingresar">
                        <label for="chk" aria-hidden="true">Inicio de Sesión</label>
                        <input type="text" name="nombre_usuario" v-model="username" placeholder="Nombre de usuario" required="">
                        <input type="password" name="pswd" v-model="pswd" placeholder="Contraseña" required="">
                        <button type="submit">Acceder</button>
                    </form>
					<p v-if="respuesta.codigo == 403" style="color:red; text-align: center;">{{ respuesta.mensaje }}</p>
                </div>
        </div>
    </div>
</body>
</template>

<script>
	import axios from "axios";
	export default {
		data() {
			return {
				respuesta: [],
			}
		},
		methods: {
			ingresar(){
				axios.post('//localhost:5000/login', {
					nombre: this.username, contrasena: this.pswd
				}).then(response => {
					this.respuesta = response.data;
					console.log(response.data.codigo);
					if (response.data.codigo === 200){
							localStorage.setItem('user', JSON.stringify(response.data.user));
							window.location.href = "/";
						}
				})
			},
			registrarse(){
				axios.post('//localhost:5000/registro', {
					nombre: this.username, contrasena: this.pswd, correo: this.email, tipo_usuario: "user"
				}).then(response => {
					this.respuesta = response.data;
					console.log(this.respuesta);
					if (response.data.codigo === 201){
							localStorage.setItem('user', JSON.stringify(response.data.user));
							window.location.href = "/";
						}
				})
			},
		}
	}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Jost&display=swap');

body{
	margin: 0;
	padding: 0;
	display: flex;
	justify-content: center;
	align-items: center;
	min-height: 100vh;
	font-family: 'Jost', sans-serif;
	background: linear-gradient(to bottom, white, whitesmoke, grey);
}
.main{
	width: 350px;
	height: 500px;
	background: red;
	overflow: hidden;
	background: url("https://doc-08-2c-docs.googleusercontent.com/docs/securesc/68c90smiglihng9534mvqmq1946dmis5/fo0picsp1nhiucmc0l25s29respgpr4j/1631524275000/03522360960922298374/03522360960922298374/1Sx0jhdpEpnNIydS4rnN4kHSJtU1EyWka?e=view&authuser=0&nonce=gcrocepgbb17m&user=03522360960922298374&hash=tfhgbs86ka6divo3llbvp93mg4csvb38") no-repeat center/ cover;
	border-radius: 10px;
	box-shadow: 5px 20px 50px #000;
}
#chk{
	display: none;
}
.signup{
	position: relative;
	width:100%;
	height: 100%;
}

.signup label{
	color:#e01304
}

label{
	color: #fff;
	font-size: 2.3em;
	justify-content: center;
	display: flex;
	margin: 60px;
	font-weight: bold;
	cursor: pointer;
	transition: .5s ease-in-out;
}
input{
	width: 60%;
	height: 20px;
	background: #e0dede;
	justify-content: center;
	display: flex;
	margin: 20px auto;
	padding: 10px;
	border: none;
	outline: none;
	border-radius: 5px;
}
button{
	width: 60%;
	height: 40px;
	margin: 10px auto;
	justify-content: center;
	display: block;
	color: #fff;
	background: #e01304;
	font-size: 1em;
	font-weight: bold;
	margin-top: 20px;
	outline: none;
	border: none;
	border-radius: 5px;
	transition: .2s ease-in;
	cursor: pointer;
}
button:hover{
	background: #e01304;
}
.login{
	height: 460px;
	background: #eee;
	border-radius: 60% / 10%;
	transform: translateY(-180px);
	transition: .8s ease-in-out;
}
.login label{
	color: #e01304;
	transform: scale(.6);
    font-size: 30px;
}

#chk:checked ~ .login{
	transform: translateY(-500px);
}
#chk:checked ~ .login label{
	transform: scale(1);	
}
#chk:checked ~ .signup label{
	transform: scale(.6);
}
/* .bigContainer{
    height: 100%;
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
} */

</style>
