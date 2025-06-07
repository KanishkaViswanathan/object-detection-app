from gradio import Interface
from detector import ObjectDetector

def main():
    detector = ObjectDetector()
    detector.load_model()

    iface = Interface(
        fn=detector.detect_objects,
        inputs="image",
        outputs="image",  # Change from "json" to "image"
        title="Object Detection App",
        description="Upload an image to detect objects using a pretrained Hugging Face model."
    )
    
    iface.launch()

if __name__ == "__main__":
    main()