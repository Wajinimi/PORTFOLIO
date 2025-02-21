import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Lasso
import joblib

# Load and clean the dataset
file_path = "C:\\Users\\WAJI\\portfolio\\backendFlask\\house_price_dataset1.csv"
data = pd.read_csv(file_path).dropna(subset=["House_Price"])

# Split features and target
X = data.drop(columns=["House_Price"])
y = data["House_Price"]

# Split into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Lasso regression with GridSearchCV
param_grid = {'alpha': [30.0, 60.0, 70.0, 100.0]}
lasso = Lasso()
grid_search = GridSearchCV(estimator=lasso, param_grid=param_grid, cv=5, scoring='neg_mean_squared_error')
grid_search.fit(X_train_scaled, y_train)

# Output best parameters and RMSE
best_alpha = grid_search.best_params_['alpha']
best_rmse = np.sqrt(-grid_search.best_score_)
mean_price = y.mean()
error_percentage = (best_rmse / mean_price) * 100


joblib.dump(grid_search, 'model.pkl')



