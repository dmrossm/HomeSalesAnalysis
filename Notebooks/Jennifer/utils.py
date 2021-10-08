

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


from datetime import datetime

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import cross_validate
from statsmodels.formula.api import ols
import statsmodels.api as sm
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.datasets import make_regression
from sklearn.linear_model import LinearRegression
import sklearn.metrics as metrics
from random import gauss
from mpl_toolkits.mplot3d import Axes3D
from scipy import stats as stats
import warnings
warnings.filterwarnings('ignore')
from sklearn.metrics import r2_score, mean_absolute_error

def evaluate(y_tr, tr_preds, y_te, te_preds):
    """
    Evaluate the amount of error between my model's predictions and the actual values for both a train and a test set.
    
    Inputs:
    y_train - array like, actual vales for 'price' for my train dataset
    train_preds - array like, predicted values for 'price' for my train dataset
    y_teast - array like, actual vales for 'price' for my train dataset
    test_preds - array like, predicted values for 'price' for my train dataset
    
    Outputs:
    
    """
    
    
    print(f"Train R2: {r2_score(y_tr, tr_preds):.4f}")
    print(f"Test R2: {r2_score(y_te, te_preds):.4f}")
    print('****')
    print(f"Train RMSE: ${mean_squared_error(y_tr, tr_preds, squared = False):,.2f}")
    print(f"Test RMSE: ${mean_squared_error(y_te, te_preds, squared = False):,.2f}") 
    print('****')
    print(f"Train MAE: ${mean_absolute_error(y_tr, tr_preds):,.2f}")
    print(f"Test MAE: ${mean_absolute_error(y_te, te_preds):,.2f}")
    
    #calculate our residiuals
    
    train_residuals = y_tr - tr_preds
    test_residuals = y_te - te_preds
    #Scatter plot
    plt.scatter(tr_preds,train_residuals, label = "Train")
    plt.scatter(te_preds, test_residuals, label = "Test")
    
    plt.axhline(y = 0, color = 'red', label = '0')
    plt.xlabel('predictions')
    plt.ylabel('residuals')
    plt.legend()
    plt.show()