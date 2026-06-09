export default defineNuxtConfig({
  compatibilityDate: '2025-07-15',
  devtools: { enabled: true },

  modules: [
    '@nuxtjs/tailwindcss',
  ],

  app: {
    head: {
      title: 'PanCraft - Premium Frying Pans & Cookware',
      meta: [
        { charset: 'utf-8' },
        { name: 'viewport', content: 'width=device-width, initial-scale=1' },
        { name: 'description', content: 'PanCraft is a precision metalworking manufacturer producing premium cookware and heating radiators for distributors, retailers, and consumers worldwide.' },
      ],
      link: [
        { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' },
      ],
    },
  },
})
