import streamlit as st
import base64

disease_symptoms = {
    "Malaria": "Fever, Headache, Sweating, Diarrhea, Vomiting, Fatigue",
    "Measles": "Fever, Cough, Red Eyes, Sore Throat, Rash, Runny Nose",
    "Meningitis": "Headache, Stiff Neck, Nausea, Vomiting",
    "Mononucleosis": "Sore Throat, Fatigue, Swollen Lymph Nodes, Rash",
    "Pneumonia": "Fever, Cough, Shortness Of Breath, Chest Pain, Fatigue",
    "Rabies": "Fever, Headache, Muscle Aches, Tingling At The Bite Site, Hydrophobia",
    "Salmonella": "Fever, Diarrhea, Abdominal Cramps, Nausea",
    "Shingles": "Painful Rash That Follows Nerve Path",
    "Tuberculosis (TB)": "Cough, Night Sweating, Fever, Weight Loss, Chest Pain",
    "Urinary Tract Infection": "Pain In Urination, Burning, Frequent Urination, Blood In Urine",
    "Varicose Veins": "Swollen, Twisted Veins",
    "Warts": "Raised Rough Growths On Skin",
    "Yeast Infection": "Itching, Burning, Discharge From The Vagina Or Penis",
    "Acanthamoeba Keratitis": "Pain, Redness, Inflammation In The Eye",
    "Acute Appendicitis": "Pain In Lower Right Abdomen, Nausea, Vomiting, Fever",
    "Acute Kidney Injury (AKI)": "Decreased Kidney Function",
    "Alzheimer's Disease": "Memory Loss, Confusion, Difficulty In Thinking, Personality Change",
    "Anemia": "Fatigue, Shortness Of Breath, Pale Skin, Dizziness",
    "Aortic Aneurysm": "Bulge In The Wall Of Aorta",
    "Bacterial Meningitis": "Fever, Headache, Stiff Neck, Nausea, Vomiting",
    "Bipolar Disorder": "Extreme Mood Swings, Mania To Depression",
    "Colorectal Cancer": "Change In Bowel Habits, Constipation, Blood In Stool, Abdominal Pain",
    "Cervical Cancer": "Pain During Sex, Abnormal Vaginal Bleeding, Abnormal Pap Test Result",
    "Dementia": "Memory Loss, Confusion, Difficulty In Thinking, Personality Change",
    "Erectile Dysfunction": "Difficulty Getting Or Keeping An Erection",
    "Fibromyalgia": "Widespread Pain, Fatigue, Tenderness",
    "Glaucoma": "Increased Pressure In The Eye That Can Damage The Optic Nerve, Lead To Vision Loss",
    "Heart Failure": "Condition In Which The Heart Cannot Pump Blood As Well As It Should",
    "Kidney Disease": "Damage To The Kidneys That Can Lead To Kidney Failure",
    "Lung Disease": "Condition That Affects The Lungs, Can Make It Difficult To Breathe",
    "Parkinson's Disease": "Tremors, Slow Movement, Stiffness, Difficulty With Balance, Coordination",
    "Peptic Ulcer Disease": "Pain In The Upper Abdomen, Indigestion, Nausea, Vomiting",
    "Peripheral Artery Disease": "Pain, Numbness, Tingling In The Arms Or Legs",
    "Prostate Cancer": "Difficulty Urinating, Blood In The Urine, Pain In The Back Or Hips, Erectile Dysfunction",
    "Rheumatoid Arthritis": "Pain, Swelling, Stiffness In The Joints",
    "Stroke": "Sudden Weakness, Numbness On One Side Of The Body, Difficulty Speaking, Confusion, Trouble Seeing In One Eye, Severe Headache",
    "Stomach Cancer": "Pain In The Upper Abdomen, Indigestion, Nausea, Vomiting, Weight Loss",
    "Thyroid Cancer": "Lump In The Neck, Hoarseness, Fatigue, Weight Loss, Unexplained Heat Intolerance, Sensitivity To Cold",
    "Ulcerative Colitis": "Diarrhea, Bloody Stool, Abdominal Pain, Weight Loss",
    "Atopic Dermatitis": "Itchy, Red, Inflamed Skin",
    "Celiac Disease": "Diarrhea, Bloating, Weight Loss, Fatigue, Abdominal Pain",
    "Chronic Kidney Disease": "Fatigue, Shortness Of Breath, Swelling, High Blood Pressure, Changes In Urination",
    "Crohn's Disease": "Diarrhea, Bloody Stool, Abdominal Pain, Weight Loss",
    "Epilepsy": "Seizures",
    "Graves' Disease": "Hyperthyroidism, Which Is An Overactive Thyroid",
    "Hashimoto's Thyroiditis": "Hypothyroidism, Which Is An Underactive Thyroid",
    "Lupus": "Chronic Autoimmune Disease That Can Affect Any Part Of The Body",
    "Flu": "Fever, Cough, Sore Throat, Runny Or Stuffy Nose, Muscle Aches, Headache, Fatigue",
    "Bronchitis": "Cough, Mucus Production, Shortness Of Breath, Chest Pain",
    "Heart Attack": "Chest Pain, Shortness Of Breath, Nausea, Vomiting, Lightheadedness, Sweating",
    "Cancer": "Lump, Unexplained Weight Loss, Fatigue, Changes In Bowel, Bladder Habits, Persistent Cough, Indigestion, Unexplained Bleeding Or Discharge",
    "Diabetes": "Increased Thirst, Frequent Urination, Unexplained Weight Loss, Fatigue, Blurred Vision, Cuts That Are Slow To Heal",
    "Alzheimer's": "Memory Loss, Confusion, Difficulty Thinking, Changes In Personality, changes in Behavior",
    "Arthritis": "Pain, Stiffness, Swelling, Inflammation In The Joints",
    "Adenovirus": "Fever, Sore Throat, Cough, Conjunctivitis, Rash, Pink Eye",
    "Aflatoxicosis": "Vomiting, Diarrhea, Jaundice, Liver Damage",
    "Allergic Rhinitis": "Runny Nose, Sneezing, Itchy Eyes, Itchy Nose, Throat, Palate",
    "Anxiety Disorder": "Excessive Worry, Fear, Anxiety That Interferes With Daily Life",
    "Appendicitis": "Pain In The Lower Right Abdomen, Nausea, Vomiting, Fever",
    "Asperger Syndrome": "Difficulty With Social Interaction, Repetitive Behaviors, Restricted Interests",
    "Asthma": "Wheezing, Shortness Of Breath, Coughing, Chest Tightness",
    "Bladder Cancer": "Blood In The Urine, Pain Or Burning When Urinating, Frequent Urination, Urgency To Urinate, Incontinence",
    "Blood Clot": "Pain, Swelling, Redness, Warmth, Tenderness In The Affected Area, Shortness Of Breath, Chest Pain, Difficulty Breathing, Coughing Up Blood",
    "Gallstones": "Pain In Upper Right Abdomen, Nausea, Vomiting, Fever, Gas After Meals, Indigestion",
    "Gonorrhea": "Pain In Urination, Pain In One Testicle, Sore Throat, Pain In Lower Abdomen",
    "Heart Disease": "Chest Pain, Shortness Of Breath, Fatigue",
    "Hepatitis": "Inflammation Of The Liver, Dark Urine, Itchy Skin",
    "Herpes": "Flu-Like Symptoms, Sexually Transmitted Infection That Can Cause Blisters On The Genitals, Mouth, Other Parts Of The Body",
    "Influenza": "Fever, Cough, Sore Throat, Runny Or Stuffy Nose, Muscle Aches, Headache, Fatigue",
    "Irritable Bowel Syndrome (IBS)": "Abdominal Pain, Bloating, Constipation, Diarrhea",
    "Kidney Stones": "Pain In The Lower Back Or Side, Nausea, Vomiting, Blood In The Urine",
    "Lung Cancer": "Cough That Does Not Go Away, Shortness Of Breath, Chest Pain, Unexplained Weight Loss, Fatigue, Blood In The Sputum",
    "Covid-19": "Fever,Cough,Shortness of breath, difficulty breathing, Fatigue ,Muscle or body aches,Headache, loss of taste,loss of smell,Sore throat, runny nose,Nausea,Diarrhea",
    "Anthrax": "Fever, Chills, Shortness Of Breath, Skin Ulcers, Chest Pain",
    "Chikungunya": "Fever, Joint Pain, Rash, Headache, Fatigue",
    "Dengue": "Fever, Severe Headache, Pain Behind The Eyes, Joint Pain, Muscle Pain, Rash",
    "Ebola": "Fever, Severe Headache, Muscle Pain, Weakness, Fatigue, Diarrhea, Vomiting, Abdominal Pain, Unexplained Bleeding",
    "Hantavirus": "Fever, Muscle Aches, Fatigue, Shortness Of Breath, Cough",
    "HIV/AIDS": "Fatigue, Weight Loss, Fever, Swollen Lymph Nodes, Opportunistic Infections",
    "Leprosy": "Skin Lesions, Numbness, Muscle Weakness, Eye Problems",
    "Leptospirosis": "Fever, Muscle Pain, Red Eyes, Abdominal Pain, Jaundice",
    "Lyme Disease": "Rash, Fever, Headache, Fatigue, Joint Pain, Muscle Pain",
    "Marburg Virus": "Fever, Headache, Muscle Pain, Nausea, Vomiting, Diarrhea, Bleeding",
    "Norovirus": "Vomiting, Diarrhea, Stomach Pain, Nausea, Fever",
    "Polio": "Fever, Sore Throat, Headache, Vomiting, Muscle Weakness, Paralysis",
    "Scrub Typhus": "Fever, Rash, Eschar (Black Scab At The Site Of A Bite), Headache, Muscle Pain",
    "Sepsis": "Fever, Chills, Rapid Heart Rate, Rapid Breathing, Confusion, Low Blood Pressure",
    "Syphilis": "Sores, Rash, Fever, Swollen Lymph Nodes, Fatigue, Muscle Aches",
    "Tetanus": "Jaw Stiffness, Muscle Spasms, Difficulty Swallowing, Seizures",
    "Toxoplasmosis": "Fever, Muscle Pain, Sore Throat, Swollen Lymph Nodes",
    "Typhoid Fever": "High Fever, Weakness, Stomach Pain, Constipation, Rash",
    "Zika Virus": "Fever, Rash, Joint Pain, Conjunctivitis, Headache",
    "Yellow Fever": "Fever, Chills, Headache, Nausea, Vomiting, Jaundice",
    "Brucellosis": "Fever, Sweating, Fatigue, Muscle Pain, Joint Pain, Loss Of Appetite",
    "Hepatitis A": "Fatigue, Nausea, Stomach Pain, Jaundice, Loss Of Appetite",
    "Hepatitis B": "Fatigue, Jaundice, Dark Urine, Abdominal Pain, Nausea",
    "Hepatitis C": "Fatigue, Jaundice, Dark Urine, Joint Pain, Nausea",
    "Cholera": "Diarrhea, Dehydration, Vomiting, Rapid Heart Rate, Low Blood Pressure",
    "Plague": "Fever, Chills, Headache, Weakness, Swollen Lymph Nodes, Abdominal Pain",
    "Tularemia": "Fever, Skin Ulcers, Swollen Lymph Nodes, Fatigue, Shortness Of Breath",
    "Rotavirus": "Diarrhea, Vomiting, Fever, Abdominal Pain, Dehydration",
    "Hendra Virus": "Fever, Cough, Shortness Of Breath, Headache, Fatigue",
    "Nipah Virus": "Fever, Headache, Drowsiness, Confusion, Seizures",
    "Schistosomiasis": "Rash, Fever, Chills, Muscle Pain, Cough",
    "Ehrlichiosis": "Fever, Headache, Fatigue, Muscle Pain, Nausea",
    "Babesiosis": "Fever, Chills, Sweats, Fatigue, Muscle Pain, Headache",
    "Lassa Fever": "Fever, Sore Throat, Chest Pain, Vomiting, Diarrhea",
    "Filariasis": "Swelling In Limbs, Fever, Skin Lesions, Enlarged Lymph Nodes",
    "Onchocerciasis (River Blindness)": "Skin Rash, Itching, Vision Problems, Nodules Under The Skin",
    "Toxocariasis": "Fever, Cough, Rash, Abdominal Pain, Swollen Lymph Nodes",
    "Trachoma": "Eye Discharge, Irritation, Swollen Eyelids, Vision Problems",
    "Whipple's Disease": "Joint Pain, Chronic Diarrhea, Abdominal Pain, Weight Loss",
}
    


