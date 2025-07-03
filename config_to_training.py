import os
import shutil
from set_path import PRETRAINED_MODEL_PATH, MODEL_PATH  # Import paths

# Define the custom model name
CUSTOM_MODEL_NAME = 'my_ssd_mobnet'

# Create the model directory
model_dir = os.path.join(MODEL_PATH, CUSTOM_MODEL_NAME)
os.makedirs(model_dir, exist_ok=True)
print(f"Created directory: {model_dir}")

# Define source and destination paths for the pipeline.config file
source_config = os.path.join(PRETRAINED_MODEL_PATH, 'ssd_mobilenet_v2_fpnlite_320x320_coco17_tpu-8', 'pipeline.config')
destination_config = os.path.join(model_dir, 'pipeline.config')

# Copy the pipeline.config file
try:
    shutil.copy(source_config, destination_config)
    print(f"Copied pipeline.config to {destination_config}")
except FileNotFoundError as e:
    print(f"Error: {e}")
