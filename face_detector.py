import cv2

# load pre-trained data in xml file
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


# choose an image to detect a face.
# img = cv2.imread('test.jpeg')

# captures video, 0 is default camera
def facedetection():
    webcam = cv2.VideoCapture(0)

    while True:
        successful_frame_read, frame = webcam.read()

        # converting to greyscale so the cv2 will work
        grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # cv2.imshow('title of what the window will say' "the image path or variable")

        # keeps the window with the image we made .imshow above, stay open for longer than a millisecond

        # Detects faces, calling the classifier which is the xml file that was loaded firts
        # detect multi scale means it can detect all size and shapes of faces, its only
        # looking for relations between eyes nose mouth etc.
        face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)
        # print(face_coordinate) to get coordinates on the terminal.

        # prints the rectangle to the original picture
        # cv2.rectangle(pic, (x,y) (then x plus w(which is the 3 rd in coordinates print above

        for (x, y, w, h) in face_coordinates:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        # keeps the window with the image we made .imshow above, stay open for longer than a millisecond

        cv2.imshow('Check this shit out', frame)
        key = cv2.waitKey(1)
        if key == 81 or key == 113:
            break

    webcam.release()


facedetection()

print('code completed')
