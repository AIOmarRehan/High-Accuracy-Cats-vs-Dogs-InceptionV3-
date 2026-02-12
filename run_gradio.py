import sys
import os

# Add the parent directory to the path so we can import the app module
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.gradio_app import demo

if __name__ == "__main__":
    print("=" * 60)
    print("Starting Cats vs Dogs Classifier (Gradio Interface)")
    print("=" * 60)
    print("\nOpen your browser and go to: http://localhost:7860")
    print("\nUpload an image of a cat or dog to get started!")
    print("\nPress Ctrl+C to stop the server.\n")
    
    demo.launch(
        server_name="127.0.0.1",
        server_port=7860,
        share=False,
        show_error=True
    )
