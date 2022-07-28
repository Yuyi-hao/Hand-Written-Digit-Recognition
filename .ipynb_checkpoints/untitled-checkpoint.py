import pygame,sys
from pygame.locals import * 
import numpy  as np 
from keras.models import load_model
import cv2


# initialize pygame 
pygame.init()
pygame.display.set_mode(640, 480)