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

def get_multimedia_paths(input_dir=os.getcwd()):
    paths = []
    for root, dirs, files in os.walk(input_dir, topdown=True):
        for file in sorted(files):
            if file.endswith(('jpg', 'png', 'mp4', 'gif')):
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

def runPictureSlideshow(window, logger=None):
    image_paths = get_image_paths()
    # random.shuffle(image_paths) TODO: having a set list would be useful for future scrolling backwards/forwards
    img = pyglet.image.load(random.choice(image_paths))

    sprite = pyglet.sprite.Sprite(img)
    sprite.scale = get_scale(window, img)

    @window.event
    def on_draw():
        sprite.draw()
        
    pyglet.clock.schedule_interval(update_image, 6.0, sprite, image_paths, window)
    
def runVideoSlideshow(window, logger=None):
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
            
            # logging input
            if logger:
                logger.info("Key: 'P' is pressed")
            
            # pause the video
            player.pause()
            
            # printing message
            print("Video is paused")
        # key "r" get press
        if symbol == pyglet.window.key.R:
            
            # logging input
            if logger:
                logger.info("Key: 'R' is pressed")
            
            # resume the video
            player.play()
            
            # printing message
            print("Video is resumed")
        # key "q" gets pressed
        if symbol == pyglet.window.key.Q:
            
            # logging input
            if logger:
                logger.info("Key: 'Q' is pressed")
            
            # pause and dump resources
            player.pause()
            player.delete()

            pyglet.app.exit()
            
            # printing message
            print("Video is ended, app is exited")
    
    return player

def runPicAndVidSlideshow(window, logger=None):
    # multimedia_paths = get_multimedia_paths()
    multimedia_paths = get_multimedia_paths()
    print(multimedia_paths)
    # random.shuffle(multimedia_paths)

    player = pyglet.media.Player()
    # source = pyglet.media.StreamingSource()

    a = 0
    for media in multimedia_paths:
        sourceMedia = pyglet.media.load(media)
        sourceMedia.info.title = "track #" + str(a)
        a = a + 1
        player.queue(sourceMedia)

    # player.source.info.title = "test"
    track_eos = 1

    def update_eosTracker(dt):
        nonlocal track_eos
        nonlocal player

        print("\tupdates comin through")
        track_eos = 1
        currSrc = player.source
        player.next_source() #sets loop to False by default
        newSrc = player.source
        
        window.switch_to()
        # window.flip()
        # window.clear()
        # player.texture.blit(0, 0)
        # window.on_draw()

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
            
            # logging input
            if logger:
                logger.info("Key: 'P' is pressed")
            
            # pause the video
            player.pause()
            
            # printing message
            print("Video is paused")
        # key "r" get press
        if symbol == pyglet.window.key.R:
            
            # logging input
            if logger:
                logger.info("Key: 'R' is pressed")
            
            # resume the video
            player.play()
            
            # printing message
            print("Video is resumed")
        # key "n" get press
        if symbol == pyglet.window.key.N:
            # logging input
            if logger:
                logger.info("Key: 'N' is pressed")
            
            # play the next media source
            player.next_source()
            
            #if new source is an image, loop for 6 seconds
            if player.source == None:
                player.pause()
                player.delete()
                pyglet.app.exit()
            elif player.source.duration == 0.04:
                #NOTE: pyglet gives images a duration of 0.04 and a audio_format of None type (included to avoid potentially skipping GIF files)
                pyglet.clock.unschedule(update_eosTracker)
            # else:
            #     player.loop = False
            
            # printing message
            print("Next video is played")
        # key "b" go to previous source
        if symbol == pyglet.window.key.B:
            """Additional work required to implement since pyglet does not track previous sources used"""
            
            # logging input
            if logger:
                logger.info("Key: 'B' is pressed")
            
            # resume the video
            # player.
            
            # printing message
            print("Previous video is played")
        # key "q" gets pressed
        if symbol == pyglet.window.key.Q:
            
            # logging input
            if logger:
                logger.info("Key: 'Q' is pressed")
            
            # pause and dump resources
            player.pause()
            player.delete()

            pyglet.app.exit()
            
            # printing message
            print("Video is ended, app is exited")
    
    @player.event
    def on_eos():
        #loop for 6 seconds if an image, continue to end of source otherwise
        nonlocal track_eos

        #NOTE: pyglet gives images a duration of 0.04 and a audio_format of None type (included to avoid potentially skipping GIF files)
        # if player.source.audio_format != None and player.source.duration == 0.04:
        if player.source == None:
            player.delete()
            pyglet.app.exit()
        elif player.source.audio_format == None and player.source.duration == 0.04:
            if (track_eos):
                print("\timage comin through")
                track_eos = 0
                player.loop = True
                pyglet.clock.schedule_once(update_eosTracker, 6.0)
        else:
            player.loop = False

    return player

def MainLoop(mode, logger=None):
    # window = pyglet.window.Window(fullscreen=True)
    window = pyglet.window.Window(width=640, height=480)
    # window.push_handlers(pyglet.windo .WindowEventLogger('Resources/winlog.log'))

    if (mode == "pictures"):
        runPictureSlideshow(window, logger)
    elif (mode == "videos"):
        player = runVideoSlideshow(window, logger)
        player.play()
    elif (mode == "picsAndVids"):
        player = runPicAndVidSlideshow(window, logger)
        player.play()
    else:
        print("This is not a supported option at this time.")  
    
    pyglet.app.run()
    player.delete()
    pyglet.app.exit()
    
    if logger:
        logger.info("Just an information")


if __name__ == '__main__':
	# MainLoop("pictures")
	# MainLoop("videos")
	MainLoop("picsAndVids")