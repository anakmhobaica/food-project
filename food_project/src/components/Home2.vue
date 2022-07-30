<template>
  <div>
    <p>{{ msg }}</p>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Home',
  data() {
    return {
      msg: 'hjgjhyu',
    };
  },
  methods: {
    getMessage() {
      console.log('holi')
      const path = 'http://localhost:5000/mensaje';
      axios.get(path)
        .then((res) => {
          this.msg = res.data;
          console.log(res)
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          console.log(res)
        });
    },
  },
  created() {
    this.getMessage();
  },
};
</script>
