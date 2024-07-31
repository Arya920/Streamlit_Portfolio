import json
from llama_cpp import Llama



def extract_information( text, example=["","",""]):
    llm = Llama(
      model_path="D:/Streamlit portfolio/Streamlit_Portfolio/models/NuExtract-Q6_K.gguf",
      # n_gpu_layers=-1, # Uncomment to use GPU acceleration
      # seed=1337, # Uncomment to set a specific seed
      n_ctx= 2048  # 1 word = 1.63 token (max 500 words)      #2048, # Uncomment to increase the context window
    )

    # schema = """{
    #     "Required Education Qualification": [],
    #     "Required Skills": [],
    #     "Required Experience": ""
    #     }"""
    
    schema2 = """{
    "Programming Languages": [],
    "Technical Skills": []
    }"""


    schema = json.dumps(json.loads(schema2), indent=4)
    input_llm =  "<|input|>\n### Template:\n" +  schema + "\n"
    for i in example:
      if i != "":
          input_llm += "### Example:\n"+ json.dumps(json.loads(i), indent=4)+"\n"
    
    input_llm +=  "### Text:\n"+text +"\n<|output|>\n"

    output = llm(input_llm,
                   max_tokens = 300,
                   stop=["<|input|>"],
                    echo=False)
    
    return output['choices'][0]['text'].split("<|end-output|>")[0]





#prediction = extract_information(llm, resume_text, schema, example=["","",""])