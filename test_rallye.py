import cv2
import random
import time
import os
import mediapipe as mp
mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

def print_space():
    for i in range(50):
        print(' ')


def lancer_programme_urss():
    
    clear = lambda: os.system('cls')
    clear()
    essais = 0
    while essais < 3 :
        print_space()
        mdp = input("                                                                   Bonjour camarades, veuillez entrer le mot de passe : ")
        print_space()
        if mdp == "RIP petite Laïka" :
            print('Félicitations camarades, repose en paix brave Laïka, buvons en son honneur et quittons cette saleté de pièce. La clé était dans sa poche tout le long !')
            time.sleep(100)
        else :
            essais += 1
            if essais == 3 :
                print("Vous avez perdu et ne méritez pas de sortir vivants de cette pièces. Buvez ! ")
                time.sleep(10)
                print("Bon je rigolais, la clé est dans la poche. ")
                time.sleep(100)
            essais_restants = 3 - essais
            print('Il vous reste ' + str(essais_restants) +' essais')

flag = True

# For webcam input:
cap = cv2.VideoCapture(0)
with mp_face_detection.FaceDetection(
    model_selection=0, min_detection_confidence=0.5) as face_detection:
    while cap.isOpened():
        success, image = cap.read()
        if not success:
            print("Ignoring empty camera frame.")
            # If loading a video, use 'break' instead of 'continue'.
            continue

        # To improve performance, optionally mark the image as not writeable to
        # pass by reference.
        image.flags.writeable = False
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = face_detection.process(image)

        # Draw the face detection annotations on the image.
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        if results.detections:
            count = 0
            
            for detection in results.detections:
                count += 1
                #mp_drawing.draw_detection(image, detection)
                if count >= 4 and flag == True:
                    lancer_programme_urss()
                    flag = False
                else :
                    for a in range(118):
                        print(random.randint(0,1), end=" ")
                    print(' ')
        else :
            for a in range(118):
                if random.randint(0,5) == 1 :
                    print(' ', end=" ")
                else :
                    print(random.randint(0,1), end=" ")
            print(' ')
        # Flip the image horizontally for a selfie-view display.
        #cv2.imshow('MediaPipe Face Detection', cv2.flip(image, 1))
        if cv2.waitKey(5) & 0xFF == 27:
            break
cap.release()
