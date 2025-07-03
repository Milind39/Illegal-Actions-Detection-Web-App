import os
import subprocess


def clone_tensorflow_models():
    """Clones the TensorFlow models repository inside the 'Tensorflow' directory."""
    tensorflow_dir = "Tensorflow"

    # Ensure the directory exists
    if not os.path.exists(tensorflow_dir):
        os.makedirs(tensorflow_dir)

    # Clone the repository
    command = f"git clone https://github.com/tensorflow/models"

    try:
        subprocess.run(command, shell=True, check=True)
        print("Successfully cloned TensorFlow Models repository.")
    except subprocess.CalledProcessError as e:
        print(f"Error cloning repository: {e}")


# Run the function
clone_tensorflow_models()
