"""
This is going perform image augementation to diversify existing dataset and make it robust
for real word scenarios.
It is also going to help with class imbalance for underepresented classes by generating more images.
"""

def augment_images():
    """
    This will take an image and augment them to create version of image
    using geometric transformations ,color space augmentation and kernel filters & noise.
    It is going to return set of newly generated images from single image of the class.
    """