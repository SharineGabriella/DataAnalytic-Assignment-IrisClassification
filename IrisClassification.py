import streamlit as st
import pandas as pd
#from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier

st.write("""
# Simple Iris Flower Prediction App
This app predicts the **Iris flower** type!
""")
st.caption('This is exercise of Data Analytic Course by Air Asia Academy')

st.sidebar.header('User Input Parameters')

def user_input_features():
    sepal_length = st.sidebar.slider('Sepal length', 4.3, 7.9, 5.4)
    sepal_width = st.sidebar.slider('Sepal width', 2.0, 4.4, 3.4)
    petal_length = st.sidebar.slider('Petal length', 1.0, 6.9, 1.3)
    petal_width = st.sidebar.slider('Petal width', 0.1, 2.5, 0.2)
    data = {'sepal_length': sepal_length,
            'sepal_width': sepal_width,
            'petal_length': petal_length,
            'petal_width': petal_width}
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

st.subheader('User Input parameters')
st.write(df)

#iris = datasets.load_iris()
iris = pd.read_csv('https://raw.githubusercontent.com/SharineGabriella/DataAnalytic-Assignment-IrisClassification/main/IRIS.csv')
X = iris.drop('species', axis = 1) #iris.data
Y = iris.species #iris.target

clf = RandomForestClassifier()
clf.fit(X, Y)

prediction = clf.predict(df)
prediction_proba = clf.predict_proba(df)

st.subheader('Class labels and their corresponding index number')
#st.write(['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']) #st.write(iris.target_names)
#st.image('https://raw.githubusercontent.com/SharineGabriella/DataAnalytic-Assignment-IrisClassification/main/iris-real.png')
#st.image('https://raw.githubusercontent.com/SharineGabriella/DataAnalytic-Assignment-IrisClassification/main/irisflowers.png')
st.write('Iris-setosa')
st.image('https://raw.githubusercontent.com/SharineGabriella/DataAnalytic-Assignment-IrisClassification/main/SENTOSA1.png')
st.write('Iris-versicolor')
st.image('https://raw.githubusercontent.com/SharineGabriella/DataAnalytic-Assignment-IrisClassification/main/VERSICOLOR1.png')
st.write('Iris-virginica')
st.image('https://raw.githubusercontent.com/SharineGabriella/DataAnalytic-Assignment-IrisClassification/main/VIRGINICA1.png')

st.subheader('Prediction')
#st.write(iris.target_names[prediction])
st.write(prediction)

st.subheader('Prediction Probability')
st.write(prediction_proba)
#credit to Dr Yu and Dr YanBin from Air Asia Academy
