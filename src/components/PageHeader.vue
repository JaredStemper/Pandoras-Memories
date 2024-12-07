<script setup>
import LogoSVG from "@/assets/evil-eye.svg";
import { RouterLink } from "vue-router";
</script>

<template>
  <header class="page-header">
    <div class="logo-section">
      <LogoSVG class="header-logo" alt="Greek Eye logo" />
      <h1 class="title green">Pandora's Memories</h1>
    </div>
    <nav>
      <RouterLink to="/">Home</RouterLink>
      <RouterLink to="/about">About</RouterLink>
      <RouterLink to="/slideshow">Slideshow</RouterLink>
    </nav>
  </header>
</template>

<style scoped>
.page-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 1rem 2rem;
  width: 100%;
}

.logo-section {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.header-logo {
  width: 75px;
  height: auto;
}

.title {
  font-size: 2rem;
}

nav {
  display: flex;
  justify-content: center;
  font-size: 1rem;
  text-align: center;
  margin-left: auto;
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
</style> 