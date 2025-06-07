from transformers import pipeline
from utils import preprocess_image
from PIL import ImageDraw, ImageFont

class ObjectDetector:
    def __init__(self):
        self.detector = None

    def load_model(self):
        # You can change the model to any supported object-detection model from Hugging Face
        self.detector = pipeline("object-detection", model="facebook/detr-resnet-50")

    def detect_objects(self, image):
        # Preprocess the image to ensure correct format
        image = preprocess_image(image)
        results = self.detector(image)

        # Draw bounding boxes
        draw = ImageDraw.Draw(image)
        try:
            font = ImageFont.truetype("arial.ttf", 16)
        except:
            font = ImageFont.load_default()
        for obj in results:
            box = obj["box"]
            label = f"{obj['label']} {obj['score']:.2f}"
            draw.rectangle([box["xmin"], box["ymin"], box["xmax"], box["ymax"]], outline="red", width=2)
            draw.text((box["xmin"], box["ymin"] - 10), label, fill="red", font=font)
        return image