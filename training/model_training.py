import pandas as pd
import numpy as np
import random


NUM_RECORDS = 3000

data = []

def yes_no(probability):
    return 1 if random.random() < probability else 0

for _ in range(NUM_RECORDS):

    
    device_type = random.choice([
        "Camera",
        "Smart Lock",
        "Thermostat",
        "Smart Speaker",
        "Smart Sensor"
    ])

  
    profile = random.choices(
        [
            "Security Expert",
            "Security Aware",
            "Average User",
            "Negligent User",
            "Vulnerable User"
        ],
        weights=[15, 20, 30, 20, 15]
    )[0]



    if profile == "Security Expert":

        password_changed = yes_no(0.95)
        password_strength = random.choices([1, 2], weights=[10, 90])[0]
        mfa_enabled = yes_no(0.95)
        update_frequency = random.choices([1, 2], weights=[10, 90])[0]
        latest_firmware = yes_no(0.95)
        wifi_security = random.choices([1, 2], weights=[10, 90])[0]
        guest_network = yes_no(0.90)
        remote_access = random.choices([1, 2], weights=[20, 80])[0]
        communication_encryption = yes_no(0.95)
        data_encryption = yes_no(0.95)
        manufacturer_reputation = random.choices([1, 2], weights=[20, 80])[0]
        unused_services_disabled = yes_no(0.90)
        security_logs = yes_no(0.90)
        permission_review = yes_no(0.90)
        data_minimization = yes_no(0.90)


    elif profile == "Security Aware":

        password_changed = yes_no(0.85)
        password_strength = random.choices([0,1,2], weights=[10,30,60])[0]
        mfa_enabled = yes_no(0.75)
        update_frequency = random.choices([0,1,2], weights=[10,30,60])[0]
        latest_firmware = yes_no(0.80)
        wifi_security = random.choices([0,1,2], weights=[10,40,50])[0]
        guest_network = yes_no(0.70)
        remote_access = random.choices([0,1,2], weights=[10,40,50])[0]
        communication_encryption = yes_no(0.80)
        data_encryption = yes_no(0.80)
        manufacturer_reputation = random.choices([0,1,2], weights=[10,40,50])[0]
        unused_services_disabled = yes_no(0.70)
        security_logs = yes_no(0.70)
        permission_review = yes_no(0.70)
        data_minimization = yes_no(0.70)

    

    elif profile == "Average User":

        password_changed = yes_no(0.60)
        password_strength = random.choices([0,1,2], weights=[30,40,30])[0]
        mfa_enabled = yes_no(0.40)
        update_frequency = random.choices([0,1,2], weights=[30,40,30])[0]
        latest_firmware = yes_no(0.50)
        wifi_security = random.choices([0,1,2], weights=[30,40,30])[0]
        guest_network = yes_no(0.50)
        remote_access = random.choices([0,1,2], weights=[30,40,30])[0]
        communication_encryption = yes_no(0.50)
        data_encryption = yes_no(0.50)
        manufacturer_reputation = random.choices([0,1,2], weights=[20,50,30])[0]
        unused_services_disabled = yes_no(0.50)
        security_logs = yes_no(0.50)
        permission_review = yes_no(0.50)
        data_minimization = yes_no(0.50)

    

    elif profile == "Negligent User":

        password_changed = yes_no(0.40)
        password_strength = random.choices([0,1,2], weights=[60,30,10])[0]
        mfa_enabled = yes_no(0.20)
        update_frequency = random.choices([0,1,2], weights=[60,30,10])[0]
        latest_firmware = yes_no(0.30)
        wifi_security = random.choices([0,1,2], weights=[60,30,10])[0]
        guest_network = yes_no(0.30)
        remote_access = random.choices([0,1,2], weights=[60,30,10])[0]
        communication_encryption = yes_no(0.30)
        data_encryption = yes_no(0.30)
        manufacturer_reputation = random.choices([0,1,2], weights=[50,30,20])[0]
        unused_services_disabled = yes_no(0.30)
        security_logs = yes_no(0.30)
        permission_review = yes_no(0.30)
        data_minimization = yes_no(0.30)

    

    else:

        password_changed = yes_no(0.10)
        password_strength = random.choices([0,1], weights=[90,10])[0]
        mfa_enabled = yes_no(0.05)
        update_frequency = random.choices([0,1], weights=[90,10])[0]
        latest_firmware = yes_no(0.10)
        wifi_security = random.choices([0,1], weights=[90,10])[0]
        guest_network = yes_no(0.10)
        remote_access = random.choices([0,1], weights=[90,10])[0]
        communication_encryption = yes_no(0.10)
        data_encryption = yes_no(0.10)
        manufacturer_reputation = random.choices([0,1], weights=[80,20])[0]
        unused_services_disabled = yes_no(0.10)
        security_logs = yes_no(0.10)
        permission_review = yes_no(0.10)
        data_minimization = yes_no(0.10)

    

    score = (
        password_changed * 10 +
        (password_strength / 2) * 8 +
        mfa_enabled * 10 +
        (update_frequency / 2) * 10 +
        latest_firmware * 10 +
        (wifi_security / 2) * 8 +
        guest_network * 4 +
        (remote_access / 2) * 8 +
        communication_encryption * 8 +
        data_encryption * 8 +
        (manufacturer_reputation / 2) * 4 +
        unused_services_disabled * 4 +
        security_logs * 2 +
        permission_review * 3 +
        data_minimization * 3
    )

    

    if score >= 90:
        risk_level = "Very Low"
    elif score >= 75:
        risk_level = "Low"
    elif score >= 55:
        risk_level = "Medium"
    elif score >= 35:
        risk_level = "High"
    else:
        risk_level = "Critical"

    data.append([
        device_type,
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
        data_minimization,
        round(score, 2),
        risk_level
    ])



