import cv2
import time

def analyze_confidence(duration=20):

    cap = cv2.VideoCapture(0)

    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )

    face_frames = 0
    total_frames = 0

    start_time = time.time()

    while time.time() - start_time < duration:

        ret, frame = cap.read()

        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray,1.3,5)

        total_frames += 1

        if len(faces) > 0:
            face_frames += 1

        cv2.imshow("Confidence Analysis", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()

    if total_frames == 0:
        return 0

    confidence_score = int((face_frames / total_frames) * 100)

    return confidence_score