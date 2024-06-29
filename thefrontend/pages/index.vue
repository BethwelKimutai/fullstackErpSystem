<template>
    <div>
        <Hero />
        <Features />
        <Portfolio />
        <Pricing />
        <!-- <About /> -->
         <Contact />
         <Footer />
        
    </div>
</template>

<script>
import Hero from '/components/Hero.vue';
import Pricing from '/components/Pricing.vue';
import Portfolio from '/components/Portfolio/Portfolio.vue';
import About from '/components/About.vue';
import Contact from '/components/Contact.vue';
import Footer from '/components/Footer.vue';
import Features from '/components/Features.vue';

export default {
    components: {
        Hero,
        Pricing,
        Portfolio,
        Contact,
        About,
        Footer,
        Features
    }
};
</script>

<style scoped></style>