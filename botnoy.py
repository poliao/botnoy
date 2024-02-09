from matplotlib import pyplot as plt
from uiautomator2 import connect
import numpy as np
import cv2
import mss
import concurrent.futures
import time
emu_ip = "127.0.0.1:16384"
d = connect(emu_ip)

region_left, region_top, region_right, region_bottom = 130, 338, 250, 445
Mid_left, Mid_top, Mid_right, Mid_bottom = 450, 380, 600, 395
fis_left, fis_top, fis_right, fis_bottom = 800, 680, 885, 700
target_color_start, target_color_end = np.array([0, 0, 0]), np.array([180, 255, 30])  # สีดำถึงเทา
target_color_starts, target_color_ends = np.array([0, 0, 200]), np.array([20, 20, 255])  # เทาถึงขาว
click_position = (1400, 784)
c = (1400, 720)
T = (1350, 594)


with mss.mss() as sct: 
            while True:    # Capture and process the region_left for black color
                monitor = {"top": region_top, "left": region_left, "width": region_right - region_left, "height": region_bottom - region_top}
                full_screen = np.array(sct.grab(monitor))
                hsv_full_screen = cv2.cvtColor(full_screen, cv2.COLOR_BGR2HSV)
                mask_full_screen = cv2.inRange(hsv_full_screen, target_color_start, target_color_end)
                # plt.imshow(full_screen, cmap='gray')
                # plt.pause(0.01)
                # plt.draw()
                if np.any(mask_full_screen):
                        time.sleep(1)
                        d.click(*click_position)
                        print("ปลาแดก")
                        break
                        
                else : print("ปลายังไม่แดก") 
                       
with mss.mss() as s:
       while True:
                monitor = {"top": Mid_top, "left": Mid_left, "width": Mid_right - Mid_left, "height": Mid_bottom - Mid_top}
                mid_screen = np.array(s.grab(monitor))
                hsv_mid_screen = cv2.cvtColor(mid_screen, cv2.COLOR_BGR2HSV)
                mask_mid_screen = cv2.inRange(hsv_mid_screen, target_color_starts, target_color_ends)
                if np.any(mask_mid_screen):
                        time.sleep(0.05)
                        d.click(*click_position)
                        print("Clicked - White")
                        monitor = {"top": fis_top, "left": fis_left, "width": fis_right - fis_left, "height": fis_bottom - fis_top}
                        fis_screen = np.array(s.grab(monitor))
                        hsv_fis_screen = cv2.cvtColor(fis_screen, cv2.COLOR_BGR2HSV)
                        mask_fis_screen = cv2.inRange(hsv_fis_screen, target_color_starts, target_color_ends)
                        if np.any(mask_fis_screen): 
                                d.click(*c)
                                print("รับปลา")
                                d.click(*T)
                                
                else :
                        monitor = {"top": fis_top, "left": fis_left, "width": fis_right - fis_left, "height": fis_bottom - fis_top}
                        fis_screen = np.array(s.grab(monitor))
                        hsv_fis_screen = cv2.cvtColor(fis_screen, cv2.COLOR_BGR2HSV)
                        mask_fis_screen = cv2.inRange(hsv_fis_screen, target_color_starts, target_color_ends)
                        if np.any(mask_fis_screen): 
                                        d.click(*c)
                                        print("รับปลา")
                                        time.sleep(2)
                                        d.click(*T)
                        
               
                

                                         
       

        
        