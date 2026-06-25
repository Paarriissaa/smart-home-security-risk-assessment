import streamlit as st
import joblib
import pandas as pd
import matplotlib.pyplot as plt
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

# Security Score
def calculate_security_score(data):

    score = (
        data["password_changed"] * 10 +
        (data["password_strength"] / 2) * 8 +
        data["mfa_enabled"] * 10 +
        (data["update_frequency"] / 2) * 10 +
        data["latest_firmware"] * 10 +
        (data["wifi_security"] / 2) * 8 +
        data["guest_network"] * 4 +
        (data["remote_access"] / 2) * 8 +
        data["communication_encryption"] * 8 +
        data["data_encryption"] * 8 +
        (data["manufacturer_reputation"] / 2) * 4 +
        data["unused_services_disabled"] * 4 +
        data["security_logs"] * 2 +
        data["permission_review"] * 3 +
        data["data_minimization"] * 3
    )

    return round(score, 2)

# GDPR Compliance
def calculate_gdpr(data):

    score = (
        data["data_encryption"] +
        data["permission_review"] +
        data["data_minimization"] +
        data["communication_encryption"]
    )

    return round((score / 4) * 100, 2)

# NIST Compliance

def calculate_nist(data):

    score = (
        data["mfa_enabled"] +
        data["latest_firmware"] +
        data["security_logs"] +
        data["password_changed"] +
        data["unused_services_disabled"]
    )

    return round((score / 5) * 100, 2)

# ETSI Compliance

def calculate_etsi(data):

    score = (
        data["communication_encryption"] +
        data["password_changed"] +
        data["latest_firmware"] +
        data["data_encryption"] +
        data["unused_services_disabled"]
    )

    return round((score / 5) * 100, 2)
def generate_pdf_report(
    device_type,
    risk_level,
    security_score,
    gdpr_score,
    nist_score,
    etsi_score,
    recommendations
):

    pdf_file = "security_report.pdf"

    doc = SimpleDocTemplate(pdf_file)

    styles = getSampleStyleSheet()

    content = []

    content.append(
        Paragraph(
            "Smart Home Security Assessment Report",
            styles['Title']
        )
    )

    content.append(Spacer(1, 12))

    content.append(
        Paragraph(
            f"Device Type: {device_type}",
            styles['Normal']
        )
    )

    content.append(
        Paragraph(
            f"Predicted Risk Level: {risk_level}",
            styles['Normal']
        )
    )

    content.append(
        Paragraph(
            f"Security Score: {security_score}/100",
            styles['Normal']
        )
    )

    content.append(
        Paragraph(
            f"GDPR Compliance: {gdpr_score}%",
            styles['Normal']
        )
    )

    content.append(
        Paragraph(
            f"NIST Compliance: {nist_score}%",
            styles['Normal']
        )
    )

    content.append(
        Paragraph(
            f"ETSI Compliance: {etsi_score}%",
            styles['Normal']
        )
    )

    content.append(Spacer(1, 12))

    content.append(
        Paragraph(
            "Recommendations",
            styles['Heading2']
        )
    )

    for rec in recommendations:

        content.append(
            Paragraph(
                f"- {rec}",
                styles['Normal']
            )
        )

    doc.build(content)

    return pdf_file

# Load Models

model = joblib.load("models/smart_home_rf_model.pkl")
risk_encoder = joblib.load("models/risk_encoder.pkl")
device_encoder = joblib.load("models/device_encoder.pkl")
importance_df = pd.read_csv(
    "outputs/feature_importance.csv"
)

# Page Title

st.title(
    "Smart Home Security Risk Assessment System"
)

st.write(
    "Evaluate the security risk level of your smart home devices using Machine Learning."
)

# User Inputs

device_type = st.selectbox(
    "Device Type",
    ["Camera", "Smart Lock", "Smart Sensor", "Smart Speaker", "Thermostat"]
)

password_changed = st.selectbox(
    "Default Password Changed?",
    [0, 1]
)

password_strength = st.selectbox(
    "Password Strength",
    [0, 1, 2]
)

mfa_enabled = st.selectbox(
    "Multi-Factor Authentication Enabled?",
    [0, 1]
)

update_frequency = st.selectbox(
    "Update Frequency",
    [0, 1, 2]
)

latest_firmware = st.selectbox(
    "Latest Firmware Installed?",
    [0, 1]
)

wifi_security = st.selectbox(
    "WiFi Security Level",
    [0, 1, 2]
)

guest_network = st.selectbox(
    "Guest Network Enabled?",
    [0, 1]
)

remote_access = st.selectbox(
    "Remote Access Security",
    [0, 1, 2]
)

communication_encryption = st.selectbox(
    "Communication Encryption",
    [0, 1]
)

data_encryption = st.selectbox(
    "Data Encryption",
    [0, 1]
)

manufacturer_reputation = st.selectbox(
    "Manufacturer Reputation",
    [0, 1, 2]
)

unused_services_disabled = st.selectbox(
    "Unused Services Disabled?",
    [0, 1]
)

security_logs = st.selectbox(
    "Security Logs Enabled?",
    [0, 1]
)

permission_review = st.selectbox(
    "Permission Review Performed?",
    [0, 1]
)

data_minimization = st.selectbox(
    "Data Minimization Applied?",
    [0, 1]
)
# Prediction

