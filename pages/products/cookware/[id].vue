<template>
  <div v-if="product">
    <!-- Page Header -->
    <section class="bg-steel-50 py-16 lg:py-24 border-b border-steel-200">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative">
        <NuxtLinkLocale to="/products" class="absolute -bottom-10 lg:-bottom-16 right-4 sm:right-6 lg:right-8 text-accent-600 hover:text-accent-700 text-sm font-medium uppercase tracking-wide">
          &larr; {{ $t('common.allProducts') }}
        </NuxtLinkLocale>
        <NuxtLinkLocale to="/products/cookware" class="text-accent-600 hover:text-accent-700 text-sm font-medium uppercase tracking-wide mb-4 inline-block">
          &larr; {{ $t('cookware.detail.catalog') }}
        </NuxtLinkLocale>
        <p class="text-accent-600 font-semibold text-sm uppercase tracking-widest mb-2">{{ $t('cookware.detail.collectionEyebrow', { name: product.section }) }}</p>
        <h1 class="text-4xl md:text-5xl font-display font-bold text-steel-900">{{ displayName(product) }}</h1>
      </div>
    </section>

    <!-- Product Detail -->
    <section class="bg-white py-16 lg:py-24">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-12 lg:gap-16">
          <!-- Image + gallery -->
          <div>
            <div class="bg-steel-50 border border-steel-200 rounded-lg aspect-square flex items-center justify-center p-8">
              <img
                v-if="activeImage"
                :src="activeImage"
                :alt="displayName(product)"
                class="max-h-full max-w-full object-contain"
              />
              <span v-else class="text-steel-300 text-sm">{{ $t('common.noImage') }}</span>
            </div>
            <div v-if="product.images.length > 1" class="mt-4 flex flex-wrap gap-3">
              <button
                v-for="(img, i) in product.images"
                :key="i"
                class="w-20 h-20 bg-steel-50 border rounded-lg flex items-center justify-center p-2 transition-colors"
                :class="activeImage === img.full ? 'border-accent-500' : 'border-steel-200 hover:border-accent-300'"
                @click="activeImage = img.full"
              >
                <img :src="img.thumb" :alt="`${displayName(product)} ${i + 1}`" class="max-h-full max-w-full object-contain" />
              </button>
            </div>
          </div>

          <!-- Info -->
          <div class="flex flex-col">
            <div class="flex flex-wrap gap-2">
              <span class="text-accent-700 bg-accent-50 font-semibold text-xs uppercase tracking-widest px-3 py-1 rounded">
                {{ tType(product.type) }}
              </span>
              <span class="text-steel-500 bg-steel-100 font-mono text-xs px-3 py-1 rounded">
                {{ activeConfig.artNo }}
              </span>
            </div>
            <h2 class="text-3xl font-display font-bold text-steel-900 mt-4">{{ displayName(product) }}</h2>

            <!-- Size / config selector -->
            <div v-if="product.configs.length > 1" class="mt-6">
              <p class="text-xs font-semibold text-steel-400 uppercase tracking-widest mb-2">
                {{ $t('cookware.detail.size') }} <span class="text-steel-300 normal-case">({{ $t('cookware.detail.options', { count: product.configs.length }) }})</span>
              </p>
              <div class="flex flex-wrap gap-2">
                <button
                  v-for="cfg in product.configs"
                  :key="cfg.artNo"
                  class="px-4 py-1.5 rounded text-sm font-medium border transition-all"
                  :class="cfg.artNo === activeConfig.artNo
                    ? 'bg-accent-600 text-white border-accent-600'
                    : 'bg-white text-steel-600 border-steel-200 hover:border-accent-400 hover:text-accent-600'"
                  @click="activeConfig = cfg"
                >
                  {{ cfg.size || cfg.artNo }}
                </button>
              </div>
            </div>

            <!-- Specs table (reflects the selected size) -->
            <dl class="mt-6 divide-y divide-steel-100 border-y border-steel-100">
              <div v-for="(spec, i) in activeSpecs" :key="i" class="flex gap-4 py-2.5 text-sm">
                <dt class="w-40 shrink-0 text-steel-400">{{ $t(`spec.${spec.label}`) }}</dt>
                <dd class="text-steel-700">{{ spec.value }}</dd>
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

        <!-- Related -->
        <div v-if="related.length" class="mt-20 pt-12 border-t border-steel-200">
          <h2 class="text-2xl font-display font-bold text-steel-900 mb-8">{{ $t('cookware.detail.moreFrom', { name: product.section }) }}</h2>
          <div class="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-4 gap-6">
            <NuxtLinkLocale
              v-for="rel in related"
              :key="rel.id"
              :to="`/products/cookware/${rel.id}`"
              class="group flex flex-col bg-white border border-steel-200 rounded-lg overflow-hidden hover:border-accent-400 hover:shadow-lg transition-all"
            >
              <div class="bg-steel-50 aspect-square flex items-center justify-center p-3">
                <img v-if="rel.image" :src="rel.image" :alt="displayName(rel)" loading="lazy" class="max-h-full max-w-full object-contain" />
                <span v-else class="text-steel-300 text-xs">{{ $t('common.noImage') }}</span>
              </div>
              <div class="p-3 border-t border-steel-100">
                <span class="text-accent-600 text-[10px] font-semibold uppercase tracking-widest">{{ tType(rel.type) }}</span>
                <h3 class="text-sm text-steel-800 group-hover:text-accent-600 transition-colors truncate">{{ displayName(rel) }}</h3>
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
        <NuxtLinkLocale to="/products/cookware" class="text-accent-600 hover:text-accent-700 text-sm font-medium uppercase tracking-wide mb-4 inline-block">
          &larr; {{ $t('cookware.detail.catalog') }}
        </NuxtLinkLocale>
        <h1 class="text-4xl md:text-5xl font-display font-bold text-steel-900">{{ $t('cookware.detail.notFoundTitle') }}</h1>
        <p class="mt-4 text-lg text-steel-500">
          {{ $t('cookware.detail.notFoundText') }}
        </p>
      </div>
    </section>
  </div>
