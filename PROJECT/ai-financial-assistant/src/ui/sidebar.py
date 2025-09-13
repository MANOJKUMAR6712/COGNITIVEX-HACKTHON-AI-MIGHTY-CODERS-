from streamlit import sidebar

def display_sidebar():
    sidebar.title("User Profile")
    
    # User demographics
    user_age = sidebar.number_input("Age", min_value=0, max_value=120, value=25)
    user_income = sidebar.number_input("Annual Income (INR)", min_value=0, value=500000)
    user_status = sidebar.selectbox("User Status", ["Student", "Professional", "Retiree"])
    
    # Preferences for financial advice
    sidebar.header("Preferences")
    advice_type = sidebar.multiselect("Preferred Advice Topics", 
                                       ["Savings", "Investments", "Taxes", "Budgeting"])
    
    # Save user profile
    if sidebar.button("Save Profile"):
        # Logic to save user profile can be added here
        sidebar.success("Profile saved successfully!")

    return {
        "age": user_age,
        "income": user_income,
        "status": user_status,
        "advice_type": advice_type
    }