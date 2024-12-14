<script setup>
import LogoSVG from "@/assets/evil-eye.svg";
import mainNav from "@/components/mainNav.vue";

const props = defineProps({
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
  <div class="site-header">
    <div class="header-content">
      <div class="logo-section">
        <LogoSVG v-if="props.showLogo" class="header-logo" alt="Greek Eye logo" />
        <router-link to="/">
          <h1 class="title green" :class="{ 'title-large': props.large }">Pandora's Memories</h1>
        </router-link>
      </div>
      <mainNav align="center" />
    </div>
  </div>
</template>

<style scoped>
.site-header {
  width: 100%;
}

.header-content {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1rem;
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

.title-large {
  font-size: 3rem;
}

@media (max-width: 1024px) {
  .title-large {
    font-size: 2.5rem;
  }
}
</style> 