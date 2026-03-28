import pandas as pd 

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import tree
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.compose import ColumnTransformer

df = pd.read_csv('star_dataset.csv')



X = df.drop(columns=['Name'])

ct = ColumnTransformer(
    transformers=[
        # Column transformer vectorizes specfic columns
        ('text_rules', TfidfVectorizer(), 'Spectral Class')
    ],
    remainder='passthrough' #keeps other columns!
)

X_final = ct.fit_transform(X)

y = df['Name']

X_train, X_test, y_train, y_test = train_test_split(X_final, y, test_size=0.2) #%20 percent is allocated 

model = DecisionTreeClassifier()
model.fit(X_train, y_train)

predictions = model.predict(X_test)

score = accuracy_score(y_test, predictions)

print(score)
