<script setup>
import PageHeader from "@/components/PageHeader.vue";
</script>

<template>
  <div class="song-view">
    <PageHeader />
    <main>
      <div class="song-container">
        <h1>You Are <u>Our</u> Sunshine</h1>
        <div class="video-wrapper">
          <video
            ref="videoPlayer"
            class="main-video"
            controls
            :src="videoSrc"
            poster="/src/assets/video-poster.jpg"
          ></video>
        </div>
        <div class="description">
          <p>
            A special rendition of "You Are My Sunshine" featuring our family members,
            each singing their part separately but coming together in (almost) perfect harmony.
            Just like the original memory box, but this time the recording is here to stay.
          </p>
        </div>
      </div>
    </main>
  </div>
</template>

<style scoped>
.song-view {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

main {
  flex: 1;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 2rem;
}

.song-container {
  max-width: 1200px;
  width: 100%;
  text-align: center;
}

h1 {
  font-size: 2.5rem;
  color: var(--color-heading);
  margin-bottom: 2rem;
}

.video-wrapper {
  position: relative;
  padding-top: 56.25%; /* 16:9 Aspect Ratio */
  background-color: rgba(0, 0, 0, 0.2);
  border-radius: 8px;
  overflow: hidden;
  margin-bottom: 2rem;
}

.main-video {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: contain;
}

.description {
  max-width: 800px;
  margin: 0 auto;
  padding: 1rem;
}

.description p {
  color: var(--color-text);
  line-height: 1.6;
  font-size: 1.1rem;
}

@media (max-width: 768px) {
  main {
    padding: 1rem;
  }

  h1 {
    font-size: 2rem;
  }

  .description p {
    font-size: 1rem;
  }
}
</style>