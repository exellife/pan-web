<template>
  <header class="bg-white sticky top-0 z-50 border-b border-steel-200">
    <nav class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex justify-between items-center h-16">
        <!-- Logo -->
        <NuxtLinkLocale to="/" class="flex items-center space-x-2">
          <span class="text-2xl font-display font-bold text-steel-900">Tan<span class="text-accent-600">Dem</span></span>
        </NuxtLinkLocale>

        <!-- Right-hand controls -->
        <div class="flex items-center gap-4 sm:gap-6">
          <!-- Desktop Navigation -->
          <div class="hidden md:flex items-center space-x-8">
            <NuxtLinkLocale
              v-for="link in navLinks"
              :key="link.to"
              :to="link.to"
              class="text-steel-600 hover:text-accent-600 transition-colors font-medium text-sm uppercase tracking-wide"
              active-class="text-accent-600"
            >
              {{ $t(`nav.${link.key}`) }}
            </NuxtLinkLocale>
            <NuxtLinkLocale
              to="/contact"
              class="bg-accent-600 text-white px-5 py-2 rounded text-sm font-semibold hover:bg-accent-700 transition-colors uppercase tracking-wide"
            >
              {{ $t('nav.getQuote') }}
            </NuxtLinkLocale>
          </div>

          <!-- Language dropdown (all sizes) -->
          <div class="relative">
            <button
              type="button"
              class="flex items-center gap-1 text-steel-600 hover:text-accent-600 transition-colors"
              :aria-label="$t('language')"
              aria-haspopup="true"
              :aria-expanded="langOpen"
              @click="langOpen = !langOpen"
            >
              <svg class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
                <circle cx="12" cy="12" r="9" />
                <path stroke-linecap="round" d="M3 12h18M12 3a14 14 0 010 18M12 3a14 14 0 000 18" />
              </svg>
              <span class="text-xs font-semibold uppercase tracking-wide">{{ locale }}</span>
              <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" d="M6 9l6 6 6-6" />
              </svg>
            </button>

            <!-- click-away backdrop -->
            <div v-if="langOpen" class="fixed inset-0 z-40" @click="langOpen = false" />

            <div
              v-if="langOpen"
              class="absolute right-0 mt-2 w-44 bg-white border border-steel-200 rounded-lg shadow-lg py-1 z-50"
            >
              <NuxtLink
                v-for="l in locales"
                :key="l.code"
                :to="switchLocalePath(l.code)"
                class="flex items-center justify-between px-4 py-2 text-sm transition-colors"
                :class="l.code === locale ? 'text-accent-700 font-semibold bg-accent-50' : 'text-steel-600 hover:bg-steel-50 hover:text-accent-600'"
                @click="langOpen = false"
              >
                <span>{{ l.name }}</span>
                <span class="text-[10px] text-steel-400 uppercase">{{ l.code }}</span>
              </NuxtLink>
            </div>
          </div>

          <!-- Mobile menu button -->
          <button
            class="md:hidden p-2 -mr-2 rounded-md text-steel-600 hover:text-accent-600"
            @click="mobileMenuOpen = !mobileMenuOpen"
            aria-label="Toggle menu"
          >
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path
                v-if="!mobileMenuOpen"
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M4 6h16M4 12h16M4 18h16"
              />
              <path
                v-else
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M6 18L18 6M6 6l12 12"
              />
            </svg>
          </button>
        </div>
      </div>

      <!-- Mobile Navigation -->
      <div v-if="mobileMenuOpen" class="md:hidden pb-4 border-t border-steel-200 pt-4">
        <NuxtLinkLocale
          v-for="link in navLinks"
          :key="link.to"
          :to="link.to"
          class="block py-2 text-steel-600 hover:text-accent-600 transition-colors font-medium text-sm uppercase tracking-wide"
          active-class="text-accent-600"
          @click="mobileMenuOpen = false"
        >
          {{ $t(`nav.${link.key}`) }}
        </NuxtLinkLocale>
        <NuxtLinkLocale
          to="/contact"
          class="block mt-3 bg-accent-600 text-white px-5 py-2 rounded text-sm font-semibold text-center hover:bg-accent-700 transition-colors uppercase tracking-wide"
          @click="mobileMenuOpen = false"
        >
          {{ $t('nav.getQuote') }}
        </NuxtLinkLocale>
      </div>
    </nav>
  </header>
</template>

<script setup lang="ts">
const mobileMenuOpen = ref(false)
const langOpen = ref(false)

const { locale, locales } = useI18n()
const switchLocalePath = useSwitchLocalePath()

const navLinks = [
  { to: '/', key: 'home' },
  { to: '/about', key: 'about' },
  { to: '/products', key: 'products' },
  { to: '/contact', key: 'contact' },
]
</script>
