import cv2


fpath = "./IMG_3027.MOV"
video = cv2.VideoCapture(fpath)
if video.isOpened() == False:
    print("[INFO] ERROR OPENING VIDEO STREAM OR FILE")
total = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
width  = video.get(3)   # float `width`
height = video.get(4)  # float `height`
print("[INFO] {} RESOLUTION {}X{}".format(fpath, width, height))
count = 1
while video.isOpened():
    (check, frame) = video.read()
    if check:
        print("[INFO] IMAGE {}/{}".format(count, total))
        #frame = cv2.resize(frame, (640, 480), interpolation=cv2.INTER_AREA)
        fname = "./image/image{}.png".format(count)
        cv2.imwrite(fname, frame)
        count += 1
    else:
        break