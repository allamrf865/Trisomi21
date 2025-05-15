import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Simulasi data untuk 71.890 pasien Down Syndrome
np.random.seed(42)

num_patients = 71890

# Kolom data
ages = np.random.randint(0, 50, num_patients)  
weights = np.random.uniform(5, 30, num_patients)
heights = np.random.uniform(40, 140, num_patients)
head_circumference = np.random.uniform(40, 55, num_patients)
developmental_milestones = np.random.choice(['Met', 'Not Met'], num_patients)
motor_skills = np.random.choice(['Normal', 'Delayed'], num_patients)
speech = np.random.choice(['Normal', 'Delayed'], num_patients)
kpsp_score = np.random.uniform(0, 100, num_patients)
cognitive_functioning = np.random.choice(['Normal', 'Delayed'], num_patients)
hearing_impairment = np.random.choice(['None', 'Mild', 'Severe'], num_patients)
visual_impairment = np.random.choice(['None', 'Mild', 'Severe'], num_patients)
heart_disease = np.random.choice(['None', 'Congenital', 'Acquired'], num_patients)
hypothyroidism = np.random.choice(['None', 'Present'], num_patients)
surgical_history = np.random.choice(['None', 'Multiple', 'Single'], num_patients)
vaccination_status = np.random.choice(['Fully Vaccinated', 'Partially Vaccinated', 'Not Vaccinated'], num_patients)
genetic_screening = np.random.choice(['Normal', 'Abnormal'], num_patients)
survival_rate = np.random.uniform(0, 100, num_patients)
age_at_diagnosis = np.random.randint(0, 5, num_patients)
medication_history = np.random.choice(['None', 'Ongoing', 'Completed'], num_patients)
sleep_patterns = np.random.choice(['Normal', 'Disturbed'], num_patients)
social_behavior = np.random.choice(['Normal', 'Delayed'], num_patients)
parental_support = np.random.choice(['High', 'Moderate', 'Low'], num_patients)
speech_therapy = np.random.choice(['None', 'Regular', 'Occasional'], num_patients)
occupational_therapy = np.random.choice(['None', 'Regular', 'Occasional'], num_patients)
physical_therapy = np.random.choice(['None', 'Regular', 'Occasional'], num_patients)
mental_health_issues = np.random.choice(['None', 'Mild', 'Severe'], num_patients)
nutritional_intake = np.random.choice(['Adequate', 'Inadequate'], num_patients)
hospital_visits = np.random.randint(0, 10, num_patients)
age_at_first_diagnosis = np.random.randint(0, 5, num_patients)
communication_skills = np.random.choice(['Normal', 'Delayed'], num_patients)
educational_placement = np.random.choice(['Special Education', 'Mainstream', 'None'], num_patients)

# Membuat dataframe
df_simulation = pd.DataFrame({
    'patient_id': range(1, num_patients+1),
    'age': ages,
    'weight': weights,
    'height': heights,
    'head_circumference': head_circumference,
    'developmental_milestones': developmental_milestones,
    'motor_skills': motor_skills,
    'speech': speech,
    'kpsp_score': kpsp_score,
    'cognitive_functioning': cognitive_functioning,
    'hearing_impairment': hearing_impairment,
    'visual_impairment': visual_impairment,
    'heart_disease': heart_disease,
    'hypothyroidism': hypothyroidism,
    'surgical_history': surgical_history,
    'vaccination_status': vaccination_status,
    'genetic_screening': genetic_screening,
    'survival_rate': survival_rate,
    'age_at_diagnosis': age_at_diagnosis,
    'medication_history': medication_history,
    'sleep_patterns': sleep_patterns,
    'social_behavior': social_behavior,
    'parental_support': parental_support,
    'speech_therapy': speech_therapy,
    'occupational_therapy': occupational_therapy,
    'physical_therapy': physical_therapy,
    'mental_health_issues': mental_health_issues,
    'nutritional_intake': nutritional_intake,
    'hospital_visits': hospital_visits,
    'age_at_first_diagnosis': age_at_first_diagnosis,
    'communication_skills': communication_skills,
    'educational_placement': educational_placement
})

