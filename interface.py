import tkinter as tk
from tkinter import messagebox
import pickle
import numpy as np
import tensorflow as tf  # Only needed if using a Keras model

# Load the trained model (Make sure it's a valid .pkl or .h5 file)
model_path = r"C:/Users/ramak/OneDrive/Desktop/deep learning models/ANN/CUSTOMER CHURN/modelann churn.pkl"
# Change if using a .h5 Keras model
with open(model_path, "rb") as file:
    model = pickle.load(file)  # Use tf.keras.models.load_model() if using a Keras model

# Function to predict customer churn
def predict_churn():
    try:
        # Get values from user input
        credit_score = int(entry_credit_score.get())
        geography = entry_geography.get().strip().lower()
        gender = entry_gender.get().strip().lower()
        age = int(entry_age.get())
        tenure = int(entry_tenure.get())
        balance = float(entry_balance.get())
        num_of_products = int(entry_num_of_products.get())
        has_cr_card = int(entry_has_cr_card.get())
        is_active_member = int(entry_is_active.get())
        estimated_salary = float(entry_estimated_salary.get())

        # Convert categorical data
        geography_map = {"france": 0, "spain": 1, "germany": 2}
        gender_map = {"male": 0, "female": 1}

        if geography not in geography_map or gender not in gender_map:
            messagebox.showerror("Input Error", "Invalid Geography or Gender! Use France, Spain, Germany and Male/Female")
            return

        geography = geography_map[geography]
        gender = gender_map[gender]

        # Prepare input data for prediction
        input_data = np.array([[credit_score, geography, gender, age, tenure, balance, num_of_products, has_cr_card, is_active_member, estimated_salary]])

        # Check model type and predict accordingly
        if isinstance(model, tf.keras.Model):  # If it's a Keras model
            prediction_prob = model.predict(input_data)  # Returns probability
            prediction = (prediction_prob > 0.5).astype(int)[0][0]  # Convert to 0 or 1
        else:  # If it's a Scikit-learn model
            prediction = model.predict(input_data)[0]  # Returns 0 or 1 directly

        # Display result
        result = "Customer is likely to CHURN! (Exited = 1)" if prediction == 1 else "Customer is likely to STAY (Exited = 0)"
        messagebox.showinfo("Prediction Result", result)

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values where required.")

# Create Tkinter window
root = tk.Tk()
root.title("Churn Prediction Model")
root.geometry("400x500")

# Labels and Entry Fields
tk.Label(root, text="Credit Score:").grid(row=0, column=0, padx=10, pady=5)
entry_credit_score = tk.Entry(root)
entry_credit_score.grid(row=0, column=1)

tk.Label(root, text="Geography (France/Spain/Germany):").grid(row=1, column=0, padx=10, pady=5)
entry_geography = tk.Entry(root)
entry_geography.grid(row=1, column=1)

tk.Label(root, text="Gender (Male/Female):").grid(row=2, column=0, padx=10, pady=5)
entry_gender = tk.Entry(root)
entry_gender.grid(row=2, column=1)

tk.Label(root, text="Age:").grid(row=3, column=0, padx=10, pady=5)
entry_age = tk.Entry(root)
entry_age.grid(row=3, column=1)

tk.Label(root, text="Tenure:").grid(row=4, column=0, padx=10, pady=5)
entry_tenure = tk.Entry(root)
entry_tenure.grid(row=4, column=1)

tk.Label(root, text="Balance:").grid(row=5, column=0, padx=10, pady=5)
entry_balance = tk.Entry(root)
entry_balance.grid(row=5, column=1)

tk.Label(root, text="Num of Products:").grid(row=6, column=0, padx=10, pady=5)
entry_num_of_products = tk.Entry(root)
entry_num_of_products.grid(row=6, column=1)

tk.Label(root, text="Has Credit Card (0/1):").grid(row=7, column=0, padx=10, pady=5)
entry_has_cr_card = tk.Entry(root)
entry_has_cr_card.grid(row=7, column=1)

tk.Label(root, text="Is Active Member (0/1):").grid(row=8, column=0, padx=10, pady=5)
entry_is_active = tk.Entry(root)
entry_is_active.grid(row=8, column=1)

tk.Label(root, text="Estimated Salary:").grid(row=9, column=0, padx=10, pady=5)
entry_estimated_salary = tk.Entry(root)
entry_estimated_salary.grid(row=9, column=1)

# Predict Button
predict_button = tk.Button(root, text="Predict Churn", command=predict_churn)
predict_button.grid(row=10, column=0, columnspan=2, pady=10)

# Run application
root.mainloop()

