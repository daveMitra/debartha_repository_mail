from flask import Flask, render_template
from flask_mail import Mail, Message

app = Flask(__name__)
app.config.update(
    DEBUG=True,
    MAIL_SERVER='3.159.19.78',
    MAIL_PORT=25,
    MAIL_USE_SSL=True,
    MAIL_USERNAME='MyTech.Software@ge.com'
)
mail = Mail(app)


@app.route('/')
def mailSend():
    try:
        msg = Message("Send Mail Tutorial!",
                      sender="MyTech.Software@ge.com",
                      recipients=["Debartha.Mitra@ge.com"])
        # msg.body = "Yo!\nHave you heard the good word of Python???"
        # msg.html = render_template('text.html')
        msg.html = render_template('thankyou.html')
        mail.send(msg)
        return 'Mail sent!'
    except Exception as e:
        print(type(e))
        print(e)
        return 'error'
