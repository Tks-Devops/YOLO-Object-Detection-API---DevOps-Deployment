from flask import Flask, request, jsonify, send_from_directory
import cv2
import numpy as np
import os

app = Flask(__name__)

# Paths
IMAGE_PATH = "/app/devops.jpg"  # Default image
OUTPUT_DIR = "/app/static"  # Directory to store processed images
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "output.jpg")

# Ensure the output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Load YOLO model
net = cv2.dnn.readNet("/app/yolov3.weights", "/app/yolov3.cfg")
layer_names = net.getLayerNames()
output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]

# Define class labels (update as needed)
classes = {59: "person", 63: "laptop"}  # Modify as required

@app.route('/detect_default', methods=['GET'])
def detect_default_image():
    image = cv2.imread(IMAGE_PATH)
    
    if image is None:
        return jsonify({"error": f"Image not found at {IMAGE_PATH}"}), 404

    height, width, _ = image.shape
    blob = cv2.dnn.blobFromImage(image, 0.00392, (416, 416), swapRB=True, crop=False)
    net.setInput(blob)
    outputs = net.forward(output_layers)

    results = []
    for output in outputs:
        for detection in output:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5:
                # Get bounding box coordinates
                center_x, center_y, w, h = (
                    int(detection[0] * width),
                    int(detection[1] * height),
                    int(detection[2] * width),
                    int(detection[3] * height),
                )
                x, y = int(center_x - w / 2), int(center_y - h / 2)

                # Draw bounding box
                color = (0, 255, 0)  # Green
                cv2.rectangle(image, (x, y), (x + w, y + h), color, 2)
                text = f"{classes.get(class_id, 'Unknown')} {confidence:.2f}"
                cv2.putText(image, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

                results.append({"class_id": class_id, "confidence": float(confidence)})

    # Save processed image
    cv2.imwrite(OUTPUT_PATH, image)

    return jsonify({"detections": results, "image_url": "/static/output.jpg"})

# Route to serve the processed image
@app.route('/devops.jpg')
def get_image():
    return send_from_directory('/app', 'devops.jpg')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

