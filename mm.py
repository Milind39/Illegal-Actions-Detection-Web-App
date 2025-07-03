import os

# Set paths for training
MODEL_DIR = "models/my_ssd_mobnet"
PIPELINE_CONFIG_PATH = "models/my_ssd_mobnet/pipeline.config"
CHECKPOINT_DIR = "models/my_ssd_mobnet"

# Construct the training command
train_command = f"""
python Tensorflow/models/research/object_detection/model_main_tf2.py ^
    --model_dir={MODEL_DIR} ^
    --pipeline_config_path={PIPELINE_CONFIG_PATH} ^
    --checkpoint_dir={CHECKPOINT_DIR}
"""

# Run the training command
print("🚀 Starting model training... Please wait.")
os.system(train_command)
print("✅ Training process completed!")
