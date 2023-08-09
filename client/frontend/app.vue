<template>
  <NuxtPage />
  <MainPage />
</template>

<script>
import MainPage from "~/layouts/DefaultPage.vue";

export default {
  components: {
    MainPage,
  },
  async created() {
    const config = useRuntimeConfig();
    // Get CSRF token
  },
};
</script>

