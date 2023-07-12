import pandas as pd
from fastapi import FastAPI
from fastapi.responses import Response
from uvicorn import run
from joblib import load

app = FastAPI()

# Load the Count Encoder
try:
    c_encoder = load("model/c_encoder.joblib")
except Exception as e:
    logger.error("Error loading Count Encoder: %s", str(e))
    c_encoder = None

# Load the Binary Encoder
try:
    b_encoder = load("model/b_encoder.joblib")
except Exception as e:
    logger.error("Error loading Binary Encoder: %s", str(e))
    b_encoder = None

# Load the Ordinal Encoder
try:
    ord_encoder = load("model/ord_encoder.joblib")
except Exception as e:
    logger.error("Error loading Ordinal Encoder: %s", str(e))
    ord_encoder = None

# Load the OneHot Encoder
try:
    o_encoder = load("model/o_encoder.joblib")
except Exception as e:
    logger.error("Error loading OneHot Encoder: %s", str(e))
    o_encoder = None

# Load the Scaler
try:
    scaler = load("model/scaler.joblib")
except Exception as e:
    logger.error("Error loading Scaler: %s", str(e))
    scaler = None

# Load the Model
try:
    best_model = load("model/best_model.joblib")
except Exception as e:
    logger.error("Error loading Model: %s", str(e))
    best_model = None


@app.get("/")
async def root():
    """Root endpoint."""
    message = "The Insurance Fraud Detection API is up and running!"
    return {"message": message}


@app.post("/predict")
async def predict_fraud(data: dict):
    """Endpoint for predicting fraud."""
    if c_encoder is None or b_encoder is None or ord_encoder is None or o_encoder is None or scaler is None or best_model is None:
        return Response(content="Error: Model not loaded.", media_type="application/json")

    try:
        # Get the data from the request
        df = pd.DataFrame(data, index=[0])  # Specify the index explicitly

        high_cardinality_features = ['Age', 'AgeOfPolicyHolder', 'AgeOfVehicle', 'DayOfWeekClaimed', 'Make', 'Month',
                                     'MonthClaimed', 'PolicyNumber', 'PolicyType', 'RepNumber']

        binary_features = ['AccidentArea', 'AgentType', 'Fault', 'PoliceReportFiled', 'Sex', 'WitnessPresent']

        ordinal_features = ['VehiclePrice', 'Days_Policy_Accident', 'Days_Policy_Claim', 'PastNumberOfClaims',
                            'AgeOfVehicle', 'AgeOfPolicyHolder', 'NumberOfSuppliments', 'AddressChange_Claim',
                            'NumberOfCars']

        nominal_features = ['BasePolicy', 'DayOfWeek', 'DayOfWeekClaimed', 'Make', 'MaritalStatus', 'Month',
                            'MonthClaimed', 'PolicyType', 'VehicleCategory']

        # Preprocess inputs
        preprocessed_inputs = df.copy()

        # Apply count encoding to categorical features
        c_encoded_df = c_encoder.transform(preprocessed_inputs[high_cardinality_features])

        # Apply binary encoding to binary features
        b_encoded_df = b_encoder.transform(preprocessed_inputs[binary_features])

        # Apply ordinal encoding to ordinal features
        ord_encoded_df = ord_encoder.transform(preprocessed_inputs[ordinal_features])
        # Convert the encoded features to a DataFrame
        ord_encoded_df = pd.DataFrame(ord_encoded_df, columns=ordinal_features)

        # Apply one-hot encoding to nominal features
        o_encoded_df = o_encoder.transform(preprocessed_inputs[nominal_features])
        # Convert the encoded features to a dense numpy array
        o_encoded_df = o_encoded_df.toarray()
        # Convert the dense numpy array to a DataFrame
        o_encoded_df = pd.DataFrame(o_encoded_df, columns=o_encoder.get_feature_names_out(nominal_features))

        # Combine the encoded features using pd.concat
        preprocessed_inputs_encoded = pd.concat([c_encoded_df, b_encoded_df, ord_encoded_df, o_encoded_df], axis=1)

        # Apply scaler to the encoded features
        scaled_df = scaler.transform(preprocessed_inputs_encoded)
        # Convert the scaled features to a DataFrame
        scaled_df = pd.DataFrame(scaled_df, columns=preprocessed_inputs_encoded.columns)

        # Final preprocessed inputs
        preprocessed_inputs = pd.DataFrame(scaled_df, columns=preprocessed_inputs_encoded.columns)

        # Make predictions using the best_model
        predictions = best_model.predict(preprocessed_inputs)

        # Extract the predicted class value
        predicted_class = predictions[0]

        return Response(content=str(predicted_class), media_type="application/json")

    except Exception as e:
        return Response(content=f"Error: {str(e)}", media_type="application/json")


if __name__ == "__main__":
    run(app, host="0.0.0.0", port=8000)
