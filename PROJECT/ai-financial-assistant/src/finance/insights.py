from typing import List, Dict

class FinancialInsights:
    def __init__(self, user_data: Dict):
        self.user_data = user_data

    def analyze_spending_patterns(self) -> Dict[str, float]:
        # Analyze spending patterns based on user data
        spending_summary = {}
        for category, amount in self.user_data['spending'].items():
            spending_summary[category] = amount
        return spending_summary

    def identify_areas_for_improvement(self) -> List[str]:
        # Identify areas where the user can optimize expenses
        suggestions = []
        spending_summary = self.analyze_spending_patterns()
        
        # Example logic for identifying areas for improvement
        if spending_summary.get('entertainment', 0) > 200:
            suggestions.append("Consider reducing entertainment expenses.")
        if spending_summary.get('eating_out', 0) > 150:
            suggestions.append("Try cooking at home more often to save money.")
        if spending_summary.get('subscriptions', 0) > 50:
            suggestions.append("Review your subscriptions and cancel any you don't use.")
        
        return suggestions

    def generate_actionable_insights(self) -> Dict[str, List[str]]:
        # Generate actionable insights for the user
        insights = {
            "spending_summary": self.analyze_spending_patterns(),
            "improvement_suggestions": self.identify_areas_for_improvement()
        }
        return insights

# Example usage:
# user_data = {
#     'spending': {
#         'entertainment': 250,
#         'eating_out': 180,
#         'subscriptions': 60
#     }
# }
# insights = FinancialInsights(user_data)
# actionable_insights = insights.generate_actionable_insights()
# print(actionable_insights)