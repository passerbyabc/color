import numpy as np
import cv2

# *** load img ***
sampling_img = cv2.imread('y0.005.png')
# sampling_img = cv2.imread('y0.01.png')
# sampling_img = cv2.imread('y0.05.png')
# sampling_img = cv2.imread('y0.10.png')
# sampling_img = cv2.imread('y0.20.png')
# sampling_img = cv2.imread('y0.25.png')
# sampling_img = cv2.imread('y0.30.png')
# sampling_img = cv2.imread('y9h1.png')
# sampling_img = cv2.imread('test.jpg')
sampling_img = cv2.imread('shapes_and_colors.jpg')

# BGR->HSV
sampling_HSV = cv2.cvtColor(sampling_img, cv2.COLOR_BGR2HSV) 
# print(sampling_HSV)

dic_chart ={                       
                '0.005':([170,18,251], [170,21,252]),
                '0.01':([168,45,244], [169,51,250]),
                '0.05':([168,77, 242], [168,87,244]),
                '0.10':([168,112, 225], [168,114,228]),
                '0.15':([169,189, 236], [169,189,239]),
                '0.20':([169,180, 200], [169,191,207]),
                '0.25':([172,176, 198], [172,180,200]),
                '0.30':([172,177, 187], [172,180,190]), 
            }  
    
color_value = []
color_countNonZero =[]             
for key,(lower_red,upper_red) in dic_chart.items():    
    lower_red = np.array(lower_red, dtype = "uint8")
    upper_red = np.array(upper_red, dtype = "uint8")     
    mask = cv2.inRange(sampling_HSV, lower_red, upper_red)
    countNonZero = cv2.countNonZero(mask) 
    color_countNonZero.append(countNonZero)    
    color_value.append(key)        

print("color_count:",color_countNonZero)

if color_countNonZero==[0, 0, 0, 0, 0, 0, 0, 0]:
    print("匹配失败")
else:    
    color_countNonZero_array = np.array(color_countNonZero)
    idx = np.argmax(color_countNonZero_array)
    v = color_value[idx]
    print ("匹配成功，色卡匹配值为", v)

