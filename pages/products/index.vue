<template>
  <div>
    <!-- Page Header -->
    <section class="relative bg-steel-50 border-b border-steel-200 py-16 lg:py-24">
      <!-- Background image (thumb on mobile, full on desktop) + readability overlay -->
      <div class="absolute inset-0 bg-cover bg-center bg-no-repeat bg-[url('/images/hero/kitchen-hero-thumb.webp')] lg:bg-[url('/images/hero/kitchen-hero.webp')]">
        <div class="absolute inset-0 bg-gradient-to-r from-white/95 via-white/85 to-white/40" />
      </div>
      <div class="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <p class="text-accent-600 font-semibold text-sm uppercase tracking-widest mb-2">Product Divisions</p>
        <h1 class="text-4xl md:text-5xl font-display font-bold text-steel-900">Our Product Range</h1>
        <p class="mt-4 text-lg text-steel-600 max-w-2xl">
          Two product divisions built on the same foundation of precision metalworking,
          advanced surface treatment, and rigorous quality control.
        </p>
      </div>
    </section>

    <!-- Division Cards -->
    <section class="bg-white py-16 lg:py-24">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
          <NuxtLink
            v-for="division in divisions"
            :key="division.title"
            :to="division.to"
            class="group flex flex-col bg-white border border-steel-200 rounded-lg overflow-hidden hover:border-accent-400 hover:shadow-lg transition-all"
          >
            <div class="h-56 flex items-center justify-center p-6 bg-[radial-gradient(circle_at_50%_38%,#ffffff,#eceae7_70%,#e2dfdb)]">
              <img :src="division.image" :alt="division.title" loading="lazy" class="max-h-full max-w-full object-contain drop-shadow-lg transition-transform duration-300 group-hover:scale-105" />
            </div>
            <div class="p-8 flex flex-col flex-1">
              <h2 class="text-2xl font-display font-bold text-steel-900 mb-3 group-hover:text-accent-600 transition-colors">
                {{ division.title }}
              </h2>
              <p class="text-steel-500 leading-relaxed mb-4">{{ division.description }}</p>
              <ul class="space-y-1 mb-6">
                <li
                  v-for="line in division.lines"
                  :key="line"
                  class="text-steel-600 text-sm flex items-start gap-2"
                >
                  <span class="text-accent-500 mt-0.5">&#8226;</span>
                  {{ line }}
                </li>
              </ul>
              <span class="mt-auto self-end text-accent-600 font-semibold text-sm uppercase tracking-wide">
                View Product Lines &rarr;
              </span>
            </div>
          </NuxtLink>
        </div>
      </div>
    </section>

    <!-- Custom Manufacturing CTA -->
    <section class="bg-steel-50 py-16 border-t border-steel-200">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
        <h2 class="text-3xl font-display font-bold text-steel-900 mb-4">
          Need Custom Manufacturing?
        </h2>
        <p class="text-steel-500 text-lg mb-8 max-w-2xl mx-auto">
          We offer OEM and white-label production across both product divisions.
          Choose your materials, finishes, dimensions, and packaging. Minimum order quantities apply.
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
useHead({
  title: 'Products - PanCraft Manufacturing',
  meta: [
    { name: 'description', content: 'Explore PanCraft\'s two product divisions: premium cookware and high-efficiency heating radiators. OEM and custom manufacturing available.' },
  ],
})

const divisions = [
  {
    title: 'Cookware',
    description: 'Fry pans, sauce pans, casseroles, woks, grills and roasters across 30+ collections — in forged aluminum, die-cast, and stone-coated finishes, each offered in multiple sizes.',
    to: '/products/cookware',
    image: '/images/products/cookware/thumb/p02_25.webp',
    lines: [
      'Forged & Pressed Aluminum Series',
      'Die-cast & Granite Stone-Coat Collections',
      'Classic, Diamond & Nature Lines',
      'Grill, Roaster & Multi-functional Range',
    ],
  },
  {
    title: 'Heating Radiators',
    description: 'High-efficiency heating radiators with EN-rated heat output for residential and commercial applications. Engineered for durability and modern aesthetics.',
    to: '/products/radiators',
    image: '/images/products/radiators/full/p04_q4.webp',
    lines: [
      'Aluminum Radiators',
      'Bimetal Radiators',
      'Towel Radiators',
    ],
  },
]
</script>
