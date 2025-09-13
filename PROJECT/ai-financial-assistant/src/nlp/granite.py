from granite import GraniteModel

class GraniteNLP:
    def __init__(self, model_name="granite-financial-model"):
        self.model = GraniteModel.from_pretrained(model_name)

    def analyze_financial_data(self, user_data):
        # Process user data and generate insights using the Granite model
        insights = self.model.generate_insights(user_data)
        return insights

    def generate_personalized_recommendations(self, user_profile):
        # Generate personalized financial recommendations based on user profile
        recommendations = self.model.generate_recommendations(user_profile)
        return recommendations

    def advanced_analysis(self, financial_query):
        # Perform advanced financial analysis based on user queries
        analysis_result = self.model.perform_analysis(financial_query)
        return analysis_result