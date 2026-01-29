import os
import cv2
import numpy as np
from django.shortcuts import render
from django.apps import apps
from django.conf import settings
from django.core.files.storage import FileSystemStorage


def detect_objects(request):
    context = {}
    if request.method == "POST" and request.FILES.get("image"):
        img_file = request.FILES["image"]
        model_choice = request.POST.get("model_choice", "yolo8n")
        app_config = apps.get_app_config("detector")

        model = getattr(app_config, model_choice, None)

        if model:
            fs = FileSystemStorage()
            filename = fs.save(img_file.name, img_file)
            origin_path = fs.path(filename)
            img = cv2.imread(origin_path)

            results = model.predict(img, conf=0.25)
            annotated_img = results[0].plot()

            result_filename = f"detected_{filename}"
            result_dir = os.path.join(settings.MEDIA_ROOT, "detections")
            os.makedirs(result_dir, exist_ok=True)

            result_path = os.path.join(result_dir, result_filename)
            cv2.imwrite(result_path, annotated_img)

            context["original_url"] = fs.url(filename)
            context["result_url"] = (
                f"{settings.MEDIA_URL}detections/{result_filename}"
            )
            context["model_used"] = model_choice
        else:
            context["error"] = "Модель не загружена."

        return render(request, "detector/index.html", context)


def index(request):
    return render(request, "detector/index.html")
