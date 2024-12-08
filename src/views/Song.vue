<script setup>
import PageHeader from "@/components/PageHeader.vue";
import { ref, onMounted } from 'vue';

const videoPlayer = ref(null);
const videoLoaded = ref(false);
const videoError = ref(false);
const videoSrc = ref('/videos/riksrisk.mp4');
const videoState = ref('');

const handleVideoError = (error) => {
  console.error('Error playing video:', error);
  videoError.value = true;
};

const handleVideoLoaded = () => {
  videoLoaded.value = true;
  console.log('Video loaded successfully');
};

const handleVideoStateChange = () => {
  if (videoPlayer.value) {
    videoState.value = {
      readyState: videoPlayer.value.readyState,
      networkState: videoPlayer.value.networkState,
      currentTime: videoPlayer.value.currentTime,
      duration: videoPlayer.value.duration,
      paused: videoPlayer.value.paused,
      ended: videoPlayer.value.ended,
    };
    console.log('Video state:', videoState.value);
  }
};

onMounted(() => {
  if (videoPlayer.value) {
    videoPlayer.value.addEventListener('error', handleVideoError);
    videoPlayer.value.addEventListener('loadeddata', handleVideoLoaded);
    videoPlayer.value.addEventListener('loadedmetadata', () => console.log('Metadata loaded'));
    videoPlayer.value.addEventListener('play', () => console.log('Video started playing'));
    videoPlayer.value.addEventListener('pause', () => console.log('Video paused'));
    videoPlayer.value.addEventListener('timeupdate', handleVideoStateChange);
    
    // Force video type
    videoPlayer.value.type = 'video/mp4; codecs="avc1.42E01E, mp4a.40.2"';
  }
});
</script>

<template>
  <div class="song-view">
    <PageHeader />
    <main>
      <div class="song-container">
        <h1>You Are <u>Our</u> Sunshine</h1>
        <div class="video-wrapper">
          <div v-if="!videoLoaded && !videoError" class="loading-state">
            Loading video...
          </div>
          <div v-if="videoError" class="error-state">
            Failed to load video. Please try refreshing the page.
          </div>
          <video
            v-show="videoLoaded"
            ref="videoPlayer"
            class="main-video"
            controls
            preload="auto"
            :src="videoSrc"
            @error="handleVideoError"
            @loadeddata="handleVideoLoaded"
            @play="handleVideoStateChange"
            @pause="handleVideoStateChange"
            @timeupdate="handleVideoStateChange"
          >
            <source :src="videoSrc" type="video/mp4" />
            Your browser does not support the video tag.
          </video>
        </div>
        <!-- Debug info during development -->
        <div v-if="videoState" class="debug-info">
          <pre>{{ videoState }}</pre>
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

.loading-state,
.error-state {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  color: var(--color-text);
  text-align: center;
  width: 100%;
  padding: 1rem;
}

.error-state {
  color: #ff6b6b;
}

.debug-info {
  margin-top: 1rem;
  padding: 1rem;
  background: rgba(0, 0, 0, 0.1);
  border-radius: 4px;
  font-family: monospace;
  text-align: left;
  font-size: 0.8rem;
}
</style>