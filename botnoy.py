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
target_color_start, target_color_end = np.array([0, 0, 0]), np.array([180, 255, 30])  # Black color
target_color_starts, target_color_ends = np.array([0, 0, 200]), np.array([20, 20, 255])  # Blue color
blue_color_starts, blue_color_ends = np.array([100, 100, 50]), np.array([120, 255, 255])  # Gray to white
click_position = (1400, 784)
c = (1400, 720)
T = (1350, 594)

for i in range (1,200) :
       

        with mss.mss() as sct: 
                        restart_timer = time.time()
                        while True:    # Capture and process the region_left for black color
                                monitor = {"top": region_top, "left": region_left, "width": region_right - region_left, "height": region_bottom - region_top}
                                full_screen = np.array(sct.grab(monitor))
                                hsv_full_screen = cv2.cvtColor(full_screen, cv2.COLOR_BGR2HSV)
                                mask_full_screen = cv2.inRange(hsv_full_screen, target_color_start, target_color_end)
                                elapsed_time = time.time() - restart_timer
                                
                                if elapsed_time > 20:
                                        print("เริ่มโปรแกรมใหม่หลังจากไม่พบสีดำเป็นเวลา 20 วินาที")
                                        restart_timer = time.time()
                                        d.click(*T)
                                if np.any(mask_full_screen):
                                        time.sleep(0.5)
                                        d.click(*click_position)
                                        print("ปลาแดก")
                                        break
                                else : print("ปลายังไม่แดก")                                 
        with mss.mss() as s:
                        restart_timer = time.time()
                        while True:
                                monitor = {"top": Mid_top, "left": Mid_left, "width": Mid_right - Mid_left, "height": Mid_bottom - Mid_top}
                                mid_screen = np.array(s.grab(monitor))
                                hsv_mid_screen = cv2.cvtColor(mid_screen, cv2.COLOR_BGR2HSV)
                                mask_mid_screen = cv2.inRange(hsv_mid_screen, target_color_starts, target_color_ends)
                                elapsed_time = time.time() - restart_timer
                                if elapsed_time > 18:
                                        print("เริ่มโปรแกรมใหม่หลังจากไม่พบสีดำเป็นเวลา 20 วินาที")
                                        restart_timer = time.time()
                                        break
                                if np.any(mask_mid_screen):
                                        time.sleep(0.05)
                                        d.click(*click_position)
                                        print("Clicked - White")
                                        time.sleep(0.5)
                                        monitor = {"top": fis_top, "left": fis_left, "width": fis_right - fis_left, "height": fis_bottom - fis_top}
                                        fis_screen = np.array(s.grab(monitor))
                                        hsv_fis_screen = cv2.cvtColor(fis_screen, cv2.COLOR_BGR2HSV)
                                        mask_fis_screen = cv2.inRange(hsv_fis_screen, blue_color_starts, blue_color_ends)
                                        if np.any(mask_fis_screen): 
                                                time.sleep(2)
                                                d.click(*c)
                                                print("รับปลา")
                                                time.sleep(2)
                                                d.click(*T)
                                                break
                                else :
                                        monitor = {"top": fis_top, "left": fis_left, "width": fis_right - fis_left, "height": fis_bottom - fis_top}
                                        fis_screen = np.array(s.grab(monitor))
                                        hsv_fis_screen = cv2.cvtColor(fis_screen, cv2.COLOR_BGR2HSV)
                                        mask_fis_screen = cv2.inRange(hsv_fis_screen, blue_color_starts, blue_color_ends)
                                        if np.any(mask_fis_screen):
                                                        time.sleep(2) 
                                                        d.click(*c)
                                                        print("รับปลา")
                                                        time.sleep(2)
                                                        d.click(*T)
                                                        break
                                        
               
                

                                         
       

        
        