# Payment Fraud Prevention using TDES and Multi-Factor Facial Authentication.
## Project Overview
&nbsp;&nbsp;&nbsp;&nbsp;Credit cards and debit cards have become the most popular mode of payment
for both online as well as regular purchase, cases of fraud associated with it
are also rising.
Credit card and debit card frauds are committed in the following ways:
• An act of criminal deception (misled with intent) by use of unauthorized
accounts and/or personal information
• Illegal or unauthorized use of account for personal gain
• Misrepresentation of account information to obtain goods and/or services.
In this project the process of Cryptography has been followed, it is one of the most important security technologies which is used to secure the data transmission and the data itself and an authentication process facial
recognition is also implemented.  
&nbsp;&nbsp;&nbsp;&nbsp;**Note:** 
TDES
In the proposed system, whenever a new user registers, the credit card
and debit card details are cross checked and then only the user id is
generated. This allows only correct users to login each time. At the same
time credit card and debit card details are cross checked each time
whenever a customer buys a product. Their facial details are saved in the
database when they opted for online transactions and taken and verified
with the current user. This verification enables only the right users to
buy products. And also the credit card number will be encrypted before
leaving the browser, so hackers cannot chase the apt credit card number.
Similar to this, debit card details also will be encrypted before leaving
the browser, so hackers cannot chase the apt debit card details. After
reaching the encrypted credit card number and debit card number to the
bank, that will be decrypted by the bank. To overcome all the problems
in the existing system, development to ease the operation is

FACIAL AUTHENTICATION
Implemented Flask web application login page including face verification (1-to-1 to verify whether the person who is logging in is really that person), for security purpose, with liveness detection mechanism (to check whether the person detected on the camera is a REAL person or FAKE (eg. image, video, etc. of that person)), for Anti-Spoofting (Others pretending to be the person), built with Convolutional Neural Network. After the login page, we also provided a webpage placeholder for future use.




## Packages and Tools
Check out requirements.txt for the correct version of packages.
- Python 3.9.5
- OpenCV
- TensorFlow 2.5
- Scikit-learn
- Face_recognition
- Flask
- SQLite
- SQLAlchemy (for Flask)

