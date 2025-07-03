import cv2
import numpy as np
import tensorflow as tf
from loadTrainModelFrom_checkpoint import detect_fn
from set_path import *
from object_detection.utils import label_map_util
from object_detection.utils import visualization_utils as viz_utils

# Load category index
category_index = label_map_util.create_category_index_from_labelmap(ANNOTATION_PATH + '/label_map.pbtxt')

running = False  # Flag to control the detection
detected_label = None  # Store detected label globally

def start_detection():
    global running
    running = True

def stop_detection():
    """Stops object detection"""
    global running, detected_label
    running = False
    detected_label = None  # Clear detected object when stopping


def generate_frames():
    """Captures video frames, applies object detection, and streams frames for Django views."""
    global running, detected_label
    cap = cv2.VideoCapture(0)

    while running and cap.isOpened():
        ret, frame = cap.read()
        if not ret or not running:  # Stop processing if running is False
            break

        image_np = np.array(frame, dtype=np.uint8)
        input_tensor = tf.convert_to_tensor(np.expand_dims(image_np, 0), dtype=tf.float32)
        detections = detect_fn(input_tensor)

        num_detections = int(detections.pop('num_detections'))
        detections = {key: value[0, :num_detections].numpy() for key, value in detections.items()}
        detections['num_detections'] = num_detections
        detections['detection_classes'] = detections['detection_classes'].astype(np.int64)

        label_id_offset = 1
        detected_labels = [
            category_index.get(cls_id + label_id_offset, {}).get('name', '')
            for cls_id in detections['detection_classes']
        ]
        print(detected_labels[0])

        # Store detected label persistently if found
        if "smoking" in detected_labels:
            detected_label = "smoking"

        viz_utils.visualize_boxes_and_labels_on_image_array(
            image_np,
            detections['detection_boxes'],
            detections['detection_classes'] + label_id_offset,
            detections['detection_scores'],
            category_index,
            use_normalized_coordinates=True,
            max_boxes_to_draw=5,
            min_score_thresh=0.5,
            agnostic_mode=False
        )

        _, buffer = cv2.imencode('.jpg', image_np)
        frame = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

    cap.release()
    detected_label = None  # Reset detected object when streaming stops

def get_detected_object():
    """Returns the last detected label"""
    global detected_label
    return detected_label
