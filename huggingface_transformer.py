from transformers import pipeline

model = pipeline(task="question-answering", model="deepset/roberta-base-squad2")

context = """
The Sun is the star at the center of the Solar System. It is a nearly perfect ball of hot plasma, heated to incandescence by nuclear fusion reactions in its core, radiating the energy mainly as light, ultraviolet, and infrared radiation. It is the most important source of energy for life on Earth.

The Sun's diameter is about 1.39 million kilometers (864,000 miles), or 109 times that of Earth. Its mass is about 330,000 times that of Earth, comprising about 99.86% of the total mass of the Solar System. Roughly three-quarters of the Sun's mass consists of hydrogen (~73%); the rest is mostly helium (~25%), with much smaller quantities of heavier elements, including oxygen, carbon, neon, and iron.
"""
question = "What does the sun provide to the earth?"

response = model({ "question": question, "context": context })

print(question)
print("... Analyzing 🤖")
print("According to our AI, the answer to your question is:", response['answer']) # energy





# # Hugging Face: ML Inference Pipelines with Transformers

# This Template on Replit shows how to use the `transformers` Python library to load up an ML pipeline to run inferences on Transformers models from [Hugging Face](https://huggingface.co/). One way to use `transformers` is to include machine learning models in your Python projects! 

# Here's a step-by-step guide (Note that since step #3 has to download the model, it can take a minute to set up):

# 1. Visit the [Hugging Face Model Hub to find "Transformers" models](https://huggingface.co/models?library=transformers&sort=downloads) to find a model for your project. If you'd like to build a Q&A chatbot, for example, you could choose the [deepset/roberta-base-squad2](https://huggingface.co/deepset/roberta-base-squad2) model, which has been trained to answer questions.

# 2. Import `pipeline` from the `transformers` library, which will do all the work of pre-processing your data, passing it into your chosen model, and then generating your results.
# ```python
# from transformers import pipeline
# ```

# 3. Create your pipeline by specifying the **task** (e.g. "question-answering") and the **model ID** for the model that you'd like to use. [Visit the documentation](https://huggingface.co/docs/transformers/task_summary) for a list of the tasks that you can specify.
# ```python
# model = pipeline(task="question-answering", model="deepset/roberta-base-squad2")
# ```

# 4. Pass your inputs to the model, and receive an output! Depending on the [task](https://huggingface.co/docs/transformers/task_summary), you'll need to format your input as a string, dict, or other value. For "question-answering", we need to provide a _question_ and some _context_ which the model can use to answer our question.
# ```python
# question = "What does the sun provide to the earth?"
# context = """
# The Sun is the star at the center of the Solar System. It is a nearly perfect ball of hot plasma, heated to incandescence by nuclear fusion reactions in its core, radiating the energy mainly as light, ultraviolet, and infrared radiation. It is the most important source of energy for life on Earth.

# The Sun's diameter is about 1.39 million kilometers (864,000 miles), or 109 times that of Earth. Its mass is about 330,000 times that of Earth, comprising about 99.86% of the total mass of the Solar System. Roughly three-quarters of the Sun's mass consists of hydrogen (~73%); the rest is mostly helium (~25%), with much smaller quantities of heavier elements, including oxygen, carbon, neon, and iron.
# """
# response = model({ "question": question, "context": context })

# print(question)
# print("... Analyzing 🤖")
# print("According to our AI, the answer to your question is:", response['answer']) # energy
# ```

# There you go! You're using machine learning models to tackle complex problems, without having to set up your own complicated ML deployment stack.

# To learn more about these tools, visit:

# * https://huggingface.co/docs/transformers/pipeline_tutorial
# * https://huggingface.co/docs/hub/index
# * https://huggingface.co/docs/transformers

# If you'd like to learn more about using Hugging Face for NLP (and more!) visit the Hugging Face Course at [hf.co/course](https://hf.co/course)
