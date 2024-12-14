<script setup>
import LogoSVG from "@/assets/evil-eye.svg";

defineProps({
  showLogo: {
    type: Boolean,
    default: true
  },
  large: {
    type: Boolean,
    default: false
  }
});
</script>

<template>
  <div class="logo-section">
    <LogoSVG v-if="showLogo" class="header-logo" alt="Greek Eye logo" />
    <router-link to="/">
      <h1 class="title green" :class="{ 'title-large': large }">Pandora's Memories</h1>
    </router-link>
  </div>
</template>

<style scoped>
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

.title-large {
  font-size: 3rem;
}

@media (max-width: 1024px) {
  .title-large {
    font-size: 2.5rem;
  }
}
</style> 