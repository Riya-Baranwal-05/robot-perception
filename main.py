"""
Main pipeline script that connects all components:
downloads dataset, fine-tunes YOLOv8 model and evaluates performance.
"""

from data.download import download_dataset
from data.augment import augment_images
from train.finetune import finetune_model
from train.eval import eval_model

def main():
    dataset = download_dataset()
    data_yaml_path= dataset.location+"/data.yaml"
    model = finetune_model(data_yaml_path=data_yaml_path,epochs=50)
    results = eval_model(model,data_yaml_path)

if __name__ == "__main__":
    main()