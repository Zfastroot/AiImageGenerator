from django.shortcuts import render

from django.shortcuts import render
from django.http import JsonResponse
from PIL import Image
from io import BytesIO
from diffusers import StableDiffusionPipeline


def app(request):
    return render(request,'app/App.html')

# model_id1 = "dreamlike-art/dreamlike-diffusion-1.0"
# model_id2 = "stabilityai/stable-diffusion-xl-base-1.0"

def generator(request):
    if request.method == 'POST':
        prompt = request.POST.get('prompt')
        image = generate_image(prompt)
        image_data = BytesIO()
        image.save(image_data, format='PNG')
        return JsonResponse({'image': image_data.getvalue().decode('utf-8')})
    return render(request, 'generator.html')

def generate_image(prompt):
    model_id = "dreamlike-art/dreamlike-diffusion-1.0"
    pipe = StableDiffusionPipeline.from_pretrained(model_id, use_safetensors=True)
    image = pipe(prompt).images[0]
    return image

