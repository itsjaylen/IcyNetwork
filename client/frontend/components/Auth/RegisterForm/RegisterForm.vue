<template>
    <div class="d-flex align-center justify-center" style="height: 100vh">
      <v-sheet width="400" class="mx-auto rounded-lg">
        <v-form fast-fail @submit.prevent="register">
          <!-- Username field -->
          <v-text-field
            v-model="username"
            label="Username"
            prepend-icon="mdi-account"
          ></v-text-field>
  
          <!-- Email field -->
          <v-text-field
            v-model="email"
            label="Email"
            prepend-icon="mdi-email"
          ></v-text-field>
  
          <!-- New password field -->
          <v-text-field
            v-model="newPassword"
            label="New Password"
            prepend-icon="mdi-lock"
            type="password"
          ></v-text-field>
  
          <!-- Confirm password field -->
          <v-text-field
            v-model="confirmPassword"
            label="Confirm Password"
            prepend-icon="mdi-lock-check"
            type="password"
          ></v-text-field>
  
          <!-- Error message -->
          <v-alert type="error" v-if="errorMessage" dismissible>
            {{ errorMessage }}
          </v-alert>
  
          <!-- Register button -->
          <div class="container" style="width: 200px">
            <v-btn type="submit" color="blue" block class="mt-4">
              <!-- Increased margin top (mt-4) -->
              <v-icon left>mdi-account-plus</v-icon>
              Register
            </v-btn>
          </div>
  
          <!-- Forgot password text with increased margin top (mt-3) -->
          <div class="text-left mt-6">
            <p class="link-text mt-3">
              Forgot your
              <router-link to="/forgot-password" class="text-decoration-none"
                >password?</router-link
              >
            </p>
          </div>
  
          <div class="text-center mt-6">
            <v-divider></v-divider>
            <p class="mt-4">
              Already have an account?
              <router-link to="/login" class="text-decoration-none"
                >Sign in</router-link
              >
            </p>
          </div>
        </v-form>
      </v-sheet>
    </div>
  </template>
  
  <script>
  import RegisterFormScript from "./RegisterFormScript.ts";
  
  export default {
    ...RegisterFormScript,
  };
  </script>
  
  <style scoped>
  @import "./RegisterFormStyle.sass";
  </style>
  