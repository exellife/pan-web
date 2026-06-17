<template>
  <div>
    <!-- Hero Section -->
    <section class="relative bg-steel-50 py-24 lg:py-36 overflow-hidden">
      <div class="absolute inset-0 bg-cover bg-center bg-no-repeat bg-[url('/images/hero/home-hero-thumb.webp')] lg:bg-[url('/images/hero/home-hero.webp')]">
        <div class="absolute inset-0 bg-gradient-to-r from-white/95 via-white/80 to-white/40" />
      </div>
      <div class="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="max-w-3xl">
          <p class="text-accent-600 font-semibold text-sm uppercase tracking-widest mb-4">
            {{ $t('home.hero.eyebrow') }}
          </p>
          <i18n-t
            keypath="home.hero.title"
            tag="h1"
            class="text-4xl md:text-5xl lg:text-6xl font-display font-bold text-steel-900 leading-tight"
          >
            <template #w1><span class="text-accent-600">{{ $t('home.hero.word1') }}</span></template>
            <template #w2><span class="text-accent-600">{{ $t('home.hero.word2') }}</span></template>
          </i18n-t>
          <p class="mt-6 text-lg md:text-xl text-steel-600 leading-relaxed">
            {{ $t('home.hero.lead') }}
          </p>
          <div class="mt-8 flex flex-col sm:flex-row gap-4">
            <NuxtLinkLocale
              to="/products"
              class="inline-block bg-accent-600 text-white px-8 py-3 rounded font-semibold hover:bg-accent-700 transition-colors text-center"
            >
              {{ $t('home.hero.ctaExplore') }}
            </NuxtLinkLocale>
            <NuxtLinkLocale
              to="/contact"
              class="inline-block border-2 border-steel-300 text-steel-700 px-8 py-3 rounded font-semibold hover:border-accent-500 hover:text-accent-600 transition-colors text-center"
            >
              {{ $t('home.hero.ctaQuote') }}
            </NuxtLinkLocale>
          </div>
        </div>
      </div>
    </section>

    <!-- Stats Bar -->
    <section class="bg-white border-y border-steel-200">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        <div class="grid grid-cols-2 md:grid-cols-4 gap-8 text-center">
          <div v-for="stat in stats" :key="stat.key">
            <div class="text-3xl md:text-4xl font-bold text-accent-600">{{ stat.value }}</div>
            <div class="text-steel-500 text-sm mt-1 uppercase tracking-wide">{{ $t(`home.stats.${stat.key}`) }}</div>
          </div>
        </div>
      </div>
    </section>

    <!-- Capabilities Section -->
    <section class="bg-white py-16 lg:py-24">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-12">
          <p class="text-accent-600 font-semibold text-sm uppercase tracking-widest mb-2">{{ $t('home.capabilities.eyebrow') }}</p>
          <h2 class="text-3xl md:text-4xl font-display font-bold text-steel-900">
            {{ $t('home.capabilities.heading') }}
          </h2>
          <p class="mt-4 text-lg text-steel-500 max-w-2xl mx-auto">
            {{ $t('home.capabilities.lead') }}
          </p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
          <div
            v-for="capability in capabilities"
            :key="capability.key"
            class="p-8 rounded-lg bg-steel-50 border border-steel-200 hover:border-accent-400 transition-colors"
          >
            <div class="w-12 h-12 bg-accent-100 rounded-lg flex items-center justify-center mb-4">
              <span class="text-accent-600 text-xl font-bold">{{ capability.icon }}</span>
            </div>
            <h3 class="text-xl font-semibold text-steel-900 mb-2">{{ $t(`home.capabilities.${capability.key}.title`) }}</h3>
            <p class="text-steel-500 leading-relaxed">{{ $t(`home.capabilities.${capability.key}.desc`) }}</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Product Divisions -->
    <section class="bg-steel-50 py-16 lg:py-24 border-y border-steel-200">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-12">
          <p class="text-accent-600 font-semibold text-sm uppercase tracking-widest mb-2">{{ $t('home.divisions.eyebrow') }}</p>
          <h2 class="text-3xl md:text-4xl font-display font-bold text-steel-900">
            {{ $t('home.divisions.heading') }}
          </h2>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
          <NuxtLinkLocale
            v-for="division in divisions"
            :key="division.key"
            :to="division.to"
            class="group flex flex-col bg-white border border-steel-200 rounded-lg overflow-hidden hover:border-accent-400 transition-colors"
          >
            <div class="h-48 flex items-center justify-center p-6 bg-[radial-gradient(circle_at_50%_38%,#ffffff,#eceae7_70%,#e2dfdb)]">
              <img :src="division.image" :alt="$t(`home.divisions.${division.key}.title`)" loading="lazy" class="max-h-full max-w-full object-contain drop-shadow-lg transition-transform duration-300 group-hover:scale-105" />
            </div>
            <div class="p-8 flex flex-col flex-1">
              <h3 class="text-2xl font-display font-bold text-steel-900 mb-3 group-hover:text-accent-600 transition-colors">
                {{ $t(`home.divisions.${division.key}.title`) }}
              </h3>
              <p class="text-steel-500 leading-relaxed mb-4">{{ $t(`home.divisions.${division.key}.desc`) }}</p>
              <span class="mt-auto self-end text-accent-600 font-semibold text-sm uppercase tracking-wide">
                {{ $t('home.divisions.viewProducts') }} &rarr;
              </span>
            </div>
          </NuxtLinkLocale>
        </div>
      </div>
    </section>

    <!-- Process Section -->
    <section class="bg-white py-16 lg:py-24">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-12">
          <p class="text-accent-600 font-semibold text-sm uppercase tracking-widest mb-2">{{ $t('home.process.eyebrow') }}</p>
          <h2 class="text-3xl md:text-4xl font-display font-bold text-steel-900">
            {{ $t('home.process.heading') }}
          </h2>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-4 gap-6">
          <div
            v-for="(step, index) in processSteps"
            :key="step.key"
            class="text-center"
          >
            <div class="w-14 h-14 bg-accent-600 rounded-full flex items-center justify-center mx-auto mb-4">
              <span class="text-white text-xl font-bold">{{ index + 1 }}</span>
            </div>
            <h3 class="text-lg font-semibold text-steel-900 mb-2">{{ $t(`home.process.${step.key}.title`) }}</h3>
            <p class="text-steel-500 text-sm leading-relaxed">{{ $t(`home.process.${step.key}.desc`) }}</p>
          </div>
        </div>
      </div>
    </section>

    <!-- CTA Section -->
    <section class="bg-steel-50 py-16 border-t border-steel-200">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
        <h2 class="text-3xl md:text-4xl font-display font-bold text-steel-900 mb-4">
          {{ $t('home.cta.heading') }}
        </h2>
        <p class="text-steel-500 text-lg mb-8 max-w-2xl mx-auto">
          {{ $t('home.cta.lead') }}
        </p>
        <div class="flex flex-col sm:flex-row gap-4 justify-center">
          <NuxtLinkLocale
            to="/contact"
            class="inline-block bg-accent-600 text-white px-8 py-3 rounded font-semibold hover:bg-accent-700 transition-colors"
          >
            {{ $t('home.cta.getInTouch') }}
          </NuxtLinkLocale>
          <NuxtLinkLocale
            to="/about"
            class="inline-block border-2 border-steel-300 text-steel-700 px-8 py-3 rounded font-semibold hover:border-accent-500 hover:text-accent-600 transition-colors"
          >
            {{ $t('home.cta.learnAbout') }}
          </NuxtLinkLocale>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup lang="ts">
const { t } = useI18n()
useHead(() => ({ title: t('home.metaTitle') }))

const yearsOnMarket = new Date().getFullYear() - 2017

const stats = [
  { value: `${yearsOnMarket}+`, key: 'years' },
  { value: '2', key: 'divisions' },
  { value: 'TMAI', key: 'group' },
  { value: 'ISO 9001', key: 'certified' },
]

const capabilities = [
  { icon: '01', key: 'casting' },
  { icon: '02', key: 'coating' },
  { icon: '03', key: 'oem' },
]

const divisions = [
  { key: 'cookware', to: '/products/cookware', image: '/images/products/cookware/thumb/p02_25.webp' },
  { key: 'radiators', to: '/products/radiators', image: '/images/products/radiators/full/p04_q4.webp' },
]

const processSteps = [
  { key: 'material' },
  { key: 'forming' },
  { key: 'finishing' },
  { key: 'qc' },
]
</script>
