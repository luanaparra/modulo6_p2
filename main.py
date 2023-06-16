import cv2

face_cascade = cv2.CascadeClassifier(
    filename=f"{cv2.data.haarcascades}/haarcascade_frontalface_default.xml"
)

input_video = cv2.VideoCapture('../assets/arsene.mp4')

if not input_video.isOpened():
    print("Error opening video file")
    exit(1)

gray_video = cv2.cvtColor(src=input_video, code=cv2.COLOR_BGR2GRAY)

faces = input_video.detectMultiScale(
    image=gray_video, 
    scaleFactor=1.05, 
    minNeighbors=5 
)
    
width  = int(input_video.get(cv2.CAP_PROP_FRAME_WIDTH))   # float `width`
height = int(input_video.get(cv2.CAP_PROP_FRAME_HEIGHT))

output_video = cv2.VideoWriter( './saida/out.avi',cv2.VideoWriter_fourcc(*'DIVX'), 24, (width, height))

while True:
    ret, input_video = input_video.read()
    if not ret:
        break
    x, y, w, h = faces[0]
    cv2.rectangle(
            img=input_video,
            pt1=(x, y),
            pt2=(x+w, y+h),
            color=(0,0,255),
            thickness=5
        )

    cv2.imshow('Video Playback', input_video)
    
    output_video.write(input_video)

    if cv2.waitKey(30) & 0xFF == ord('q'):
        break
    
# Fecha tudo
output_video.release()
input_video.release()
cv2.destroyAllWindows()