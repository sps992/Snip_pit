<template>
  <div id="app">
    <div id="nav">
      <router-link to="/">Home</router-link> |
      <router-link to="/create">Create</router-link>
    </div>
    <router-view />
    <div id="footer">
      <p>Sam Sedgeman</p>
    </div>
  </div>
  
</template>
<script>
import axios from 'axios'
export default {
    name: 'List',
    data() {
        return {
            snippets: []
        };
    },
    async created() {
        try {
        const res = await axios.get(`http://127.0.0.1:8000/snippets/`);

        this.snippets = res.data;
        } catch (e) {
        console.error(e);
    }
    
    
    }
};
</script>
<style lang="scss">
@import "assets/css/tailwind.css";

h1{padding-top: 2.5rem}

#nav {
  padding: 30px;

  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #B794F4;
    }
  }
}
#footer {
  padding: 30px;
  background:#0d1014;

  p {
    font-weight: bold;
    color: #fff;
  }
  
}
</style>
