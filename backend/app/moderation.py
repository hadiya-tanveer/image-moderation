from transformers import pipeline
from PIL import Image, UnidentifiedImageError
from io import BytesIO

def analyze_image_mock(file_bytes: bytes) -> dict:
    # Try to load the image from the bytes
    try:
        image = Image.open(BytesIO(file_bytes))
    except UnidentifiedImageError:
        raise ValueError("Uploaded content is not a valid image.")

    # Initialize the combined results dictionary.
    combined_results = {
        "nsfw_detection": {},
        "hate_symbol_detection": {}
    }

    # NSFW Detection.
    nsfw_pipe = pipeline("image-classification", model="Falconsai/nsfw_image_detection")
    result_nsfw = nsfw_pipe(image)
    combined_results["nsfw_detection"] = result_nsfw

    # Hate Symbol Detection.
    hate_pipe = pipeline("image-classification", model="facebook/deit-base-patch16-224")
    result_hate = hate_pipe(image)
    combined_results["hate_symbol_detection"] = result_hate

    return combined_results
