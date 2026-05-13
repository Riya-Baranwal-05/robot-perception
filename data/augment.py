"""
This is going perform image augementation to diversify existing dataset and make it robust
for real word scenarios.
It is also going to help with class imbalance for underepresented classes by generating more images.
"""
import cv2

def augment_images(image):
    """
    This will take an image and augment them to create version of image
    using geometric transformations ,color space augmentation and kernel filters & noise.
    It is going to return set of newly generated images from single image of the class.
    """

    height,width = image.shape[:2]
    center = (width/2,height/2)
    rotate_matrix = cv2.getRotationMatrix2D(center=center,angle =90,scale =1)
    rotated_image_1 = cv2.warpAffine(src=image,M=rotate_matrix,dsize=(width,height))
   
    flipped_image_1 =cv2.flip(image,flipCode=0)

    medium_sized_image_1 =cv2.resize(image,(780,540),interpolation=cv2.INTER_LINEAR)

    alpha = 1.5
    beta= 60
    adjusted_image_1 =cv2.convertScaleAbs(image,alpha=alpha,beta=beta)

    return rotated_image_1 , flipped_image_1, medium_sized_image_1,adjusted_image_1