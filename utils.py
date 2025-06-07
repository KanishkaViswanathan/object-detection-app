from PIL import Image
import numpy as np

def preprocess_image(image):
    # Ensure image is a PIL Image in RGB mode
    if isinstance(image, np.ndarray):
        image = Image.fromarray(image)
    elif not isinstance(image, Image.Image):
        image = Image.open(image)
    if image.mode != "RGB":
        image = image.convert("RGB")
    return image

def format_results(detections):
    # Implement result formatting steps here
    pass