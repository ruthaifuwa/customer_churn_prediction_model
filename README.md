# Bank Customers Churn Prediction
Predicted customer churn with ROC-AUC 0.856.

### Problem
20% of bank customers churn.
Goal: Predict who will leave

### Results
- Logistic Regression: Roc 0.775
- XGBoost: ROC 0.856 (+12% recall at same FPR)

### Key Insights
- Age is number 1 driver of churn (older customers churn more)
- Inactive members churn 2x more
- Germany has higher churn
- 1 and 3-4 products = high churn, 2 products = sticky

### ROC Curve
![ROC](images/roc_curve.png)