</template>

<script setup lang="ts">
import products from '~/data/cookware.json'

const { t, te } = useI18n()
const route = useRoute()
const product = products.find(p => p.id === route.params.id)

const slugKey = (v: string) => v.toLowerCase().replace(/[^a-z0-9]+/g, '_').replace(/(^_|_$)/g, '')
const tType = (v: string) => (te(`productType.${slugKey(v)}`) ? t(`productType.${slugKey(v)}`) : v)
// Display name: collection stays Latin, type word is translated.
const displayName = (p: typeof products[number]) => (p.collection ? `${p.section} ${tType(p.type)}` : tType(p.type))

const activeImage = ref(product?.full || null)
const activeConfig = ref(product?.configs[0])

const shareLabel = ref(t('common.share'))
async function share() {
  if (!product) return
  const url = window.location.href
  try {
    if (navigator.share) {
      await navigator.share({ title: `${displayName(product)} — TanDem`, url })
    } else {
      await navigator.clipboard.writeText(url)
      shareLabel.value = t('common.linkCopied')
      setTimeout(() => { shareLabel.value = t('common.share') }, 2000)
    }
  } catch {
    // share cancelled or unavailable — ignore
  }
}
const activeSpecs = computed(() => [...(product?.commonSpecs || []), ...(activeConfig.value?.specs || [])])

// Related: other products from the same catalog section.
const related = computed(() =>
  product
    ? products.filter(p => p.section === product.section && p.id !== product.id).slice(0, 8)
    : [],
)

useHead(() => ({
  title: product
    ? t('cookware.detail.metaTitle', { name: displayName(product) })
    : t('cookware.detail.metaNotFound'),
}))
</script>
