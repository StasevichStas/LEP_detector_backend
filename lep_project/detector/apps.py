from django.apps import AppConfig
from django.conf import settings

from ultralytics import YOLO
import os


class DetectorConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "detector"

    def ready(self):
        if os.environ.get("RUN_MAIN") == "true":
            base_dir = settings.BASE_DIR
            yolo8n_path = os.path.join(
                base_dir, "ml_models", "best_weight_yolo8n.pt"
            )
            yolo11n_path = os.path.join(
                base_dir, "ml_models", "best_weight_yolo11n.pt"
            )
            self.yolo8n = YOLO(yolo8n_path)
            self.yolo11n = YOLO(yolo11n_path)
