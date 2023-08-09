// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  css: ["vuetify/styles/main.sass", "@mdi/font/css/materialdesignicons.css"],

  build: {
    transpile: ["vuetify"],
  },

  modules: [
    // ...
    "@pinia/nuxt",
    "nuxt-csurf",
    "@nuxtjs/tailwindcss",
  ],
  csurf: {
    // optional
    https: false, // default true if in production
    cookieKey: "", // "__Host-csrf" if https is true otherwise just "csrf"
    cookie: {
      // CookieSerializeOptions from unjs/cookie-es
      path: "/",
      httpOnly: false,
      sameSite: "strict",
    },
    methodsToProtect: ["POST", "PUT", "PATCH"], // the request methods we want CSRF protection for
    excludedUrls: ["/nocsrf1", ["/nocsrf2/.*", "i"]], // any URLs we want to exclude from CSRF protection
    encryptSecret: "aLMOEMadRPearY6X2UXliRDy5ILCVXx9", // random bytes by default
    encryptAlgorithm: "aes-256-cbc",
  },

  plugins: [],
  runtimeConfig: {
    // Private keys are only available on the server
    //apiSecret: '123',
    // Public keys that are exposed to the client
    public: {
      apiBase:
        //TODO change to load in from env
        process.env.NUXT_PUBLIC_API_BASE || "http://192.168.50.232:8002/",
    },
  },
});
