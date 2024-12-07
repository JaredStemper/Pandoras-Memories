<script setup>
import Slideshow from "@/components/Slideshow.vue";
import PageHeader from "@/components/PageHeader.vue";
</script>

<template>
  <div class="slideshow-view">
    <PageHeader />
    <main>
      <Slideshow />
    </main>
  </div>
</template>

<style scoped>
.slideshow-view {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

main {
  flex: 1;
  display: flex;
}
</style>