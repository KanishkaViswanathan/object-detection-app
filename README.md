# Object Detection Application

This project is an object detection application that utilizes a pretrained model from Hugging Face and exposes its functionality through a Gradio interface. 

## Project Structure

```
object-detection-app
├── src
│   ├── app.py          # Entry point for the Gradio application
│   ├── detector.py     # Contains the ObjectDetector class for model handling
│   └── utils.py        # Utility functions for image processing
├── requirements.txt     # Lists project dependencies
└── README.md            # Documentation for the project
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd object-detection-app
   ```

2. **Install the required packages:**
   It is recommended to use a virtual environment. You can create one using `venv` or `conda`.

   For `venv`:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

   Then install the dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the application, execute the following command:

```
python src/app.py
```

This will start a Gradio interface in your web browser where you can upload images and see the object detection results.

## Object Detection Capabilities

The application uses a pretrained model from Hugging Face to detect objects in images. It supports various object categories and provides bounding boxes around detected objects along with their confidence scores.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.

