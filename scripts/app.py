from flask import Flask, request, render_template, jsonify
import random
import smtplib
from email.message import EmailMessage

app = Flask(__name__)

# Dictionary to store email and OTP for verification
otp_storage = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_otp', methods=['POST'])
def send_otp():
    data = request.json
    email = data.get('email')

    if not email:
        return jsonify({'error': 'Email is required'}), 400

    # Generate OTP
    otp = ''.join([str(random.randint(0, 9)) for i in range(6)])

    # Send OTP via email
    from_mail = 'shreyanshgupta2020@gmail.com'
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_mail, 'qqcx efwr bzxc npmq')

    msg = EmailMessage()
    msg['Subject'] = "OTP VERIFICATION"
    msg['From'] = from_mail
    msg['To'] = email
    msg.set_content(f"Your OTP is: {otp}")

    server.send_message(msg)
    server.quit()

    # Store OTP with email
    otp_storage[email] = otp
    return jsonify({'message': 'OTP sent successfully'}), 200

@app.route('/verify_otp', methods=['POST'])
def verify_otp():
    data = request.json
    email = data.get('email')
    input_otp = data.get('otp')

    # Verify OTP
    if otp_storage.get(email) == input_otp:
        return jsonify({'message': 'OTP verified successfully'}), 200
    else:
        return jsonify({'error': 'Invalid OTP'}), 400

if __name__ == '__main__':
    app.run(debug=True)
