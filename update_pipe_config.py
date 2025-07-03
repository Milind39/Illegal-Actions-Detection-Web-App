import tensorflow as tf
from object_detection.utils import config_util
from object_detection.protos import pipeline_pb2
from google.protobuf import text_format
from set_path import PRETRAINED_MODEL_PATH, ANNOTATION_PATH  # Import paths

# Define config path
CONFIG_PATH = 'Tensorflow/workspace/models/my_ssd_mobnet/pipeline.config'
print(f"Using pipeline config: {CONFIG_PATH}")

# Load the pipeline config
config = config_util.get_configs_from_pipeline_file(CONFIG_PATH)

# Parse pipeline.config
pipeline_config = pipeline_pb2.TrainEvalPipelineConfig()
with tf.io.gfile.GFile(CONFIG_PATH, "r") as f:
    proto_str = f.read()
    text_format.Merge(proto_str, pipeline_config)

# Modify config parameters
pipeline_config.model.ssd.num_classes = 6
pipeline_config.train_config.batch_size = 4
pipeline_config.train_config.fine_tune_checkpoint = f"{PRETRAINED_MODEL_PATH}/ssd_mobilenet_v2_fpnlite_320x320_coco17_tpu-8/checkpoint/ckpt-0"
pipeline_config.train_config.fine_tune_checkpoint_type = "detection"

pipeline_config.train_input_reader.label_map_path = f"{ANNOTATION_PATH}/label_map.pbtxt"
pipeline_config.train_input_reader.tf_record_input_reader.input_path[:] = [f"{ANNOTATION_PATH}/train.record"]

pipeline_config.eval_input_reader[0].label_map_path = f"{ANNOTATION_PATH}/label_map.pbtxt"
pipeline_config.eval_input_reader[0].tf_record_input_reader.input_path[:] = [f"{ANNOTATION_PATH}/test.record"]

# Save modified config back to pipeline.config
config_text = text_format.MessageToString(pipeline_config)
with tf.io.gfile.GFile(CONFIG_PATH, "wb") as f:
    f.write(config_text.encode('utf-8'))

print("Pipeline configuration updated successfully.")
