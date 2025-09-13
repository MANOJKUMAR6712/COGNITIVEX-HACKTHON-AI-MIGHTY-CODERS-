from streamlit import card, expander

def create_tool_card(title, description, link):
    with card(title=title):
        expander(title="Details", expanded=False):
            st.write(description)
            st.button("Access Tool", on_click=lambda: st.session_state.selected_tool(link))

def display_tool_cards():
    tools = [
        {
            "title": "Budgeting Tool",
            "description": "Create and manage your budget effectively.",
            "link": "/budget"
        },
        {
            "title": "Investment Calculator",
            "description": "Calculate potential returns on your investments.",
            "link": "/investment"
        },
        {
            "title": "Tax Estimator",
            "description": "Estimate your tax obligations based on your income.",
            "link": "/tax"
        },
        {
            "title": "Savings Planner",
            "description": "Plan your savings goals and track your progress.",
            "link": "/savings"
        }
    ]

    for tool in tools:
        create_tool_card(tool["title"], tool["description"], tool["link"])