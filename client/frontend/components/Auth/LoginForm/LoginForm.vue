<template>
  <div class="d-flex align-center justify-center" style="height: 100vh">
    <v-sheet width="400" class="mx-auto rounded-lg">
      <v-form fast-fail @submit.prevent="login">
        <!-- email field -->
        <v-text-field
          v-model="email"
          label="Email"
          prepend-icon="mdi-account"
        ></v-text-field>

        <!-- Empty row for spacing -->
        <v-row justify="space-between" class="mb-4">
          <v-col cols="auto"></v-col>
        </v-row>

        <!-- Password field -->
        <v-text-field
          v-model="password"
          label="Password"
          prepend-icon="mdi-lock"
          type="password"
        ></v-text-field>

        <!-- Forgot password text with increased margin top (mt-3) -->
        <div class="text-left mt-6">
          <p class="link-text mt-3">
            Forgot your
            <router-link to="#" class="text-decoration-none"
              >password?</router-link
            >
          </p>
        </div>

        <div class="container" style="text-align: center">
          <v-btn
            type="submit"
            color="blue"
            class="mt-4"
            style="display: inline-block"
          >
            <!-- Increased margin top (mt-4) -->
            <v-icon left>mdi-login</v-icon>
            Sign in
          </v-btn>
        </div>

        <!-- Error message -->
        <v-alert type="error" v-if="errorMessage" dismissible>
          {{ errorMessage }}
        </v-alert>

        <div class="text-center mt-6">
          <v-divider></v-divider>
          <p class="mt-4">
            Don't have an account?
            <router-link to="/register" class="text-decoration-none"
              >Create one</router-link
            >
          </p>
        </div>
      </v-form>
    </v-sheet>
  </div>
</template>

<script>
import LoginFormScript from "./LoginFormScript.ts";

export default {
  ...LoginFormScript,
};
</script>

<style scoped>
@import "./LoginFormStyle.sass";
</style>
