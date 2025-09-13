from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_watson import IAMAuthenticator
import json
import os

class WatsonNLP:
    def __init__(self):
        self.api_key = os.getenv("IBM_WATSON_API_KEY")
        self.url = os.getenv("IBM_WATSON_URL")
        self.authenticator = IAMAuthenticator(self.api_key)
        self.nlp_service = NaturalLanguageUnderstandingV1(
            version='2021-08-01',
            authenticator=self.authenticator
        )
        self.nlp_service.set_service_url(self.url)

    def analyze_text(self, text):
        response = self.nlp_service.analyze(
            text=text,
            features={
                'entities': {},
                'keywords': {},
                'sentiment': {}
            }
        ).get_result()
        return response

    def extract_entities(self, text):
        analysis = self.analyze_text(text)
        entities = analysis.get('entities', [])
        return entities

    def extract_keywords(self, text):
        analysis = self.analyze_text(text)
        keywords = analysis.get('keywords', [])
        return keywords

    def get_sentiment(self, text):
        analysis = self.analyze_text(text)
        sentiment = analysis.get('sentiment', {}).get('document', {}).get('label', '')
        return sentiment