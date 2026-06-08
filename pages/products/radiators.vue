<template>
  <div>
    <!-- Page Header -->
    <section class="bg-steel-50 py-16 lg:py-24 border-b border-steel-200">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <NuxtLink to="/products" class="text-accent-600 hover:text-accent-700 text-sm font-medium uppercase tracking-wide mb-4 inline-block">
          &larr; All Products
        </NuxtLink>
        <p class="text-accent-600 font-semibold text-sm uppercase tracking-widest mb-2">Heating Division</p>
        <h1 class="text-4xl md:text-5xl font-display font-bold text-steel-900">Heating Radiators</h1>
        <p class="mt-4 text-lg text-steel-500 max-w-2xl">
          High-efficiency heating radiators engineered for optimal heat output,
          durability, and modern aesthetics — for residential and industrial applications.
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
          Need Custom Radiator Manufacturing?
        </h2>
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
useHead({
  title: 'Heating Radiators - PanCraft Manufacturing',
  meta: [
    { name: 'description', content: 'Explore PanCraft\'s heating radiator lines: panel radiators, column radiators, and industrial heating units. OEM and custom manufacturing available.' },
  ],
})

const productLines = [
  {
    name: 'Panel Radiators',
    category: 'Residential',
    description: 'Compact, efficient panel radiators for homes and apartments. Clean lines and high heat output in a space-saving design. Available in single, double, and triple panel configurations.',
    specs: [
      'Types: Type 11, Type 21, Type 22, Type 33',
      'Heights: 300mm, 400mm, 500mm, 600mm, 900mm',
      'Lengths: 400mm to 3000mm',
      'Material: Cold-rolled low-carbon steel',
      'Powder-coated finish (RAL color options)',
      'Working pressure: 10 bar, test pressure: 13 bar',
    ],
  },
  {
    name: 'Column Radiators',
    category: 'Decorative / Premium',
    description: 'Classic column-style radiators that combine high heat output with distinctive aesthetics. Ideal for period properties, renovations, and premium residential projects.',
    specs: [
      'Columns: 2-column, 3-column, 4-column',
      'Heights: 300mm to 1800mm',
      'Sections: 4 to 30 (custom lengths)',
      'Material: Cast iron or steel',
      'Finishes: Powder coat, chrome, brushed nickel',
      'Compatible with central heating and dual-fuel systems',
    ],
  },
  {
    name: 'Industrial Heating Units',
    category: 'Industrial / Commercial',
    description: 'Heavy-duty heating solutions for warehouses, factories, and commercial buildings. Engineered for high-volume heat output and long service life in demanding environments.',
    specs: [
      'High-output steel panel construction',
      'Floor-standing and wall-mounted options',
      'Custom dimensions available',
      'Anti-corrosion treatment for harsh environments',
      'Working pressure: up to 16 bar',
      'Optional thermostatic valve integration',
    ],
  },
]
</script>
