import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

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

# Membuat aplikasi Dash
app = dash.Dash(__name__)

# Layout Dash
app.layout = html.Div([
    html.H1("Dashboard Perkembangan Anak Down Syndrome"),
    
    html.Div([
        dcc.Dropdown(
            id='patient-dropdown',
            options=[{'label': f"Patient {i}", 'value': i} for i in range(1, 11)],  # 10 pasien untuk contoh
            value=1,
            style={'width': '50%'}
        )
    ]),
    
    html.Div([
        dcc.Graph(id='weight-graph'),
        dcc.Graph(id='kpsp-graph'),
        dcc.Graph(id='survival-rate-graph'),
        dcc.Graph(id='developmental-milestones-graph'),
        html.Div(id='patient-details')
    ])
])

# Callback untuk menampilkan detail pasien berdasarkan ID
@app.callback(
    [Output('patient-details', 'children'),
     Output('weight-graph', 'figure'),
     Output('kpsp-graph', 'figure'),
     Output('survival-rate-graph', 'figure'),
     Output('developmental-milestones-graph', 'figure')],
    [Input('patient-dropdown', 'value')]
)
def display_patient_details(patient_id):
    # Filter data untuk pasien yang dipilih
    patient_data = df_simulation[df_simulation['patient_id'] == patient_id].iloc[0]
    
    # Tampilkan detail
    details = [
        html.H3(f"Detail Perkembangan Pasien {patient_id}"),
        html.Div(f"Age: {patient_data['age']} years"),
        html.Div(f"Weight: {patient_data['weight']} kg"),
        html.Div(f"Height: {patient_data['height']} cm"),
        html.Div(f"Developmental Milestones: {patient_data['developmental_milestones']}"),
        html.Div(f"KPSP Score: {patient_data['kpsp_score']}"),
        html.Div(f"Survival Rate: {patient_data['survival_rate']}%"),
        html.Div(f"Motor Skills: {patient_data['motor_skills']}"),
        html.Div(f"Speech: {patient_data['speech']}")
    ]
    
    # Visualisasi data pasien
    weight_fig = px.bar(x=["Weight"], y=[patient_data['weight']], title=f"Weight of Patient {patient_id}")
    kpsp_fig = px.bar(x=["KPSP Score"], y=[patient_data['kpsp_score']], title=f"KPSP Score of Patient {patient_id}")
    survival_fig = px.bar(x=["Survival Rate"], y=[patient_data['survival_rate']], title=f"Survival Rate of Patient {patient_id}")
    milestones_fig = px.pie(names=["Met", "Not Met"], values=[(patient_data['developmental_milestones'] == "Met"), 
                                                            (patient_data['developmental_milestones'] == "Not Met")],
                            title=f"Developmental Milestones of Patient {patient_id}")

    return details, weight_fig, kpsp_fig, survival_fig, milestones_fig

# Menjalankan aplikasi
if __name__ == '__main__':
    app.run_server(debug=True)
