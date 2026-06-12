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
        <p class="text-accent-600 font-semibold text-sm uppercase tracking-widest mb-2">{{ product.section }} Collection</p>
        <h1 class="text-4xl md:text-5xl font-display font-bold text-steel-900">{{ product.name }}</h1>
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
                :alt="product.name"
                class="max-h-full max-w-full object-contain"
              />
              <span v-else class="text-steel-300 text-sm">No image available</span>
            </div>
            <div v-if="product.images.length > 1" class="mt-4 flex flex-wrap gap-3">
              <button
                v-for="(img, i) in product.images"
                :key="i"
                class="w-20 h-20 bg-steel-50 border rounded-lg flex items-center justify-center p-2 transition-colors"
                :class="activeImage === img.full ? 'border-accent-500' : 'border-steel-200 hover:border-accent-300'"
                @click="activeImage = img.full"
              >
                <img :src="img.thumb" :alt="`${product.name} view ${i + 1}`" class="max-h-full max-w-full object-contain" />
              </button>
            </div>
          </div>

          <!-- Info -->
          <div class="flex flex-col">
            <div class="flex flex-wrap gap-2">
              <span class="text-accent-700 bg-accent-50 font-semibold text-xs uppercase tracking-widest px-3 py-1 rounded">
                {{ product.type }}
              </span>
              <span class="text-steel-500 bg-steel-100 font-mono text-xs px-3 py-1 rounded">
                {{ activeConfig.artNo }}
              </span>
            </div>
            <h2 class="text-3xl font-display font-bold text-steel-900 mt-4">{{ product.name }}</h2>

            <!-- Size / config selector -->
            <div v-if="product.configs.length > 1" class="mt-6">
              <p class="text-xs font-semibold text-steel-400 uppercase tracking-widest mb-2">
                Size <span class="text-steel-300 normal-case">({{ product.configs.length }} options)</span>
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
                <dt class="w-40 shrink-0 text-steel-400">{{ spec.split(':')[0] }}</dt>
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

        <!-- Related -->
        <div v-if="related.length" class="mt-20 pt-12 border-t border-steel-200">
          <h2 class="text-2xl font-display font-bold text-steel-900 mb-8">More from {{ product.section }}</h2>
          <div class="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-4 gap-6">
            <NuxtLink
              v-for="rel in related"
              :key="rel.id"
              :to="`/products/cookware/${rel.id}`"
              class="group flex flex-col bg-white border border-steel-200 rounded-lg overflow-hidden hover:border-accent-400 hover:shadow-lg transition-all"
            >
              <div class="bg-steel-50 aspect-square flex items-center justify-center p-3">
                <img v-if="rel.image" :src="rel.image" :alt="rel.name" loading="lazy" class="max-h-full max-w-full object-contain" />
                <span v-else class="text-steel-300 text-xs">No image</span>
              </div>
              <div class="p-3 border-t border-steel-100">
                <span class="text-accent-600 text-[10px] font-semibold uppercase tracking-widest">{{ rel.type }}</span>
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

const activeImage = ref(product?.full || null)
const activeConfig = ref(product?.configs[0])
const activeSpecs = computed(() => [...(product?.commonSpecs || []), ...(activeConfig.value?.specs || [])])

// Related: other products from the same catalog section.
const related = computed(() =>
  product
    ? products.filter(p => p.section === product.section && p.id !== product.id).slice(0, 8)
    : [],
)

useHead({
  title: product
    ? `${product.name} - Cookware - PanCraft Manufacturing`
    : 'Product Not Found - PanCraft Manufacturing',
})
</script>
