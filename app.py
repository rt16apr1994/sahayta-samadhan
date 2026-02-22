import streamlit as st
import pandas as pd

# Page Configuration
st.set_page_config(page_title="Sahayta - Connect & Grow", layout="wide")

# Header Section
st.title("🤝 Sahayta: Overcome Your Communication Fears")
st.markdown("""
    *Stage par kaampna? Gussa aana? Ya sawalon ka jawab na de paana?* Yahan aap help maang sakte hain ya dusron ki madad kar sakte hain.
""")

# Sidebar for Navigation
menu = ["Home", "Need Help?", "Become a Mentor", "Resources"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Home":
    st.subheader("Welcome to the Community")
    st.write("Yeh platform students aur professionals ko connect karta hai taaki wo apne communication issues ko solve kar sakein.")
    

elif choice == "Need Help?":
    st.subheader("Apni Mushkil Share Karein")
    with st.form("help_form"):
        name = st.text_input("Aapka Naam (Optional)")
        issue = st.selectbox("Aapko kya issue hai?", 
                            ["Stage Fright", "Breathlessness while speaking", "Handling Counter Questions", "Anger Management", "Stuttering"])
        details = st.text_area("Humein vistar se batayein")
        submit = st.form_submit_button("Submit")
        if submit:
            st.success("Aapki request submit ho gayi hai. Koi mentor jald hi connect karega.")

elif choice == "Become a Mentor":
    st.subheader("Dusron ki Madad Karein")
    with st.form("mentor_form"):
        m_name = st.text_input("Full Name")
        expertise = st.multiselect("Aap kis cheez mein expert hain?", 
                                  ["Public Speaking", "Psychology", "Soft Skills", "Stress Management"])
        contact = st.text_input("LinkedIn Profile ya Email")
        submit_m = st.form_submit_button("Join as Mentor")
        if submit_m:
            st.success("Humein join karne ke liye shukriya!")

elif choice == "Resources":
    st.subheader("Quick Tips & Solutions")
    col1, col2 = st.columns(2)
    with col1:
        st.info("📌 **Stage Fear?**\n'Box Breathing' try karein: 4 second saans lein, 4 second rokein, 4 second chhodein.")
    with col2:
        st.info("📌 **Counter Questions?**\nJawab dene se pehle 2 second ka 'Pause' lein. Isse aapka dimag calm rehta hai.")