if st.button("Predict Risk"):

    device_encoded = device_encoder.transform(
        [device_type]
    )[0]

    input_data = pd.DataFrame([[
        device_encoded,
        password_changed,
        password_strength,
        mfa_enabled,
        update_frequency,
        latest_firmware,
        wifi_security,
        guest_network,
        remote_access,
        communication_encryption,
        data_encryption,
        manufacturer_reputation,
        unused_services_disabled,
        security_logs,
        permission_review,
        data_minimization
    ]], columns=[
        'device_type',
        'password_changed',
        'password_strength',
        'mfa_enabled',
        'update_frequency',
        'latest_firmware',
        'wifi_security',
        'guest_network',
        'remote_access',
        'communication_encryption',
        'data_encryption',
        'manufacturer_reputation',
        'unused_services_disabled',
        'security_logs',
        'permission_review',
        'data_minimization'
    ])

    user_data = {
        "password_changed": password_changed,
        "password_strength": password_strength,
        "mfa_enabled": mfa_enabled,
        "update_frequency": update_frequency,
        "latest_firmware": latest_firmware,
        "wifi_security": wifi_security,
        "guest_network": guest_network,
        "remote_access": remote_access,
        "communication_encryption": communication_encryption,
        "data_encryption": data_encryption,
        "manufacturer_reputation": manufacturer_reputation,
        "unused_services_disabled": unused_services_disabled,
        "security_logs": security_logs,
        "permission_review": permission_review,
        "data_minimization": data_minimization
    }

    prediction = model.predict(input_data)

    risk_level = risk_encoder.inverse_transform(
        prediction
    )[0]

    security_score = calculate_security_score(
        user_data
    )

    gdpr_score = calculate_gdpr(
        user_data
    )

    nist_score = calculate_nist(
        user_data
    )

    etsi_score = calculate_etsi(
        user_data
    )

    # Risk Level

    if risk_level == "Critical":

        st.error(
            f"Predicted Risk Level: {risk_level}"
        )

    elif risk_level == "High":

        st.warning(
            f"Predicted Risk Level: {risk_level}"
        )

    elif risk_level == "Medium":

        st.info(
            f"Predicted Risk Level: {risk_level}"
        )

    else:

        st.success(
            f"Predicted Risk Level: {risk_level}"
        )

    # Security Assessment

    st.subheader(
        "Security Assessment"
    )

    st.metric(
        "Security Score",
        f"{security_score}/100"
    )

    st.progress(
        security_score / 100
    )

    st.metric(
        "GDPR Compliance",
        f"{gdpr_score}%"
    )

    st.metric(
        "NIST Compliance",
        f"{nist_score}%"
    )

    st.metric(
        "ETSI Compliance",
        f"{etsi_score}%"
    )

    # Compliance Chart
   
    st.subheader(
        "Compliance Comparison"
    )

    frameworks = [
        "GDPR",
        "NIST",
        "ETSI"
    ]

    scores = [
        gdpr_score,
        nist_score,
        etsi_score
    ]

    fig, ax = plt.subplots(
        figsize=(6,4)
    )

    ax.bar(
        frameworks,
        scores
    )

    ax.set_ylim(
        0,
        100
    )

    ax.set_ylabel(
        "Compliance (%)"
    )

    ax.set_title(
        "Security Compliance Assessment"
    )

    st.pyplot(
        fig
    )

    # Security Status

    st.subheader(
        "Security Status"
    )

    if security_score >= 80:

        st.success(
            "Excellent Security Posture"
        )

    elif security_score >= 60:

        st.info(
            "Good Security Posture"
        )

    elif security_score >= 40:

        st.warning(
            "Moderate Security Risk"
        )

    else:

        st.error(
            "High Security Risk"
        )
   
    # Feature Importance

    st.subheader(
        "Top Security Factors"
    )

    top_features = importance_df.head(10)

    fig2, ax2 = plt.subplots(
        figsize=(8,5)
    )

    ax2.barh(
        top_features["Feature"],
        top_features["Importance"]
    )

    ax2.set_title(
        "Feature Importance (Random Forest)"
    )

    st.pyplot(fig2)

# Importance Table

    importance_table = top_features.copy()

    importance_table["Importance (%)"] = (
        importance_table["Importance"] * 100
    ).round(2)

    importance_table = importance_table[
        ["Feature", "Importance (%)"]
    ]

    st.subheader(
        "Feature Importance Values"
    )

    st.dataframe(
        importance_table,
        use_container_width=True
    )

    # Recommendations

    recommendations = []

    if mfa_enabled == 0:

        recommendations.append(
            "Enable Multi-Factor Authentication (MFA)"
        )

    if latest_firmware == 0:

        recommendations.append(
            "Update device firmware regularly"
        )

    if data_encryption == 0:

        recommendations.append(
            "Enable data encryption"
        )

    if password_changed == 0:

        recommendations.append(
            "Change default passwords"
        )

    if security_logs == 0:

        recommendations.append(
            "Enable security logging"
        )

        st.subheader(
        "Recommendations"
    )

    if recommendations:

        for item in recommendations:

            st.write(
                "✓",
                item
            )

    else:

        st.success(
            "Excellent security posture. No major issues detected."
        )

    # PDF Report

    pdf_file = generate_pdf_report(
        device_type,
        risk_level,
        security_score,
        gdpr_score,
        nist_score,
        etsi_score,
        recommendations
    )

    with open(pdf_file, "rb") as file:

        st.download_button(
            label="Download PDF Report",
            data=file,
            file_name="Smart_Home_Security_Report.pdf",
            mime="application/pdf"
        )