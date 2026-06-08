<template>
  <div v-if="product">
    <!-- Page Header -->
    <section class="bg-steel-50 py-16 lg:py-24 border-b border-steel-200">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative">
        <NuxtLink to="/products" class="absolute -bottom-10 lg:-bottom-16 right-4 sm:right-6 lg:right-8 text-accent-600 hover:text-accent-700 text-sm font-medium uppercase tracking-wide">
          &larr; All Products
        </NuxtLink>
        <NuxtLink to="/products/cookware" class="text-accent-600 hover:text-accent-700 text-sm font-medium uppercase tracking-wide mb-4 inline-block">
          &larr; Cookware Catalog
        </NuxtLink>
        <p class="text-accent-600 font-semibold text-sm uppercase tracking-widest mb-2">Cookware Division</p>
        <h1 class="text-4xl md:text-5xl font-display font-bold text-steel-900">{{ product.name }}</h1>
      </div>
    </section>

    <!-- Product Detail -->
    <section class="bg-white py-16 lg:py-24">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-12 lg:gap-16">
          <!-- Image -->
          <div class="bg-steel-100 h-80 lg:h-[28rem] rounded-lg flex items-center justify-center">
            <span class="text-steel-400 text-sm">[{{ product.name }} photo]</span>
          </div>

          <!-- Info -->
          <div class="flex flex-col">
            <span class="text-accent-600 font-semibold text-xs uppercase tracking-widest">
              {{ product.category }}
            </span>
            <h2 class="text-3xl font-display font-bold text-steel-900 mt-2">{{ product.name }}</h2>
            <p class="text-steel-500 leading-relaxed mt-4">{{ product.description }}</p>

            <!-- Specs -->
            <ul class="mt-6 space-y-2">
              <li v-for="(spec, i) in product.specs" :key="i" class="flex items-start gap-2 text-steel-600 text-sm">
                <span class="text-accent-600 mt-0.5">&bull;</span>
                <span>{{ spec }}</span>
              </li>
            </ul>

            <!-- CTA Buttons -->
            <div class="mt-8 flex flex-wrap gap-4">
              <NuxtLink
                to="/contact"
                class="inline-block bg-accent-600 text-white px-8 py-3 rounded font-semibold hover:bg-accent-700 transition-colors"
              >
                Request Quote
              </NuxtLink>
              <NuxtLink
                to="/contact"
                class="inline-block bg-white text-steel-700 px-8 py-3 rounded font-semibold border border-steel-300 hover:border-accent-400 hover:text-accent-600 transition-colors"
              >
                Download Spec Sheet
              </NuxtLink>
            </div>
          </div>
        </div>
      </div>
    </section>

  </div>

  <!-- Not Found -->
  <div v-else>
    <section class="bg-steel-50 py-16 lg:py-24 border-b border-steel-200">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <NuxtLink to="/products/cookware" class="text-accent-600 hover:text-accent-700 text-sm font-medium uppercase tracking-wide mb-4 inline-block">
          &larr; Cookware Catalog
        </NuxtLink>
        <h1 class="text-4xl md:text-5xl font-display font-bold text-steel-900">Product Not Found</h1>
        <p class="mt-4 text-lg text-steel-500">
          The cookware product you're looking for doesn't exist. Please check the URL or browse the catalog.
        </p>
      </div>
    </section>
  </div>
</template>

<script setup lang="ts">
import products from '~/data/cookware.json'

const route = useRoute()
const product = products.find(p => p.id === route.params.id)

useHead({
  title: product
    ? `${product.name} - Cookware - PanCraft Manufacturing`
    : 'Product Not Found - PanCraft Manufacturing',
})
</script>
