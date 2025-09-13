from transformers import pipeline

class HuggingFaceNLP:
    def __init__(self, model_name="gpt-2"):
        self.model_name = model_name
        self.nlp_pipeline = pipeline("text-generation", model=self.model_name)

    def generate_response(self, prompt, max_length=150):
        response = self.nlp_pipeline(prompt, max_length=max_length, num_return_sequences=1)
        return response[0]['generated_text']

    def set_model(self, model_name):
        self.model_name = model_name
        self.nlp_pipeline = pipeline("text-generation", model=self.model_name)