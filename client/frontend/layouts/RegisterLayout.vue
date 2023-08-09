<template>
    <v-container>
      <v-card>
        <v-card-title class="text-center">Layout</v-card-title>
        <v-card-text>
          <!-- ...other layout content... -->
        </v-card-text>
      </v-card>
    </v-container>
    
    <RegisterForm />
  </template>
  
  <script>
  import RegisterForm from "@/components/Auth/RegisterForm/RegisterForm.vue";
  
  export default {
    components: {
        RegisterForm,
    },
  };
  </script>
  