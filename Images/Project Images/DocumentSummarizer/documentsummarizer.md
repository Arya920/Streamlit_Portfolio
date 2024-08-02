## Overview
Unlock the power of Natural Language Processing (NLP) with our Automatic Document Summarization Model (ADSM), designed to effortlessly distill the essence of lengthy articles and research papers. Tired of drowning in information overload? Let our ADSM be your guide, providing crisp and coherent summaries, saving you valuable time and effort.

## Problem Statement

Long articles and research papers contain a wealth of information, posing a challenge for readers to efficiently grasp essential details. The objective is to develop an Automatic Document Summarization Model (ADSM) using NLP techniques. This model will employ advanced methods to generate succinct and meaningful summaries of lengthy textual documents.

## Features 

### 1. Frontend 

- **Text Input:** Users can input documents through typing or copy-pasting.
- **Summary Length Selection:** Option for users to choose the desired length of the summary.
- **Model Selection:** Users can choose from various summarization models.
- **Language Selection:** Support for over 150 languages.
- **Keyword Generation:** Automatic extraction of key words based on the document.
- **Text-to-Speech:** Option to listen to the summarized document.

### 2. Models 

- **Fine-tuned BART:** Created a fine-tuned BART model (uploaded to HuggingFace). [link to our model](https://huggingface.co/datasets/scientific_papers?row=0)
- **Pegasus:** Used a powerful pre-trained model for abstractive summarization.
- **BART:** Leveraged a pre-trained Bidirectional and Auto-Regressive Transformers for text generation.

### 3. Datasets

Scientific papers datasets from ArXiv and PubMed OpenAccess repositories. The datasets include:

- **article:** The document body, presented in paragraphs.
- **abstract:** The summary of the document.
- **section_names:** Clearly defined titles of document sections.

[Explore Datasets](https://huggingface.co/datasets/scientific_papers?row=0)

## Seamless User Experience

1. **Input:** Type or paste your document.
2. **Customize:** Choose your preferred summary length and model.
3. **Diversity:** Select from a multitude of languages.
4. **Discover:** Automatically generated keywords provide extra insights.
5. **Listen:** Transform your document into an auditory experience with text-to-speech.


![flowchart](https://github.com/Arya920/Document_Summarizer/assets/57805586/c932268c-1851-45ed-84d9-314383d3b0f8)

## Important components in Action
1. **Keyword Generation** - 
This Python code defines a function for keyword extraction using the KeyBERT library. It initializes a KeyBERT model based on BERT embeddings, extracts keywords and their scores from the input text, and then filters out similar keywords to ensure diversity. The function returns a list of filtered keywords along with their scores. The similarity between keywords is determined using cosine similarity, and only keywords with a similarity score below a threshold (0.8) are considered unique.

2. **Translation** - 
This Python script utilizes the Hugging Face Transformers library to perform language translation. It defines a function called translate that takes a source text, target language, and maximum length as input parameters. The function uses a pre-trained sequence-to-sequence model ('facebook/nllb-200-distilled-600M') for translation. It leverages the Hugging Face pipeline class to create a translation pipeline, and then translates the source text to the specified target language. The script also defines a dictionary language that maps human-readable language names to their respective language codes used by the translation model.

4. **Text-to-Speech** - The "text_to_speech" function utilizes the gTTS library to convert the provided 'text' into speech, specifying the language through 'lang_key'. The synthesized speech is then saved as 'saved_audio.wav'.
   
6. **Fine-Tuned Model** - This model leveraged LoRA and PEFT in creating long text summaries. Starting with gathering components such as a base model (facebook/bart-large-cnn) and our dataset, it introduced LoRA configuration for fine-tuning. The  process involved loading the base model, wrapping it with LoRA, tokenizing the text, training the PEFT model with new dataset, and finally, generating a summary using the configured LoRA-PEFT model with adjustable parameters like max_length and num_beams.
7. **Accuracy** - Used ROUGE score to evaluate our fine-tuned model.
   
**NOTE: We achieved higher accuracy score of 0.31 as compared to that of other pretrained models i.e., (0.28). Which is 10.71% better than the pre-trained models**

