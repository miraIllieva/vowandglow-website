from flask import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__)

# ✉️ Email Configuration (for Gmail)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'vowandglowbeauty@gmail.com'
app.config['MAIL_PASSWORD'] = 'zdsh fpwy tdjc clgc'  # your 16-digit Gmail app password

mail = Mail(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/book', methods=['GET', 'POST'])
def book():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        service = request.form['service']
        people = request.form['people']
        date = request.form['date']
        message = request.form['message']

        # Print in terminal (optional for testing)
        print("Booking Received:")
        print(f"Name: {name}")
        print(f"Email: {email}")
        print(f"Service: {service}")
        print(f"Number of People: {people}")
        print(f"Date: {date}")
        print(f"Message: {message}")

        # 📨 Send Email to You
        msg = Message('New Booking from Vow & Glow',
                      sender=app.config['MAIL_USERNAME'],
                      recipients=[app.config['MAIL_USERNAME']])
        msg.body = f"""
        Name: {name}
        Email: {email}
        Service: {service}
        Number of People: {people}
        Date: {date}
        Message: {message}
        """
        mail.send(msg)

        return render_template('thankyou.html')


    return render_template('book.html')

if __name__ == '__main__':
    app.run(debug=True)
