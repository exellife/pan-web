<template>
  <div>
    <!-- Page Header -->
    <section class="bg-steel-50 py-16 lg:py-24 border-b border-steel-200">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <NuxtLink to="/products" class="text-accent-600 hover:text-accent-700 text-sm font-medium uppercase tracking-wide mb-4 inline-block">
          &larr; All Products
        </NuxtLink>
        <p class="text-accent-600 font-semibold text-sm uppercase tracking-widest mb-2">Cookware Division</p>
        <h1 class="text-4xl md:text-5xl font-display font-bold text-steel-900">Cookware Product Lines</h1>
        <p class="mt-4 text-lg text-steel-500 max-w-2xl">
          From everyday non-stick pans to professional-grade stainless steel,
          we manufacture cookware for every market segment.
        </p>
      </div>
    </section>

    <!-- Product Lines -->
    <section class="bg-white py-16 lg:py-24">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="space-y-16">
          <div
            v-for="(line, index) in productLines"
            :key="line.name"
            class="grid grid-cols-1 lg:grid-cols-2 gap-8 items-center"
          >
            <div :class="index % 2 === 1 ? 'lg:order-2' : ''">
              <span class="text-accent-600 font-semibold text-sm uppercase tracking-widest">{{ line.category }}</span>
              <h2 class="text-2xl md:text-3xl font-display font-bold text-steel-900 mt-2">{{ line.name }}</h2>
              <p class="text-steel-600 mt-4 leading-relaxed">{{ line.description }}</p>

              <div class="mt-6 space-y-2">
                <h4 class="text-steel-900 text-sm font-semibold uppercase tracking-wide">Specifications</h4>
                <ul class="space-y-1">
                  <li
                    v-for="spec in line.specs"
                    :key="spec"
                    class="text-steel-500 text-sm flex items-start gap-2"
                  >
                    <span class="text-accent-500 mt-0.5">&#8226;</span>
                    {{ spec }}
                  </li>
                </ul>
              </div>

              <div class="mt-6 flex gap-3">
                <NuxtLink
                  to="/contact"
                  class="bg-accent-600 text-white px-6 py-2 rounded text-sm font-semibold hover:bg-accent-700 transition-colors"
                >
                  Request Quote
                </NuxtLink>
                <button
                  class="border border-steel-300 text-steel-600 px-6 py-2 rounded text-sm font-semibold hover:border-accent-500 hover:text-accent-600 transition-colors"
                >
                  Download Spec Sheet
                </button>
              </div>
            </div>

            <div
              class="bg-steel-100 border border-steel-200 rounded-lg h-72 flex items-center justify-center"
              :class="index % 2 === 1 ? 'lg:order-1' : ''"
            >
              <span class="text-steel-400">[{{ line.name }} photo]</span>
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
useHead({
  title: 'Cookware - PanCraft Manufacturing',
  meta: [
    { name: 'description', content: 'Explore PanCraft\'s cookware lines: non-stick frying pans, stainless steel, cast iron, and ceramic-coated pans. OEM available.' },
  ],
})

const productLines = [
  {
    name: 'Classic Non-Stick Series',
    category: 'Non-Stick',
    description: 'Our flagship line for everyday cooking. Multi-layer PFOA-free non-stick coating on forged aluminum bodies delivers reliable performance at scale.',
    specs: [
      'Sizes: 20cm, 24cm, 26cm, 28cm, 30cm',
      'Body: Forged aluminum (3.0mm - 4.5mm)',
      'Coating: 3-layer PFOA-free non-stick',
      'Handles: Bakelite, silicone, or stainless steel',
      'Induction-compatible base available',
    ],
  },
  {
    name: 'Pro Stainless Steel Line',
    category: 'Professional',
    description: 'Restaurant-grade tri-ply stainless steel with aluminum core. Designed for professional kitchens and premium retail markets.',
    specs: [
      'Sizes: 20cm, 24cm, 28cm, 32cm',
      'Construction: 18/10 stainless steel, aluminum core',
      'Riveted cast stainless handles',
      'Oven-safe to 260\u00b0C',
      'Dishwasher safe, lifetime warranty eligible',
    ],
  },
  {
    name: 'Heritage Cast Iron',
    category: 'Cast Iron',
    description: 'Pre-seasoned cast iron cookware manufactured using traditional sand-casting methods. Built to last generations.',
    specs: [
      'Sizes: 20cm, 25cm, 30cm skillets; griddles',
      'Material: Premium gray iron',
      'Pre-seasoned with food-grade flaxseed oil',
      'Weight-optimized wall design',
      'Compatible with all heat sources',
    ],
  },
  {
    name: 'EcoCeram Series',
    category: 'Ceramic Coated',
    description: 'Eco-friendly ceramic-coated pans for the health-conscious market segment. Vibrant finishes available for retail appeal.',
    specs: [
      'Sizes: 20cm, 24cm, 26cm, 28cm',
      'Body: Forged aluminum (3.5mm)',
      'Coating: Water-based ceramic non-stick',
      'Available in 12 exterior color options',
      'Soft-touch ergonomic handles',
    ],
  },
]
</script>
