<script setup>
import { RouterLink, RouterView } from "vue-router";
import HelloWorld from "./components/HelloWorld.vue";
import LogoSVG from "./assets/evil-eye.svg";
// import LogoSVG from "./assets/logo.svg";
</script>

<template>
  <header>
    <LogoSVG alt="Greek Eye logo" class="logo" />

    <div class="wrapper">
      <HelloWorld msg="Pandora's Memories" />
      <!-- <HelloWorld msg="Slideshow Website" /> -->

      <nav>
        <RouterLink to="/">Home</RouterLink>
        <RouterLink to="/about">About</RouterLink>
        <RouterLink to="/slideshow">Slideshow</RouterLink>
      </nav>
    </div>
  </header>
  <br />

  <RouterView />
</template>

<style scoped>
[id='app'] * {
  /* width: 100%; */
  max-width: 100%;
  /* max-height: 100vh; */
  /* min-height: 0; */
  min-width: 0;
  /* swiper library bug
    commented out are other fixes potentially necessary with this issue seen in the swiper github
    https://github.com/nolimits4web/swiper/issues/3599
  */
}
header {
  line-height: 1.5;
  max-height: 100vh;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

nav {
  width: 100%;
  font-size: 12px;
  text-align: center;
  margin-top: 2rem;
}

nav a.router-link-exact-active {
  color: var(--color-text);
}

nav a.router-link-exact-active:hover {
  background-color: transparent;
}

nav a {
  display: inline-block;
  padding: 0 1rem;
  border-left: 1px solid var(--color-border);
}

nav a:first-of-type {
  border: 0;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }

  nav {
    text-align: left;
    margin-left: -1rem;
    font-size: 1rem;

    padding: 1rem 0;
    margin-top: 1rem;
  }
}
</style>
