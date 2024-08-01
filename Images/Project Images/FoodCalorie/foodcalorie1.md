### Abstract
This project presents a novel approach to estimate the calories and weight of food items using image and
video analysis. Using state-of-the-art YOLO models for object detection and classification, we first detect
and crop the food contained within bowls. Subsequently, the area of the detected food is calculated, and
a pretrained KNN model predicts the weight based on this area. Caloric content is then derived using
a dictionary of food items and their respective calorie values per 100 grams. The system provides an
accurate estimate of unique food items, their count, total calories, and weight.
        
### Project Pipeline
- **:orange[Input Processor]** 
    The input processor is responsible for handling three types of inputs: PDF, image,
    and video. For PDF inputs, the processor extracts images from the document. For videos, the processor
    selects the median frame to ensure a representative image is used for analysis. Image inputs are directly
    forwarded for processing. The first step involves detecting the bowl containing the food using the YOLO
    V8X model. This object detection model is trained to accurately identify bowls in various conditions.
    Once the bowl is detected, a bounding box is created around it, isolating it from the rest of the image
    for further processing.