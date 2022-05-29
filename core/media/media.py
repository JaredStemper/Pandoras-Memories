import random
import os

import pyglet

def update_pan_zoom_speeds():
    global _pan_speed_x
    global _pan_speed_y
    global _zoom_speed
    _pan_speed_x = random.randint(-8, 8)
    _pan_speed_y = random.randint(-8, 8)
    _zoom_speed = random.uniform(-0.02, 0.02)
    return _pan_speed_x, _pan_speed_y, _zoom_speed

def update_pan(dt, sprite):
    sprite.x += dt * _pan_speed_x
    sprite.y += dt * _pan_speed_y

def update_zoom(dt, sprite):
    sprite.scale += dt * _zoom_speed

def update_image(dt, sprite, image_paths, window):
    img = pyglet.image.load(random.choice(image_paths))
    sprite = pyglet.sprite.Sprite(img)
    sprite.scale = get_scale(window, img)

    @window.event
    def on_draw():
        sprite.draw()

    img = pyglet.image.load(random.choice(image_paths))
    sprite.image = img
    sprite.scale = get_scale(window, img)
    sprite.x = 0
    sprite.y = 0
    window.clear()
    
def get_image_paths(input_dir=os.getcwd()):
    paths = []
    for root, dirs, files in os.walk(input_dir, topdown=True):
        for file in sorted(files):
            if file.endswith(('jpg', 'png')):
                path = os.path.abspath(os.path.join(root, file))
                paths.append(path)
    return paths

def get_media_paths(input_dir=os.getcwd()):
    paths = []
    for root, dirs, files in os.walk(input_dir, topdown=True):
        for file in sorted(files):
            if file.endswith(('mp4', 'gif')):
                path = os.path.abspath(os.path.join(root, file))
                paths.append(path)
    return paths

def get_scale(window, image):
    if image.width > image.height:
        scale = float(window.width) / image.width
    else:
        scale = float(window.height) / image.height
    return scale

def get_video_size(width, height, sample_aspect):
    if sample_aspect > 1.:
        return width * sample_aspect, height
    elif sample_aspect < 1.:
        return width, height / sample_aspect
    else:
        return width, height

def runPictureSlideshow(window):
    image_paths = get_image_paths()
    # random.shuffle(image_paths)
    img = pyglet.image.load(random.choice(image_paths))

    sprite = pyglet.sprite.Sprite(img)
    sprite.scale = get_scale(window, img)

    @window.event
    def on_draw():
        sprite.draw()
        
    pyglet.clock.schedule_interval(update_image, 6.0, sprite, image_paths, window)
    
def runVideoSlideshow(window):
    media_paths = get_media_paths()
    random.shuffle(media_paths)

    player = pyglet.media.Player()
    source = pyglet.media.StreamingSource()

    for media in media_paths:
        sourceMedia = pyglet.media.load(media)
        player.queue(sourceMedia)

    # on draw event
    @window.event
    def on_draw():
        
        # clear the window
        window.clear()
        
        # if player source exist
        # and video format exist
        if player.source and player.source.video_format:
            
            # get the texture of video and
            # make surface to display on the screen
            player.get_texture().blit(0, 0)

    # key press event	
    @window.event
    def on_key_press(symbol, modifier):

        # key "p" get press
        if symbol == pyglet.window.key.P:
            
            # printing the message
            print("Key : P is pressed")
            
            # pause the video
            player.pause()
            
            # printing message
            print("Video is paused")
            
            
        # key "r" get press
        if symbol == pyglet.window.key.R:
            
            # printing the message
            print("Key : R is pressed")
            
            # resume the video
            player.play()
            
            # printing message
            print("Video is resumed")
                # key "q" gets pressed
        if symbol == pyglet.window.key.Q:
            
            # printing the message
            print("Key : Q is pressed")
            
            # pause and dump resources
            player.pause()
            player.delete()

            pyglet.app.exit()
            
            # printing message
            print("Video is ended, app is exited")
    
    return player

def runPicAndVidSlideshow(window):
    media_paths = get_media_paths()
    random.shuffle(media_paths)

    player = pyglet.media.Player()
    source = pyglet.media.StreamingSource()

    for media in media_paths:
        sourceMedia = pyglet.media.load(media)
        player.queue(sourceMedia)

    # on draw event
    @window.event
    def on_draw():
        
        # clear the window
        window.clear()
        
        # if player source exist
        # and video format exist
        if player.source and player.source.video_format:
            
            # get the texture of video and
            # make surface to display on the screen
            player.get_texture().blit(0, 0)

    # key press event	
    @window.event
    def on_key_press(symbol, modifier):

        # key "p" get press
        if symbol == pyglet.window.key.P:
            
            # printing the message
            print("Key : P is pressed")
            
            # pause the video
            player.pause()
            
            # printing message
            print("Video is paused")
            
            
        # key "r" get press
        if symbol == pyglet.window.key.R:
            
            # printing the message
            print("Key : R is pressed")
            
            # resume the video
            player.play()
            
            # printing message
            print("Video is resumed")
                # key "q" gets pressed
        if symbol == pyglet.window.key.Q:
            
            # printing the message
            print("Key : Q is pressed")
            
            # pause and dump resources
            player.pause()
            player.delete()

            pyglet.app.exit()
            
            # printing message
            print("Video is ended, app is exited")
    
    return player


def MainLoop(mode, logger=None):
    window = pyglet.window.Window(fullscreen=True)

    if (mode == "pictures"):
        runPictureSlideshow(window)
    elif (mode == "videos"):
        player = runVideoSlideshow(window)
        player.play()
    elif (mode == "picsAndVids"):
        player = runPicAndVidSlideshow(window)
        player.play()
    else:
        print("This is not a supported option at this time.")  
    
    pyglet.app.run()
    pyglet.app.exit()
    
    if logger:
        logger.info("Just an information")


if __name__ == '__main__':
	# MainLoop("pictures")
	MainLoop("videos")
	# MainLoop("picsAndVids")