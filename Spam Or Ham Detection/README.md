# SmsSpamCollections
LinkedIn Demo Video: https://www.linkedin.com/feed/update/urn:li:activity:7203799496210685952/
![Screenshot (327)](https://github.com/Lavan1999/Project-11_Spam-Or_Ham_Detection/assets/152668558/94fcd50a-428d-42cf-8f54-104b6a5aa212)

## Data Loading and Exploration:
- Loaded the dataset from Google Drive using pandas.
- Explored the dataset's structure and information.
- Checked for missing values in the dataset.
  
## Sentiment Analysis:
- Used NLTK's VADER sentiment analyzer to analyze the sentiment of text messages.
- Calculated a compound sentiment score for each message.
- Classified messages as "ham" or "spam" based on the compound score.
  
## NLP - Natural Language Processing:
- Utilized spaCy to process text messages and generate vector representations.
  
## Machine Learning:
- Concatenated spaCy-generated message vectors with 'length' and 'punct' features.
- Split the dataset into training and testing sets.
- Trained a Support Vector Machine (SVM) model on the training data.
- Made predictions on the test data using the trained model.
  
## Evaluation:
- Evaluated the SVM model'
