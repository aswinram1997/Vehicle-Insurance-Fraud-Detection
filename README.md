# Vehicle-Insurance-Fraud-Detection-API

![pexels-dominika-kwiatkowska-3368844](https://github.com/aswinram1997/Vehicle-Insurance-Fraud-Detection/assets/102771069/06b0b753-5c01-4929-b8dd-55135491c799)


## Project Overview
Vehicle insurance fraud is a significant problem that involves false or exaggerated claims following an accident. Fraudsters may stage accidents, fabricate injuries, or engage in other deceptive practices to make claims. To address this issue, a kaggle dataset The [Kaggle Dataset](<https://www.kaggle.com/datasets/shivamb/vehicle-claim-fraud-detection>) which includes information on vehicle attributes, accident details, and policy information has been used. The primary objective of this project is to develop a machine learning model that can assist insurance companies in identifying fraudulent claims. This ML model can help insurance companies to prioritize and investigate claims that are identified as high-risk, potentially preventing them from making payouts on fraudulent claims. Additionally, by identifying fraudulent claims, insurance companies can deter fraudsters from attempting to commit fraud, which can help to reduce the overall incidence of fraud in the company.<br>

## Dataset Overview
The dataset used in this project contains the following features used in the context of vehicle insurance fraud detection:

#### Time related features:
- Month: The month in which the policy was issued or the claim was made.
- WeekOfMonth: The week number in the month in which the policy was issued or the claim was made.
- DayOfWeek: The day of the week on which the policy was issued or the claim was made.
- DayOfWeekClaimed: The day of the week on which the claim was made.
- MonthClaimed: The month in which the claim was made.
- WeekOfMonthClaimed: The week number in the month in which the claim was made.
- Days_Policy_Accident: The number of days between policy issuance and the accident.
- Days_Policy_Claim: The number of days between policy issuance and the claim.
- Year: The year in which the policy was issued or the claim was made.

#### Policy and vehicle related features:
- AgentType: The type of insurance agent who sold the policy.
- PolicyType: The type of policy (e.g., comprehensive, third party) taken out by the policyholder.
- PolicyNumber: The unique identifier of the insurance policy.
- Deductible: The amount of the deductible for the policy.
- BasePolicy: The type of base policy taken out by the policyholder (e.g., liability-only, comprehensive).
- Make: The make of the vehicle insured.
- AccidentArea: The area where the accident took place.
- VehicleCategory: The category of the vehicle insured (e.g., SUV, sedan, truck).
- VehiclePrice: The price of the insured vehicle.
- RepNumber: The unique identifier of the insurance representative handling the claim.
- DriverRating: The driver rating for the policyholder or the driver involved in the accident.
- PastNumberOfClaims: The number of claims made by the policyholder in the past.
- AgeOfVehicle: The age of the insured vehicle.
- AgeOfPolicyHolder: The age of the policyholder.
- NumberOfSuppliments: The number of additional insurance supplements taken out by the policyholder.
- NumberOfCars: The number of cars insured under the policy.

#### Accident related features:
- Sex: The gender of the policyholder or the driver involved in the accident.
- MaritalStatus: The marital status of the policyholder or the driver involved in the accident.
- Age: The age of the policyholder or the driver involved in the accident.
- Fault: The party at fault in the accident.
- PoliceReportFiled: Whether a police report was filed for the accident.
- WitnessPresent: Whether a witness was present at the accident.
- AddressChange_Claim: Whether the policyholder changed their address after making the claim.<br>

## Methodology
In this Jupyter notebook, an extensive analysis of the data has been conducted, including exploring its characteristics, splitting it into training, validation, and testing sets using a stratified approach, and pre-processing it for machine learning. Various techniques such as encoding categorical features and scaling numerical features have been employed to ensure optimal performance of the models. Then, different algorithms, including Logistic Regression, Support Vector Machine, and XGBoost classifiers, have been trained and fine-tuned using random search CV with 5-fold cross-validation. After comparing their performance, the best ML model was selected based on precision, recall, and F1 score. Finally, after selecting the best model, a model interpretation analysis is conducted to gain valuable insights into the key predictors used in fraud detection.

The project follows a typical machine learning workflow consisting of exploratory data analysis (EDA), data splitting, preprocessing, modeling, and evaluation. Additionally, a comparison of ML algorithms, including Logistic Regression, Support Vector Machine, and XGBoost classifiers, was performed to determine the winning model. The chosen model was then utilized to build a FAST API endpoint. Finally, the API endpoint was containerized using Docker for scalability. The resulting containerized API provides an accessible and scalable solution for credit risk assessment, contributing to efficient fraud detection in insurance claims.

#### Exploratory Data Analysis (EDA):
EDA was conducted on the dataset to gain insights into the distributions, relationships, and characteristics of the features. This involved performing statistical analysis, visualizations, and identifying any data quality issues or patterns that could impact the modeling process.

#### Data Splitting:
The dataset was divided into training, validation, and testing sets to assess the model's predictive performance and generalizability. 

#### Data Preprocessing:
Data preprocessing steps were applied to ensure the dataset's quality and compatibility with the chosen algorithms. This involved encoding categorical features, and scaling numerical features. 

#### Modeling and Evaluation:
Model training involves selecting an appropriate algorithm and fine-tuning its parameters to obtain the best possible model for the given dataset. In this case, Logistic Regression, Support Vector Machine, and XGBoost classifiers were trained and fine-tuned using random search CV with 5-fold cross-validation. The best model selected based on cross-validation performance was then trained on the entire train set and evaluated on the validation set. Once the model was optimized, it was evaluated on the test set to ensure that it generalizes well to unseen data.

#### FAST API Endpoint:
The winning model, chosen for its exceptional performance, was integrated into a FAST API endpoint. This endpoint enables seamless integration into internal bank applications, allowing users to request credit risk assessments for loan applicants. This integration enhances efficiency and ensures informed lending decisions.

#### Docker Containerization:
To ensure scalability and ease of deployment, the API endpoint was containerized using Docker. Containerization encapsulated the API, its dependencies, and the ML model within a portable environment. This approach facilitated easy deployment and scaling across different environments, reducing potential compatibility issues.


## Running the API Locally
To run the credit risk assessment API locally, you can follow these steps:

1. Clone the project repository: `git clone https://github.com/aswinram1997/Vehicle-Insurance-Fraud-Detection-API.git`

2. Install Docker and ensure it is running properly on your machine.

3. Navigate to the project directory.

4. Build the Docker image using the Dockerfile: `docker build -t insurance-fraud-api .`

5. Run the Docker container based on the created image: `docker run -p 8000:8000 insurance-fraud-api`

6. Once the Docker container is running, you can send POST requests to http://localhost:8000/predict for fraud detection.


### Example Request
```
{
    "Month": "Dec",
    "WeekOfMonth": 5,
    "DayOfWeek": "Wednesday",
    "Make": "Honda",
    "AccidentArea": "Urban",
    "DayOfWeekClaimed": "Tuesday",
    "MonthClaimed": "Jan",
    "WeekOfMonthClaimed": 1,
    "Sex": "Female",
    "MaritalStatus": "Single",
    "Age": 21,
    "Fault": "Policy Holder",
    "PolicyType": "Sport - Liability",
    "VehicleCategory": "Sport",
    "VehiclePrice": "more than 69000",
    "PolicyNumber": 1,
    "RepNumber": 12,
    "Deductible": 300,
    "DriverRating": 1,
    "Days_Policy_Accident": "more than 30",
    "Days_Policy_Claim": "more than 30",
    "PastNumberOfClaims": "none",
    "AgeOfVehicle": "3 years",
    "AgeOfPolicyHolder": "26 to 30",
    "PoliceReportFiled": "No",
    "WitnessPresent": "No",
    "AgentType": "External",
    "NumberOfSuppliments": "none",
    "AddressChange_Claim": "1 year",
    "NumberOfCars": "3 to 4",
    "Year": 1994,
    "BasePolicy": "Liability"
}
```

### Request Body Details
- `WeekOfMonth`: integer (range: 1 - 5)
- `WeekOfMonthClaimed`: integer (range: 1 - 5)
- `Age`: integer (range: 0 - 80 years)
- `FraudFound_P`: integer (range: 0 - 1)
- `PolicyNumber`: integer (range: 1 - 15420)
- `RepNumber`: integer (range: 1 - 16)
- `Deductible`: integer (range: 300 - 700)
- `DriverRating`: integer (range: 1 - 4)
- `Year`: integer (range: 1994 - 1996)
- `Month`: string (values: 'Dec', 'Jan', 'Oct', 'Jun', 'Feb', 'Nov', 'Apr', 'Mar', 'Aug', 'Jul', 'May', 'Sep')
- `DayOfWeek`: string (values: 'Wednesday', 'Friday', 'Saturday', 'Monday', 'Tuesday', 'Sunday', 'Thursday')
- `Make`: string (values: 'Honda', 'Toyota', 'Ford', 'Mazda', 'Chevrolet', 'Pontiac', 'Accura', 'Dodge', 'Mercury', 'Jaguar', 'Nisson', 'VW', 'Saab', 'Saturn', 'Porche', 'BMW', 'Mecedes', 'Ferrari', 'Lexus')
- `AccidentArea`: string (values: 'Urban', 'Rural')
- `DayOfWeekClaimed`: string (values: 'Tuesday', 'Monday', 'Thursday', 'Friday', 'Wednesday', 'Saturday', 'Sunday', '0')
- `MonthClaimed`: string (values: 'Jan', 'Nov', 'Jul', 'Feb', 'Mar', 'Dec', 'Apr', 'Aug', 'May', 'Jun', 'Sep', 'Oct', '0')
- `Sex`: string (values: 'Female', 'Male')
- `MaritalStatus`: string (values: 'Single', 'Married', 'Widow', 'Divorced')
- `Fault`: string (values: 'Policy Holder', 'Third Party')
- `PolicyType`: string (values: 'Sport - Liability', 'Sport - Collision', 'Sedan - - Liability', 'Utility - All Perils', 'Sedan - All Perils', 'Sedan - Collision', 'Utility - Collision', 'Utility - Liability', 'Sport - All Perils')
- `VehicleCategory`: string (values: 'Sport', 'Utility', 'Sedan')
- `VehiclePrice`: string (values: 'more than 69000', '20000 to 29000', '30000 to 39000', 'less than 20000', '40000 to 59000', '60000 to 69000')
- `Days_Policy_Accident`: string (values: 'more than 30', '15 to 30', 'none', '1 to 7', '8 to 15')
- `Days_Policy_Claim`: string (values: 'more than 30', '15 to 30', '8 to 15', 'none')
- `PastNumberOfClaims`: string (values: 'none', '1', '2 to 4', 'more than 4')
- `AgeOfVehicle`: string (values: '3 years', '6 years', '7 years', 'more than 7', '5 years', 'new', '4 years', '2 years')
- `AgeOfPolicyHolder`: string (values: '26 to 30', '31 to 35', '41 to 50', '51 to 65', '21 to 25', '36 to 40', '16 to 17', 'over 65', '18 to 20')
- `PoliceReportFiled`: string (values: 'No', 'Yes')
- `WitnessPresent`: string (values: 'No', 'Yes')
- `AgentType`: string (values: 'External', 'Internal')
- `NumberOfSuppliments`: string (values: 'none', 'more than 5', '3 to 5', '1 to 2')
- `AddressChange_Claim`: string (values: '1 year', 'no change', '4 to 8 years', '2 to 3 years', 'under 6 months')
- `NumberOfCars`: string (values: '3 to 4', '1 vehicle', '2 vehicles', '5 to 8', 'more than 8')
- `BasePolicy`: string (values: 'Liability', 'Collision', 'All Perils')



## Conclusion
The development of an ML model that can assist insurance companies in detecting fraudulent claims is a crucial step in preventing and reducing insurance fraud. This project has demonstrated that the XGBoost algorithm, when trained on a dataset containing policy, vehicle, and accident-related features, can effectively identify fraudulent claims with high precision and recall. The top predictors identified by the model can also provide insights into the factors that contribute to insurance fraud. Therefore, this ML model can be useful for insurance companies in prioritizing and investigating claims, reducing payouts on fraudulent claims, and deterring fraudsters from attempting to commit fraud.<br>