disease_specialist = {
    "Infectious Disease Specialist": [ "Anthrax", "Chikungunya", "Dengue", "Ebola", "Hantavirus", "HIV/AIDS", "Leprosy",
    "Leptospirosis", "Lyme Disease", "Marburg Virus", "Norovirus", "Polio", "Scrub Typhus",
    "Sepsis", "Syphilis", "Tetanus", "Toxoplasmosis", "Typhoid Fever", "Zika Virus",
    "Yellow Fever", "Brucellosis", "Hepatitis A", "Hepatitis B", "Hepatitis C", "Cholera",
    "Plague", "Tularemia", "Rotavirus", "Hendra Virus", "Nipah Virus", "Schistosomiasis",
    "Ehrlichiosis", "Babesiosis", "Lassa Fever", "Filariasis", "Onchocerciasis (River Blindness)",
    "Toxocariasis", "Malaria", "Measles", "Meningitis", "Mononucleosis", "Rabies", "Shingles", "Tuberculosis (TB)", "Bacterial Meningitis", "Adenovirus", "Gonorrhea", "Herpes"],
    "Pediatrician or Infectious Disease Specialist": ["Measles"],
    "Primary Care Physician": ["Mononucleosis", "Flu", "Influenza"],
    "Pulmonologist": ["Pneumonia", "Tuberculosis (TB)", "Lung Disease","Covid-19", "Bronchitis", "Asthma", "Lung Cancer","Hantavirus", "Plague", "Hendra Virus"],
    "Urologist": ["Urinary Tract Infection", "Erectile Dysfunction", "Prostate Cancer", "Bladder Cancer", "Kidney Stones", "Gonorrhea"],
    "Vascular Surgeon": ["Varicose Veins", "Aortic Aneurysm", "Peripheral Artery Disease"],
    "Dermatologist": ["Warts", "Shingles", "Atopic Dermatitis", "Herpes","Leprosy", "Syphilis"],
    "Gynecologist or Urologist": ["Yeast Infection"],
    "Ophthalmologist": ["Acanthamoeba Keratitis", "Glaucoma","Onchocerciasis (River Blindness)", "Toxocariasis", "Trachoma"],
    "Surgeon": ["Acute Appendicitis", "Appendicitis", "Gallstones"],
    "Nephrologist": ["Leptospirosis","Acute Kidney Injury (AKI)", "Kidney Disease", "Chronic Kidney Disease"],
    "Neurologist": ["Polio", "Tetanus", "Nipah Virus","Alzheimer's Disease", "Meningitis", "Bipolar Disorder", "Dementia", "Stroke","Epilepsy", "Parkinson's Disease", "Alzheimer's"],
    "Hematologist": ["Anemia", "Blood Clot","Dengue", "Babesiosis"],
    "Cardiovascular Surgeon": ["Aortic Aneurysm"],
    "Psychiatrist": ["Bipolar Disorder", "Anxiety Disorder"],
    "Oncologist": ["Colorectal Cancer", "Prostate Cancer", "Thyroid Cancer", "Stomach Cancer", "Cancer", "Lung Cancer"],
    "Gastroenterologist": ["Norovirus", "Typhoid Fever", "Hepatitis A", "Hepatitis B", "Hepatitis C",
    "Cholera", "Rotavirus", "Whipple's Disease","Colorectal Cancer", "Salmonella", "Peptic Ulcer Disease", "Celiac Disease", "Crohn's Disease","Ulcerative Colitis", "Gallstones", "Irritable Bowel Syndrome (IBS)"],
    "Gynecologic Oncologist": ["Cervical Cancer"],
    "Endocrinologist": ["Thyroid Cancer", "Diabetes", "Hashimoto's Thyroiditis", "Graves' Disease"],
    "Rheumatologist": ["Fibromyalgia", "Rheumatoid Arthritis", "Lupus", "Arthritis","Chikungunya", "Lyme Disease"],
    "Primary Care Physician or Infectious Disease Specialist": ["Adenovirus"],
    "Allergist": ["Allergic Rhinitis", "Asthma"],
    "Psychiatrist or Psychologist": ["Anxiety Disorder"],
    "Developmental Specialist": ["Asperger Syndrome"],
    "Hepatologist": ["Aflatoxicosis", "Hepatitis"],
    "Critical Care Specialist": ["Sepsis"],
    "Hepatologist": ["Hepatitis A", "Hepatitis B", "Hepatitis C"],
    "Pediatrician":["Rotavirus"]
    
}

