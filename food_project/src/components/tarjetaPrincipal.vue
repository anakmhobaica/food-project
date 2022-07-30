<template>
<div class="receta-home" :id="link">
    <div class="info-home">
        <h1>{{titulo}}</h1>
        <p class="parrafo-home">
            {{parrafo}}
        </p>
    </div>
    <div class="imagen-home" :style="{ backgroundImage: `url(${imagen})`, backgroundSize: 'cover' }"></div> 
    <br> 
    <button class="button1" @click="navigate()">Leer más</button>
    <br><br><br>
    <hr>
    <br>
</div>
</template>

<script>
    export default{
        props : {
            imagen:String,
            titulo:String,
            parrafo:String,
            link:String,
        }, 
        mounted(){
            const xpath = `//div[@id='${this.link}']/div/h1`;
            //console.log(xpath);
            const title = this.getElementByXpath(xpath);
            //title && console.log(title);
            title && title.addEventListener('click', () => {
                this.navigate();
            });
            
        },
        methods : {
            navigate() {
                this.$router.push({ path: `/receta/${this.link}`});
            },
            getElementByXpath(path) {
                return document.evaluate(path, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
            },
            getElementsByXpath(path) {
                const snapshot = document.evaluate(path, document, null, XPathResult.ORDERED_NODE_SNAPSHOT_TYPE, null);
                const list = [];
                for (let i = 0; i < snapshot.snapshotLength; i++) {
                    list.push(snapshot.snapshotItem(i));
                }
                return list;
            }
        }
    }
</script>

<style scoped>
.imagen-home{
    height: 400px;
}

title {
    font-family: Verdana, Geneva, Tahoma, sans-serif;
    font-size: 20px;
}

h1 {
    cursor: pointer;
}

</style>