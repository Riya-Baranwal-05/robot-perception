"""
This is going to download and prepare the household objects dataset 
from Robotflow in YOLOv8 format
"""

def download_dataset():
    """
    This downloads the dataset from Roboflow using the API.
    It is going to save it in local data directory in YOLOv8 format.
    """
    

    from roboflow import Roboflow
    api_key = os.environ.get("ROBOFLOW_API_KEY")
    rf = Roboflow(api_key=api_key)
    project = rf.workspace("household-j10i9").project("household-khbd4")
    version = project.version(1)
    dataset = version.download("yolov8")
                
