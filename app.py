import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

st.set_page_config(page_title="Sahayta Portal", layout="centered")

# Google Sheets Connection
conn = st.connection("gsheets", type=GSheetsConnection)

st.title("🤝 Sahayta: Connection Portal")

menu = ["Home", "Registration"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Home":
    st.markdown("### Empowering Students & Professionals")
    st.write("This platform connects people facing communication challenges with experts.")

elif choice == "Registration":
    st.subheader("Join the Community")
    
    role = st.selectbox("Please select your role", ["--Select--", "Student/Needy/Learner", "Expert/Trainer/Teacher"])

    if role != "--Select--":
        with st.form(key="reg_form"):
            name = st.text_input("Full Name*")
            contact = st.text_input("Contact Number*")
            email = st.text_input("Email ID*")
            detail = st.text_area("Specific Issue or Expertise area*")
            
            submit = st.form_submit_button("Submit & Connect")

            if submit:
                if name and contact and email:
                    # Naya data jo save karna hai
                    new_row = {
                        "Name": name, 
                        "Contact": contact, 
                        "Email": email, 
                        "Role": role, 
                        "Detail": detail
                    }
                    
                    try:
                        # Aapki sheet ka naam 'sahayta-samadhan' yahan use ho raha hai
                        existing_data = conn.read(worksheet="sahayta-samadhan")
                        updated_df = pd.concat([existing_data, pd.DataFrame([new_row])], ignore_index=True)
                    except Exception:
                        # Agar sheet khali hai ya koi error hai toh naya dataframe banayein
                        updated_df = pd.DataFrame([new_row])
                    
                    # Google Sheet ko update karna
                    conn.update(worksheet="sahayta-samadhan", data=updated_df)
                    
                    st.success(f"✅ Success! Your details as {role} are saved.")
                    st.balloons()
                else:
                    st.warning("Please fill all mandatory fields.")
