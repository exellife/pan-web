<template>
  <footer class="bg-steel-50 text-steel-600 border-t border-steel-200">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
      <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
        <!-- Brand -->
        <div>
          <h3 class="text-2xl font-display font-bold text-steel-900 mb-4">
            Pan<span class="text-accent-600">Craft</span>
          </h3>
          <p class="text-steel-500 leading-relaxed">
            Precision metalworking manufacturer since 1995. Premium cookware
            and heating radiators trusted by distributors, retailers, and consumers worldwide.
          </p>
        </div>

        <!-- Quick Links -->
        <div>
          <h4 class="text-steel-900 font-semibold mb-4 text-sm uppercase tracking-wide">Navigation</h4>
          <ul class="space-y-2">
            <li v-for="link in footerLinks" :key="link.to">
              <NuxtLink :to="link.to" class="hover:text-accent-600 transition-colors">
                {{ link.label }}
              </NuxtLink>
            </li>
          </ul>
        </div>

        <!-- Contact Info -->
        <div>
          <h4 class="text-steel-900 font-semibold mb-4 text-sm uppercase tracking-wide">Factory & Office</h4>
          <ul class="space-y-2 text-steel-500">
            <li>123 Industrial Boulevard</li>
            <li>Manufacturing District, MD 10001</li>
            <li>
              <a href="mailto:info@pancraft.com" class="hover:text-accent-600 transition-colors">
                info@pancraft.com
              </a>
            </li>
            <li>
              <a href="tel:+15551234567" class="hover:text-accent-600 transition-colors">
                +1 (555) 123-4567
              </a>
            </li>
          </ul>
        </div>
      </div>

      <div class="border-t border-steel-200 mt-8 pt-8 text-center text-steel-400 text-sm">
        &copy; {{ new Date().getFullYear() }} PanCraft Manufacturing. All rights reserved.
      </div>
    </div>
  </footer>
</template>

<script setup lang="ts">
const footerLinks = [
  { to: '/', label: 'Home' },
  { to: '/about', label: 'About Us' },
  { to: '/products', label: 'Product Lines' },
  { to: '/contact', label: 'Contact & Inquiries' },
]
</script>
