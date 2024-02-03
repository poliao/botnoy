from uiautomator2 import connect
from PIL import ImageDraw, Image
import subprocess
# กำหนด IP ของ MuMu
emu_ip = "127.0.0.1:16448"

# เปิดการเชื่อมต่อกับ MuMu
d = connect(emu_ip)


# กำหนดขนาดและตำแหน่งที่ต้องการดึงสี
region_left = 200
region_top = 200
region_right = 400
region_bottom = 400

# กำหนดสีที่ต้องการตรวจสอบ (RGB format)
# ตั้งค่าให้เป็นช่วงสีดำถึงสีเทา
target_color_start = (0, 0, 0)  # สีดำ
target_color_end = (28,26,31)  # สีเทา

# กำหนดตำแหน่งที่ต้องการ click หลังจากพบสี
click_position = (1370, 704)  # ตำแหน่ง x, y ที่ต้องการ click

color_found = False
# ทดสอบตรวจสอบสี 20 ครั้ง
for iteration in range(1, 200):
    # print(f"\nIteration {iteration}:")

    # ดึงรูปภาพจากพื้นที่ที่กำหนด
    screenshot_full = d.screenshot()

    screenshot = screenshot_full.crop((region_left, region_top, region_right, region_bottom))

    # Save the captured image for reference
    # screenshot.save(f"screenshot_iteration_{iteration}.png")
    # screenshot.show()
    # ดึงค่าสีที่ต้องการตรวจสอบจากรูปภาพ
    # ดึงสีของทุก pixel ในพื้นที่
    all_colors = list(screenshot_full.crop((region_left, region_top, region_right, region_bottom)).getdata())

    for color in all_colors:
        if all(start <= value <= end for start, value, end in zip(target_color_start, color, target_color_end)):
            d.click(click_position[0], click_position[1])
            print("Color found in the specified range (between black and gray)")
            color_found = True
            break  # หยุดการทำงานทันทีหลังจากพบสี

    if color_found:
        break  # หยุดลูปทั้งหมดหลังจากพบสี
    else:
        print("No color found in the specified range")
