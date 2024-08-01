### Overview
This project focuses on classifying the gender of individuals from facial images. It employs a combination of techniques including transfer learning, fine-tuning, and custom CNN models.

1. **Transfer Learning with VGG16**
   - Trained on a dataset of 12,000 face images.
   - Achieved 55% accuracy, but was slower than desired.

2. **Fine-tuned Model from Hugging Face (rizvandwiki)**
   - Improved performance using a pre-trained model specifically designed for gender detection.
   - Provided a good balance of accuracy and speed.

3. **Face Detection with OpenCV**
   - Utilized OpenCV's in-built [harcascade model](https://docs.opencv.org/3.4/db/d28/tutorial_cascade_classifier.html) for face detection.

### Selected Model

After training multiple CNN models on a dataset of 12,000+ images with corresponding testing on 5,000+ samples, the following results were obtained:

1. **Model 1:**
   - Train Accuracy: 86%
   - Test Accuracy: 85%

2. **Model 2:**
   - Train Accuracy: 90%
   - Test Accuracy: 89%

3. **Model 3:**
   - Train Accuracy: 85%
   - Test Accuracy: 83%

Given these results, the second model was selected for the final implementation. It demonstrated a commendable balance between training and testing accuracy, achieving 90% and 89% respectively.

#### Model Performance 


| Model                       | Train Accuracy | Test Accuracy |
|-----------------------------|----------------|---------------|
| Fine-tuned VGG16            | 61%            | 55%           |
| rizvandwiki's Model         | -              | -             |
| Custom CNN Model 1          | 86%            | 85%           |
| Custom CNN Model 2          | 90%            | 89%           |
| Custom CNN Model 3          | 85%            | 83%           |
## Application Setup

### Download the Best fitted model ~

[Click Here](https://drive.google.com/file/d/1YhnwqgYIVEd92hvoZwwsxpq2qDEM65Q9/view?usp=sharing)

### Requirements
- Python 3.x
- OpenCV
- Tensorflow >=2.4
- Transformers
- ThreadPoolExecutor
- keras.applications 
- download the model & keep it in your working Directory
- [Gender Detection Model by rizvandwiki](https://huggingface.co/rizvandwiki/gender-classification-2)



### How to Use the Fine-tuned model
```bash
from transformers import AutoFeatureExtractor, AutoModelForImageClassification

extractor = AutoFeatureExtractor.from_pretrained("rizvandwiki/gender-classification-2")
model = AutoModelForImageClassification.from_pretrained("rizvandwiki/gender-classification-2")
inputs = extractor(images = train_images[image_name], return_tensors="pt" )
    with torch.no_grad():
        logits = model(**inputs).logits
        predicted_label = logits.argmax(-1).item()
        label = model.config.id2label[predicted_label]

```
### How to clone the repository & run the file

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your_username/your_project.git
   cd your_project
   ```
2. **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```
3. **Run the main file**
    ```bash
    python gender_detection_app.py
    ```

### NOTE:
This Project was a part of a College Assignment (Partial). For any inquiry please feel free to concat me or you can raise an issue in the GitHub issue section.

[MY LINKEDIN](https://www.linkedin.com/in/arya-chakraborty2002/)
[MY MAIL ID](aryachakraborty.official@gmail.com)