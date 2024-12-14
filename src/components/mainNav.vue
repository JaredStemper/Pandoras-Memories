<script setup>
import { RouterLink } from "vue-router";

defineProps({
  align: {
    type: String,
    default: 'center'
  }
});
</script>

<template>
  <nav :class="align">
    <RouterLink to="/">Home</RouterLink>
    <RouterLink to="/about">About</RouterLink>
    <RouterLink to="/slideshow">Slideshow</RouterLink>
    <RouterLink to="/song">Song</RouterLink>
  </nav>
</template>

<style scoped>
nav {
  display: flex;
  font-size: 1rem;
  text-align: center;
}

nav.center {
  justify-content: center;
  width: 100%;
}

nav.right {
  justify-content: flex-end;
  min-width: 300px;
}

nav a {
  display: inline-block;
  padding: 0 1rem;
  border-left: 1px solid var(--color-border);
}

nav a:first-child {
  border-left: none;
}

nav a.router-link-active {
  color: var(--color-text);
}

@media (max-width: 1024px) {
  nav {
    font-size: 12px;
    margin-top: 1rem;
  }
  
  nav.right {
    width: 100%;
    min-width: unset;
  }
}
</style> 