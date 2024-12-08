<script setup>
import SiteTitle from "./SiteTitle.vue";
import MainNav from "./MainNav.vue";
</script>

<template>
  <header class="page-header">
    <SiteTitle />
    <MainNav align="right" />
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
</style> 