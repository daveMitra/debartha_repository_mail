from flask import Flask, render_template
from flask_mail import Mail, Message

app = Flask(__name__)
app.config.update(
    DEBUG=True,
    # MAIL_SERVER='e2ksmtp01.e2k.ad.ge.com',
    MAIL_SERVER='mail.ad.ge.com', # public server cred
    MAIL_PORT=25,
    MAIL_USERNAME='MyTech.Software@ge.com'
)



mail = Mail(app)


@app.route('/')
def mailSend():
    try:
        # print("in mail email function---1")
        msg = Message("Send Mail Tutorial!",
                      sender="MyTech.Software@ge.com",
                      recipients=["Debartha.Mitra@ge.com"])
        # print("in mail email function---2")
        msg.html = render_template('thankyou.html')
        # print(msg)
        mail.send(msg)
        return 'Mail sent!'
    except Exception as e:
        print(type(e))
        print(e)
        return 'error'


if __name__ == "__main__":
    # app.run(debug=True) # while running on local pc
    # app.run(host="127.0.0.1", port=5000) #while running on cloud instance
     app.run(host="0.0.0.0", port=80) #while running on cloud instance
