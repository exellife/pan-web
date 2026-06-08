<template>
  <div>
    <!-- Hero Section -->
    <section class="relative bg-steel-50 py-24 lg:py-36 overflow-hidden">
      <div class="absolute inset-0 bg-gradient-to-br from-white to-steel-100" />
      <div class="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="max-w-3xl">
          <p class="text-accent-600 font-semibold text-sm uppercase tracking-widest mb-4">
            Established 1995
          </p>
          <h1 class="text-4xl md:text-5xl lg:text-6xl font-display font-bold text-steel-900 leading-tight">
            Precision
            <span class="text-accent-600">Metalworking</span>
            & Manufacturing
          </h1>
          <p class="mt-6 text-lg md:text-xl text-steel-600 leading-relaxed">
            From premium cookware to high-efficiency heating radiators — we engineer
            and manufacture metal products for distributors, retailers, and consumers worldwide.
          </p>
          <div class="mt-8 flex flex-col sm:flex-row gap-4">
            <NuxtLink
              to="/products"
              class="inline-block bg-accent-600 text-white px-8 py-3 rounded font-semibold hover:bg-accent-700 transition-colors text-center"
            >
              Explore Our Products
            </NuxtLink>
            <NuxtLink
              to="/contact"
              class="inline-block border-2 border-steel-300 text-steel-700 px-8 py-3 rounded font-semibold hover:border-accent-500 hover:text-accent-600 transition-colors text-center"
            >
              Request a Quote
            </NuxtLink>
          </div>
        </div>
      </div>
    </section>

    <!-- Stats Bar -->
    <section class="bg-white border-y border-steel-200">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        <div class="grid grid-cols-2 md:grid-cols-4 gap-8 text-center">
          <div v-for="stat in stats" :key="stat.label">
            <div class="text-3xl md:text-4xl font-bold text-accent-600">{{ stat.value }}</div>
            <div class="text-steel-500 text-sm mt-1 uppercase tracking-wide">{{ stat.label }}</div>
          </div>
        </div>
      </div>
    </section>

    <!-- Capabilities Section -->
    <section class="bg-white py-16 lg:py-24">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-12">
          <p class="text-accent-600 font-semibold text-sm uppercase tracking-widest mb-2">What We Do</p>
          <h2 class="text-3xl md:text-4xl font-display font-bold text-steel-900">
            Manufacturing Capabilities
          </h2>
          <p class="mt-4 text-lg text-steel-500 max-w-2xl mx-auto">
            Our facility combines advanced machinery with skilled craftsmanship
            to produce metal products that meet the highest industry standards.
          </p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
          <div
            v-for="capability in capabilities"
            :key="capability.title"
            class="p-8 rounded-lg bg-steel-50 border border-steel-200 hover:border-accent-400 transition-colors"
          >
            <div class="w-12 h-12 bg-accent-100 rounded-lg flex items-center justify-center mb-4">
              <span class="text-accent-600 text-xl font-bold">{{ capability.icon }}</span>
            </div>
            <h3 class="text-xl font-semibold text-steel-900 mb-2">{{ capability.title }}</h3>
            <p class="text-steel-500 leading-relaxed">{{ capability.description }}</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Product Divisions -->
    <section class="bg-steel-50 py-16 lg:py-24 border-y border-steel-200">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-12">
          <p class="text-accent-600 font-semibold text-sm uppercase tracking-widest mb-2">Our Divisions</p>
          <h2 class="text-3xl md:text-4xl font-display font-bold text-steel-900">
            Two Product Lines, One Standard of Excellence
          </h2>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
          <NuxtLink
            v-for="division in divisions"
            :key="division.title"
            :to="division.to"
            class="group bg-white border border-steel-200 rounded-lg overflow-hidden hover:border-accent-400 transition-colors"
          >
            <div class="bg-steel-100 h-48 flex items-center justify-center">
              <span class="text-steel-400 text-lg">[{{ division.title }} photo]</span>
            </div>
            <div class="p-8">
              <h3 class="text-2xl font-display font-bold text-steel-900 mb-3 group-hover:text-accent-600 transition-colors">
                {{ division.title }}
              </h3>
              <p class="text-steel-500 leading-relaxed mb-4">{{ division.description }}</p>
              <span class="text-accent-600 font-semibold text-sm uppercase tracking-wide">
                View Products &rarr;
              </span>
            </div>
          </NuxtLink>
        </div>
      </div>
    </section>

    <!-- Process Section -->
    <section class="bg-white py-16 lg:py-24">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-12">
          <p class="text-accent-600 font-semibold text-sm uppercase tracking-widest mb-2">Our Process</p>
          <h2 class="text-3xl md:text-4xl font-display font-bold text-steel-900">
            From Raw Material to Finished Product
          </h2>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-4 gap-6">
          <div
            v-for="(step, index) in processSteps"
            :key="step.title"
            class="text-center"
          >
            <div class="w-14 h-14 bg-accent-600 rounded-full flex items-center justify-center mx-auto mb-4">
              <span class="text-white text-xl font-bold">{{ index + 1 }}</span>
            </div>
            <h3 class="text-lg font-semibold text-steel-900 mb-2">{{ step.title }}</h3>
            <p class="text-steel-500 text-sm leading-relaxed">{{ step.description }}</p>
          </div>
        </div>
      </div>
    </section>

    <!-- CTA Section -->
    <section class="bg-steel-50 py-16 border-t border-steel-200">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
        <h2 class="text-3xl md:text-4xl font-display font-bold text-steel-900 mb-4">
          Partner With Us
        </h2>
        <p class="text-steel-500 text-lg mb-8 max-w-2xl mx-auto">
          Whether you're a distributor looking for reliable supply, a retailer seeking quality products,
          or a business with custom manufacturing needs — we'd like to hear from you.
        </p>
        <div class="flex flex-col sm:flex-row gap-4 justify-center">
          <NuxtLink
            to="/contact"
            class="inline-block bg-accent-600 text-white px-8 py-3 rounded font-semibold hover:bg-accent-700 transition-colors"
          >
            Get in Touch
          </NuxtLink>
          <NuxtLink
            to="/about"
            class="inline-block border-2 border-steel-300 text-steel-700 px-8 py-3 rounded font-semibold hover:border-accent-500 hover:text-accent-600 transition-colors"
          >
            Learn About Us
          </NuxtLink>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup lang="ts">
