import streamlit as slit
import pandas as pd
import joblib

#do pip install streamlit first

#run with command streamlit run demoGBmodel.py

#load our model, Gradient Boosting 
demoModel = joblib.load('gradBoostModel.pkl')

#title
slit.title("Demo of Gradient Boost Model trained on NutAlleriges set, derived from Childhood Allergies: Prevalance by TheDevastator")
slit.write("Select and Enter Patient info to predict prescription of allergy medication")

#Factors
raceFactor = slit.selectbox("Race: 0 - White, 1 - Black, 2 - Asian or Pacific Islander, 3 - Other, 4 - Unknown", [0,1,2,3,4])
genderFactor = slit.selectbox("Gender: 0 - Male, 1 - Female",[0,1])
payerFactor = slit.selectbox("Payer Factor: 0 - Medicaid, 1 - Non-Medicaid",[0,1])
curedFactor = slit.selectbox("Patient Cured: 0 - Not Cured, 1 - Cured",[0,1])
ageStartFactor = slit.number_input("Age of Patient:")
ageEndFactor = slit.number_input("End Age of Patient:")


#Take user input to fit with the model's parameters(see foodAllergies.ipynb)
genderFactorMale = (genderFactor == 0)
genderFactorFemale = (genderFactor == 1)


white = (raceFactor == 0)
black = (raceFactor == 1) 
asian = (raceFactor == 2)
other = (raceFactor == 3)
unknown = (raceFactor == 4)

medicaid = (payerFactor == 0)
nonMedicaid = (payerFactor == 1)



inputData = {
    'PATIENT_CURED': curedFactor,
    'AGE_START_YEARS': ageStartFactor,
    'AGE_END_YEARS': ageEndFactor,
    'RACE_FACTOR_R0 - White': white,
    'RACE_FACTOR_R1 - Black': black,
    'RACE_FACTOR_R2 - Asian or Pacific Islander': asian,
    'RACE_FACTOR_R3 - Other': other,
    'RACE_FACTOR_R4 - Unknown': unknown,
    'GENDER_FACTOR_S0 - Male': genderFactorMale,
    'GENDER_FACTOR_S1 - Female': genderFactorFemale,
    'PAYER_FACTOR_P0 - Non-Medicaid': nonMedicaid,
    'PAYER_FACTOR_P1 - Medicaid': medicaid
}

#Make Frame
inputDF = pd.DataFrame([inputData])

#Predict
if slit.button("Predict"):
   prediction = demoModel.predict(inputDF)
   slit.success(f"Prediction of Asthma Prescription(0 means no prescription, 1 means prescribed): {int(prediction[0])}")