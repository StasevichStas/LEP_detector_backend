import queue
import threading
import time
import cv2
import os
from django.apps import apps
from django.conf import settings

task_queue = queue.Queue()


def worker():
    while True:
        task = task_queue.get()
        if task is None:
            break
        origin_path, result_path, model_choice = task

        try:
            app_config = apps.get_app_config("detector")
            model = getattr(app_config, model_choice, None)

            if model:
                img = cv2.imread(origin_path)
                results = model.predict(img, conf=0.25)
                annotated_img = results[0].plot()
                os.makedirs(os.path.dirname(result_path), exist_ok=True)
                cv2.imwrite(result_path, annotated_img)
        except Exception as e:
            print(f"Ошибка воркера: {e}")
        task_queue.task_done()


threading.Thread(target=worker, daemon=True).start()