risklevels_disease = {
    "Malaria": "High",
    "Measles": "High",
    "Meningitis": "High",
    "Mononucleosis": "Moderate",
    "Pneumonia": "High",
    "Rabies": "High",
    "Salmonella": "Moderate",
    "Shingles": "Low",
    "Tuberculosis (TB)": "High",
    "Urinary Tract Infection": "Low",
    "Varicose Veins": "Low",
    "Warts": "Low",
    "Yeast Infection": "Low",
    "Acanthamoeba Keratitis": "Moderate",
    "Acute Appendicitis": "High",
    "Acute Kidney Injury (AKI)": "High",
    "Alzheimer's Disease": "High",
    "Anemia": "Moderate",
    "Aortic Aneurysm": "High",
    "Bacterial Meningitis": "High",
    "Bipolar Disorder": "Moderate",
    "Colorectal Cancer": "High",
    "Cervical Cancer": "High",
    "Dementia": "High",
    "Erectile Dysfunction": "Low",
    "Fibromyalgia": "Moderate",
    "Glaucoma": "Moderate",
    "Heart Failure": "High",
    "Kidney Disease": "High",
    "Lung Disease": "High",
    "Parkinson's Disease": "High",
    "Peptic Ulcer Disease": "Moderate",
    "Peripheral Artery Disease": "High",
    "Prostate Cancer": "High",
    "Rheumatoid Arthritis": "Moderate",
    "Stroke": "High",
    "Stomach Cancer": "High",
    "Thyroid Cancer": "High",
    "Ulcerative Colitis": "Moderate",
    "Atopic Dermatitis": "Low",
    "Celiac Disease": "Moderate",
    "Chronic Kidney Disease": "High",
    "Crohn's Disease": "Moderate",
    "Epilepsy": "Moderate",
    "Graves' Disease": "Moderate",
    "Hashimoto's Thyroiditis": "Moderate",
    "Lupus": "Moderate",
    "Flu": "Moderate",
    "Bronchitis": "Moderate",
    "Heart Attack": "High",
    "Cancer": "High",
    "Diabetes": "High",
    "Alzheimer's": "High",
    "Arthritis": "Moderate",
    "Adenovirus": "Moderate",
    "Aflatoxicosis": "High",
    "Allergic Rhinitis": "Low",
    "Anxiety Disorder": "Moderate",
    "Appendicitis": "High",
    "Asperger Syndrome": "Low",
    "Asthma": "Moderate",
    "Bladder Cancer": "High",
    "Blood Clot": "High",
    "Gallstones": "Moderate",
    "Gonorrhea": "Moderate",
    "Heart Disease": "High",
    "Hepatitis": "High",
    "Herpes": "Moderate",
    "Influenza": "Moderate",
    "Irritable Bowel Syndrome (IBS)": "Moderate",
    "Kidney Stones": "Moderate",
    "Lung Cancer": "High",
    "Covid-19": "High",
    "Anthrax": "High",
    "Chikungunya": "Moderate",
    "Dengue": "High",
    "Ebola": "High",
    "Hantavirus": "High",
    "HIV/AIDS": "High",
    "Leprosy": "Moderate",
    "Leptospirosis": "Moderate",
    "Lyme Disease": "Moderate",
    "Marburg Virus": "High",
    "Norovirus": "Low",
    "Polio": "High",
    "Scrub Typhus": "Moderate",
    "Sepsis": "High",
    "Syphilis": "Moderate",
    "Tetanus": "High",
    "Toxoplasmosis": "Low",
    "Typhoid Fever": "High",
    "Zika Virus": "Moderate",
    "Yellow Fever": "High",
    "Brucellosis": "Moderate",
    "Hepatitis A": "Moderate",
    "Hepatitis B": "High",
    "Hepatitis C": "High",
    "Cholera": "High",
    "Plague": "High",
    "Tularemia": "High",
    "Rotavirus": "Low",
    "Hendra Virus": "High",
    "Nipah Virus": "High",
    "Schistosomiasis": "Moderate",
    "Ehrlichiosis": "Moderate",
    "Babesiosis": "Moderate",
    "Lassa Fever": "High",
    "Filariasis": "Low",
    "Onchocerciasis (River Blindness)": "Low",
    "Toxocariasis": "Low",
    "Trachoma": "Low",
    "Whipple's Disease": "Moderate"

}
def add_custom_header():
    st.markdown(f"""
        <style>
        /* Position the background image */
        .stApp {{
            background-image: url("data:image/jpeg;base64,{get_image_base64('backgroundimage.jpg')}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}

        /* header styling */
        .header-container {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            background-color: rgba(150, 195, 210, 0.9);  
            padding: 15px 20px;
            border-bottom: 2px solid #ddd;
            width: 100%;
            box-sizing: border-box;
        }}

        /* Logo */
        .logo {{
            display: flex;
            align-items: center;
            font-weight: bold;
            font-size: 24px;
            color: #fff;  /* White text color for logo */
        }}

        .logo img {{
            height: 35px;
            margin-right: 10px;
        }}

        /* Navigation links styling */
        .nav-links {{
            display: flex;
            gap: 20px;
        }}

        .nav-links a {{
            color: #000;  /* Black text for nav links */
            text-decoration: none;
            font-size: 18px;
            font-weight: bold;
        }}

        .nav-links a:hover {{
            color: #007acc;
            text-decoration: underline;
        }}

        /* Section */
        .section {{
            padding: 50px 20px;
            margin: 20px 0;
            border-radius: 8px;
        }}

        /* About us and Contact  */
        #about, #contact {{
            background-color:  rgba(150, 195, 210, 0.9); 
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
        }}
        </style>

        <div class="header-container">
            <div class="logo">
                <img src="data:image/png;base64,{get_image_base64('finalwhite.png')}" alt="Logo">
                <span></span>
            </div>
            <div class="nav-links">
                <a href="/">Home</a>
                <a href="#contact">Contact</a>
                <a href="#about">About Us</a>
            </div>
        </div>
    """, unsafe_allow_html=True)

