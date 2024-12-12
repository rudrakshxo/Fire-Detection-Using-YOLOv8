from ultralytics import YOLO
import cv2
import math

video_path = 'Media\\Zenmuse1.mp4'
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Cannot open video file.")
    exit()

model = YOLO('BestModel.pt')
classnames = ['Fire', 'Smoke']
colors = {'Fire': (0, 0, 255),
          'Smoke': (255, 0, 0)}

while True:
    ret, frame = cap.read()
    if not ret:
        print("End of video or cannot read frame.")
        break

    h, w = frame.shape[:2]
    aspect_ratio = w / h
    frame = cv2.resize(frame, (640, int(640 / aspect_ratio)))

    results = model(frame)

    for result in results:
        for box in result.boxes:
            confidence = box.conf[0]
            confidence = math.ceil(confidence * 100)
            class_id = int(box.cls[0])
            
            if confidence > 50:
                x1, y1, x2, y2 = box.xyxy[0]
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                class_name = classnames[class_id]
                box_color = colors[class_name]

                cv2.rectangle(frame, (x1, y1), (x2, y2), box_color, thickness=2)

                label = f'{class_name} {confidence}%'
                font = cv2.FONT_HERSHEY_TRIPLEX
                font_scale = 0.6
                font_thickness = 1
                text_size = cv2.getTextSize(label, font, font_scale, font_thickness)[0]
                text_x = x1
                text_y = y1 - 10 if y1 - 10 > 10 else y1 + 10
                cv2.rectangle(frame, (text_x, text_y - text_size[1] - 5), 
                              (text_x + text_size[0] + 5, text_y + 5), box_color, -1)
                cv2.putText(frame, label, (text_x, text_y), font, font_scale, 
                            (255, 255, 255), thickness=font_thickness, lineType=cv2.LINE_AA)

    cv2.imshow('Detection', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
