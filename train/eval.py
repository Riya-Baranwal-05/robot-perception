"""
This module is going to test the trained model using test dataset.
"""
from ultralytics import YOLO 

def eval_model(model,data_yaml_path):
    """
    This is going to take test dataset and the fine tuned model 
    and validate it using mAP metrics.
    """
    results = model.val(data=data_yaml_path)
    print(results.box.map)
    print(results.box.map50)
    return results