<template>
  <div>
    <!-- Page Header -->
    <section class="bg-steel-50 py-16 lg:py-24 border-b border-steel-200">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <p class="text-accent-600 font-semibold text-sm uppercase tracking-widest mb-2">Contact</p>
        <h1 class="text-4xl md:text-5xl font-display font-bold text-steel-900">Get in Touch</h1>
        <p class="mt-4 text-lg text-steel-500 max-w-2xl">
          Whether you're a distributor, retailer, or individual buyer — we're ready to discuss
          your requirements.
        </p>
      </div>
    </section>

    <!-- Contact Section -->
    <section class="bg-white py-16 lg:py-24">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-12">
          <!-- Contact Form -->
          <div>
            <h2 class="text-2xl font-display font-bold text-steel-900 mb-6">Send Us an Inquiry</h2>
            <form @submit.prevent="handleSubmit" class="space-y-6">
              <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                <div>
                  <label for="name" class="block text-sm font-medium text-steel-700 mb-1">Name</label>
                  <input
                    id="name"
                    v-model="form.name"
                    type="text"
                    required
                    class="w-full px-4 py-2 bg-white border border-steel-300 rounded text-steel-900 placeholder-steel-400 focus:ring-2 focus:ring-accent-500 focus:border-accent-500 outline-none transition-colors"
                    placeholder="Your name"
                  />
                </div>
                <div>
                  <label for="company" class="block text-sm font-medium text-steel-700 mb-1">Company</label>
                  <input
                    id="company"
                    v-model="form.company"
                    type="text"
                    class="w-full px-4 py-2 bg-white border border-steel-300 rounded text-steel-900 placeholder-steel-400 focus:ring-2 focus:ring-accent-500 focus:border-accent-500 outline-none transition-colors"
                    placeholder="Company name (optional)"
                  />
                </div>
              </div>
              <div>
                <label for="email" class="block text-sm font-medium text-steel-700 mb-1">Email</label>
                <input
                  id="email"
                  v-model="form.email"
                  type="email"
                  required
                  class="w-full px-4 py-2 bg-white border border-steel-300 rounded text-steel-900 placeholder-steel-400 focus:ring-2 focus:ring-accent-500 focus:border-accent-500 outline-none transition-colors"
                  placeholder="you@example.com"
                />
              </div>
              <div>
                <label for="inquiry" class="block text-sm font-medium text-steel-700 mb-1">Inquiry Type</label>
                <select
                  id="inquiry"
                  v-model="form.inquiryType"
                  class="w-full px-4 py-2 bg-white border border-steel-300 rounded text-steel-900 focus:ring-2 focus:ring-accent-500 focus:border-accent-500 outline-none transition-colors"
                >
                  <option value="wholesale">Wholesale / Distribution</option>
                  <option value="oem">OEM / Custom Manufacturing</option>
                  <option value="retail">Retail Partnership</option>
                  <option value="consumer">Individual Purchase</option>
                  <option value="other">Other</option>
                </select>
              </div>
              <div>
                <label for="message" class="block text-sm font-medium text-steel-700 mb-1">Message</label>
                <textarea
                  id="message"
                  v-model="form.message"
                  rows="5"
                  required
                  class="w-full px-4 py-2 bg-white border border-steel-300 rounded text-steel-900 placeholder-steel-400 focus:ring-2 focus:ring-accent-500 focus:border-accent-500 outline-none transition-colors resize-vertical"
                  placeholder="Tell us about your requirements..."
                />
              </div>
              <button
                type="submit"
                class="bg-accent-600 text-white px-8 py-3 rounded font-semibold hover:bg-accent-700 transition-colors"
              >
                Submit Inquiry
              </button>
            </form>
          </div>

          <!-- Contact Info -->
          <div>
            <h2 class="text-2xl font-display font-bold text-steel-900 mb-6">Factory & Office</h2>
            <div class="space-y-6">
              <div v-for="info in contactInfo" :key="info.label">
                <h3 class="font-semibold text-steel-900 text-sm uppercase tracking-wide">{{ info.label }}</h3>
                <p class="text-steel-600 mt-1">{{ info.value }}</p>
              </div>
            </div>

            <!-- Map placeholder -->
            <div class="mt-8 bg-steel-100 border border-steel-200 rounded-lg h-64 flex items-center justify-center">
              <span class="text-steel-400">[Map placeholder]</span>
            </div>

            <div class="mt-8 bg-steel-50 border border-steel-200 rounded-lg p-6">
              <h3 class="font-semibold text-steel-900 text-sm uppercase tracking-wide mb-3">For Wholesale Inquiries</h3>
              <p class="text-steel-500 text-sm leading-relaxed">
                Minimum order quantities start at 500 units per SKU.
                For OEM/white-label orders, minimum is 1,000 units.
                Lead times typically range from 4-8 weeks depending on specifications.
              </p>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup lang="ts">
useHead({
  title: 'Contact - TanDem Manufacturing',
  meta: [
    { name: 'description', content: 'Contact TanDem for wholesale, OEM, retail partnerships, or individual purchases. Request a quote today.' },
  ],
})

const form = reactive({
  name: '',
  company: '',
  email: '',
  inquiryType: 'wholesale',
  message: '',
})

const contactInfo = [
  { label: 'Address', value: '1/55, Free Economic Zone "Bishkek", Bishkek, Kyrgyzstan' },
  { label: 'Phone', value: '+996 312 90 00 00' },
  { label: 'Email', value: 'info@tandem.kg' },
  { label: 'Sales Department', value: 'sales@tandem.kg' },
  { label: 'Business Hours', value: 'Monday - Friday, 9:00 AM - 6:00 PM' },
]

function handleSubmit() {
  alert('Thank you for your inquiry! Our team will respond within 1-2 business days.')
  form.name = ''
  form.company = ''
  form.email = ''
  form.inquiryType = 'wholesale'
  form.message = ''
}
</script>
