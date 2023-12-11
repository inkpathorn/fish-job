import mss
import numpy as np
import cv2
import pyautogui
import time
import keyboard
import pydirectinput

def take_screenshot():
    with mss.mss() as sct:
        filename = sct.shot(output='fullscreen.png')
    print('TAKE SCREEN')
    return filename

def get_frame(region):
    with mss.mss() as sct:
        screen = np.array(sct.grab(region))
        hsv = cv2.cvtColor(screen, cv2.COLOR_BGR2HSV)
    
        # define range wanted color in HSV
        lower_val = np.array([37,42,0]) 
        upper_val = np.array([84,255,255]) 

        # Threshold the HSV image - any green color will show up as white
        mask = cv2.inRange(hsv, lower_val, upper_val)

        # if there are any white pixels on mask, sum will be > 0
        hasGreen = np.sum(mask)
        detected = False
        if hasGreen > 0:
            pydirectinput.press('e')
            print('hasGreen: ', hasGreen)
            print('Green detected!')
            detected = True

        # show image 
        # apply mask to image
        res = cv2.bitwise_and(screen,screen,mask=mask)
        fin = np.hstack((screen, res))
        # display image
        cv2.imshow("Res", fin)
        cv2.imshow("Mask", mask)

        # cv2.imwrite('region'+ str(num) + '.png', mask)
    return detected

# PLEASE MAPPING YOUR DEVIEC HERE
region = {"top": 862, "left": 787, "width": 352, "height": 2}
startJob = "STAY"

for i in list(range(4))[::-1]:
    print(i+1)
    time.sleep(1)
    

if __name__ == "__main__":
    while True:
        if keyboard.is_pressed('q'):
            break
        start_time = time.time()
        if startJob == "STAY":
            pydirectinput.press('e')
            startJob = 'RUNNING'
        # take_screenshot()
        detected = get_frame(region)
        if detected: 
            # Sleep for next job
            time.sleep(9) 
            startJob = "STAY"