from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import torch

# Detect device
device = "cuda" if torch.cuda.is_available() else "cpu"

# Load model
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained(
    "Salesforce/blip-image-captioning-base"
)

# Move model to GPU if available
model.to(device)


def generate_caption(image):

    inputs = processor(image, return_tensors="pt").to(device)

    out = model.generate(**inputs)

    caption = processor.decode(out[0], skip_special_tokens=True)

    return caption