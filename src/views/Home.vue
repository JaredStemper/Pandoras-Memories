<script setup>
import TheWelcome from "@/components/TheWelcome.vue";
import LogoSVG from "@/assets/evil-eye.svg?component";
import SiteTitle from "@/components/SiteTitle.vue";
import MainNav from "@/components/MainNav.vue";
</script>

<template>
  <div class="split-container">
    <div class="left-pane">
      <LogoSVG class="large-logo" alt="Greek Eye logo" />
    </div>
    <div class="right-pane">
      <div class="header-section">
        <SiteTitle :showLogo="false" :large="true" />
        <MainNav align="center" />
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

@media (max-width: 1024px) {
  .split-container {
    flex-direction: column;
  }
  
  .left-pane, .right-pane {
    width: 100%;
  }
}
</style>
