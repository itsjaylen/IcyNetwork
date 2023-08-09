<template>
  <v-app class="app">
    <p>Default Page</p>
    <MainFooter />
  </v-app>
</template>

<script>
import MainFooter from "@/components/Designs/Footer/MainFooter.vue";
export default {
  components: {
    MainFooter,
  },
};
</script>

<style>
.app {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

.v-main {
  flex: 1;
}
</style>
