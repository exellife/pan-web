<template>
  <div>
    <!-- Page Header -->
    <section class="bg-steel-50 py-16 lg:py-24 border-b border-steel-200">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative">
        <NuxtLink to="/products" class="absolute -bottom-10 lg:-bottom-16 right-4 sm:right-6 lg:right-8 text-accent-600 hover:text-accent-700 text-sm font-medium uppercase tracking-wide">
          &larr; All Products
        </NuxtLink>
        <p class="text-accent-600 font-semibold text-sm uppercase tracking-widest mb-2">Heating Division</p>
        <h1 class="text-4xl md:text-5xl font-display font-bold text-steel-900">Radiator Catalog</h1>
        <p class="mt-4 text-lg text-steel-500 max-w-2xl">
          High-efficiency aluminum and bimetal heating radiators engineered for optimal
          heat output, durability, and modern aesthetics.
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
            :key="cat.name"
            class="px-5 py-2 rounded text-sm font-semibold transition-all"
            :class="activeCategory === cat.name
              ? 'bg-accent-600 text-white border border-accent-600'
              : 'bg-white text-steel-600 border border-steel-200 hover:border-accent-400 hover:text-accent-600'"
            @click="activeCategory = cat.name"
          >
            {{ cat.label }} <span class="opacity-60">({{ cat.count }})</span>
          </button>
        </div>

        <!-- Product Grid -->
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-8">
          <NuxtLink
            v-for="product in filteredProducts"
            :key="product.id"
            :to="`/products/radiators/${product.id}`"
            class="group flex flex-col bg-white border border-steel-200 rounded-lg overflow-hidden hover:border-accent-400 hover:shadow-lg transition-all"
          >
            <div class="bg-steel-50 h-56 flex items-center justify-center p-6">
              <img
                v-if="product.image"
                :src="product.image"
                :alt="product.name"
                loading="lazy"
                class="max-h-full max-w-full object-contain group-hover:scale-105 transition-transform"
              />
              <span v-else class="text-steel-300 text-sm">No image</span>
            </div>
            <div class="p-6 flex flex-col flex-1 border-t border-steel-100">
              <span class="text-accent-600 font-semibold text-xs uppercase tracking-widest">
                {{ titleCase(product.category) }}
              </span>
              <h3 class="text-lg font-display font-bold text-steel-900 mt-2 group-hover:text-accent-600 transition-colors">
                {{ product.name }}
              </h3>
              <p v-if="thermal(product)" class="text-steel-500 text-sm mt-2">{{ thermal(product) }}</p>
              <span class="mt-auto pt-4 self-end text-accent-600 font-semibold text-sm uppercase tracking-wide">
                View Details &rarr;
              </span>
            </div>
          </NuxtLink>
        </div>
      </div>
    </section>

    <!-- CTA -->
    <section class="bg-steel-50 py-16 border-t border-steel-200">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
        <h2 class="text-3xl font-display font-bold text-steel-900 mb-4">Need Custom Radiator Manufacturing?</h2>
        <p class="text-steel-500 text-lg mb-8 max-w-2xl mx-auto">
          We offer OEM and white-label production. Custom dimensions, heat outputs,
          finishes, and configurations available. Minimum order quantities apply.
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
import products from '~/data/radiators.json'

useHead({
  title: 'Heating Radiators - PanCraft Manufacturing',
  meta: [
    { name: 'description', content: 'Explore PanCraft\'s heating radiator catalog: aluminum, bimetal, and towel radiators with EN-rated heat output. OEM and custom manufacturing available.' },
  ],
})

const titleCase = (s: string) => s.split(' ').map(w => w.charAt(0) + w.slice(1).toLowerCase()).join(' ')
const thermal = (p: typeof products[number]) => {
  const s = p.specs.find(x => x.startsWith('Thermal output'))
  return s ? s.replace('Thermal output:', 'Heat output:') : ''
}

const activeCategory = ref('All')

const categories = computed(() => {
  const counts = new Map<string, number>()
  for (const p of products) counts.set(p.category, (counts.get(p.category) || 0) + 1)
  const cats = [...counts.entries()]
    .map(([name, count]) => ({ name, label: titleCase(name), count }))
    .sort((a, b) => b.count - a.count)
  return [{ name: 'All', label: 'All', count: products.length }, ...cats]
})

const filteredProducts = computed(() =>
  activeCategory.value === 'All' ? products : products.filter(p => p.category === activeCategory.value),
)
</script>