useHead({
  title: 'PanCraft - Precision Metalworking & Manufacturing',
})

const stats = [
  { value: '30+', label: 'Years of Experience' },
  { value: '2M+', label: 'Units Produced Yearly' },
  { value: '45+', label: 'Countries Served' },
  { value: '200+', label: 'Team Members' },
]

const capabilities = [
  {
    icon: '01',
    title: 'Metal Forging & Casting',
    description: 'Advanced forging and casting techniques for aluminum, stainless steel, cast iron, and low-carbon steel — delivering structural integrity across product lines.',
  },
  {
    icon: '02',
    title: 'Surface Treatment & Coating',
    description: 'Precision coating application — from PFOA-free non-stick for cookware to powder coating and electroplating for radiators and industrial products.',
  },
  {
    icon: '03',
    title: 'Custom & OEM Production',
    description: 'We manufacture under your brand or ours. Full customization of materials, finishes, dimensions, and packaging for both product divisions.',
  },
]

const divisions = [
  {
    title: 'Cookware',
    description: 'Premium frying pans and cookware for professional kitchens and home cooks. Non-stick, stainless steel, cast iron, and ceramic-coated lines.',
    to: '/products/cookware',
  },
  {
    title: 'Heating Radiators',
    description: 'High-efficiency heating radiators for residential and industrial applications. Panel, column, and custom configurations.',
    to: '/products/radiators',
  },
]

const processSteps = [
  {
    title: 'Material Selection',
    description: 'Premium metals sourced from certified suppliers — aluminum, stainless steel, cast iron, and low-carbon steel.',
  },
  {
    title: 'Forming & Shaping',
    description: 'Precision stamping, forging, and welding on our automated production lines.',
  },
  {
    title: 'Finishing & Assembly',
    description: 'Surface treatment, coating application, component assembly, and quality finishing.',
  },
  {
    title: 'Quality Control',
    description: 'Every unit inspected and tested before packaging and shipment.',
  },
]
</script>
