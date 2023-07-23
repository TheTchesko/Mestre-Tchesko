# arquivo bibliotecas.py

import imageio
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
import optuna
import pandas as pd
import plotly.graph_objects as go
import random
import seaborn as sns
import statsmodels.api as sm
import tensorflow as tf
import logging
from IPython.display import HTML
from pmdarima import auto_arima
from openpyxl import load_workbook
import warnings
from tensorflow import keras
from matplotlib import rcParams
from keras.layers import Conv1D, Dense, Flatten, GRU, LSTM, MaxPooling1D
from keras.models import Sequential
from lightgbm import LGBMRegressor
from pmdarima.arima import ADFTest
from scipy import stats
from skopt import BayesSearchCV, space
from sklearn.datasets import make_regression
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import Lasso, LinearRegression, Ridge
from sklearn.metrics import (make_scorer, mean_absolute_error,
                             mean_absolute_percentage_error, mean_squared_error,
                             r2_score)
from sklearn.model_selection import (GridSearchCV, RandomizedSearchCV,
                                     cross_val_score, learning_curve,
                                     train_test_split, validation_curve)
from sklearn.tree import DecisionTreeRegressor as dt
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.ar_model import AutoReg as AR
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.filters.hp_filter import hpfilter
from statsmodels.tsa.seasonal import seasonal_decompose as stl
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.statespace.sarimax import SARIMAX as sr
from scikeras.wrappers import KerasRegressor
from xgboost import XGBRegressor
