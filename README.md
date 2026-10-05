📧 Spam Email Classifier

A Machine Learning-based project that automatically classifies emails as Spam or Ham (Normal) using Multinomial Naive Bayes and CountVectorizer.

📌 Project Overview

The main objective of this project is to detect unwanted or suspicious emails automatically. The system reads email content, analyzes the text, and predicts whether the email is Spam or Ham.

🚀 Features

- Classifies emails as Spam or Ham
- Uses Machine Learning for text classification
- Extracts email subject and body
- Converts text into numerical features using CountVectorizer
- Uses Multinomial Naive Bayes for prediction
- Reads emails using IMAP
- Stores prediction results in CSV and Excel files

🛠️ Technologies Used

- Python
- Pandas
- CountVectorizer
- Multinomial Naive Bayes
- IMAPLIB
- Email Library
- CSV
- Excel

🔄 Project Workflow

Gmail
   ↓
Read Emails
   ↓
Extract Subject & Body
   ↓
Text Preprocessing
   ↓
CountVectorizer
   ↓
Multinomial Naive Bayes
   ↓
Spam / Ham Prediction
   ↓
Save Results
   ↓
CSV & Excel

🤖 Machine Learning Algorithm

Multinomial Naive Bayes

Multinomial Naive Bayes is a supervised machine learning algorithm commonly used for text classification.

In this project, it learns the word patterns from the training dataset and predicts whether a new email is Spam or Ham.

📊 Text Feature Extraction

CountVectorizer

CountVectorizer converts email text into numerical features based on the frequency of words.

For example:

"free money offer"

is converted into numerical values that can be processed by the machine learning model.

📂 Project Structure

Spam-Email-Classifier/
│
├── spam_email_classifier.py
├── dataset.csv
├── spam_results.csv
├── spam_results.xlsx
└── README.md

⚙️ Installation

Install the required Python libraries:

pip install pandas scikit-learn openpyxl

▶️ How to Run

1. Clone the repository:

git clone https://github.com/your-username/spam-email-classifier.git

2. Open the project folder:

cd spam-email-classifier

3. Run the Python program:

python spam_email_classifier.py

4. The program will classify the emails as Spam or Ham.

5. The results will be saved in CSV and Excel format.

🎯 Example

Input Email:

Congratulations! You have won a free prize.

Output:

SPAM

Input Email:

Please send me the project report.

Output:

HAM

🔮 Future Enhancements

- Improve model accuracy using a larger dataset
- Add more machine learning algorithms
- Create a web-based interface
- Add real-time email classification
- Improve email preprocessing and feature extraction

👨‍💻 Author

MATHUMITHA S

Machine Learning Project – Spam Email Classifier

📜 License

This project is created for educational purposes.
