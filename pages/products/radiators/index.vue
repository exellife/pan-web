<template>
  <div>
    <!-- Page Header -->
    <section class="relative bg-steel-50 border-b border-steel-200 py-16 lg:py-24">
      <!-- Background image (thumb on mobile, full on desktop) + readability overlay -->
      <div class="absolute inset-0 bg-cover bg-center bg-no-repeat bg-[url('/images/hero/radiators-hero-thumb.webp')] lg:bg-[url('/images/hero/radiators-hero.webp')]">
        <div class="absolute inset-0 bg-gradient-to-r from-white/95 via-white/85 to-white/40" />
      </div>
      <div class="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <NuxtLinkLocale to="/products" class="absolute -bottom-10 lg:-bottom-16 right-4 sm:right-6 lg:right-8 text-accent-600 hover:text-accent-700 text-sm font-medium uppercase tracking-wide">
          &larr; {{ $t('common.allProducts') }}
        </NuxtLinkLocale>
        <p class="text-accent-600 font-semibold text-sm uppercase tracking-widest mb-2">{{ $t('radiators.eyebrow') }}</p>
        <h1 class="text-4xl md:text-5xl font-display font-bold text-steel-900">{{ $t('radiators.title') }}</h1>
        <p class="mt-4 text-lg text-steel-600 max-w-2xl">
          {{ $t('radiators.subtitle') }}
        </p>
      </div>
    </section>

    <!-- Sticky mobile filter toolbar (category) -->
    <div class="lg:hidden sticky top-16 z-30 bg-white/95 backdrop-blur border-b border-steel-200 shadow-sm">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 py-3">
        <div class="flex gap-2 overflow-x-auto -mx-4 px-4 pb-0.5">
          <button
            v-for="cat in categories"
            :key="cat.name"
            class="shrink-0 px-3.5 py-1.5 rounded-full text-sm font-medium transition-all"
            :class="activeCategory === cat.name
              ? 'bg-accent-600 text-white border border-accent-600'
              : 'bg-white text-steel-600 border border-steel-200'"
            @click="activeCategory = cat.name"
          >
            {{ cat.name === 'All' ? $t('common.all') : cat.label }} <span class="opacity-60">{{ cat.count }}</span>
          </button>
        </div>
      </div>
    </div>

    <!-- Filter + Grid -->
    <section class="bg-white py-16 lg:py-24">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <!-- Category Tabs (desktop) -->
        <div class="hidden lg:flex flex-wrap gap-2 mb-12">
          <button
            v-for="cat in categories"
            :key="cat.name"
            class="px-5 py-2 rounded text-sm font-semibold transition-all"
            :class="activeCategory === cat.name
              ? 'bg-accent-600 text-white border border-accent-600'
              : 'bg-white text-steel-600 border border-steel-200 hover:border-accent-400 hover:text-accent-600'"
            @click="activeCategory = cat.name"
          >
            {{ cat.name === 'All' ? $t('common.all') : cat.label }} <span class="opacity-60">({{ cat.count }})</span>
          </button>
        </div>

        <!-- Product Grid -->
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-8">
          <NuxtLinkLocale
            v-for="product in filteredProducts"
            :key="product.id"
            :to="`/products/radiators/${product.id}`"
            class="group flex flex-col bg-white border border-steel-200 rounded-lg overflow-hidden hover:border-accent-400 hover:shadow-lg transition-all"
          >
            <div class="h-56 flex items-center justify-center p-6 bg-[radial-gradient(circle_at_50%_38%,#ffffff,#eceae7_70%,#e2dfdb)]">
              <img
                v-if="product.image"
                :src="product.image"
                :alt="product.name"
                loading="lazy"
                class="max-h-full max-w-full object-contain drop-shadow-lg transition-transform duration-300 group-hover:scale-105"
              />
              <span v-else class="text-steel-300 text-sm">{{ $t('common.noImage') }}</span>
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
                {{ $t('common.viewDetails') }} &rarr;
              </span>
            </div>
          </NuxtLinkLocale>
        </div>
      </div>
    </section>

    <!-- CTA -->
    <section class="bg-steel-50 py-16 border-t border-steel-200">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
        <h2 class="text-3xl font-display font-bold text-steel-900 mb-4">{{ $t('radiators.customHeading') }}</h2>
        <p class="text-steel-500 text-lg mb-8 max-w-2xl mx-auto">
          {{ $t('radiators.customLead') }}
        </p>
        <NuxtLinkLocale
          to="/contact"
          class="inline-block bg-accent-600 text-white px-8 py-3 rounded font-semibold hover:bg-accent-700 transition-colors"
        >
          {{ $t('radiators.customButton') }}
        </NuxtLinkLocale>
      </div>
    </section>
  </div>
</template>

<script setup lang="ts">
import products from '~/data/radiators.json'

const { t } = useI18n()
useHead(() => ({
  title: t('radiators.metaTitle'),
  meta: [{ name: 'description', content: t('radiators.metaDescription') }],
}))

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
