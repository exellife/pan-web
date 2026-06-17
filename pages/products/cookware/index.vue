<template>
  <div>
    <!-- Page Header -->
    <section class="relative bg-steel-50 border-b border-steel-200 py-16 lg:py-24">
      <!-- Background image (thumb on mobile, full on desktop) + readability overlay -->
      <div class="absolute inset-0 bg-cover bg-center bg-no-repeat bg-[url('/images/hero/cookware-hero-thumb.webp')] lg:bg-[url('/images/hero/cookware-hero.webp')]">
        <div class="absolute inset-0 bg-gradient-to-r from-white/95 via-white/85 to-white/40" />
      </div>
      <div class="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <NuxtLink to="/products" class="absolute -bottom-10 lg:-bottom-16 right-4 sm:right-6 lg:right-8 text-accent-600 hover:text-accent-700 text-sm font-medium uppercase tracking-wide">
          &larr; All Products
        </NuxtLink>
        <p class="text-accent-600 font-semibold text-sm uppercase tracking-widest mb-2">Cookware Division</p>
        <h1 class="text-4xl md:text-5xl font-display font-bold text-steel-900">Cookware Catalog</h1>
        <p class="mt-4 text-lg text-steel-600 max-w-2xl">
          {{ products.length }} products across {{ collections.length }} collections — browse by
          collection, then narrow by type. Each product is offered in multiple sizes.
        </p>
      </div>
    </section>

    <!-- Sticky mobile filter toolbar (collection + type) -->
    <div class="lg:hidden sticky top-16 z-30 bg-white/95 backdrop-blur border-b border-steel-200 shadow-sm">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 py-3 space-y-3">
        <select
          v-model="activeCollection"
          class="w-full px-4 py-2 bg-white border border-steel-300 rounded text-steel-900 focus:ring-2 focus:ring-accent-500 focus:border-accent-500 outline-none"
        >
          <option value="All">All Collections ({{ products.length }})</option>
          <option v-for="c in collections" :key="c.name" :value="c.name">{{ c.name }} ({{ c.count }})</option>
        </select>
        <div class="flex gap-2 overflow-x-auto -mx-4 px-4 pb-0.5">
          <button
            v-for="t in typeGroups"
            :key="t.name"
            class="shrink-0 px-3.5 py-1.5 rounded-full text-sm font-medium transition-all"
            :class="activeType === t.name
              ? 'bg-accent-600 text-white border border-accent-600'
              : 'bg-white text-steel-600 border border-steel-200'"
            @click="activeType = t.name"
          >
            {{ t.name }} <span class="opacity-60">{{ t.count }}</span>
          </button>
        </div>
      </div>
    </div>

    <!-- Catalog -->
    <section class="bg-white py-12 lg:py-20">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="lg:grid lg:grid-cols-[16rem_1fr] lg:gap-12">
          <!-- Collections sidebar (desktop) -->
          <aside class="hidden lg:block">
            <nav class="lg:sticky lg:top-20">
              <h2 class="text-xs font-semibold text-steel-400 uppercase tracking-widest mb-3">Collections</h2>
              <ul class="space-y-0.5 max-h-[70vh] overflow-y-auto pr-2">
                <li>
                  <button
                    class="w-full text-left px-3 py-1.5 rounded text-sm transition-colors flex justify-between items-center gap-2"
                    :class="activeCollection === 'All' ? 'bg-accent-50 text-accent-700 font-semibold' : 'text-steel-600 hover:bg-steel-50 hover:text-accent-600'"
                    @click="activeCollection = 'All'"
                  >
                    <span>All Collections</span>
                    <span class="text-xs text-steel-400">{{ products.length }}</span>
                  </button>
                </li>
                <li v-for="c in collections" :key="c.name">
                  <button
                    class="w-full text-left px-3 py-1.5 rounded text-sm transition-colors flex justify-between items-center gap-2"
                    :class="activeCollection === c.name ? 'bg-accent-50 text-accent-700 font-semibold' : 'text-steel-600 hover:bg-steel-50 hover:text-accent-600'"
                    @click="activeCollection = c.name"
                  >
                    <span class="truncate">{{ c.name }}</span>
                    <span class="text-xs text-steel-400">{{ c.count }}</span>
                  </button>
                </li>
              </ul>
            </nav>
          </aside>

          <!-- Grid + type filter -->
          <div>
            <div class="hidden lg:flex flex-wrap gap-2 mb-6">
              <button
                v-for="t in typeGroups"
                :key="t.name"
                class="px-4 py-1.5 rounded-full text-sm font-medium transition-all"
                :class="activeType === t.name
                  ? 'bg-accent-600 text-white border border-accent-600'
                  : 'bg-white text-steel-600 border border-steel-200 hover:border-accent-400 hover:text-accent-600'"
                @click="activeType = t.name"
              >
                {{ t.name }} <span class="opacity-60">{{ t.count }}</span>
              </button>
            </div>

            <p class="text-steel-400 text-sm mb-6">Showing {{ filteredProducts.length }} of {{ products.length }} products</p>

            <div v-if="filteredProducts.length" class="grid grid-cols-1 sm:grid-cols-2 xl:grid-cols-3 gap-6 lg:gap-8">
              <NuxtLink
                v-for="product in filteredProducts"
                :key="product.id"
                :to="`/products/cookware/${product.id}`"
                class="group flex flex-col bg-white border border-steel-200 rounded-lg overflow-hidden hover:border-accent-400 hover:shadow-lg transition-all"
              >
                <div class="relative aspect-square flex items-center justify-center p-4 bg-[radial-gradient(circle_at_50%_38%,#ffffff,#eceae7_70%,#e2dfdb)]">
                  <img
                    v-if="product.image"
                    :src="product.image"
                    :alt="product.name"
                    loading="lazy"
                    class="max-h-full max-w-full object-contain drop-shadow-lg transition-transform duration-300 group-hover:scale-105"
                  />
                  <span v-else class="text-steel-300 text-sm">No image</span>
                  <!-- Secondary / alternate views, overlaid bottom-right (gallery products only) -->
                  <div v-if="product.images.length > 1" class="absolute right-2 bottom-2 flex gap-1">
                    <span
                      v-for="(img, i) in product.images.slice(1, 4)"
                      :key="i"
                      class="w-8 h-8 shrink-0 bg-white border border-steel-200 rounded-md shadow-sm flex items-center justify-center p-0.5"
                    >
                      <img :src="img.thumb" alt="" loading="lazy" class="max-h-full max-w-full object-contain" />
                    </span>
                    <span
                      v-if="product.images.length > 4"
                      class="w-8 h-8 shrink-0 rounded-md bg-white/90 border border-steel-200 shadow-sm text-steel-500 text-[10px] font-medium flex items-center justify-center"
                    >
                      +{{ product.images.length - 4 }}
                    </span>
                  </div>
                </div>
                <div class="p-5 flex flex-col flex-1 border-t border-steel-100">
                  <span class="text-accent-600 font-semibold text-xs uppercase tracking-widest">{{ product.type }}</span>
                  <h3 class="text-base font-display font-bold text-steel-900 mt-1 group-hover:text-accent-600 transition-colors">
                    {{ product.name }}
                  </h3>
                  <span class="text-steel-400 text-xs mt-1">{{ sizeSummary(product) }}</span>
                  <span class="mt-auto pt-3 text-accent-600 font-semibold text-xs uppercase tracking-wide">
                    View Details &rarr;
                  </span>
                </div>
              </NuxtLink>
            </div>
            <p v-else class="text-steel-400 py-12">
              No products match this combination. <button class="text-accent-600 underline" @click="activeType = 'All'">Reset type filter</button>.
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- CTA -->
    <section class="bg-steel-50 py-16 border-t border-steel-200">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
        <h2 class="text-3xl font-display font-bold text-steel-900 mb-4">Need Custom Cookware Manufacturing?</h2>
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
  title: 'Cookware - TanDem Manufacturing',
  meta: [
    { name: 'description', content: 'Browse TanDem\'s cookware catalog: 147 products across 27 collections — fry pans, sauce pans, casseroles, woks, grills and roasters, each in multiple sizes. OEM available.' },
  ],
})

