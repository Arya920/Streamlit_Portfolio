### Abstract

This project focuses on the development of a web application that
utilizes Large Language Model fine-tuning to convert natural language
queries into SQL queries for interaction with a MySQL database.
Leveraging Large Language Models (**LLM**s), specifically tailored for this
task, the application provides users with a seamless interface to input
natural language queries, which are then processed into SQL queries and
executed against the database. The integration of **LLM**s enhances the
accuracy and flexibility of query interpretation, enabling efficient
retrieval of relevant information from the database. The project
demonstrates the potential of advanced natural language processing
techniques in simplifying database interactions and facilitating more
intuitive user experiences in querying structured data.

### Introduction

In the rapidly evolving landscape of natural language processing (NLP),
the utilization of large language models (**LLM**s) has become increasingly
prevalent, promising unparalleled capabilities in understanding and
generating human-like text. Using this cutting-edge technology, our
project embarks on a journey to enhance the user experience and
efficiency of database management systems through the integration of
fine-tuned **LLM**s.

At the core of our endeavor lies the meticulous tuning and comparison of
diverse **LLM** architectures using sophisticated techniques such as Peft
Lora. This process enables us to discern the optimal model for our
specific application, evaluating their performance metrics, notably the
BLEU score.

With the most adept models identified, our focus shifts towards the
practical implementation within an intuitive application framework. This
application serves as a gateway for users to seamlessly interact with
their databases using natural language commands, streamlining the
traditional complexities associated with database querying.

Upon accessing the application, users are greeted with a user-friendly
login interface, where they can securely authenticate and input their
database credentials. Subsequently, they gain visibility into their
databases and schemas, empowering them with comprehensive insights into
their data infrastructure.

The aim of our application lies in its ability to facilitate effortless
communication between users and databases. Through the integration of
advanced natural language processing techniques, user input in everyday
language seamlessly translates into structured SQL commands. These SQL
commands are then executed within the connected database, fetching the
desired results and presenting them to the user in a comprehensible
format.

In summary, our project combines advanced language models with the
everyday needs of managing databases, bringing forward user-friendly and
efficient data interaction.

### Data Preparation

In our data preparation phase, we begin by sourcing data from the
Huggingface repository, specifically the dataset named
**\"Clinton/texttosqlv2_25000_v2\"**, which comprises 25,000 entries.
Each entry contains four key components: **instruction**, **input**,
**output**, and **text**. The **instruction** field represents the
natural language command, while **input** corresponds to its SQL
equivalent. The **output** field holds the SQL query, and **text** is
the Alpaca prompt for chat interactions. This column is the main column
needed for training and inferencing our models.

To ensure manageable data size and consistency, we establish a threshold
of **512 tokens**, retaining only entries that fall below this limit.
Additionally, we employ the **GTE-large embeddings** model from Sentence
Transformers to eliminate duplicate tokens effectively.

For enhanced data distribution and normalization, we consider techniques
like the **Box-Cox transformation**, ensuring that the selected subset
of entries closely adheres to a normal distribution of token lengths.

Finally, after pre-processing and refining the dataset, we save and
upload the customized data to the Huggingface platform for future
utilization and accessibility.

- **Training Set (3000 rows):** This set is used primarily for training
our models. It consists of 3000 rows of data, where each row contains
SQL table schemas paired with instructions that describe a task, along
with the corresponding responses.

- **Training Subset (400 rows):** In addition to the main training set, we
maintain a smaller training subset containing 400 rows. This subset is
often used for fine-tuning or experimenting with model configurations.

- **Inference Set (100 rows):** Finally, we have a dedicated inference set
comprising 100 rows. This set is exclusively reserved for evaluating the
performance of our trained models. During inference, the models generate
responses based on the provided SQL table schemas and task instructions,
without access to the actual responses. This evaluation helps us assess
the model's ability to generalize to unseen data.

### Final Data Format

    alpeca_prompt = f"""Below are SQL table schemas paired with instructions that describe a task.

    Using valid SQLite, write a response that appropriately completes the request for the provided tables. 
    ### Instruction: {Instructions}. 
    ### Input: {Input}
    ### Response: {response}"""

