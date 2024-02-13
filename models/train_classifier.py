# train_classifier.py

import sys
import pandas as pd
from sqlalchemy import create_engine
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.multioutput import MultiOutputClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report
import joblib
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

import nltk
nltk.download('punkt')
nltk.download('wordnet')


def load_data(database_filepath):
    engine = create_engine(f'sqlite:///{database_filepath}')
    df = pd.read_sql_table('disaster_data', engine)
    X = df['message']
    y = df.iloc[:, 4:]
    return X, y, y.columns


def tokenize(text):
    """
    Tokenize and lemmatize the text
    
    Parameters:
    - text (str): Input text
    
    Returns:
    - tokens (list): List of tokens
    """
    # Tokenize the text using NLTK
    tokens = word_tokenize(text)
    
    # Lemmatize the tokens
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(token).lower().strip() for token in tokens]
    
    return tokens



def build_model():
    # Reduce the number of trees in the RandomForestClassifier
    # You can adjust n_estimators based on your preferences
    n_estimators = 10
    
    pipeline = Pipeline([
        ('vect', CountVectorizer(tokenizer=tokenize)),
        ('tfidf', TfidfTransformer()),
        ('clf', MultiOutputClassifier(RandomForestClassifier(n_estimators=n_estimators)))
    ])
    return pipeline


def evaluate_model(model, X_test, y_test, category_names):
    y_pred = model.predict(X_test)
    for i, category in enumerate(category_names):
        print(f"Classification Report for {category}:\n")
        print(classification_report(y_test[category], y_pred[:, i]))

def save_model(model, model_filepath):
    joblib.dump(model, model_filepath)

def main():
    if len(sys.argv) == 3:
        database_filepath, model_filepath = sys.argv[1:]

        print(f'Loading data from {database_filepath}...')
        X, y, category_names = load_data(database_filepath)

        print('Splitting data into train and test sets...')
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        print('Building model...')
        model = build_model()

        print('Training model...')
        model.fit(X_train, y_train)

        print('Evaluating model...')
        evaluate_model(model, X_test, y_test, category_names)

        print(f'Saving model to {model_filepath}...')
        save_model(model, model_filepath)


    else:
        print('Please provide the filepath for the database and the desired model.')

if __name__ == '__main__':
    main()
