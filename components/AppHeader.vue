<template>
  <header class="bg-white sticky top-0 z-50 border-b border-steel-200">
    <nav class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex justify-between items-center h-16">
        <!-- Logo -->
        <NuxtLink to="/" class="flex items-center space-x-2">
          <span class="text-2xl font-display font-bold text-steel-900">Pan<span class="text-accent-600">Craft</span></span>
        </NuxtLink>

        <!-- Desktop Navigation -->
        <div class="hidden md:flex items-center space-x-8">
          <NuxtLink
            v-for="link in navLinks"
            :key="link.to"
            :to="link.to"
            class="text-steel-600 hover:text-accent-600 transition-colors font-medium text-sm uppercase tracking-wide"
            active-class="text-accent-600"
          >
            {{ link.label }}
          </NuxtLink>
          <NuxtLink
            to="/contact"
            class="bg-accent-600 text-white px-5 py-2 rounded text-sm font-semibold hover:bg-accent-700 transition-colors uppercase tracking-wide"
          >
            Get a Quote
          </NuxtLink>
        </div>

        <!-- Mobile menu button -->
        <button
          class="md:hidden p-2 rounded-md text-steel-600 hover:text-accent-600"
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

      <!-- Mobile Navigation -->
      <div v-if="mobileMenuOpen" class="md:hidden pb-4 border-t border-steel-200 pt-4">
        <NuxtLink
          v-for="link in navLinks"
          :key="link.to"
          :to="link.to"
          class="block py-2 text-steel-600 hover:text-accent-600 transition-colors font-medium text-sm uppercase tracking-wide"
          active-class="text-accent-600"
          @click="mobileMenuOpen = false"
        >
          {{ link.label }}
        </NuxtLink>
        <NuxtLink
          to="/contact"
          class="block mt-3 bg-accent-600 text-white px-5 py-2 rounded text-sm font-semibold text-center hover:bg-accent-700 transition-colors uppercase tracking-wide"
          @click="mobileMenuOpen = false"
        >
          Get a Quote
        </NuxtLink>
      </div>
    </nav>
  </header>
</template>

<script setup lang="ts">
const mobileMenuOpen = ref(false)

const navLinks = [
  { to: '/', label: 'Home' },
  { to: '/about', label: 'About' },
  { to: '/products', label: 'Products' },
  { to: '/contact', label: 'Contact' },
]
</script>