>**Explanation:** In the training data format, **{Instructions}** represent the natural language query given by the user, **{Input}** represents the table details **(table schema)** serving as context for the model, and **{response}** represents the actual output for the given input and instructions.

### ****LLM****s used in the Project

1. **Google Gemma-2B-it Model** - Gemma 2B instruct is one of the models
released under the Gemma family. It is a lightweight, state-of-the-art
open model developed by Google DeepMind and other teams across Google.
Gemma models are inspired by the larger Gemini models and are designed
to provide best-in-class performance for their sizes compared to other
open models. Gemma 2B comes in two sizes: Gemma 2B and Gemma 7B, each
with pre-trained and instruction-tuned variants. These models are
capable of running directly on developer laptops or desktop computers
and can also be deployed on Google Cloud platforms. They are optimized
for performance across multiple AI hardware platforms, including NVIDIA
GPUs and Google Cloud TPUs. Gemma 2B adheres to rigorous standards for
safe and responsible outputs and is designed with Google's AI Principles
in mind, ensuring reliability and safety in AI applications.

2. **DeepSeekCoder 1.3B-it Model** - The Deepseek Coder 1.3B instruct
model is part of the Deepseek Coder series, composed of code language
models trained from scratch on a massive dataset of 2 trillion tokens.
This dataset comprises 87% code and 13% natural language in both English
and Chinese languages, ensuring comprehensive coverage. The 1.3B model,
specifically, is initialized from a base model and fine-tuned on 2
billion tokens of instruction data. It offers advanced code completion
capabilities, utilizing a window size of 16K and a fill-in-the-blank
task to support project-level code completion and infilling tasks. This
model demonstrates superior performance among publicly available code
models, achieving state-of-the-art results on various benchmarks such as
HumanEval, MultiPL-E, MBPP, DS-1000, and APPS. With its flexibility,
scalability, and advanced capabilities, the Deepseek Coder 1.3B model
serves as a powerful tool for developers and programmers across
different programming languages and project requirements.

### Model Results

The evaluation of the language models (**LLM**s) in this project was
conducted using three key metrics: SACRE BLEU, BLEU SCORE, and EM RATIO.
SACRE BLEU, a variant of the BLEU metric, measures the similarity
between the generated sequence and reference sequences, considering
n-gram overlap and sentence length. BLEU SCORE assesses the precision of
n-grams in the generated sequence relative to reference sequences, while
EM RATIO measures the percentage of generated sequences that exactly
match the reference sequences.

### Comparison of Results

| Model                                   | SACRE BLEU | BLEU SCORE | EM RATIO |
|-----------------------------------------|------------|------------|----------|
| Base GEMMA-2B Model                     | 3.59       | 0.036      | 0.00     |
| Fine-Tuned GEMMA-2B Model (400 rows)    | 70.38      | 0.704      | 0.14     |
| Fine-Tuned GEMMA-2B Model (3000 rows)   | 70.38      | 0.704      | 0.14     |
| Base DeepSeek Coder-1.3B Model          | 41.79      | 0.418      | 0.01     |
| Fine-Tuned DeepSeek Coder-1.3B Model V1 | 57.78      | 0.578      | 0.00     |
| Fine-Tuned DeepSeek Coder-1.3B Model V2 | 70.35      | 0.703      | 0.02     |


### Evaluation Results

The base GEMMA-2B model exhibited low performance across all evaluation
metrics, indicating minimal agreement and precision compared to the
reference sequences. However, fine-tuning the GEMMA-2B model with 400
and 3000 rows of training data resulted in significant improvements,
with SACRE BLEU scores reaching 70.38. This highlights the effectiveness
of fine-tuning in enhancing the model's ability to generate accurate SQL
queries from natural language inputs.

Similarly, the DeepSeek Coder-1.3B base model initially showed moderate
performance. Fine-tuning the DeepSeek Coder-1.3B model further improved
its performance, with SACRE BLEU scores reaching 70.35 for one of the
fine-tuned versions. These results underscore the efficacy of
fine-tuning in enhancing the accuracy and effectiveness of **LLM**s in
generating SQL queries.

Overall, the evaluation metrics provide valuable insights into the
performance improvements achieved through fine-tuning, demonstrating the
potential of **LLM**s in facilitating seamless interaction with databases
through natural language interfaces.

