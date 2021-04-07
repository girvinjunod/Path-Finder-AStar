<template>
  <div id="app">
    <Openstreetmap/>
  </div>
</template>

<script>
import Openstreetmap from './components/Openstreetmap.vue'

export default {
  name: 'App',
  components: {
    Openstreetmap
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
