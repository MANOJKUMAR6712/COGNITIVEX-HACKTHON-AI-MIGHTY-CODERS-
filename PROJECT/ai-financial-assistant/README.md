# AI Financial Assistant

This project is an AI-powered financial assistant application built using Python and Streamlit. It integrates various natural language processing models, including IBM Watson NLP, HuggingFace models, and IBM Granite LLM, to provide personalized financial advice, budget summaries, and actionable insights.

## Features

- **Personalized Financial Advice**: Users can receive tailored advice on savings, taxes, and investments based on their individual profiles and queries.
- **Budget Summaries**: The application automatically generates easy-to-understand budget summaries and spending reports from user data.
- **Actionable Insights**: Users are provided with insights to optimize their expenses, highlighting spending patterns and areas for improvement.
- **Customizable User Experience**: The app adjusts its tone and complexity based on user demographics (e.g., student, professional, retiree) for maximum engagement.
- **Seamless Chatbot Experience**: The chatbot simulates conversational flow, answering a wide range of finance-related questions using advanced NLP capabilities.

## Project Structure

```
ai-financial-assistant
├── src
│   ├── app.py                # Main entry point of the application
│   ├── ui
│   │   ├── chat.py           # Chat interface implementation
│   │   ├── sidebar.py        # User profile management and customization
│   │   └── tool_cards.py     # Financial tool cards management
│   ├── nlp
│   │   ├── watson.py         # IBM Watson NLP integration
│   │   ├── huggingface.py     # HuggingFace model integration
│   │   └── granite.py        # IBM Granite model integration
│   ├── finance
│   │   ├── advice.py         # Personalized financial advice generation
│   │   ├── budget.py         # Budget summaries and spending reports
│   │   └── insights.py       # Actionable insights for expense optimization
│   └── utils
│       └── secrets.py        # Secure handling of API keys and sensitive information
├── requirements.txt          # Project dependencies
└── README.md                 # Project documentation
```

## Installation

To set up the project, follow these steps:

1. Clone the repository:
   ```
   git clone <repository-url>
   cd ai-financial-assistant
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up your API keys and sensitive information in `src/utils/secrets.py`.

## Usage

To run the application, execute the following command:
```
streamlit run src/app.py
```

Open your web browser and navigate to `http://localhost:8501` to access the AI financial assistant.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.