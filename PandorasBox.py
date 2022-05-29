import logging

from core import media

def init():
	"""Starts the logger"""
	
	logging.basicConfig(filename="Misc./log.log",
						format='%(asctime)s %(message)s',
						filemode='a')
	logger = logging.getLogger()
	logger.setLevel(logging.DEBUG)
	
	return logger

	"""
	# Creating an object
	logger = logging.getLogger()

	# Setting the threshold of logger to DEBUG
	logger.setLevel(logging.DEBUG)

	# Test messages
	logger.debug("Harmless debug Message")
	logger.info("Just an information")
	logger.warning("Its a Warning")
	logger.error("Did you try to divide by zero")
	logger.critical("Internet is down")
	"""
	# fullScreen = flag.Bool("f", false, "set in fullscreen mode")
	# isSlideshow = flag.Bool("s", false, "set auto slideshow")
	# recurse = flag.Bool("r", false, "scan pictures recursively in folders")
	# flag.Parse()

def main():
	logger = init()

	# Starts the main loop
	media.media.MainLoop(logger)
	# Core.MainLoop(*fullScreen, *isSlideshow)

if __name__ == '__main__':
	main()