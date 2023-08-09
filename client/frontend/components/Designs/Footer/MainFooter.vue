<template>
  <v-footer class="footer">
    <v-row justify="center" no-gutters>
      <v-col v-for="column in footerColumns" :key="column.title" :cols="12" md="4" class="footer-column">
        <h3 class="footer-column-title">{{ column.title }}</h3>
        <div v-for="link in column.links" :key="link.text" class="footer-link">
          <v-btn color="transparent" class="mx-2" rounded="xl">
            <a :href="link.url" class="link-text">
              <v-icon left :size="iconSize">{{ link.icon }}</v-icon>
              {{ link.text }}
            </a>
          </v-btn>
        </div>
      </v-col>
      <v-col class="text-center mt-4" cols="12">
        {{ new Date().getFullYear() }} — <strong>Icy Studios</strong>
      </v-col>
    </v-row>
  </v-footer>
</template>

<script>
export default {
  data: () => ({
    footerColumns: [
      {
        title: 'Explore',
        links: [
          { text: 'Home', url: '/', icon: 'mdi-home' },
          { text: 'About', url: '/about', icon: 'mdi-information' },
          { text: 'Services', url: '/services', icon: 'mdi-cogs' },
          { text: 'Help', url: '/help', icon: 'mdi-help-circle' },
        ],
      },
      {
        title: 'Company',
        links: [
          { text: 'Contact Us', url: '/contact', icon: 'mdi-email' },
          { text: 'Methods', url: '/methods', icon: 'mdi-pencil' },
        ],
      },
      {
        title: 'Legal',
        links: [
          { text: 'Privacy Policy', url: '/privacy-policy', icon: 'mdi-lock' },
          { text: 'Terms of Service', url: '/terms-of-service', icon: 'mdi-file-document' },
          { text: 'Sitemap', url: '/sitemap', icon: 'mdi-map' },
        ],
      },
    ],
    iconSize: '20px', // Adjust the size as needed
  }),
};
</script>

<style>
.footer {
  position: relative;
  width: 100%;
  background-color: #f7f7f7;
  padding: 20px 0;
}

.footer-column {
  text-align: center;
  padding: 0 10px;
  margin-bottom: 20px;
}

.footer-column-title {
  font-size: 1.2rem;
  margin-bottom: 10px;
}

.footer-link {
  margin: 5px 0;
}

.link-text {
  text-decoration: none;
  color: inherit;
  display: inline-flex;
  align-items: center;
}

.link-text:hover {
  text-decoration: underline;
}

.v-btn {
  border: none;
  max-width: 250px; /* Limit button width */
}
</style>
