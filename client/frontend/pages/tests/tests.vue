<template>
    <v-app>
      <v-main>
        <v-container fluid>
          <div class="settings-menu">
            <div class="menu-header">
              <h2>Settings</h2>
            </div>
            <div class="menu-content">
              <v-card>
                <v-card-title>
                  <h3>General</h3>
                </v-card-title>
                <v-card-text>
                  <v-text-field label="Username" placeholder="Enter your username"></v-text-field>
                  <v-text-field label="Email" placeholder="Enter your email address"></v-text-field>
                  <v-select label="Theme" :items="themes" placeholder="Select a theme"></v-select>
                </v-card-text>
              </v-card>
              <v-card>
                <v-card-title>
                  <h3>Privacy</h3>
                </v-card-title>
                <v-card-text>
                  <v-checkbox label="Allow friend requests" v-model="friendRequests"></v-checkbox>
                  <v-checkbox label="Enable notifications" v-model="notifications"></v-checkbox>
                </v-card-text>
              </v-card>
              <v-card>
                <v-card-title>
                  <h3>Security</h3>
                </v-card-title>
                <v-card-text>
                  <v-text-field label="Password" placeholder="Enter your password" type="password"></v-text-field>
                  <v-checkbox label="Two-factor authentication" v-model="twoFactorAuth"></v-checkbox>
                </v-card-text>
              </v-card>
              <v-card>
                <v-card-title>
                  <h3>API</h3>
                </v-card-title>
                <v-card-text>
                  <v-button-toggle v-model="showCode" multiple flat class="code-toggle-button">
                    <template v-slot:selection="{ value }">
                      <v-btn v-if="value" color="primary">Hide Code</v-btn>
                      <v-btn v-else color="primary">Show Code</v-btn>
                    </template>
                  </v-button-toggle>
                  <div v-if="showCode" class="code-section">
                    <pre>{{ apiCode }}</pre>
                    <v-btn color="primary" class="copy-button" @click="copyCode">Copy</v-btn>
                  </div>
                </v-card-text>
              </v-card>
              <div class="save-button">
                <v-btn color="primary" @click="saveSettings">Save Settings</v-btn>
              </div>
            </div>
          </div>
        </v-container>
      </v-main>
    </v-app>
  </template>
  
  <script>
  export default {
    name: 'SettingsMenu',
    data() {
      return {
        themes: ['Dark', 'Light', 'Custom'],
        friendRequests: true,
        notifications: true,
        twoFactorAuth: false,
        showCode: false,
        apiCode: 'API CODE HERE',
      };
    },
    methods: {
      copyCode() {
        const textarea = document.createElement('textarea');
        textarea.value = this.apiCode;
        document.body.appendChild(textarea);
        textarea.select();
        document.execCommand('copy');
        document.body.removeChild(textarea);
        alert('Code copied to clipboard!');
      },
      saveSettings() {
        // Handle saving of settings
      },
    },
  };
  </script>
  
  <style scoped>
  .settings-menu {
    margin: 20px auto;
    max-width: 600px;
  }
  
  .menu-header {
    text-align: center;
    margin-bottom: 20px;
  }
  
  .menu-content {
    margin-bottom: 20px;
  }
  
  h2, h3 {
    margin: 0;
  }
  
  .save-button {
    text-align: center;
    margin-top: 20px;
  }
  
  .code-toggle-button {
    margin-bottom: 10px;
  }
  
  .code-section {
    position: relative;
  }
  
  .copy-button {
    position: absolute;
    top: 0;
    right: 0;
  }
  </style>
  