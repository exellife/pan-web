<template>
  <div v-if="product">
    <!-- Page Header -->
    <section class="bg-steel-50 py-16 lg:py-24 border-b border-steel-200">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative">
        <NuxtLinkLocale to="/products" class="absolute -bottom-10 lg:-bottom-16 right-4 sm:right-6 lg:right-8 text-accent-600 hover:text-accent-700 text-sm font-medium uppercase tracking-wide">
          &larr; {{ $t('common.allProducts') }}
        </NuxtLinkLocale>
        <NuxtLinkLocale to="/products/radiators" class="text-accent-600 hover:text-accent-700 text-sm font-medium uppercase tracking-wide mb-4 inline-block">
          &larr; {{ $t('radiators.detail.catalog') }}
        </NuxtLinkLocale>
        <p class="text-accent-600 font-semibold text-sm uppercase tracking-widest mb-2">{{ titleCase(product.category) }} · {{ $t('radiators.detail.division') }}</p>
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
            <span v-else class="text-steel-300 text-sm">{{ $t('common.noImage') }}</span>
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
              <NuxtLinkLocale
                to="/contact"
                class="inline-block bg-accent-600 text-white px-8 py-3 rounded font-semibold hover:bg-accent-700 transition-colors"
              >
                {{ $t('common.requestQuote') }}
              </NuxtLinkLocale>
              <button
                type="button"
                class="inline-flex items-center gap-2 bg-white text-steel-700 px-8 py-3 rounded font-semibold border border-steel-300 hover:border-accent-400 hover:text-accent-600 transition-colors"
                @click="share"
              >
                <svg class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" d="M8.7 10.7l6.6-3.4M8.7 13.3l6.6 3.4M18 8a3 3 0 10-3-3 3 3 0 003 3zm0 13a3 3 0 10-3-3 3 3 0 003 3zM6 15a3 3 0 10-3-3 3 3 0 003 3z" />
                </svg>
                {{ shareLabel }}
              </button>
            </div>
          </div>
        </div>

        <!-- Related in category -->
        <div v-if="related.length" class="mt-20 pt-12 border-t border-steel-200">
          <h2 class="text-2xl font-display font-bold text-steel-900 mb-8">{{ $t('radiators.detail.moreCategory', { category: titleCase(product.category) }) }}</h2>
          <div class="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-4 gap-6">
            <NuxtLinkLocale
              v-for="rel in related"
              :key="rel.id"
              :to="`/products/radiators/${rel.id}`"
              class="group flex flex-col bg-white border border-steel-200 rounded-lg overflow-hidden hover:border-accent-400 hover:shadow-lg transition-all"
            >
              <div class="bg-steel-50 aspect-square flex items-center justify-center p-3">
                <img v-if="rel.image" :src="rel.image" :alt="rel.name" loading="lazy" class="max-h-full max-w-full object-contain" />
                <span v-else class="text-steel-300 text-xs">{{ $t('common.noImage') }}</span>
              </div>
              <div class="p-3 border-t border-steel-100">
                <h3 class="text-sm text-steel-800 group-hover:text-accent-600 transition-colors truncate">{{ rel.name }}</h3>
              </div>
            </NuxtLinkLocale>
          </div>
        </div>
      </div>
    </section>
  </div>

  <!-- Not Found -->
  <div v-else>
    <section class="bg-steel-50 py-16 lg:py-24 border-b border-steel-200">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <NuxtLinkLocale to="/products/radiators" class="text-accent-600 hover:text-accent-700 text-sm font-medium uppercase tracking-wide mb-4 inline-block">
          &larr; {{ $t('radiators.detail.catalog') }}
        </NuxtLinkLocale>
        <h1 class="text-4xl md:text-5xl font-display font-bold text-steel-900">{{ $t('radiators.detail.notFoundTitle') }}</h1>
        <p class="mt-4 text-lg text-steel-500">
          {{ $t('radiators.detail.notFoundText') }}
        </p>
      </div>
    </section>
  </div>
</template>

<script setup lang="ts">
import products from '~/data/radiators.json'

const { t } = useI18n()
const route = useRoute()
const product = products.find(p => p.id === route.params.id)

const titleCase = (s: string) => s.split(' ').map(w => w.charAt(0) + w.slice(1).toLowerCase()).join(' ')

const shareLabel = ref(t('common.share'))
async function share() {
  if (!product) return
  const url = window.location.href
  try {
    if (navigator.share) {
      await navigator.share({ title: `${product.name} — TanDem`, url })
    } else {
      await navigator.clipboard.writeText(url)
      shareLabel.value = t('common.linkCopied')
      setTimeout(() => { shareLabel.value = t('common.share') }, 2000)
    }
  } catch {
    // share cancelled or unavailable — ignore
  }
}

const related = computed(() =>
  product
    ? products.filter(p => p.category === product.category && p.id !== product.id).slice(0, 8)
    : [],
)

useHead(() => ({
  title: product
    ? t('radiators.detail.metaTitle', { name: product.name })
    : t('radiators.detail.metaNotFound'),
}))
</script>
