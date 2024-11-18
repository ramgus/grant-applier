import streamlit as st

# Sample grant data
grants = [
    {
        'name': 'Grant A',
        'summary': 'This grant supports projects in education.',
        'requirements': ['Education Sector', 'Budget < $50,000'],
        'deadline': '2024-01-31'
    },
    {
        'name': 'Grant B',
        'summary': 'Funding for healthcare innovations.',
        'requirements': ['Healthcare Sector', 'Non-Profit'],
        'deadline': '2024-02-28'
    },
    {
        'name': 'Grant C',
        'summary': 'Support for environmental conservation projects.',
        'requirements': ['Environment Sector', 'Established Organization'],
        'deadline': '2024-03-15'
    },
]

# Navigation menu
st.sidebar.title("Navigation")
menu = st.sidebar.radio("Go to", ["Home", "Application Form", "Grant Matching", "Grant Summaries", "Chatbot"])

if menu == "Home":
    st.title("Welcome to the Goldhirsh Foundation Grant Application Platform")
    st.write("""
    This platform streamlines the application process by allowing you to fill out one application
    and apply to multiple grants that you are eligible for.
    """)

elif menu == "Application Form":
    st.title("Unified Application Form")
    st.write("Please fill out the following information:")
    
    with st.form(key='application_form'):
        name = st.text_input("Full Name")
        email = st.text_input("Email Address")
        organization = st.text_input("Organization Name")
        sector = st.selectbox("Sector", ["Education", "Healthcare", "Environment", "Technology", "Arts"])
        budget = st.number_input("Project Budget ($)", min_value=0)
        non_profit = st.selectbox("Is your organization a non-profit?", ["Yes", "No"])
        established = st.selectbox("Is your organization established?", ["Yes", "No"])
        submit_button = st.form_submit_button(label='Submit Application')
    
    if submit_button:
        st.success("Application submitted successfully!")
        st.session_state['applicant_info'] = {
            'name': name,
            'email': email,
            'organization': organization,
            'sector': sector,
            'budget': budget,
            'non_profit': non_profit,
            'established': established
        }

elif menu == "Grant Matching":
    st.title("Eligible Grants")
    if 'applicant_info' in st.session_state:
        applicant = st.session_state['applicant_info']
        eligible_grants = []
        
        for grant in grants:
            eligibility = True
            requirements = grant['requirements']
            # Check sector
            if f"{applicant['sector']} Sector" not in requirements and 'Any Sector' not in requirements:
                eligibility = False
            # Check budget
            if any('Budget' in req for req in requirements):
                max_budget = int(requirements[1].split('< $')[1].replace(',', ''))
                if applicant['budget'] >= max_budget:
                    eligibility = False
            # Check non-profit status
            if 'Non-Profit' in requirements and applicant['non_profit'] != 'Yes':
                eligibility = False
            # Check established organization
            if 'Established Organization' in requirements and applicant['established'] != 'Yes':
                eligibility = False
            if eligibility:
                eligible_grants.append(grant)
        
        if eligible_grants:
            st.write("Based on your application, you are eligible for the following grants:")
            for grant in eligible_grants:
                st.subheader(grant['name'])
                st.write(grant['summary'])
                st.write(f"**Deadline:** {grant['deadline']}")
        else:
            st.write("Sorry, you are not eligible for any grants at this time.")
    else:
        st.write("Please fill out the [application form](#) first.")

elif menu == "Grant Summaries":
    st.title("Grant Summaries")
    for grant in grants:
        st.subheader(grant['name'])
        st.write(grant['summary'])
        st.write(f"**Requirements:** {', '.join(grant['requirements'])}")
        st.write(f"**Deadline:** {grant['deadline']}")
        st.markdown("---")

elif menu == "Chatbot":
    st.title("Grant Assistance Chatbot")
    st.write("How can we assist you today?")
    st.write("_Note: This is a placeholder for the chatbot feature._")
    user_input = st.text_input("You:")
    if user_input:
        st.write("Chatbot: Thank you for your message. We will get back to you shortly.")