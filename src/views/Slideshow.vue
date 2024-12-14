<template>
  <div class="slideshow-container">
    <swiper
      @swiper="onSwiper"
      :modules="[SwiperAutoplay, SwiperPagination, SwiperNavigation]"
      :slides-per-view="1"
      :loop="true"
      :autoplay="{
        delay: 3000,
        disableOnInteraction: false,
      }"
      :pagination="{ clickable: true }"
      :navigation="true"
      class="w-full max-w-4xl mx-auto"
    >
      <swiper-slide v-for="(slide, index) in slides" :key="index">
        <div class="relative h-[400px]">
          <!-- Video Slide -->
          <video
            v-if="slide.type === 'video'"
            :src="slide.src"
            class="w-full h-full object-cover"
            :autoplay="isVideoPlaying"
            loop
            muted
            @ended="handleVideoEnd"
            ref="videoRefs"
          ></video>
          <!-- Image Slide -->
          <img
            v-else
            :src="slide.src"
            :alt="slide.title"
            class="w-full h-full object-cover"
          />
          <div class="absolute bottom-0 left-0 right-0 bg-black bg-opacity-50 p-4 text-white">
            <h3 class="text-xl font-bold">{{ slide.title }}</h3>
            <p>{{ slide.description }}</p>
          </div>
        </div>
      </swiper-slide>
    </swiper>
    
    <!-- Custom Controls -->
    <div class="custom-controls">
      <button 
        @click="previousSlide" 
        class="control-btn"
        aria-label="Previous slide"
      >
        <font-awesome-icon :icon="faBackward" />
      </button>
      <button 
        @click="toggleSlideshow" 
        class="control-btn"
        :aria-label="isSlideshowPlaying ? 'Pause slideshow' : 'Play slideshow'"
      >
        <font-awesome-icon :icon="isSlideshowPlaying ? faPause : faPlay" />
      </button>
      <button 
        @click="nextSlide" 
        class="control-btn"
        aria-label="Next slide"
      >
        <font-awesome-icon :icon="faForward" />
      </button>
      <!-- Video Control Button -->
      <button 
        v-if="currentSlideIsVideo"
        @click="toggleVideo" 
        class="control-btn"
        :aria-label="isVideoPlaying ? 'Pause video' : 'Play video'"
      >
        <font-awesome-icon :icon="isVideoPlaying ? faStop : faPlay" />
      </button>
    </div>
  </div>
</template>

<script setup>
import { Swiper, SwiperSlide } from 'swiper/vue';
import { Autoplay as SwiperAutoplay, Pagination as SwiperPagination, Navigation as SwiperNavigation } from 'swiper';
import { ref, onMounted } from 'vue';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
import { 
  faPlay, 
  faPause, 
  faForward, 
  faBackward,
  faStop
} from '@fortawesome/free-solid-svg-icons';
import 'swiper/css';
import 'swiper/css/pagination';
import 'swiper/css/navigation';

let swiperInstance = null;
const isSlideshowPlaying = ref(true);
const isVideoPlaying = ref(true);
const videoRefs = ref([]);
const currentSlideIsVideo = ref(false);

// Function to determine media type based on file extension
const getMediaType = (filename) => {
  const extension = filename.toLowerCase().split('.').pop();
  const videoExtensions = ['mp4', 'webm', 'ogg'];
  const imageExtensions = ['jpg', 'jpeg', 'png', 'gif', 'webp'];
  
  if (videoExtensions.includes(extension)) return 'video';
  if (imageExtensions.includes(extension)) return 'image';
  return null;
};

// Import all media files from the slideshowVideos directory
const mediaFiles = import.meta.glob('/src/assets/slideshowVideos/*.*');
const slides = ref([]);

// Load all media files
const loadMediaFiles = async () => {
  const mediaPromises = Object.entries(mediaFiles).map(async ([path, importFunc]) => {
    const filename = path.split('/').pop();
    const type = getMediaType(filename);
    
    if (!type) return null; // Skip files that aren't images or videos
    
    const module = await importFunc();
    return {
      type,
      src: module.default,
      title: filename.split('.')[0].replace(/-/g, ' '),
    //   description: `Your custom description for ${filename}`
    };
  });

  const loadedMedia = (await Promise.all(mediaPromises)).filter(item => item !== null);
  slides.value = loadedMedia;
};

// Load media files when component mounts
onMounted(async () => {
  await loadMediaFiles();
  if (isVideoPlaying.value) {
    playCurrentVideo();
  }
});

const onSwiper = (swiper) => {
  swiperInstance = swiper;
  
  // Handle slide change
  swiper.on('slideChange', () => {
    const currentSlide = slides.value[swiper.realIndex];
    currentSlideIsVideo.value = currentSlide?.type === 'video';
    
    if (currentSlideIsVideo.value && isVideoPlaying.value) {
      playCurrentVideo();
    }
  });
};

const pauseAllVideos = () => {
  document.querySelectorAll('video').forEach(video => {
    video.pause();
  });
};

const playCurrentVideo = () => {
  const currentSlide = swiperInstance?.slides[swiperInstance.activeIndex];
  const video = currentSlide?.querySelector('video');
  if (video && isVideoPlaying.value) {
    video.play();
  }
};

const toggleVideo = () => {
  isVideoPlaying.value = !isVideoPlaying.value;
  if (isVideoPlaying.value) {
    playCurrentVideo();
  } else {
    pauseAllVideos();
  }
};

const toggleSlideshow = () => {
  if (!swiperInstance) return;
  
  isSlideshowPlaying.value = !isSlideshowPlaying.value;
  
  if (isSlideshowPlaying.value) {
    swiperInstance.autoplay.start();
  } else {
    swiperInstance.autoplay.stop();
  }
};

const nextSlide = () => {
  if (swiperInstance) {
    swiperInstance.slideNext();
  }
};

const previousSlide = () => {
  if (swiperInstance) {
    swiperInstance.slidePrev();
  }
};

const handleVideoEnd = () => {
  if (isSlideshowPlaying.value && swiperInstance) {
    swiperInstance.slideNext();
  } else {
    // If slideshow is paused, restart the video
    playCurrentVideo();
  }
};
</script>

<style scoped>
.swiper {
  --swiper-theme-color: #fff;
  --swiper-navigation-size: 25px;
}

.swiper-button-next,
.swiper-button-prev {
  background-color: rgba(0, 0, 0, 0.5);
  padding: 20px;
  border-radius: 50%;
}

.swiper-pagination-bullet {
  background: white;
}

.slideshow-container {
  position: relative;
}

.custom-controls {
  position: absolute;
  bottom: 20px;
  left: 50%;
  transform: translateX(-50%);
  z-index: 10;
  display: flex;
  gap: 0.75rem;
  background-color: rgba(0, 0, 0, 0.5);
  padding: 0.5rem;
  border-radius: 20px;
}

.control-btn {
  background: none;
  border: none;
  color: white;
  cursor: pointer;
  padding: 0.5rem;
  border-radius: 50%;
  transition: background-color 0.3s;
  width: 2.5rem;
  height: 2.5rem;
  display: flex;
  align-items: center;
  justify-content: center;
}

.control-btn svg {
  width: 1rem;
  height: 1rem;
}

.control-btn:hover {
  background-color: rgba(255, 255, 255, 0.2);
}
</style> 