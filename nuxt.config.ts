export default defineNuxtConfig({
  compatibilityDate: '2025-07-15',
  devtools: { enabled: true },

  modules: [
    '@nuxtjs/tailwindcss',
    '@nuxtjs/i18n',
  ],

  i18n: {
    baseUrl: 'https://pan-web-mocha.vercel.app',
    strategy: 'prefix_except_default',
    defaultLocale: 'en',
    locales: [
      { code: 'en', language: 'en-US', file: 'en.json', name: 'English' },
      // { code: 'ru', language: 'ru-RU', file: 'ru.json', name: 'Русский' },
      // { code: 'ky', language: 'ky-KG', file: 'ky.json', name: 'Кыргызча' },
      { code: 'zh', language: 'zh-CN', file: 'zh.json', name: '中文' },
    ],
    langDir: 'locales',
    detectBrowserLanguage: false,
  },

  nitro: {
    static: true,
  },

  app: {
    head: {
      title: 'TanDem - Premium Cookware & Heating Radiators',
      meta: [
        { charset: 'utf-8' },
        { name: 'viewport', content: 'width=device-width, initial-scale=1' },
        { name: 'description', content: 'TanDem is a precision metalworking manufacturer in Bishkek, Kyrgyzstan — part of the international TMAI group — producing cookware and central-heating radiators and boilers for distributors, retailers, and consumers.' },
      ],
      link: [
        { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' },
        { rel: 'preconnect', href: 'https://fonts.googleapis.com' },
        { rel: 'preconnect', href: 'https://fonts.gstatic.com', crossorigin: '' },
        { rel: 'stylesheet', href: 'https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Playfair+Display:wght@400;500;600;700&display=swap' },
      ],
    },
  },
})
