import cv2

# path = './dk7iz-sjris.mp4'
path = '/media/smallflyfly/Data/yolov3/test.mp4'
cap = cv2.VideoCapture(path)
print(cap.isOpened())
temp2=cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
temp3=cap.get(cv2.CAP_PROP_FRAME_WIDTH)
print(temp2)
print(temp3)
n = cap.get(cv2.CAP_PROP_FRAME_COUNT)
print(n)