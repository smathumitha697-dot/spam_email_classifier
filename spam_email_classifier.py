import email
import imaplib
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# 1. Dataset Setup & Model Training
train_data = {
    "text": [
        "Win a free iPhone now! Click here to claim.",
        "Hey, are we still meeting for lunch today?",
        "Urgent! You have won $1000 cash prize.",
        "Please review the attached project document.",
        "Free offer! Get unlimited discount today.",
        "Hi, I sent the file to your email.",
    ],
    "label": ["spam", "ham", "spam", "ham", "spam", "ham"],
}

df = pd.DataFrame(train_data)
cv = CountVectorizer()
X_train = cv.fit_transform(df["text"])
y_train = df["label"]

model = MultinomialNB()
model.fit(X_train, y_train)

# 2. Gmail Details
EMAIL_ACCOUNT = "xxxxxxxxxxxx"  (your mail id)
APP_PASSWORD = "xxxxxxxxxxxxx" (your password) 

try:
    # Connect to Gmail IMAP
    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login(EMAIL_ACCOUNT, APP_PASSWORD)
    mail.select("inbox")

    # Search for Emails ("UNSEEN" - Unread Mails | "ALL" - All Mails)
    status, messages = mail.search(None, "ALL")
    email_ids = messages[0].split()

    if not email_ids:
        print("No unread emails found in your inbox.")
    else:
        print(f"Found {len(email_ids)} unread email(s). Processing...\n")

        results = []

        for e_id in email_ids:
            _, msg_data = mail.fetch(e_id, "(RFC822)")
            for response_part in msg_data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_bytes(response_part[1])
                    subject = msg["subject"] or ""

                    # Extract Email Body
                    body = ""
                    if msg.is_multipart():
                        for part in msg.walk():
                            if part.get_content_type() == "text/plain":
                                body = part.get_payload(decode=True).decode(
                                    errors="ignore"
                                )
                                break
                    else:
                        body = msg.get_payload(decode=True).decode(
                            errors="ignore"
                        )

                    # Combine Subject + Body
                    email_text = f"{subject} {body}"

                    # Predict using Machine Learning Model
                    text_transformed = cv.transform([email_text])
                    prediction = model.predict(text_transformed)[0]

                    print(f"Subject: {subject}")
                    print(f"Prediction: {prediction.upper()}\n" + "-" * 40)

                    results.append(
                        {
                            "Subject": subject,
                            "Content": body.strip(),
                            "Result": prediction.upper(),
                        }
                    )

        # 3. Save Output to BOTH CSV & EXCEL
        output_df = pd.DataFrame(results)

        # Save to CSV File
        output_df.to_csv("spam_email_classifier.csv", index=False)

        # Save to Excel File (.xlsx)
        output_df.to_excel("spam_email_classifier.xlsx", index=False)

        print(
            "SUCCESS: Results successfully saved to BOTH 'spam_email_classifier.csv' and 'spam_email_classifier.xlsx'!"
        )

    mail.logout()

except Exception as e:
    print("Error connecting to Gmail:", e)
