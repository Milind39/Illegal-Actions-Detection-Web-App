import os
import subprocess
from set_path import * # Import paths


def generate_tfrecord(dataset_type):
    """Generate TFRecord for the given dataset type (Train or Test)."""
    image_path = os.path.join(IMAGE_PATH, dataset_type)
    output_path = os.path.join(ANNOTATION_PATH, f"{dataset_type}.record")
    label_map_path = os.path.join(ANNOTATION_PATH, "label_map.pbtxt")
    script_path = os.path.join(SCRIPTS_PATH, "generate_tfrecord.py")

    command = f"python {script_path} -x {image_path} -l {label_map_path} -o {output_path}"

    try:
        subprocess.run(command, shell=True, check=True)
        print(f"Successfully generated {dataset_type}.record")
    except subprocess.CalledProcessError as e:
        print(f"Error generating {dataset_type}.record: {e}")


# Run the function for both Train and Test datasets
generate_tfrecord("Train")
generate_tfrecord("Test")
