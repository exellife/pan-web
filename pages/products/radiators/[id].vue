<template>
  <div v-if="product">
    <!-- Page Header -->
    <section class="bg-steel-50 py-16 lg:py-24 border-b border-steel-200">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative">
        <NuxtLink to="/products" class="absolute -bottom-10 lg:-bottom-16 right-4 sm:right-6 lg:right-8 text-accent-600 hover:text-accent-700 text-sm font-medium uppercase tracking-wide">
          &larr; All Products
        </NuxtLink>
        <NuxtLink to="/products/radiators" class="text-accent-600 hover:text-accent-700 text-sm font-medium uppercase tracking-wide mb-4 inline-block">
          &larr; Radiator Catalog
        </NuxtLink>
        <p class="text-accent-600 font-semibold text-sm uppercase tracking-widest mb-2">{{ titleCase(product.category) }} · Heating Division</p>
        <h1 class="text-4xl md:text-5xl font-display font-bold text-steel-900">{{ product.name }}</h1>
      </div>
    </section>

    <!-- Product Detail -->
    <section class="bg-white py-16 lg:py-24">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-12 lg:gap-16">
          <!-- Image -->
          <div class="bg-steel-50 border border-steel-200 rounded-lg h-80 lg:h-[28rem] flex items-center justify-center p-8">
            <img
              v-if="product.full"
              :src="product.full"
              :alt="product.name"
              class="max-h-full max-w-full object-contain"
            />
            <span v-else class="text-steel-300 text-sm">No image available</span>
          </div>

          <!-- Info -->
          <div class="flex flex-col">
            <div class="flex flex-wrap gap-2">
              <span class="text-accent-700 bg-accent-50 font-semibold text-xs uppercase tracking-widest px-3 py-1 rounded">
                {{ titleCase(product.category) }}
              </span>
              <span v-if="product.model" class="text-steel-500 bg-steel-100 font-mono text-xs px-3 py-1 rounded">
                {{ product.model }}
              </span>
            </div>
            <h2 class="text-3xl font-display font-bold text-steel-900 mt-4">{{ product.name }}</h2>

            <!-- Specs table -->
            <dl class="mt-6 divide-y divide-steel-100 border-y border-steel-100">
              <div v-for="(spec, i) in product.specs" :key="i" class="flex gap-4 py-2.5 text-sm">
                <dt class="w-48 shrink-0 text-steel-400">{{ spec.split(':')[0] }}</dt>
                <dd class="text-steel-700">{{ spec.split(':').slice(1).join(':').trim() }}</dd>
              </div>
            </dl>

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

        <!-- Related in category -->
        <div v-if="related.length" class="mt-20 pt-12 border-t border-steel-200">
          <h2 class="text-2xl font-display font-bold text-steel-900 mb-8">More {{ titleCase(product.category) }} radiators</h2>
          <div class="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-4 gap-6">
            <NuxtLink
              v-for="rel in related"
              :key="rel.id"
              :to="`/products/radiators/${rel.id}`"
              class="group flex flex-col bg-white border border-steel-200 rounded-lg overflow-hidden hover:border-accent-400 hover:shadow-lg transition-all"
            >
              <div class="bg-steel-50 aspect-square flex items-center justify-center p-3">
                <img v-if="rel.image" :src="rel.image" :alt="rel.name" loading="lazy" class="max-h-full max-w-full object-contain" />
                <span v-else class="text-steel-300 text-xs">No image</span>
              </div>
              <div class="p-3 border-t border-steel-100">
                <h3 class="text-sm text-steel-800 group-hover:text-accent-600 transition-colors truncate">{{ rel.name }}</h3>
              </div>
            </NuxtLink>
          </div>
        </div>
      </div>
    </section>
  </div>

  <!-- Not Found -->
  <div v-else>
    <section class="bg-steel-50 py-16 lg:py-24 border-b border-steel-200">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <NuxtLink to="/products/radiators" class="text-accent-600 hover:text-accent-700 text-sm font-medium uppercase tracking-wide mb-4 inline-block">
          &larr; Radiator Catalog
        </NuxtLink>
        <h1 class="text-4xl md:text-5xl font-display font-bold text-steel-900">Product Not Found</h1>
        <p class="mt-4 text-lg text-steel-500">
          The radiator product you're looking for doesn't exist. Please check the URL or browse the catalog.
        </p>
      </div>
    </section>
  </div>
</template>

<script setup lang="ts">
import products from '~/data/radiators.json'

const route = useRoute()
const product = products.find(p => p.id === route.params.id)

const titleCase = (s: string) => s.split(' ').map(w => w.charAt(0) + w.slice(1).toLowerCase()).join(' ')

const related = computed(() =>
  product
    ? products.filter(p => p.category === product.category && p.id !== product.id).slice(0, 8)
    : [],
)

useHead({
  title: product
    ? `${product.name} - Radiators - PanCraft Manufacturing`
    : 'Product Not Found - PanCraft Manufacturing',
})
</script>
