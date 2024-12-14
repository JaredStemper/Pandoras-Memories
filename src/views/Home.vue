<script setup>
import siteTitle from "@/components/siteTitle.vue";
import TheWelcome from "@/components/TheWelcome.vue";
import LogoSVG from "@/assets/evil-eye.svg";
import { RouterLink } from "vue-router";
</script>

<template>
  <div class="split-container">
    <div class="left-pane">
      <LogoSVG class="large-logo" alt="Greek Eye logo" />
    </div>
    <div class="right-pane">
      <div class="header-section">
        <siteTitle :large="true" :showLogo="false" />
      </div>
      <TheWelcome />
    </div>
  </div>
</template>

<style scoped>
.split-container {
  display: flex;
  min-height: 80vh;
  width: 100%;
  gap: 2rem;
}

.left-pane {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 2rem;
}

.right-pane {
  flex: 1;
  display: flex;
  flex-direction: column;
  padding: 2rem;
  overflow-y: auto;
}

.large-logo {
  width: 100%;
  height: auto;
  max-width: 500px;
}

.title {
  font-size: 2.5rem;
  color: var(--color-heading);
  margin-bottom: 2rem;
  text-align: center;
}

.header-section {
  margin-bottom: 2rem;
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
}

nav {
  width: 100%;
  font-size: 12px;
  text-align: center;
  margin-top: 1rem;
}

nav a {
  display: inline-block;
  padding: 0 1rem;
  border-left: 1px solid var(--color-border);
}

nav a:first-of-type {
  border: 0;
}

nav a.router-link-exact-active {
  color: var(--color-text);
}

nav a.router-link-exact-active:hover {
  background-color: transparent;
}

@media (min-width: 1024px) {
  nav {
    text-align: center;
    font-size: 1rem;
    padding: 1rem 0;
  }
}

@media (max-width: 1024px) {
  .split-container {
    flex-direction: column;
  }
  
  .left-pane, .right-pane {
    width: 100%;
  }
}
</style>
