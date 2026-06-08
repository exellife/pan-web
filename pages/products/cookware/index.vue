<template>
  <div>
    <!-- Page Header -->
    <section class="bg-steel-50 py-16 lg:py-24 border-b border-steel-200">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative">
        <NuxtLink to="/products" class="absolute -bottom-10 lg:-bottom-16 right-4 sm:right-6 lg:right-8 text-accent-600 hover:text-accent-700 text-sm font-medium uppercase tracking-wide">
          &larr; All Products
        </NuxtLink>
        <p class="text-accent-600 font-semibold text-sm uppercase tracking-widest mb-2">Cookware Division</p>
        <h1 class="text-4xl md:text-5xl font-display font-bold text-steel-900">Cookware Catalog</h1>
        <p class="mt-4 text-lg text-steel-500 max-w-2xl">
          From everyday non-stick pans to professional-grade stainless steel,
          we manufacture cookware for every market segment.
        </p>
      </div>
    </section>

    <!-- Filter + Grid -->
    <section class="bg-white py-16 lg:py-24">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <!-- Category Tabs -->
        <div class="flex flex-wrap gap-2 mb-12">
          <button
            v-for="cat in categories"
            :key="cat"
            class="px-5 py-2 rounded text-sm font-semibold transition-all"
            :class="activeCategory === cat
              ? 'bg-accent-600 text-white border border-accent-600'
              : 'bg-white text-steel-600 border border-steel-200 hover:border-accent-400 hover:text-accent-600'"
            @click="activeCategory = cat"
          >
            {{ cat }}
          </button>
        </div>

        <!-- Product Grid -->
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-8">
          <div
            v-for="product in filteredProducts"
            :key="product.id"
            class="group flex flex-col bg-white border border-steel-200 rounded-lg overflow-hidden hover:border-accent-400 hover:shadow-lg transition-all"
          >
            <!-- Image Placeholder -->
            <NuxtLink :to="`/products/cookware/${product.id}`">
              <div class="bg-steel-100 h-48 flex items-center justify-center">
                <span class="text-steel-400 text-sm">[{{ product.name }} photo]</span>
              </div>
            </NuxtLink>

            <!-- Card Body -->
            <div class="p-6 sm:p-8 flex flex-col flex-1">
              <span class="text-accent-600 font-semibold text-xs uppercase tracking-widest">
                {{ product.category }}
              </span>
              <NuxtLink :to="`/products/cookware/${product.id}`">
                <h3 class="text-xl font-display font-bold text-steel-900 mt-2 group-hover:text-accent-600 transition-colors">
                  {{ product.name }}
                </h3>
              </NuxtLink>
              <p class="text-steel-500 leading-relaxed text-sm mt-2 line-clamp-2">{{ product.description }}</p>
              <NuxtLink
                :to="`/products/cookware/${product.id}`"
                class="mt-auto pt-4 self-end text-accent-600 font-semibold text-sm uppercase tracking-wide"
              >
                View Details &rarr;
              </NuxtLink>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- CTA -->
    <section class="bg-steel-50 py-16 border-t border-steel-200">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
        <h2 class="text-3xl font-display font-bold text-steel-900 mb-4">
          Need Custom Cookware Manufacturing?
        </h2>
        <p class="text-steel-500 text-lg mb-8 max-w-2xl mx-auto">
          We offer OEM and white-label production. Choose your materials, coatings,
          handle designs, and packaging. Minimum order quantities apply.
        </p>
        <NuxtLink
          to="/contact"
          class="inline-block bg-accent-600 text-white px-8 py-3 rounded font-semibold hover:bg-accent-700 transition-colors"
        >
          Discuss Your Requirements
        </NuxtLink>
      </div>
    </section>

  </div>
</template>

<script setup lang="ts">
import products from '~/data/cookware.json'

useHead({
  title: 'Cookware - PanCraft Manufacturing',
  meta: [
    { name: 'description', content: 'Explore PanCraft\'s cookware catalog: non-stick frying pans, stainless steel, cast iron, and ceramic-coated pans. OEM available.' },
  ],
})

const categories = ['All', 'Non-Stick', 'Stainless Steel', 'Cast Iron', 'Ceramic']
const activeCategory = ref('All')

const filteredProducts = computed(() => {
  if (activeCategory.value === 'All') return products
  return products.filter(p => p.category === activeCategory.value)
})
</script>