def get_base64_encoded_image(file_path):
    with open(file_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")
        
def detect_diseases(user_symptoms):
    disease_matches = {}
    
    for disease, symptoms in disease_symptoms.items():
        symptoms_list = [symptom.strip().lower() for symptom in symptoms.split(",")]
        match_count = len(set(user_symptoms).intersection(symptoms_list))
        disease_matches[disease] = match_count
    
    max_matches = max(disease_matches.values(), default=0)
    likely_diseases = [disease for disease, matches in disease_matches.items() if matches == max_matches and matches > 0]
    return likely_diseases, disease_matches
    
def show_about_us():
    st.markdown("""
        <div class="section" id="about">
            <h2>About Us</h2>
            <p>MedTech is an online fitness tool that helps individuals understand possible causes of their symptoms. 
            By entering symptoms into the website, users receive information about potential health conditions, 
            risk levels, and relevant disease specialists. MedTech aims to empower users to manage their health 
            with accessible, easy-to-understand information, enabling them to make more informed decisions 
            about consulting healthcare providers.</p>
    """, unsafe_allow_html=True)

def show_contact():
    st.markdown("""
        <div class="section" id="contact">
            <h2>Contact Us</h2>
            <p>If you need any support, please don't hesitate to reach out:</p>
            <ul>
                <li>Email: electric.capybara.llmr@instantletter.net</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

def main():
    add_custom_header()

    st.title("MedTech - Disease Prediction System")
    st.write("Enter your symptoms to get a possible diagnosis")

    all_symptoms = set()
    for symptoms in disease_symptoms.values():
        all_symptoms.update([symptom.strip().lower() for symptom in symptoms.split(",")])
    all_symptoms = sorted(list(all_symptoms))

    user_symptoms = st.multiselect(
        "Select your symptoms:",
        all_symptoms
    )

    if st.button("Get Diagnosis"):
        if not user_symptoms:
            st.warning("Please select at least one symptom")
        else:
            predicted_diseases, disease_matches = detect_diseases(user_symptoms)

            if predicted_diseases:
                st.subheader("Predicted Diseases:")
                for disease in predicted_diseases:
                    st.write(f"- {disease}")

                    risk = risklevels_disease.get(disease, "Unknown")
                    st.write(f"Risk Level: {risk}")

                    st.write("Recommended Specialists:")
                    specialist_found = False
                    for specialist, diseases in disease_specialist.items():
                        if disease in diseases:
                            st.write(f"- {specialist}")
                            specialist_found = True
                    
                    if not specialist_found:
                        st.write("- Please consult a general physician")
                    
                    st.write("---")
            else:
                st.warning("No disease matches your symptoms. Please consult a general physician.")
            st.write("Thank you for using MedTech...")

    show_about_us()
    show_contact()

    st.markdown("""
    ---
    **Disclaimer:** This is not a substitute for professional medical advice. 
    Always consult with a qualified healthcare provider for proper diagnosis and treatment.
    """)

    st.markdown("""
    ---
    Criteria for Risk Assessment:\n
    High: Diseases with a high fatality rate, rapid progression, or potential for outbreaks.\n
    Moderate: Diseases with significant health impacts but lower fatality rates or slower progression.\n
    Low: Diseases that are usually manageable or cause mild symptoms.\n
    """)


if __name__ == "__main__":
    main()
