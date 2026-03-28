import pandas as pd 
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.compose import ColumnTransformer
import os
import joblib


class MLStarDectector:

    def __init__(self):
        self.model = None
        self.file_name = 'TrainStarData.joblib'

    def TrainModel_Test(self, datalist):

        df = pd.read_csv('star_dataset.csv')


        X = df.drop(columns=['Name', 'Spectral Class'])
        y = df['Name']

        #This is from gemini (23-28)
      

        if os.path.exists(self.file_name):
            self.model = joblib.load(self.file_name) 
        else:

            self.model = DecisionTreeClassifier()
            self.model.fit(X, y)

            joblib.dump(self.model, self.file_name)

       
        df_user_input = pd.DataFrame([datalist], columns=['Distance (ly)', 'Luminosity (L/Lo)', 'Radius (R/Ro)', 'Temperature (K)'])

        star_names = self.model.classes_

        #this gets first probiility 
        predictions_withprob = self.model.predict_proba(df_user_input)[0]

        top_5_prob = np.argsort(predictions_withprob)[::-1][:5]

        #Loop from gemini 
        best_star_index = top_5_prob[0]
        
        # Get the name and probability for just that one star
        name = star_names[best_star_index]

        return f"Prediction: {name}"

        




         






