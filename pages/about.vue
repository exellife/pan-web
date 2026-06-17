<template>
  <div>
    <!-- Page Header -->
    <section class="relative bg-steel-50 border-b border-steel-200 py-16 lg:py-24">
      <!-- Background image (thumb on mobile, full on desktop) + readability overlay -->
      <div class="absolute inset-0 bg-cover bg-center bg-no-repeat bg-[url('/images/hero/about-hero-thumb.webp')] lg:bg-[url('/images/hero/about-hero.webp')]">
        <div class="absolute inset-0 bg-gradient-to-r from-white/95 via-white/85 to-white/40" />
      </div>
      <div class="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <p class="text-accent-600 font-semibold text-sm uppercase tracking-widest mb-2">About Us</p>
        <h1 class="text-4xl md:text-5xl font-display font-bold text-steel-900">
          Cookware and Heating, Made to Last
        </h1>
        <p class="mt-4 text-lg text-steel-500 max-w-2xl">
          Quality cookware and heating, serving clients across
          Central Asia, Russia, and Europe.
        </p>
      </div>
    </section>

    <!-- Story Section -->
    <section class="bg-white py-16 lg:py-24">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
          <div>
            <h2 class="text-3xl font-display font-bold text-steel-900 mb-6">Who We Are</h2>
            <div class="space-y-4 text-steel-600 leading-relaxed">
              <p>
                Established in 2017, TanDem LLC is a metalworking manufacturer and part of the
                international TMAI group. We produce two core lines — premium cookware and
                central-heating radiators and boilers — for distributors, retailers, and consumers.
              </p>
              <p>
                Our manufacturing facility is based in Kyrgyzstan's Free Economic Zone &ldquo;Bishkek&rdquo; —
                an ideal gateway location from which we ship to partners across Central Asia, Russia, and Europe.
              </p>
              <p>
                Backed by the group's expertise in metal forging, casting, and surface treatment, we pair
                advanced machinery with skilled craftsmanship and manufacture to internationally certified
                standards — under our own brand or yours, with full OEM and custom production.
              </p>
            </div>
            <!-- Advantage chips -->
            <ul class="mt-6 flex flex-wrap gap-2">
              <li v-for="chip in advantages" :key="chip" class="text-xs font-medium text-steel-600 bg-steel-100 border border-steel-200 rounded-full px-3 py-1">
                {{ chip }}
              </li>
            </ul>
          </div>
          <div class="relative rounded-lg h-80 overflow-hidden border border-steel-200">
            <img
              src="/images/about/factory.webp"
              alt="TanDem manufacturing facility in Bishkek"
              loading="lazy"
              class="w-full h-full object-cover"
            />
            <!-- Scrim -->
            <div class="absolute inset-0 bg-gradient-to-t from-steel-900/45 via-steel-900/10 to-transparent" />
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
          <p class="mt-4 text-steel-500 max-w-2xl mx-auto">
            Our products are manufactured to the internationally recognized standards held
            across the TMAI group — independently audited and tested. Click any certificate to view it in full.
          </p>
        </div>
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
          <a
            v-for="cert in certifications"
            :key="cert.name"
            :href="cert.image"
            target="_blank"
            rel="noopener"
            class="group flex flex-col bg-white border border-steel-200 rounded-lg overflow-hidden hover:border-accent-400 hover:shadow-lg transition-all"
          >
            <div class="bg-steel-50 p-5 flex items-center justify-center">
              <img
                :src="cert.image"
                :alt="`${cert.name} certificate`"
                loading="lazy"
                class="h-72 w-auto max-w-full object-contain shadow-sm ring-1 ring-steel-200 group-hover:scale-[1.02] transition-transform duration-300"
              />
            </div>
            <div class="p-5 border-t border-steel-100 text-center">
              <h3 class="text-steel-900 font-semibold text-sm">{{ cert.name }}</h3>
              <p class="text-steel-500 text-xs mt-1">{{ cert.description }}</p>
              <span class="mt-2 inline-block text-accent-600 text-xs font-semibold uppercase tracking-wide">View certificate &rarr;</span>
            </div>
          </a>
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
  title: 'About Us - TanDem Manufacturing',
  meta: [
    { name: 'description', content: 'Learn about TanDem — the Bishkek, Kyrgyzstan manufacturing arm of the international TMAI group, producing premium cookware and heating radiators to certified standards.' },
  ],
})

const advantages = [
  'Established 2017',
  'Free Economic Zone "Bishkek"',
  'ISO 9001 certified',
  'OEM / white-label',
]

const certifications = [
  { image: '/images/certificates/cert1_iso9001.webp', name: 'ISO 9001:2015', description: 'Quality Management System' },
  { image: '/images/certificates/cert6_ohsms.webp', name: 'OHSAS 18001:2007', description: 'Occupational Health & Safety Management' },
  { image: '/images/certificates/cert4_amfori.webp', name: 'amfori BSCI', description: 'Social Compliance Audit' },
  { image: '/images/certificates/cert2_tuv.webp', name: 'TÜV Rheinland', description: 'Food-Contact Safety Test (LFGB)' },
  { image: '/images/certificates/cert3_tuv.webp', name: 'TÜV Rheinland', description: 'Cookware Fitness-for-Use Test (DIN 44904)' },
  { image: '/images/certificates/cert5_wit.webp', name: 'Product Test Report', description: 'Independent Consumer-Product Testing' },
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
