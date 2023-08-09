<template>
  <v-card>
    <v-layout>
      <v-navigation-drawer
        class="custom-drawer"
        dark
        v-model="drawer"
        :clipped="clipped"
        :mini-variant.sync="miniVariant"
        permanent
        transition="slide-x-transition"
      >
        <div class="menu-icon" @click="toggleDrawer">
          <v-icon>{{ miniVariant ? "mdi-menu" : "mdi-close" }}</v-icon>
        </div>
        <v-list color="transparent">
          <v-list-item-group>
            <!-- First group of navigation items -->
            <v-list-item
              :to="{ path: '/dashboard' }"
              exact
              prepend-icon="mdi-view-dashboard"
              title="Dashboard"
              :class="{ 'active-item': $route.path === '/dashboard' }"
            ></v-list-item>
            <v-list-item
              :to="{ path: '/account' }"
              exact
              prepend-icon="mdi-account-box"
              title="Account"
              :class="{ 'active-item': $route.path === '/account' }"
            ></v-list-item>
            <v-list-item
              :to="{ path: '/settings' }"
              exact
              prepend-icon="mdi-cog"
              title="Settings"
              :class="{ 'active-item': $route.path === '/settings' }"
            ></v-list-item>
          </v-list-item-group>

          <v-list-item-group v-if="showAdminLink">
            <!-- Admin group of navigation items -->
            <v-list-item
              :to="{ path: '/admin' }"
              exact
              prepend-icon="mdi-gavel"
              title="Admin"
              :class="{ 'active-item': $route.path === '/admin' }"
            ></v-list-item>
          </v-list-item-group>
        </v-list>

        <template v-slot:append>
          <div class="pa-2">
            <v-btn block>Logout</v-btn>
          </div>
        </template>
      </v-navigation-drawer>
      <v-main style="height: 400px">
        <v-btn
          class="custom-button"
          fab
          fixed
          right
          bottom
          @click="toggleDrawer"
          color="primary"
        >
          <v-icon>{{
            miniVariant ? "mdi-chevron-right" : "mdi-chevron-left"
          }}</v-icon>
        </v-btn>
      </v-main>
    </v-layout>
  </v-card>
</template>

<script>
export default {
  data() {
    return {
      drawer: true,
      clipped: false,
      miniVariant: false,
      loading: true,
      error: null,
      user: null,
    };
  },
  computed: {
    showAdminLink() {
      return this.user && this.user.is_admin && this.$route.path !== "/admin";
    },
  },
  methods: {
    toggleDrawer() {
      this.miniVariant = !this.miniVariant;
      this.drawer = !this.miniVariant;
    },
    async fetchUserData() {
      try {
        const config = useRuntimeConfig();

        // Check if the cached response exists and if it is still valid
        const cachedResponse = localStorage.getItem("userData");
        if (cachedResponse) {
          const { timestamp, data } = JSON.parse(cachedResponse);
          const currentTime = new Date().getTime();
          const expirationTime = timestamp + 30 * 60 * 1000; // 30 minutes in milliseconds

          if (currentTime < expirationTime) {
            this.user = data.user;
            this.loading = false;
            return;
          }
        }

        const response = await fetch(`${config.public.apiBase}/api/protected`, {
          credentials: "include", // Include credentials (session cookie) in the request
        });

        const responseData = await response.json();

        console.log(responseData);

        if (response.ok) {
          this.loading = false;
          this.user = responseData.user;
          // Cache the API response with timestamp
          const timestampedData = {
            timestamp: new Date().getTime(),
            data: responseData,
          };
          localStorage.setItem("userData", JSON.stringify(timestampedData));
        } else {
          throw new Error(`Failed to fetch user data: ${responseData.error}`);
        }
      } catch (error) {
        this.loading = false;
        this.error = error.message;
      }
    },
  },
  async mounted() {
    this.fetchUserData();
  },
};
</script>

<style scoped>
@import "./MainSideBarStyle.sass";
</style>
