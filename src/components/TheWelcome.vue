<script setup>
import WelcomeItem from "./WelcomeItem.vue";
import DocumentationIcon from "./icons/IconDocumentation.vue";
import ToolingIcon from "./icons/IconTooling.vue";
import EcosystemIcon from "./icons/IconEcosystem.vue";
import CommunityIcon from "./icons/IconCommunity.vue";
import SupportIcon from "./icons/IconSupport.vue";
</script>

<template>
  <WelcomeItem>
    <template #icon>
      <DocumentationIcon />
    </template>
    <template #heading>About Pandora's Memories</template>
    A digital tribute to family memories, inspired by a childhood memory box. Explore our collection of photos and videos, and experience our special rendition of "You Are My Sunshine." Learn more about our project's story <RouterLink to="/about">here</RouterLink>.
  </WelcomeItem>

  <WelcomeItem>
    <template #icon>
      <ToolingIcon />
    </template>
    <template #heading>Interactive Features</template>
    Navigate through our family memories with our intuitive slideshow controls. Watch videos, view photos, and experience our special recordings. The interface is designed to be simple yet meaningful, just like the original memory box that inspired it.
  </WelcomeItem>

  <WelcomeItem>
    <template #icon>
      <EcosystemIcon />
    </template>
    <template #heading>Memory Collection</template>
    The memories collected here are pulled from the full history of our family- with every photo pulled in from talking with each family member. The four-panel display rotates through different memory collections, each telling its own story.
  </WelcomeItem>

  <WelcomeItem>
    <template #icon>
      <CommunityIcon />
    </template>
    <template #heading>Family Harmony</template>
    Experience our unique take on "You Are My Sunshine" - where each family member's individual recording comes together to create a beautiful whole. It's our way of showing that even when apart, we're always (mostly) together in harmony.
  </WelcomeItem>

  <WelcomeItem>
    <template #icon>
      <SupportIcon />
    </template>
    <template #heading>Dear Mom</template>
    This project is our way of preserving and sharing our precious memories with you. Unlike the original box that lost its recording to a curious toddler, these memories are here to stay. Thank you for giving us so many beautiful moments to remember. We love you!
  </WelcomeItem>
</template>
