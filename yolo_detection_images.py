import numpy as np
import cv2


def YoloDetection(image_path):
    confidenceThreshold = 0.5
    NMSThreshold = 0.3

    modelConfiguration = 'cfg/yolov3.cfg'
    modelWeights = 'yolov3.weights'

    labelsPath = 'df2.names'
    labels = open(labelsPath).read().strip().split('\n')

    np.random.seed(10)
    COLORS = np.random.randint(0, 255, size=(len(labels), 3), dtype="uint8")

    net = cv2.dnn.readNetFromDarknet(modelConfiguration, modelWeights)

    # image = cv2.imread('images/a.jpg')
    image = cv2.imread(image_path)

    (H, W) = image.shape[:2]

    # Determine output layer names
    layerName = net.getLayerNames()
    layerName = [layerName[i[0] - 1] for i in net.getUnconnectedOutLayers()]

    blob = cv2.dnn.blobFromImage(
        image, 1 / 255.0, (416, 416), swapRB=True, crop=False)
    net.setInput(blob)
    layersOutputs = net.forward(layerName)

    boxes = []
    confidences = []
    classIDs = []

    for output in layersOutputs:
        for detection in output:
            scores = detection[5:]
            classID = np.argmax(scores)
            confidence = scores[classID]
            if confidence > confidenceThreshold:
                box = detection[0:4] * np.array([W, H, W, H])
                (centerX, centerY,  width, height) = box.astype('int')
                x = int(centerX - (width/2))
                y = int(centerY - (height/2))

                boxes.append([x, y, int(width), int(height)])
                confidences.append(float(confidence))
                classIDs.append(classID)

    # Apply Non Maxima Suppression
    detectionNMS = cv2.dnn.NMSBoxes(
        boxes, confidences, confidenceThreshold, NMSThreshold)

    # if(len(detectionNMS) > 0):
    #     for i in detectionNMS.flatten():
    #         (x, y) = (boxes[i][0], boxes[i][1])
    #         (w, h) = (boxes[i][2], boxes[i][3])

    #         color = [int(c) for c in COLORS[classIDs[i]]]
    #         cv2.rectangle(image, (x, y), (x + w, y + h), color, 2)
    #         text = '{}: {:.4f}'.format(labels[classIDs[i]], confidences[i])
    #         cv2.putText(image, text, (x, y - 5),
    #                     cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

    # cv2.imshow('Image', image)
    # cv2.waitKey(0)

    outputs = {}

    if len(detectionNMS) > 0:
        outputs['detections'] = {}  # dictionary
        outputs['detections']['labels'] = []  # list
        for i in detectionNMS.flatten():
            detection = {}
            detection['labels'] = (labels[classIDs[i]])
            detection['confidence'] = (confidences[i])
            detection['x'] = (boxes[i][0])
            detection['y'] = (boxes[i][1])
            detection['w'] = (boxes[i][2])
            detection['h'] = (boxes[i][3])
            outputs['detections']['labels'].append(detection)
    else:
        outputs['detections'] = 'No object detected'

    return outputs


def YoloDetectionImg(image):
    confidenceThreshold = 0.5
    NMSThreshold = 0.3

    modelConfiguration = 'cfg/yolov3.cfg'
    modelWeights = 'yolov3.weights'

    labelsPath = 'df2.names'
    labels = open(labelsPath).read().strip().split('\n')

    np.random.seed(10)
    COLORS = np.random.randint(0, 255, size=(len(labels), 3), dtype="uint8")

    net = cv2.dnn.readNetFromDarknet(modelConfiguration, modelWeights)

    # image = cv2.imread('images/a.jpg')
    # image = cv2.imread(image)

    (H, W) = image.shape[:2]

    # Determine output layer names
    layerName = net.getLayerNames()
    layerName = [layerName[i[0] - 1] for i in net.getUnconnectedOutLayers()]

    blob = cv2.dnn.blobFromImage(
        image, 1 / 255.0, (416, 416), swapRB=True, crop=False)
    net.setInput(blob)
    layersOutputs = net.forward(layerName)

    boxes = []
    confidences = []
    classIDs = []

    for output in layersOutputs:
        for detection in output:
            scores = detection[5:]
            classID = np.argmax(scores)
            confidence = scores[classID]
            if confidence > confidenceThreshold:
                box = detection[0:4] * np.array([W, H, W, H])
                (centerX, centerY,  width, height) = box.astype('int')
                x = int(centerX - (width/2))
                y = int(centerY - (height/2))

                boxes.append([x, y, int(width), int(height)])
                confidences.append(float(confidence))
                classIDs.append(classID)

    # Apply Non Maxima Suppression
    detectionNMS = cv2.dnn.NMSBoxes(
        boxes, confidences, confidenceThreshold, NMSThreshold)

    # if(len(detectionNMS) > 0):
    #     for i in detectionNMS.flatten():
    #         (x, y) = (boxes[i][0], boxes[i][1])
    #         (w, h) = (boxes[i][2], boxes[i][3])

    #         color = [int(c) for c in COLORS[classIDs[i]]]
    #         cv2.rectangle(image, (x, y), (x + w, y + h), color, 2)
    #         text = '{}: {:.4f}'.format(labels[classIDs[i]], confidences[i])
    #         cv2.putText(image, text, (x, y - 5),
    #                     cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

    # cv2.imshow('Image', image)
    # cv2.waitKey(0)

    outputs = {}

    if len(detectionNMS) > 0:
        outputs['detections'] = {}  # dictionary
        outputs['detections']['labels'] = []  # list
        for i in detectionNMS.flatten():
            detection = {}
            detection['labels'] = (labels[classIDs[i]])
            detection['confidence'] = (confidences[i])
            detection['x'] = (boxes[i][0])
            detection['y'] = (boxes[i][1])
            detection['w'] = (boxes[i][2])
            detection['h'] = (boxes[i][3])
            outputs['detections']['labels'].append(detection)
    else:
        outputs['detections'] = 'No object detected'

    return outputs