# Judul dan Deskripsi
st.title("Dashboard Perkembangan Anak Down Syndrome")
st.write("Pilih salah satu pasien untuk melihat perkembangan mereka berdasarkan berbagai indikator.")

# Dropdown untuk memilih pasien
patient_id = st.selectbox('Pilih Patient ID', df_simulation['patient_id'].head(10))

# Filter data pasien
patient_data = df_simulation[df_simulation['patient_id'] == patient_id].iloc[0]

# Tampilkan detail pasien
st.subheader(f"Detail Perkembangan Pasien {patient_id}")
st.write(f"**Age**: {patient_data['age']} years")
st.write(f"**Weight**: {patient_data['weight']} kg")
st.write(f"**Height**: {patient_data['height']} cm")
st.write(f"**Head Circumference**: {patient_data['head_circumference']} cm")
st.write(f"**Developmental Milestones**: {patient_data['developmental_milestones']}")
st.write(f"**Motor Skills**: {patient_data['motor_skills']}")
st.write(f"**Speech**: {patient_data['speech']}")
st.write(f"**KPSP Score**: {patient_data['kpsp_score']}")
st.write(f"**Cognitive Functioning**: {patient_data['cognitive_functioning']}")
st.write(f"**Hearing Impairment**: {patient_data['hearing_impairment']}")
st.write(f"**Visual Impairment**: {patient_data['visual_impairment']}")
st.write(f"**Heart Disease**: {patient_data['heart_disease']}")
st.write(f"**Hypothyroidism**: {patient_data['hypothyroidism']}")
st.write(f"**Surgical History**: {patient_data['surgical_history']}")
st.write(f"**Vaccination Status**: {patient_data['vaccination_status']}")
st.write(f"**Genetic Screening**: {patient_data['genetic_screening']}")
st.write(f"**Survival Rate**: {patient_data['survival_rate']}%")
st.write(f"**Age at Diagnosis**: {patient_data['age_at_diagnosis']} years")
st.write(f"**Medication History**: {patient_data['medication_history']}")
st.write(f"**Sleep Patterns**: {patient_data['sleep_patterns']}")
st.write(f"**Social Behavior**: {patient_data['social_behavior']}")
st.write(f"**Parental Support**: {patient_data['parental_support']}")
st.write(f"**Speech Therapy**: {patient_data['speech_therapy']}")
st.write(f"**Occupational Therapy**: {patient_data['occupational_therapy']}")
st.write(f"**Physical Therapy**: {patient_data['physical_therapy']}")
st.write(f"**Mental Health Issues**: {patient_data['mental_health_issues']}")
st.write(f"**Nutritional Intake**: {patient_data['nutritional_intake']}")
st.write(f"**Hospital Visits**: {patient_data['hospital_visits']}")
st.write(f"**Age at First Diagnosis**: {patient_data['age_at_first_diagnosis']} years")
st.write(f"**Communication Skills**: {patient_data['communication_skills']}")
st.write(f"**Educational Placement**: {patient_data['educational_placement']}")

# Visualisasi Grafik menggunakan Matplotlib dan Seaborn
st.subheader("Grafik Visualisasi")

# Weight Chart
fig, ax = plt.subplots()
ax.bar(["Weight"], [patient_data['weight']])
ax.set_title(f"Weight of Patient {patient_id}")
ax.set_ylabel("Weight (kg)")
st.pyplot(fig)

# KPSP Score Chart
fig, ax = plt.subplots()
ax.bar(["KPSP Score"], [patient_data['kpsp_score']])
ax.set_title(f"KPSP Score of Patient {patient_id}")
ax.set_ylabel("KPSP Score")
st.pyplot(fig)

# Survival Rate Chart
fig, ax = plt.subplots()
ax.bar(["Survival Rate"], [patient_data['survival_rate']])
ax.set_title(f"Survival Rate of Patient {patient_id}")
ax.set_ylabel("Survival Rate (%)")
st.pyplot(fig)

# Developmental Milestones Pie Chart
fig, ax = plt.subplots()
labels = ["Met", "Not Met"]
sizes = [(patient_data['developmental_milestones'] == "Met"), 
         (patient_data['developmental_milestones'] == "Not Met")]
ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
ax.set_title(f"Developmental Milestones of Patient {patient_id}")
st.pyplot(fig)
