from set_path import APIMODEL_PATH, MODEL_PATH  # Import paths

# Define the custom model name
CUSTOM_MODEL_NAME = 'my_ssd_mobnet'

# Construct the training command
train_command = (
    f"python {APIMODEL_PATH}/research/object_detection/model_main_tf2.py "
    f"--model_dir={MODEL_PATH}/{CUSTOM_MODEL_NAME} "
    f"--pipeline_config_path={MODEL_PATH}/{CUSTOM_MODEL_NAME}/pipeline.config "
    f"--num_train_steps=5000"
)

# Print the training command
print(train_command)
