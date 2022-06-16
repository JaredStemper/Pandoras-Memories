import argparse
import logging
import os

from core import media

def init():
	"""Starts the logger"""
	
	logging.basicConfig(filename="Resources/log.log",
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

	# parser = argparse.ArgumentParser()
	# parser.add_argument('dir', help='directory of images',
	# 				nargs='?', default=os.getcwd())
	# args = parser.parse_args()

	modes = ["pictures","videos","picsAndVids"]
	# Starts the main loop
	media.media.MainLoop(modes[0], logger=logger)
	# Core.MainLoop(*fullScreen, *isSlideshow)

if __name__ == '__main__':
	main()