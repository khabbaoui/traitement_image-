from django.shortcuts import render
from .forms import ImageUploadForm
from .utils import process_image

def home(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            method = form.cleaned_data['method']
            result_path = process_image(image, method)
            print(f"Result URL: {result_path}")  # Debug print
            return render(request, 'result.html', {'result_url': result_path})
    else:
        form = ImageUploadForm()
    return render(request, 'home.html', {'form': form})
