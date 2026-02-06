import os
import cv2
from django.shortcuts import render
from django.apps import apps
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .proccesor import task_queue


def detect_objects(request):
    context = {}
    if request.method == "POST" and request.FILES.get("image"):
        img_file = request.FILES["image"]
        model_choice = request.POST.get("model_choice", "yolo8n")
        fs = FileSystemStorage()
        filename = fs.save(img_file.name, img_file)
        origin_path = fs.path(filename)
        result_filename = f"detected_{filename}"
        result_path = os.path.join(
            settings.MEDIA_ROOT, "detections", result_filename
        )
        task_queue.put((origin_path, result_path, model_choice))
        context["original_url"] = fs.url(filename)
        context["result_url"] = (
            f"{settings.MEDIA_URL}detections/{result_filename}" 
        )
        context["model_used"] = model_choice
        context["status"] = "Processing"
        return render(request, "detector/index.html", context)
    return render(request, "detector/index.html")


def index(request):
    return render(request, "detector/index.html")