columns = [
    "device_type",
    "password_changed",
    "password_strength",
    "mfa_enabled",
    "update_frequency",
    "latest_firmware",
    "wifi_security",
    "guest_network",
    "remote_access",
    "communication_encryption",
    "data_encryption",
    "manufacturer_reputation",
    "unused_services_disabled",
    "security_logs",
    "permission_review",
    "data_minimization",
    "security_score",
    "risk_level"
]

df = pd.DataFrame(data, columns=columns)


df.to_csv("smart_home_security_dataset_v2.csv", index=False)

print("Dataset Shape:", df.shape)
print("\nRisk Distribution:")
print(df["risk_level"].value_counts())


# Data Preparation

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
# Features (X)
X = df.drop(columns=["risk_level", "security_score"])

# Target (y)

y = df["risk_level"]


# Encode Device Type

le_device = LabelEncoder()

X["device_type"] = le_device.fit_transform(
    X["device_type"]
)

device_mapping = dict(
    zip(
        le_device.classes_,
        le_device.transform(le_device.classes_)
    )
)

print("Device Encoding:")
print(device_mapping)

 
# Encode Risk Levels


le_risk = LabelEncoder()

y = le_risk.fit_transform(y)

risk_mapping = dict(
    zip(
        le_risk.classes_,
        le_risk.transform(le_risk.classes_)
    )
)

print("\nRisk Encoding:")
print(risk_mapping)

# Train / Test Split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("\nDataset Shapes")

print("X_train:", X_train.shape)
print("X_test :", X_test.shape)

print("y_train:", y_train.shape)
print("y_test :", y_test.shape)


from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

dt_model = DecisionTreeClassifier(
    random_state=42
)

dt_model.fit(X_train, y_train)

y_pred_dt = dt_model.predict(X_test)

accuracy_dt = accuracy_score(
    y_test,
    y_pred_dt
)

print("Decision Tree Accuracy:")
print(round(accuracy_dt * 100, 2), "%")

from sklearn.metrics import classification_report

print(
    classification_report(
        y_test,
        y_pred_dt,
        target_names=le_risk.classes_
    )
)

from sklearn.metrics import confusion_matrix

cm = confusion_matrix(
    y_test,
    y_pred_dt
)

print(cm)


from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

rf_model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

rf_model.fit(X_train, y_train)

y_pred_rf = rf_model.predict(X_test)

rf_accuracy = accuracy_score(
    y_test,
    y_pred_rf
)

print("Random Forest Accuracy:")
print(round(rf_accuracy * 100, 2), "%")

importance_df = pd.DataFrame({
    "Feature": X.columns,
    "Importance": rf_model.feature_importances_
})

importance_df = importance_df.sort_values(
    by="Importance",
    ascending=False
)

print(importance_df)

importance_df.to_csv(
    "feature_importance.csv",
    index=False
)


importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": rf_model.feature_importances_
})

importance = importance.sort_values(
    by="Importance",
    ascending=False
)

print(importance)

import matplotlib.pyplot as plt

plt.figure(figsize=(10,6))

plt.barh(
    importance["Feature"],
    importance["Importance"]
)

plt.xlabel("Importance Score")
plt.ylabel("Features")

plt.title("Feature Importance - Random Forest")

plt.tight_layout()

plt.show()


from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)

X_test_scaled = scaler.transform(X_test)

print(X_train_scaled.shape)
print(X_test_scaled.shape)

from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

results = []

for k in range(1, 31):

    model = KNeighborsClassifier(
        n_neighbors=k
    )

    model.fit(
        X_train_scaled,
        y_train
    )

    pred = model.predict(
        X_test_scaled
    )

    acc = accuracy_score(
        y_test,
        pred
    )

    results.append([k, acc])

for k, acc in results:
    print(
        f"K={k}  Accuracy={acc:.4f}"
    )

from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

knn_model = KNeighborsClassifier(
    n_neighbors=5
)

knn_model.fit(
    X_train_scaled,
    y_train
)

y_pred_knn = knn_model.predict(
    X_test_scaled
)

knn_accuracy = accuracy_score(
    y_test,
    y_pred_knn
)

print("KNN Accuracy:")
print(round(knn_accuracy * 100, 2), "%")

import joblib

joblib.dump(
    rf_model,
    "smart_home_rf_model.pkl"
)

joblib.dump(
    le_risk,
    "risk_encoder.pkl"
)

joblib.dump(
    le_device,
    "device_encoder.pkl"
)

print("Models saved successfully")
