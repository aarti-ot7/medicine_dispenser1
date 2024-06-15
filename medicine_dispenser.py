import streamlit as st
from datetime import datetime

# Dictionary of medicines and their associated keywords
medicine_keywords = {
    "Paracetamol": ["fever", "pain", "headache", "body ache"],
    "Ibuprofen": ["inflammation", "pain relief", "swelling"],
    "Antacid": ["heartburn", "indigestion", "acid reflux"],
    "Antihistamine": ["allergies", "runny nose", "itchy eyes"],
}

def recommend_medicine(symptoms):
    for medicine, keywords in medicine_keywords.items():
        if any(keyword in symptoms.lower() for keyword in keywords):
            return medicine
    return None

st.title("Virtual Medicine Dispenser")

# Current Time
current_time = datetime.now().strftime("%I:%M %p")
st.write(f"Current Time: {current_time}")

st.write("Please describe your symptoms:")
symptoms = st.text_area("Symptoms")

if st.button("Dispense"):
    if symptoms:
        recommended_medicine = recommend_medicine(symptoms)
        if recommended_medicine:
            st.success(f"Based on your symptoms, you can take {recommended_medicine}.")
        else:
            st.warning("I couldn't find a suitable medicine for your symptoms. Please consult a doctor.")
    else:
         st.warning("Please describe your symptoms.")