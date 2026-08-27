# 📧 Spam Email Classifier

An interactive and user-friendly **Spam Email Classifier** web application built using **Python, Flask, HTML, CSS, and JavaScript**.

The application analyzes email text and identifies whether it is likely to be **🚨 SPAM** or **✅ NOT SPAM** using a keyword-based scoring system.


## ✨ Features

📧 **Email Classification**
- Enter an email subject or message.
- Instantly check whether it is spam.

🔍 **Spam Detection**
- Detects predefined spam-related keywords.
- Calculates a spam score based on matched keywords.

📊 **Score Analysis**
- Displays the total spam score.
- Shows exactly which keywords were detected.

🚨 **Spam Alert**
- Clearly displays `SPAM` when the score reaches the threshold.
- Uses a red warning-style result.

✅ **Safe Email Detection**
- Displays `NOT SPAM` when the score is below the threshold.
- Uses a green success-style result.

🎨 **Interactive UI**
- Modern gradient background.
- Clean and attractive interface.
- Smooth hover effects and animations.
- Responsive design for different screen sizes.

💡 **Example Messages**
- Includes ready-to-use spam examples.
- Includes normal email examples for testing.

🗑️ **Clear Button**
- Quickly clears the entered text and previous result.

⌨️ **Keyboard Support**
- Press `Enter` to check the email.

📱 **Responsive Design**
- Works on desktop, tablet, and mobile devices.

---

## 🛠️ Technologies Used

🐍 **Python**  
Used for the backend logic.

🌐 **Flask**  
Used to create the web server and prediction API.

🎨 **HTML5**  
Used to create the structure of the website.

💅 **CSS3**  
Used for styling, animations, gradients, buttons, cards, and responsive design.

⚡ **JavaScript**  
Used for frontend interaction and communication with the Flask API.

🔎 **Regular Expressions**  
Used to clean and process the input text.

---

## 📂 Project Structure

```text
spam-email-classifier/
│
├── app.py
│
├── templates/
│   └── index.html
│
└── README.md
