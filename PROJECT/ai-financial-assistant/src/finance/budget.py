from typing import List, Dict
import pandas as pd

def generate_budget_summary(transactions: List[Dict[str, float]]) -> pd.DataFrame:
    """
    Generate a budget summary from a list of transactions.

    Args:
        transactions (List[Dict[str, float]]): A list of transaction dictionaries with 'category' and 'amount'.

    Returns:
        pd.DataFrame: A DataFrame summarizing the budget by category.
    """
    df = pd.DataFrame(transactions)
    summary = df.groupby('category')['amount'].sum().reset_index()
    summary.columns = ['Category', 'Total Amount']
    return summary

def generate_spending_report(transactions: List[Dict[str, float]]) -> pd.DataFrame:
    """
    Generate a spending report from a list of transactions.

    Args:
        transactions (List[Dict[str, float]]): A list of transaction dictionaries with 'date', 'description', and 'amount'.

    Returns:
        pd.DataFrame: A DataFrame containing the spending report.
    """
    df = pd.DataFrame(transactions)
    df['date'] = pd.to_datetime(df['date'])
    report = df.sort_values(by='date')
    return report

def process_uploaded_data(file_path: str) -> List[Dict[str, float]]:
    """
    Process uploaded CSV data for transactions.

    Args:
        file_path (str): The path to the uploaded CSV file.

    Returns:
        List[Dict[str, float]]: A list of transaction dictionaries.
    """
    df = pd.read_csv(file_path)
    transactions = df.to_dict(orient='records')
    return transactions

def analyze_budget(transactions: List[Dict[str, float]]) -> Dict[str, float]:
    """
    Analyze the budget and provide insights.

    Args:
        transactions (List[Dict[str, float]]): A list of transaction dictionaries.

    Returns:
        Dict[str, float]: A dictionary with total income, total expenses, and balance.
    """
    df = pd.DataFrame(transactions)
    total_income = df[df['amount'] > 0]['amount'].sum()
    total_expenses = df[df['amount'] < 0]['amount'].sum()
    balance = total_income + total_expenses
    return {
        'Total Income': total_income,
        'Total Expenses': total_expenses,
        'Balance': balance
    }