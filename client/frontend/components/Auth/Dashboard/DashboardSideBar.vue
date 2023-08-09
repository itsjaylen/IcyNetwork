<template>
  <v-card>
    <v-layout>
      <v-navigation-drawer expand-on-hover rail>
        <v-list>
          <v-list-item
            :prepend-avatar="user && user.profile_picture ? user.profile_picture : defaultAvatar"
            :title="user ? user.username : ''"
            :subtitle="user ? user.email : ''"
          ></v-list-item>
        </v-list>

        <v-list density="compact" nav>
          <v-list-item>
            <v-text-field
              v-model="search"
              prepend-icon="mdi-magnify"
              label="Search..."
              single-line
              hide-details
            ></v-text-field>
          </v-list-item>

          <v-list-item
            v-for="setting in filteredSettings"
            :key="setting.id"
            :prepend-icon="setting.icon"
            :title="setting.title"
            @click="setting.action"
            v-if="loggedIn"
          ></v-list-item>

          <v-divider class="border-opacity-100" inset></v-divider>
          <v-divider vertical></v-divider>

          <v-list-item
            prepend-icon="mdi-white-balance-sunny"
            :title="
              lightModeEnabled ? 'Disable Light Mode' : 'Enable Light Mode'
            "
            @click="toggleLightMode"
            v-if="loggedIn"
          ></v-list-item>

          <v-list-item
            prepend-icon="mdi-logout"
            title="Logout"
            @click="goToLogout"
            v-if="loggedIn"
          ></v-list-item>
        </v-list>
      </v-navigation-drawer>

      <v-main style="height: 250px"></v-main>
    </v-layout>
  </v-card>
</template>

<script>
import DashboardScript from "./DashboardScript.ts";

export default {
  ...DashboardScript,
  name: "DashboardSideBar",
  data() {
    return {
      loggedIn: true, // Set this to true if the user is logged in, false otherwise
      search: "", // Variable to store the search query
      lightModeEnabled: false, // Variable to store the light mode state
      settings: [], // Empty array for settings
      user: DashboardScript.setup().user, // User name
      defaultAvatar: "https://i.pravatar.cc/300", // Default avatar image #TODO FIX WITH CDN
    };
  },
  computed: {
    filteredSettings() {
      // Use computed property to filter the settings based on the search query
      const query = this.search.toLowerCase();
      return this.settings.filter((setting) =>
        setting.title.toLowerCase().includes(query)
      );
    },
  },
  methods: {
    goToSettings() {
      // Navigate to "/settings"
      this.$router.push("/settings");
    },
    goToAccount() {
      // Navigate to "/account"
      this.$router.push("/account");
    },
    goToNotifications() {
      // Navigate to "/notifications"
      this.$router.push("/notifications");
    },
    goToPrivacy() {
      // Navigate to "/privacy"
      this.$router.push("/privacy");
    },
    goToLogout() {
      // Perform logout logic here
    },
    toggleLightMode() {
      // Toggle the state of light mode
      this.lightModeEnabled = !this.lightModeEnabled;

      // Save the lightModeEnabled value in local storage
      localStorage.setItem(
        "lightModeEnabled",
        JSON.stringify(this.lightModeEnabled)
      );

      // Add your logic here to enable/disable light mode
      // For example, you can update CSS classes, change themes, or apply different styles based on the value of this.lightModeEnabled.
      if (this.lightModeEnabled) {
        // Light mode is enabled
        // Apply light mode styles
      } else {
        // Light mode is disabled
        // Apply default styles
      }
    },
    goToMessages() {
      // Navigate to "/messages"
      this.$router.push("/messages");
    },
    goToDashboard() {
      // Navigate to "/dashboard"
      this.$router.push("/dashboard");
    },
    goToHome() {
      // Navigate to "/"
      this.$router.push("/");
    },

    addNewItem(id, title, icon, action) {
      // Add a new setting to the settings array
      this.settings.push({
        id,
        title,
        icon,
        action,
      });
    },
  },
  mounted() {
    // Retrieve the lightModeEnabled value from local storage
    const storedLightModeEnabled = localStorage.getItem("lightModeEnabled");

    // Check if a stored value exists and parse it to update the state
    if (storedLightModeEnabled !== null) {
      this.lightModeEnabled = JSON.parse(storedLightModeEnabled);
    }

    // Add new settings dynamically
    this.addNewItem(1, "Home", "mdi-home", this.goToHome);
    this.addNewItem(2, "Dashboard", "mdi-view-dashboard", this.goToDashboard);
    this.addNewItem(3, "Settings", "mdi-cog", this.goToSettings);
    this.addNewItem(4, "Account", "mdi-account", this.goToAccount);
    this.addNewItem(
      5,
      "Notifications",
      "mdi-bell-ring",
      this.goToNotifications
    );
  },
};
</script>

<style>
/* Add your CSS code here */
.centered-item {
  display: flex;
  align-items: center;
}
</style>
