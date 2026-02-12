import gradio as gr
from PIL import Image
from .model import predict
import os

model_path = os.path.join(
    os.path.dirname(os.path.dirname(__file__)), 
    "saved_model", 
    "InceptionV3_Dogs_and_Cats_Classification.h5"
)

def classify_image(image):
    if image is None:
        return None, {"error": "Please upload an image"}
    
    try:
        label, confidence, probs = predict(image)
        results = {
            "Predicted Class": label,
            "Confidence": f"{confidence * 100:.2f}%",
            "Cat Probability": f"{probs['Cat'] * 100:.2f}%",
            "Dog Probability": f"{probs['Dog'] * 100:.2f}%"
        }
        return image, results
    
    except Exception as e:
        return image, {"error": f"Classification failed: {str(e)}"}

with gr.Blocks(title="Cats vs Dogs Classifier", theme=gr.themes.Soft()) as demo:
    gr.Markdown(
        """
        # Cats vs Dogs Classifier
        
        Upload an image of a cat or dog, and the InceptionV3 model will classify it!
        
        **Model:** InceptionV3 (Transfer Learning)  
        **Classes:** Cat | Dog  
        **Image Size:** 256x256 pixels
        """
    )
    
    with gr.Row():
        with gr.Column():
            gr.Markdown("### Upload Image")
            image_input = gr.Image(
                type="pil",
                label="Upload Image",
                sources=["upload", "webcam"],
                interactive=True
            )
        with gr.Column():
            gr.Markdown("### Prediction Results")
            output = gr.JSON(label="Classification Results")
    
    submit_btn = gr.Button("Classify Image", variant="primary", scale=1)
    submit_btn.click(
        fn=classify_image,
        inputs=image_input,
        outputs=[image_input, output]
    )
    
    gr.Markdown("### Examples")
    gr.Examples(
        examples=[
            ["examples/cat1.jpg"],
            ["examples/cat2.jpg"],
            ["examples/cat3.jpg"],
            ["examples/dog1.jpg"],
            ["examples/dog2.jpg"]
        ],
        inputs=image_input,
        outputs=[image_input, output],
        fn=classify_image,
        run_on_click=True,
        label="Example Images (Click to run)"
    )

if __name__ == "__main__":
    demo.launch(
        server_name="0.0.0.0",
        server_port=7860,
        share=False,
        show_error=True
    )