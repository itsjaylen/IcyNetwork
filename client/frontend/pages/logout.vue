<template>
  <v-btn @click="logout" color="primary" dark> Logout </v-btn>
</template>

<script>
export default {
  methods: {
    async logout() {
      try {
        const config = useRuntimeConfig();
        const csrf_token = localStorage.getItem("csrf_token"); // Retrieve the CSRF token from local storage

        const response = await $fetch(`${config.public.apiBase}/api/logout`, {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            "X-CSRF-TOKEN": csrf_token, // Add the CSRF token to the headers
          },
          credentials: "include",
          body: JSON.stringify({}),
        });
        console.log(response);

        if (response.message === "Logout successful") {
          localStorage.removeItem("userData");
          await navigateTo("/ProtectedPage");
        } else {
          throw new Error("Logout failed. Please try again.");
        }
      } catch (error) {
        console.error(error);
        this.errorMessage = "Logout failed. Please try again.";
      }
    },
  },
};
</script>
