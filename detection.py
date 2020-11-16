from tkinter import *
import tkinter as tk
import cv2
import numpy as np
import time

class Detection :

    def __init__(self,root):
        detect = tk.Toplevel(root)
        detect.title("Detection d'objet")
        detect.geometry("+%d+%d" % ((detect.winfo_screenwidth() / 2) - 200, (detect.winfo_screenheight() / 2) - 260))

        btn11 = tk.Button(detect, text="En temps reel", command = lambda : Detection.detected(1))
        btn11.config(height=10, width=20)
        btn11.pack(side=LEFT)
        btn12 = tk.Button(detect, text="Sur image", command= lambda : Detection.detected(2))
        btn12.config(height=10, width=20)
        btn12.pack(side=LEFT)


    def detected(a):

        # Load Yolo

        net = cv2.dnn.readNet("yolov3-tiny.weights", "yolov3-tiny.cfg")
        classes = []

        with open("coco.names", "r") as f:
            classes = [line.strip() for line in f.readlines()]
        layer_names = net.getLayerNames()
        output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
        colors = np.random.uniform(0, 255, size=(len(classes), 3))

        if a == 1 :

            # load camera

            cap = cv2.VideoCapture(0)
            #cap = cv2.imread('/Users/vince/Desktop/Projet_Image_ISC/myImage.jpg')

            font = cv2.FONT_HERSHEY_PLAIN
            frame_id = 0



            while True:
                _, frame = cap.read()
                frame_id += 1
                height, width, channels = frame.shape
                # detecting objects

                blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False)

                net.setInput(blob)
                outs = net.forward(output_layers)

                # showing information on the screen


                class_ids = []
                confidences = []
                boxes = []
                for out in outs:
                    for detection in out:
                        scores = detection[5:]
                        class_id = np.argmax(scores)
                        confidence = scores[class_id]
                        if confidence > 0.2:
                            # Object detected

                            center_x = int(detection[0] * width)
                            center_y = int(detection[1] * height)
                            w = int(detection[2] * width)
                            h = int(detection[3] * height)

                            # Rectangle coordinates

                            x = int(center_x - w / 2)
                            y = int(center_y - h / 2)
                            boxes.append([x, y, w, h])
                            confidences.append(float(confidence))
                            class_ids.append(class_id)
                indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.4, 0.3)
                for i in range(len(boxes)):
                    if i in indexes:
                        x, y, w, h = boxes[i]
                        label = str(classes[class_ids[i]])
                        confidence = confidences[i]

                        color = colors[class_ids[i]]

                        cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)

                        cv2.rectangle(frame, (x, y), (x + w, y + 30), color, -1)

                        cv2.putText(frame, label + " " + str(round(confidence, 2)), (x, y + 30), font, 2, (255, 255, 255), 2)

                cv2.putText(frame, "Touche Echap pour quitter", (10, 50), font, 2, (255, 255, 0), 3)
                cv2.imshow("Image1", frame)

                key = cv2.waitKey(1)
                if key == 27:
                    cap.release()
                    cv2.destroyAllWindows()

            cap.release()
            cv2.destroyAllWindows()

        elif a == 2 :

            cap = cv2.imread('im.jpg')
            (height, width, channels) = cap.shape
            font = cv2.FONT_HERSHEY_PLAIN
            # detecting objects

            blob = cv2.dnn.blobFromImage(cap, 0.00392, (416, 416), (0, 0, 0), True, crop=False)

            net.setInput(blob)
            outs = net.forward(output_layers)

            # showing information on the screen

            class_ids = []
            confidences = []
            boxes = []
            for out in outs:
                for detection in out:
                    scores = detection[5:]
                    class_id = np.argmax(scores)
                    confidence = scores[class_id]
                    if confidence > 0.2:
                        # Object detected

                        center_x = int(detection[0] * width)
                        center_y = int(detection[1] * height)
                        w = int(detection[2] * width)
                        h = int(detection[3] * height)

                        # Rectangle coordinates

                        x = int(center_x - w / 2)
                        y = int(center_y - h / 2)
                        boxes.append([x, y, w, h])
                        confidences.append(float(confidence))
                        class_ids.append(class_id)
                        indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.4, 0.3)
            for i in range(len(boxes)):
                if i in indexes:
                    x, y, w, h = boxes[i]
                    label = str(classes[class_ids[i]])
                    confidence = confidences[i]

                    color = colors[class_ids[i]]

                    cv2.rectangle(cap, (x, y), (x + w, y + h), color, 2)

                    cv2.rectangle(cap, (x, y), (x + w, y + 30), color, -1)

                    cv2.putText(cap, label + " " + str(round(confidence, 2)), (x, y + 30), font, 2, (255, 255, 255), 2)

            cv2.imshow("Image1", cap)
            cv2.waitKey(1)
            if key == 27:
                cap.release()
                cv2.destroyAllWindows()




