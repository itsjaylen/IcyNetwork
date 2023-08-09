<template>
    <v-switch
      v-model="darkMode"
      @change="toggleDarkMode"
      hide-details
      color="primary"
      class="dark-mode-switch"
    >
      <template #label>
        <v-icon dark>{{ darkMode ? 'mdi-weather-night' : 'mdi-white-balance-sunny' }}</v-icon>
      </template>
    </v-switch>
  </template>
  
  <style scoped>
  .dark-mode-switch {
    position: fixed;
    top: 20px;
    left: 20px;
  }
  </style>
  
  <script>
  export default {
    data() {
      return {
        darkMode: false,
      };
    },
    methods: {
        toggleDarkMode() {
  this.$vuetify.theme.dark = this.darkMode;

  if (this.darkMode) {
    this.$vuetify.theme.themes.dark = customDarkTheme();
  } else {
    this.$vuetify.theme.themes.light = customLightTheme();
  }
},

    },
  };
  </script>
  