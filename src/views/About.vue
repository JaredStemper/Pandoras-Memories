<script setup>
import PageHeader from "@/components/PageHeader.vue";
</script>

<template>
  <div class="about">
    <PageHeader />
    <div class="about-content">
      <h1>About Pandora's Memories</h1>
      
      <div class="story-section">
        <h2>The Origin Story</h2>
        <p>
          It all started with a curious toddler and a small memory box. This box was special - it had four pictures on its sides and a magical button that, when pressed, played back the voices of my two sisters singing "You Are My Sunshine." Like any inquisitive child, I discovered a small recording button on the bottom. Without much thought, I recorded over my sisters' singing with an assortment of weird noises, heavy breathing, and what I'm sure I thought were hilarious sounds at the time.
        </p>
        
        <p>
          While the original box is long gone, its memory has stayed with me through the years. This project is my attempt to recreate that box - but with a special twist. This time, when you open Pandora's Memories, nothing leaves except the time you spend with it.
        </p>
      </div>

      <div class="features-section">
        <h2>Features</h2>
        <ul>
          <li>Interactive slideshow of family photos and videos</li>
          <li>Special "You Are My Sunshine" mode featuring individual family member recordings</li>
          <li>Four LCD panels rotating through memory folders</li>
          <li>Integration with both local storage and Google Photos Drive</li>
        </ul>
      </div>

      <div class="dedication">
        <p>Love ya mum! ❤️</p>
      </div>
    </div>
  </div>
</template>

<style lang="scss">
.about {
  @apply lg:min-h-screen;

  .about-content {
    @apply max-w-3xl mx-auto p-8 mt-8;

    h1 {
      @apply text-3xl font-bold text-white mb-8 text-center;
    }

    h2 {
      @apply text-xl font-semibold text-white mb-4 mt-8;
    }

    .story-section, .features-section {
      @apply mb-8;

      p {
        @apply text-gray-300 mb-4 leading-relaxed;
      }
    }

    .features-section {
      ul {
        @apply list-disc list-inside text-gray-300 space-y-2;
      }
    }

    .dedication {
      @apply text-center mt-12 text-xl text-white font-medium italic;
    }
  }
}
</style>
