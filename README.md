# Vehicle Insurance Fraud Detection

## Project Overview
Vehicle insurance fraud is a significant problem that involves false or exaggerated claims following an accident. Fraudsters may stage accidents, fabricate injuries, or engage in other deceptive practices to make claims. To address this issue, a kaggle dataset (*https://www.kaggle.com/datasets/shivamb/vehicle-claim-fraud-detection*) which includes information on vehicle attributes, accident details, and policy information has been used. The primary objective of this project is to develop a machine learning model that can assist insurance companies in identifying fraudulent claims. This ML model can help insurance companies to prioritize and investigate claims that are identified as high-risk, potentially preventing them from making payouts on fraudulent claims. Additionally, by identifying fraudulent claims, insurance companies can deter fraudsters from attempting to commit fraud, which can help to reduce the overall incidence of fraud in the company.<br>

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
In this Jupyter notebook, an extensive analysis of the data has been conducted, including exploring its characteristics, splitting it into training, validation, and testing sets using a stratified approach, and pre-processing it for machine learning. Various techniques such as encoding categorical features and scaling numerical features have been employed to ensure optimal performance of the models. Then, different algorithms, including logistic regression, random forest, and XGBoost, have been trained and fine-tuned using random search CV with 5-fold cross-validation. After comparing their performance, the best ML model was selected based on precision, recall, and F1 score. Finally, ANOVA test is used to explore the feature importances for the Test Set to provide insights into the important predictors for fraud detection.<br>

## Results
The best performing machine learning model was the XGBoost algorithm with an F1 score of 1. This model outperformed the other models, including logistic regression and random forest. The model also achieved high precision and recall scores, indicating that it was effective in identifying fraudulent claims. Feature importance analysis revealed that Day of the Week, Make, Month, Month Claimeed were some of the top predictors of fraud.<br>

## Conclusion
The development of an ML model that can assist insurance companies in detecting fraudulent claims is a crucial step in preventing and reducing insurance fraud. This project has demonstrated that the XGBoost algorithm, when trained on a dataset containing policy, vehicle, and accident-related features, can effectively identify fraudulent claims with high precision and recall. The top predictors identified by the model can also provide insights into the factors that contribute to insurance fraud. Therefore, this ML model can be useful for insurance companies in prioritizing and investigating claims, reducing payouts on fraudulent claims, and deterring fraudsters from attempting to commit fraud.<br>

