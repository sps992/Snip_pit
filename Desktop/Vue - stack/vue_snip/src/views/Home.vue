<template>
  <div class="home bg-gray-800 w-full h-screen text-white">
    <div class="container text-center mx-auto">
   <h1 class="text-5xl">Snip Pit</h1>
   <p>A pit to store your snips...</p>
   <input class="mx-auto m-10 block appearance-none bg-gray-200 border border-gray-200 text-gray-700 py-3 px-4 pr-8 rounded leading-tight focus:outline-none focus:bg-white focus:border-gray-500" type="text" placeholder="Search the pit..." />
   <ul class="mx-auto">
    <li  class="p-4 bg-purple-400 rounded m-4 shadow hover:bg-purple-500 focus:shadow-outline focus:outline-none" v-for="snippet of snippets" :key="snippet.id"><router-link to="/Edit"> {{ snippet.title }} | {{ snippet.created_by }}</router-link></li>
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