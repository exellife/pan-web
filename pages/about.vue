<template>
  <div>
    <!-- Page Header -->
    <section class="relative bg-steel-50 border-b border-steel-200 py-16 lg:py-24">
      <!-- Background image (thumb on mobile, full on desktop) + readability overlay -->
      <div class="absolute inset-0 bg-cover bg-center bg-no-repeat bg-[url('/images/hero/about-hero-thumb.webp')] lg:bg-[url('/images/hero/about-hero.webp')]">
        <div class="absolute inset-0 bg-gradient-to-r from-white/95 via-white/85 to-white/40" />
      </div>
      <div class="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <p class="text-accent-600 font-semibold text-sm uppercase tracking-widest mb-2">{{ $t('about.eyebrow') }}</p>
        <h1 class="text-4xl md:text-5xl font-display font-bold text-steel-900">
          {{ $t('about.title') }}
        </h1>
        <p class="mt-4 text-lg text-steel-500 max-w-2xl">
          {{ $t('about.subtitle') }}
        </p>
      </div>
    </section>

    <!-- Story Section -->
    <section class="bg-white py-16 lg:py-24">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
          <div>
            <h2 class="text-3xl font-display font-bold text-steel-900 mb-6">{{ $t('about.story.heading') }}</h2>
            <div class="space-y-4 text-steel-600 leading-relaxed">
              <p>{{ $t('about.story.p1') }}</p>
              <p>{{ $t('about.story.p2') }}</p>
              <p>{{ $t('about.story.p3') }}</p>
            </div>
            <!-- Advantage chips -->
            <ul class="mt-6 flex flex-wrap gap-2">
              <li v-for="chip in chips" :key="chip" class="text-xs font-medium text-steel-600 bg-steel-100 border border-steel-200 rounded-full px-3 py-1">
                {{ $t(`about.chips.${chip}`) }}
              </li>
            </ul>
          </div>
          <div class="relative rounded-lg h-80 overflow-hidden border border-steel-200">
            <img
              src="/images/about/factory.webp"
              :alt="$t('about.story.factoryAlt')"
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
          <p class="text-accent-600 font-semibold text-sm uppercase tracking-widest mb-2">{{ $t('about.certs.eyebrow') }}</p>
          <h2 class="text-3xl font-display font-bold text-steel-900">{{ $t('about.certs.heading') }}</h2>
          <p class="mt-4 text-steel-500 max-w-2xl mx-auto">
            {{ $t('about.certs.intro') }}
          </p>
        </div>
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
          <a
            v-for="cert in certifications"
            :key="cert.key"
            :href="cert.image"
            target="_blank"
            rel="noopener"
            class="group flex flex-col bg-white border border-steel-200 rounded-lg overflow-hidden hover:border-accent-400 hover:shadow-lg transition-all"
          >
            <div class="bg-steel-50 p-5 flex items-center justify-center">
              <img
                :src="cert.image"
                :alt="`${$t(`about.certs.items.${cert.key}.name`)} certificate`"
                loading="lazy"
                class="h-72 w-auto max-w-full object-contain shadow-sm ring-1 ring-steel-200 group-hover:scale-[1.02] transition-transform duration-300"
              />
            </div>
            <div class="p-5 border-t border-steel-100 text-center">
              <h3 class="text-steel-900 font-semibold text-sm">{{ $t(`about.certs.items.${cert.key}.name`) }}</h3>
              <p class="text-steel-500 text-xs mt-1">{{ $t(`about.certs.items.${cert.key}.desc`) }}</p>
              <span class="mt-2 inline-block text-accent-600 text-xs font-semibold uppercase tracking-wide">{{ $t('about.certs.view') }} &rarr;</span>
            </div>
          </a>
        </div>
      </div>
    </section>

    <!-- Values Section -->
    <section class="bg-white py-16 lg:py-24">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-12">
          <p class="text-accent-600 font-semibold text-sm uppercase tracking-widest mb-2">{{ $t('about.values.eyebrow') }}</p>
          <h2 class="text-3xl font-display font-bold text-steel-900">{{ $t('about.values.heading') }}</h2>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
          <div
            v-for="value in values"
            :key="value"
            class="bg-steel-50 border border-steel-200 p-8 rounded-lg"
          >
            <h3 class="text-xl font-semibold text-steel-900 mb-3">{{ $t(`about.values.${value}.title`) }}</h3>
            <p class="text-steel-500 leading-relaxed">{{ $t(`about.values.${value}.desc`) }}</p>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup lang="ts">
const { t } = useI18n()
useHead(() => ({
  title: t('about.metaTitle'),
  meta: [{ name: 'description', content: t('about.metaDescription') }],
}))

const chips = ['established', 'fez', 'iso', 'oem']

const certifications = [
  { key: 'iso9001', image: '/images/certificates/cert1_iso9001.webp' },
  { key: 'ohsas', image: '/images/certificates/cert6_ohsms.webp' },
  { key: 'amfori', image: '/images/certificates/cert4_amfori.webp' },
  { key: 'tuvFood', image: '/images/certificates/cert2_tuv.webp' },
  { key: 'tuvFitness', image: '/images/certificates/cert3_tuv.webp' },
  { key: 'testReport', image: '/images/certificates/cert5_wit.webp' },
]

const values = ['quality', 'certified', 'flexible']
</script>
