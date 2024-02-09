import cv2
import numpy as np
from uiautomator2 import connect
import time

d = uiautomator2.connect("emulator_ip:16384")  # replace with your emulator IP and port
d.stream.start()