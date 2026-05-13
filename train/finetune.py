"""
This module is going to fine tune pre-trained YOLOv8 model.
It is going to use multiple methods to fine tune the model if it doesnt adapt 
itself while training on new data.
"""
from ultralytics import YOLO
from data.download import download_dataset


def finetune_model(data_yaml_path,epochs=50):
    """
    This is going to take the pre-trained model values and 
    perform changes such that the evaluation improves 
    """
    model=YOLO('yolov8n.pt')
    model.train(
        data=data_yaml_path,
        epochs=epochs,
        lr0=0.01,        # initial learning rate
        optimizer='Adam', # optimizer choice
        batch=16,        # batch size
        imgsz=640        # image size
    )
    return model


