<template>
  <v-container>
    <v-card>
      <v-card-title class="text-center">Layout</v-card-title>
      <v-card-text>
        <!-- ...other layout content... -->
      </v-card-text>
    </v-card>
  </v-container>
  
  <LoginForm />
</template>

<script>
import LoginForm from "@/components/Auth/LoginForm/LoginForm.vue";
import DarkModeSwitch from "@/components/themes/darkMode.vue";

export default {
  components: {
    LoginForm,
    DarkModeSwitch,
  },
};
</script>
