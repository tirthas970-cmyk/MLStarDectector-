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
        pass

    def TrainModel_Test(self, datalist):

        df = pd.read_csv('star_dataset.csv')


        X = df.drop(columns=['Name'])

        #This is from gemini (23-28)
        ct = ColumnTransformer(
            transformers=[
                # Column transformer vectorizes specfic columns
                ('text_rules', TfidfVectorizer(), 'Spectral Class')
            ],
            remainder='passthrough' #keeps other columns
        )


        #Save trained file
        file_name = 'TrainStarData'

        if os.path.exists(file_name):
            model = joblib.load(file_name) 
        else:
            X_final = ct.fit_transform(X)

            y = df['Name']

            model = DecisionTreeClassifier()
            model.fit(X_final, y)

            joblib.dump(model, file_name)

       
        df_user_input = pd.DataFrame([datalist], columns=['Distance (ly)', 'Luminosity (L/Lo)', 'Temperature (K)', 'Spectral Class'])

        user_data = ct.transform(df_user_input)

        star_names = model.classes_

        #this gets first probiility 
        predictions_withprob = model.predict_proba(user_data)[0]

        top_5_prob = np.argsort(predictions_withprob)[::-1][:5]



        #Loop from gemini 
        for star in top_5_prob:
             print(f"{star_names[star]}: {top_5_prob[star] * 100:.2f}%")



         