def YoloDetectionOnlyTags(image_path):
    confidenceThreshold = 0.5
    NMSThreshold = 0.3

    modelConfiguration = 'cfg/yolov3.cfg'
    modelWeights = 'yolov3.weights'

    labelsPath = 'df2.names'
    labels = open(labelsPath).read().strip().split('\n')

    np.random.seed(10)
    COLORS = np.random.randint(0, 255, size=(len(labels), 3), dtype="uint8")

    net = cv2.dnn.readNetFromDarknet(modelConfiguration, modelWeights)

    # image = cv2.imread('images/a.jpg')
    image = cv2.imread(image_path)

    (H, W) = image.shape[:2]

    # Determine output layer names
    layerName = net.getLayerNames()
    layerName = [layerName[i[0] - 1] for i in net.getUnconnectedOutLayers()]

    blob = cv2.dnn.blobFromImage(
        image, 1 / 255.0, (416, 416), swapRB=True, crop=False)
    net.setInput(blob)
    layersOutputs = net.forward(layerName)

    boxes = []
    confidences = []
    classIDs = []

    for output in layersOutputs:
        for detection in output:
            scores = detection[5:]
            classID = np.argmax(scores)
            confidence = scores[classID]
            if confidence > confidenceThreshold:
                box = detection[0:4] * np.array([W, H, W, H])
                (centerX, centerY,  width, height) = box.astype('int')
                x = int(centerX - (width/2))
                y = int(centerY - (height/2))

                boxes.append([x, y, int(width), int(height)])
                confidences.append(float(confidence))
                classIDs.append(classID)

    # Apply Non Maxima Suppression
    detectionNMS = cv2.dnn.NMSBoxes(
        boxes, confidences, confidenceThreshold, NMSThreshold)

    # if(len(detectionNMS) > 0):
    #     for i in detectionNMS.flatten():
    #         (x, y) = (boxes[i][0], boxes[i][1])
    #         (w, h) = (boxes[i][2], boxes[i][3])

    #         color = [int(c) for c in COLORS[classIDs[i]]]
    #         cv2.rectangle(image, (x, y), (x + w, y + h), color, 2)
    #         text = '{}: {:.4f}'.format(labels[classIDs[i]], confidences[i])
    #         cv2.putText(image, text, (x, y - 5),
    #                     cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

    # cv2.imshow('Image', image)
    # cv2.waitKey(0)

    outputs = {}

    if len(detectionNMS) > 0:
        # dictionary is not used br sure of not dublication
        outputs['labels'] = []
        # outputs['detections']['labels'] = []  # list
        for i in detectionNMS.flatten():
            # detection = {}
            # detection['label'] = (labels[classIDs[i]])
            # detection['confidence'] = (confidences[i])
            # detection['x'] = (boxes[i][0])
            # detection['y'] = (boxes[i][1])
            # detection['w'] = (boxes[i][2])
            # detection['h'] = (boxes[i][3])
            outputs['labels'].append(labels[classIDs[i]])
    else:
        outputs['labels'] = 'No object detected'

    return outputs
