# Robot Perception using YOLOv8
This project is going to work on small household relevant dataset and recognize object through perception pipeline. 
Node in ROS2 will be publishing detection results to complete showcase robot perception pipeline.


## Demo
<!--GIF Will go here-->

## What does this project do
Robot needs to see its environment and identify humans, objects or the things it has to work on or navigate through. 
I am going to fine tune the existing YOLOv8 model for this specific project. Training from scratch is needed when we need 
a model that doesn't exist for particular task. In CV , it is common practise to fine tune existing models where changing few parameters
we can get good results.

## Dataset
-household Computer Vision Model: https://universe.roboflow.com/household-j10i9/household-khbd4
-Total Images : 23575 
-Dataset Split : Train set = 20655 , Valid set = 1949 , Test set = 971
-Number of classes : 101
-Classes = Bottle ,Chair ,Cup ,Plate ,Box ,Book ,Tomato ,Laptop ,Bed ,Bowl ,Spoon ,Fork ,Sink ,Sofa ,Vase ,Window ,Pen ,Microwave ,Egg ,   Potato ,DiningTable ,Bread , Watch ,Mug ,Knife ,Mirror ,BasketBall ,Pencil ,Shelf ,Cloth and 71 more.
## Project Structure

robot-perception/

-data/
--- download.py # script to fetch/prepare dataset
--- augment.py # data augmentation helpers
-train/
--- finetune.py # YOLOv8 fine-tuning script
--- eval.py # mAP, speed benchmarks
-ros2_node/
--- detector_node.py # ROS 2 node publishing detections
--- launch # launch files
--- camera_publisher.py # Real time prediction
-notebooks/  
--- results.ipynb # visualizations and analysis
-docker/ 
--- Dockerfile requirements.txt # reproducible environment
-README.md


## How to Run
- Clone the repo
- Install requirements: pip install -r requirements.txt
- Place best.pt (your trained YOLOv8 model) in ros2_node/
- Run the camera script i.e. camera_publisher.py


## Benchmarks
- mAP50 : 0.557
- mAP50-95 : 0.416
- Precision : 0.642
- Recall : 0.511
- Epochs trained : 5 
- Model training in progress with 50 epochs


## Limitations
- Model may underperform on objects that are partially occluded or at unusual scales not represented in training data
- Performance degrades under poor lighting conditions since the dataset may not represent all real-world lighting scenarios
- The dataset with so many classes can cause model to prioritize frequently occurring classes, otherwise known as class imbalance.


## References 
- [YOLOv8 / Ultralytics](https://github.com/ultralytics/ultralytics)
- https://universe.roboflow.com/household-j10i9/household-khbd4