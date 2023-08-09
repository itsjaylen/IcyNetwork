<template>
  <div class="dashboard-layout">
    <DashboardSideBar />
    <Dashboard />
  </div>
</template>

<script>
import Dashboard from "@/components/Auth/Dashboard/Dashboard.vue";
import DashboardSideBar from "@/components/Auth/Dashboard/DashboardSideBar.vue";

export default {
  components: {
    Dashboard,
    DashboardSideBar,
  },
};
</script>

<style>
.dashboard-layout {
  display: flex;
}

.dashboard-layout .sidebar {
  width: 250px; /* Adjust the width according to your sidebar width */
  padding-right: 20px; /* Adjust the padding as needed */
}

.dashboard-layout .content {
  flex-grow: 1;
}
</style>
