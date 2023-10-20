from flask import Flask, jsonify, request
from twilio.rest import Client

app = Flask(__name__)

account_sid = 'ACd5100780fabc471857b9b468fb60198c'
auth_token = '40f3ab9922bfd5007e0467abbdfaed41'
client = Client(account_sid, auth_token)
service_sid='VAd5e49d004e7029008b223d5358053691'

def send_otp(phone_number, otp):
     client.verify \
                     .v2 \
                     .services(service_sid) \
                     .verifications \
                     .create(to=phone_number, channel='sms')


@app.route('/send_otp', methods=['GET'])
def api():
    send_otp("+91"+request.args.get("phno"),"12345")
    data = {"status":"success" }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