const SPECIALTY = 'Specialty & Grills'
const activeCollection = ref('All')
const activeType = ref('All')

const sizeSummary = (p: typeof products[number]) =>
  p.configs.length === 1 ? p.configs[0].size : `${p.configs.length} sizes`

// Collections sidebar — counts respect the active type; "Specialty & Grills" sorts last.
const collections = computed(() => {
  const base = activeType.value === 'All' ? products : products.filter(p => p.typeGroup === activeType.value)
  const counts = new Map<string, number>()
  for (const p of base) counts.set(p.collectionLabel, (counts.get(p.collectionLabel) || 0) + 1)
  return [...counts.entries()]
    .map(([name, count]) => ({ name, count }))
    .sort((a, b) =>
      a.name === SPECIALTY ? 1 : b.name === SPECIALTY ? -1 : a.name.localeCompare(b.name),
    )
})

// Type chips — counts respect the active collection.
const typeGroups = computed(() => {
  const base = activeCollection.value === 'All' ? products : products.filter(p => p.collectionLabel === activeCollection.value)
  const counts = new Map<string, number>()
  for (const p of base) counts.set(p.typeGroup, (counts.get(p.typeGroup) || 0) + 1)
  const list = [...counts.entries()].map(([name, count]) => ({ name, count })).sort((a, b) => b.count - a.count)
  return [{ name: 'All', count: base.length }, ...list]
})

const filteredProducts = computed(() =>
  products.filter(p =>
    (activeCollection.value === 'All' || p.collectionLabel === activeCollection.value) &&
    (activeType.value === 'All' || p.typeGroup === activeType.value),
  ),
)
</script>
