<template>
    <div>
      <v-text-field
        v-model="search"
        prepend-icon="mdi-magnify"
        label="Search"
        hide-details
      ></v-text-field>
  
      <div v-if="isUserProfilePresent" class="popup">
        Element "user profile" is present on this page!
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        search: '', // Variable to store the search query
        isUserProfilePresent: false, // Flag to track if "user profile" element is present
      };
    },
    watch: {
      search(newQuery) {
        // Check if "user profile" element is present based on the search query
        this.isUserProfilePresent = newQuery.toLowerCase().includes('user profile');
      },
    },
  };
  </script>
  
  <style>
  .popup {
    position: fixed;
    top: 10px;
    left: 50%;
    transform: translateX(-50%);
    padding: 10px;
    background-color: #fff;
    border: 1px solid #ccc;
    border-radius: 4px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
  }
  </style>
  