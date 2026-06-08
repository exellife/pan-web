<template>
  <div>
    <!-- Page Header -->
    <section class="bg-steel-50 py-16 lg:py-24 border-b border-steel-200">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <p class="text-accent-600 font-semibold text-sm uppercase tracking-widest mb-2">About Us</p>
        <h1 class="text-4xl md:text-5xl font-display font-bold text-steel-900">
          Three Decades of Manufacturing Excellence
        </h1>
        <p class="mt-4 text-lg text-steel-500 max-w-2xl">
          From a small workshop to a modern production facility, our commitment to quality has never changed.
        </p>
      </div>
    </section>

    <!-- Story Section -->
    <section class="bg-white py-16 lg:py-24">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
          <div>
            <h2 class="text-3xl font-display font-bold text-steel-900 mb-6">Our Story</h2>
            <div class="space-y-4 text-steel-600 leading-relaxed">
              <p>
                Founded in 1995, PanCraft began as a small metalworking workshop with a clear vision:
                to manufacture products that professionals and consumers could rely on every day.
              </p>
              <p>
                What started with cookware quickly expanded into heating solutions as our expertise
                in metal forging, casting, and surface treatment grew. Over three decades, we invested
                in advanced equipment, built a team of experienced engineers and metalworkers, and
                expanded our production capacity to over 2 million units per year. Our facility now
                spans 15,000 square meters.
              </p>
              <p>
                Today, we serve distributors and retailers in over 45 countries with two core product
                lines — premium cookware and high-efficiency heating radiators — while also offering
                custom manufacturing for businesses with specific requirements.
              </p>
            </div>
          </div>
          <div class="bg-steel-100 border border-steel-200 rounded-lg h-80 flex items-center justify-center">
            <span class="text-steel-400 text-lg">[Factory photo placeholder]</span>
          </div>
        </div>
      </div>
    </section>

    <!-- Certifications -->
    <section class="bg-steel-50 py-16 lg:py-24 border-y border-steel-200">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-12">
          <p class="text-accent-600 font-semibold text-sm uppercase tracking-widest mb-2">Standards</p>
          <h2 class="text-3xl font-display font-bold text-steel-900">Certifications & Compliance</h2>
        </div>
        <div class="grid grid-cols-2 md:grid-cols-4 gap-6">
          <div
            v-for="cert in certifications"
            :key="cert.name"
            class="bg-white border border-steel-200 rounded-lg p-6 text-center"
          >
            <div class="text-accent-600 text-2xl font-bold mb-2">{{ cert.icon }}</div>
            <h3 class="text-steel-900 font-semibold text-sm">{{ cert.name }}</h3>
            <p class="text-steel-400 text-xs mt-1">{{ cert.description }}</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Values Section -->
    <section class="bg-white py-16 lg:py-24">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-12">
          <p class="text-accent-600 font-semibold text-sm uppercase tracking-widest mb-2">Our Principles</p>
          <h2 class="text-3xl font-display font-bold text-steel-900">What Drives Us</h2>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
          <div
            v-for="value in values"
            :key="value.title"
            class="bg-steel-50 border border-steel-200 p-8 rounded-lg"
          >
            <h3 class="text-xl font-semibold text-steel-900 mb-3">{{ value.title }}</h3>
            <p class="text-steel-500 leading-relaxed">{{ value.description }}</p>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup lang="ts">
useHead({
  title: 'About Us - PanCraft Manufacturing',
  meta: [
    { name: 'description', content: 'Learn about PanCraft\'s 30-year history of precision metalworking — manufacturing premium cookware and heating radiators.' },
  ],
})

const certifications = [
  { icon: 'ISO', name: 'ISO 9001:2015', description: 'Quality Management' },
  { icon: 'CE', name: 'CE Marking', description: 'European Conformity' },
  { icon: 'EN', name: 'EN 442 Certified', description: 'Radiator Standards' },
  { icon: 'SGS', name: 'SGS Tested', description: 'Independent Testing' },
]

const values = [
  {
    title: 'Quality Without Compromise',
    description: 'Every product passes rigorous multi-point inspection. We test for structural integrity, surface finish, dimensional accuracy, and performance before any unit leaves our facility.',
  },
  {
    title: 'Sustainable Manufacturing',
    description: 'Our production processes minimize waste and energy consumption. We use recycled metals where possible and our coatings and finishes meet the latest environmental standards.',
  },
  {
    title: 'Continuous Innovation',
    description: 'Our R&D team works on next-generation materials and manufacturing techniques. We invest in new tooling and processes to stay ahead of industry standards across both product divisions.',
  },
]
</script>
