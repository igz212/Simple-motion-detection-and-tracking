import cv2

captured = cv2.VideoCapture(0)

_, frame1 = captured.read()
_, frame2 = captured.read()

assert captured.isOpened(), f"Something went wrong. video could not be captured. try again... :)"

while captured.isOpened():
    difference = cv2.absdiff(frame1, frame2)
    gray = cv2.cvtColor(difference, cv2.COLOR_BGR2GRAY)  
    blur = cv2.GaussianBlur(gray, (7, 7), 0)   
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    cv2.imshow('threshold', thresh)
    dilated = cv2.dilate(thresh, None, iterations=3)
    cv2.imshow('dilated', dilated)
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    minimum_area_to_detect_motion = 650
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        if cv2.contourArea(contour) < minimum_area_to_detect_motion:
            continue
        cv2.rectangle(frame1, (x, y), (x + w, y + h), (125, 125, 255), 2)
        cv2.putText(frame1, 'Movement Detect', (15, 25),
                    cv2.FONT_HERSHEY_DUPLEX, 1, (0, 25, 250), 1)

    cv2.imshow('feed', frame1)
    frame1 = frame2
    ret, frame2 = captured.read()
    #  stop key would be 's'
    if cv2.waitKey(40) & 0xFF == ord('s'):
        break

captured.release()
cv2.destroyAllWindows()
