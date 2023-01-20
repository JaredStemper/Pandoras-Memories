<template>
  <swiper
    class="default-slider"
    @swiper="onSwiper"
    @slideChange="onSlideChange"
    :slides-per-view="1"
    :space-between="30"
    :navigation="true"
    >
  <!-- <swiper-slide v-for="n in 7" :key="n"> {{ n }} </swiper-slide> -->
  <swiper-slide src="https://player.vimeo.com/video/741185245?background=1" width="640" height="360" allow="autoplay; fullscreen;" allowfullscreen></swiper-slide>
  </swiper>

  <!-- <div class="swiper-wrapper">
    <div class="swiper-slide">
    </div>
    <div class="swiper-slide">
      <iframe src="https://player.vimeo.com/video/740426857?background=1" width="640" height="360" allow="autoplay; fullscreen;" allowfullscreen></iframe>
    </div>
    <div class="swiper-slide">
      <iframe src="https://player.vimeo.com/video/739573957?background=1" width="640" height="360" allow="autoplay; fullscreen;" allowfullscreen></iframe>
    </div>
  </div>
  <div class="swiper-pagination"></div>

  <div class="swiper-button-prev"></div>
  <div class="swiper-button-next"></div>

  <div class="swiper-scrollbar"></div> -->
</template>


<script>
  // Import Swiper Vue.js components
  import SwiperCore, { Navigation, Pagination, Scrollbar, A11y } from 'swiper';
  import { Swiper, SwiperSlide} from 'vue-awesome-swiper';

  // Import Swiper styles
  import 'swiper/css';
  import 'swiper/css/navigation';
  import 'swiper/css/pagination';
  import 'swiper/css/scrollbar';

  SwiperCore.use([Navigation]);

  export default {
    components: {
      Swiper,
      SwiperSlide,
    },
    setup() {
      const onSwiper = (swiper) => {
        console.log(swiper);
      };
      const onSlideChange = () => {
        console.log('slide change');
      };
      return {
        onSwiper,
        onSlideChange,
      };
    },
  };


  // let realPrevIndex = 1;

  // const swiper = new Swiper('.swiper', {
  //   loop: true,
  //   speed: 1000,
  //   preventInteractionOnTransition: true,
  //   followFinger: false,
  //   preloadImages: false,
  //   lazy: {
  //     loadOnTransitionStart: true
  //   },
  //   effect: 'fade',
  //   fadeEffect: {
  //     crossFade: true
  //   },
  //   navigation: {
  //     nextEl: '.swiper-button-next',
  //     prevEl: '.swiper-button-prev'
  //   },
  //   pagination: {
  //     el: '.swiper-pagination',
  //   },
  // });

  // swiper.on('realIndexChange', function(){
  //   let current = swiper.slides[swiper.activeIndex].querySelector('iframe');
  //   let prev = swiper.slides[realPrevIndex].querySelector('iframe');
  //   let currVimeo = new Vimeo.Player( current );
  //   let prevVimeo = new Vimeo.Player( prev );
    
  //   currVimeo.setCurrentTime( 0 );
  //   currVimeo.play();
  //   prevVimeo.pause();
    
  //   realPrevIndex = swiper.activeIndex;
  // });
</script>

<style scoped>
/* [id='app'] * {
  max-width: 100%;
} */
.swiper {
  width: 640px;
  height: 360px;
}

.swiper-pagination-bullet { 
  background:#fff;
  opacity:1;
}

.swiper-pagination-bullet-active {
  background:var(--swiper-pagination-color,var(--swiper-theme-color));
}




.default-slider .swiper-slide {
  display: flex;
  height: 300px !important;
  justify-content: center;
  align-items: center;
  color: #000;
  font-size: 24px;
  font-weight: 700;
  }
  .swiper-slide:nth-child(1n) {
    background-color: palevioletred;
  }.swiper-slide:nth-child(2n) {
    background-color: skyblue;
  }.swiper-slide:nth-child(3n) {
    background-color: peru;
  }.swiper-slide:nth-child(4n) {
    background-color: cadetblue;
  }.swiper-slide:nth-child(5n) {
    background-color: plum;
  }.swiper-slide:nth-child(6n) {
    background-color: goldenrod;
  }.swiper-slide:nth-child(7n) {
    background-color: palegreen;
  }

</style>


