<template>
<div class=" bg-gray-800 w-full h-screen text-white">
    <div class="container  text-left mx-auto">
   <h1 class="text-5xl text-center">Edit Snippet</h1>
   <p class="text-center">Things are gonna change around here...</p>
   <form class="w-full max-w-md mx-auto m-10">
  <div class="md:flex md:items-center mb-6">
    <div class="md:w-2/4">
      <label class="block text-gray-500 font-bold   mb-1 md:mb-0 pr-4" for="created-by">
        Created By
      </label>
    </div>
    <div class="md:w-2/4">
     <select class="block appearance-none w-full bg-gray-200 border border-gray-200 text-gray-700 py-3 px-4 pr-8 rounded leading-tight focus:outline-none focus:bg-white focus:border-gray-500" id="created-by">
         <option>Select a team member</option>
         <option>Ian Malcolm</option>
         <option>John Hammond</option>
         <option>Alan Grant</option>
         <option>Dennis Nedry</option>
         <option>Dr.Henry Wu</option>
         <option>Henry Arnold</option>
    </select>

    </div>
  </div>
  <div class="md:flex md:items-center mb-6">
    <div class="md:w-2/4">
      <label class="block text-gray-500 font-bold   mb-1 md:mb-0 pr-4" for="title">
        Title
      </label>
    </div>
    <div class="md:w-2/4">
      <input class="bg-gray-200 appearance-none border-2 border-gray-200 rounded w-full py-2 px-4 text-gray-700 leading-tight focus:outline-none focus:bg-white focus:border-purple-500" id="title" type="text" >
    </div>
    </div>
   <div class="md:flex md:items-center mb-6">
    <div class="md:w-2/4">
      <label class="block text-gray-500 font-bold   mb-1 md:mb-0 pr-4" for="description">
        Description
      </label>
    </div>
    <div class="md:w-2/4">
      <textarea class="bg-gray-200 appearance-none border-2 border-gray-200 rounded w-full py-2 px-4 text-gray-700 leading-tight focus:outline-none focus:bg-white focus:border-purple-500" id="description" type="text" >
      </textarea>
    </div>
    </div>
    <div class="md:flex md:items-center mb-6">
    <div class="md:w-2/4">
      <label class="block text-gray-500 font-bold   mb-1 md:mb-0 pr-4" for="description">
        Code Snippet
      </label>
    </div>
    <div class="w-full mx-auto">
      <textarea class="bg-gray-200 appearance-none border-2 border-gray-200 rounded w-full py-2 px-4 text-gray-700 leading-tight focus:outline-none focus:bg-white focus:border-purple-500" id="description" type="text" >
      </textarea>
    </div>
    </div>
  <div class="text-left">
      <button class="shadow bg-purple-500 hover:bg-purple-400 focus:shadow-outline focus:outline-none text-white font-bold py-2 px-4 rounded" type="button">
        Submit
      </button>
  </div>
</form>
    </div>
    </div>
    
</template>

<script>
export default {
    
}
</script>
<style>

</style>