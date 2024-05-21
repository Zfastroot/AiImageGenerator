from diffusers import StableDiffusionPipeline
import torch

model_id = "stabilityai/stable-diffusion-xl-base-1.0"
pipeline = StableDiffusionPipeline.from_pretrained(model_id)
generator = torch.manual_seed(42)

def generate_image(prompt):
    return pipeline(prompt, generator=generator).images[0]
