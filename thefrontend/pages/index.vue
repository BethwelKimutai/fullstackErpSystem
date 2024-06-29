<template>
    <div>
        <Hero />
        <Portfolio />
        <Pricing />
        <!-- <About /> -->
         <Contact />
        
    </div>
</template>

<script>
import Hero from '/components/Hero.vue';
import Pricing from '/components/Pricing.vue';
import Portfolio from '/components/Portfolio/Portfolio.vue';
import About from '/components/About.vue';
import Contact from '/components/Contact.vue';

export default {
    components: {
        Hero,
        Pricing,
        Portfolio,
        Contact,
        About
    }
};
</script>

<style scoped></style>