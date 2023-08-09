import { createVuetify, ThemeDefinition } from 'vuetify';
import * as components from 'vuetify/components';
import * as directives from 'vuetify/directives';

//TODO themes https://vuetifyjs.com/en/features/theme/ Light & Dark
export default defineNuxtPlugin((nuxt) => {
  const vuetify = createVuetify({
    ssr: true,
    components,
    directives,
    
  });

  nuxt.vueApp.use(vuetify);
});
