<template>
    
</template>

<script>
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
export default{
    compoments:{
        FontAwesomeIcon
    },
    props: {
        titulo: String,
        categoria: String,
    },
    methods: {
        async deleteReceta() {
            const eliminar = await axios.delete('//localhost:5000/eliminar_receta');
        }
    },
}
</script>