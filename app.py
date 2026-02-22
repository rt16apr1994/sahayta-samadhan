import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

# Page Configuration
st.set_page_config(page_title="Sahayta - Connect & Grow", layout="wide")

# Google Sheets Connection
conn = st.connection("gsheets", type=GSheetsConnection)

st.title("🤝 Sahayta: Overcome Your Communication Fears")
st.markdown("Bridge the gap between those who need help and those who can provide solutions.")

# Navigation
menu = ["Home", "Registration", "Resources"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Home":
    st.subheader("Welcome to our Community")
    st.write("Whether you struggle with stage fright, anxiety during counter-questions, or managing emotions, we are here to connect you with the right mentors.")

elif choice == "Registration":
    st.subheader("Join the Platform")
    
    # Role Selection Dropdown
    role = st.selectbox("Please select your role", ["--Select--", "Student/Needy/Learner", "Expert/Trainer/Teacher"])

    if role != "--Select--":
        st.write(f"You are registering as: **{role}**")
        
        with st.form(key="registration_form"):
            name = st.text_input("Full Name*")
            contact = st.text_input("Contact Number*")
            email = st.text_input("Email ID*")
            
            # Specific details based on role
            if role == "Student/Needy/Learner":
                issue = st.selectbox("Main Concern", ["Stage Fear", "Breathlessness", "Anger Management", "Answering Questions"])
            else:
                issue = st.text_input("Area of Expertise (e.g. Public Speaking)")

            submit_button = st.form_submit_button(label="Submit Details")

            if submit_button:
                if name and contact and email:
                    # Prepare data for Google Sheets
                    new_data = pd.DataFrame([{
                        "Name": name,
                        "Contact": contact,
                        "Email": email,
                        "Role": role,
                        "Detail/Issue": issue
                    }])
                    
                    # Logically saving to Sheet (You need to configure the URL in secrets)
                    # st.write(new_data) # Testing purpose
                    st.success(f"Thank you {name}! Your details as a {role} have been submitted.")
                else:
                    st.error("Please fill all mandatory fields.")

elif choice == "Resources":
    st.subheader("Self-Help Guide")
    st.info("💡 **Tip:** Practice 'Power Posing' for 2 minutes before any presentation to boost confidence.")
