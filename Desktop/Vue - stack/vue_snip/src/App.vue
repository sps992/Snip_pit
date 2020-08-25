<template>
  <div id="app">
    <div id="nav">
      <router-link to="/">Home</router-link> |
      <router-link to="/create">Create</router-link>
    </div>
    <router-view />
  </div>
</template>
<script>
export default {
  
}
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
</style>
