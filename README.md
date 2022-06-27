# Pandora's Memories

Project to create a slideshow of pictures and videos on 4 sides of a cube.

Dedicated to a mother that never stopped trying for her kids. Thanks mum.

# Features
## Current Features:
- Modes:
  - Local-storage picture slideshow

## Planned Features:
- Modes:
  - Local-storage video slideshow
  - Google folder slideshow
  - picture and video slideshow
- Slideshow/Modes can be controlled from buttons on board
- Grabs photos dynamically from a Google Drive folder
- Controlled through remote control or buttons on hardware

### TODO:
- BUG:
  - slides scroll after 5 seconds, whether or not a video slide has finished playing
- access local files from directory (e.g. /home/Music/*)
  - open local directory, grab all files with appropriate extensions, play shuffled with non-shuffled option
- access remote files from google drive folder
  - NPM library for oauth2/service account handling
- controls on videos/pictures
  - add slick-arrows, imitate CSS for slick-dots and put arrows on the same bar
  - option to hide that bar (if touchscreen, it's already draggable)
- Notes:
  - what is the difference between "autoplay speed" and "speed" in slidewrapper.slick?
  - autoload metadata vs whole video? with carousel it makes sense to always preload

# Shoutouts
- Slick Slider
  - Forked from [tommydunn](https://codepen.io/tommydunn), who forked from [digistate](https://codepen.io/digistate).