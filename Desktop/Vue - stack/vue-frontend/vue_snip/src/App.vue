<template>
  <div id="app" class="bg-teal-700 w-full h-screen text-gray-100">
    <div class="container text-center mx-auto">
   <h1 class="text-5xl">Snip Pit</h1>
   <p>A pit to store your snips...</p>
   <input type="text" v-model="search" placeholder="Search the pit..." />
   <ul v-for="snippet in snippets" v-bind:key="snippet.id">
    <li>{{snippet.title}}</li>
    </ul>
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

        }
    },
    mounted () {
        this.getSnippets()
    },
    methods: {
        getSnippets() {
            axios({
                method: 'get',
                url: 'http://127.0.0.1:8000/snippets',
                auth: {
                    username: 'admin',
                    password: 'S3dg3m4n'
                }
            }).then(response => this.snippets = response.data)
        }
        }
    }

</script>

<style lang="scss">
@import "assets/css/tailwind.css"

</style>
