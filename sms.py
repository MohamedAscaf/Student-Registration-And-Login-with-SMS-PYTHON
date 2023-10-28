

from warnings import filterwarnings
filterwarnings("ignore")

from twilio.rest import Client

def sms1(a):
    b="Welcome "+a+":\n\tyou got a success man,\n Your Registration will be Successfully Done"
    account_sid = 'ACe350703a955d164261c79f0433f86b92'
    auth_token = '51bec6acf105b178f5b7c1f395e0f8c4'
    client1 = Client(account_sid, auth_token)
    message = client1.messages \
                  .create(
                      body=b,
                      from_='+13345398215',
                      to='+916380361993'
                      )
    print(message.sid)

def sms2(a,b):
    c="Hi "+a+":\n\t "+b
    account_sid = 'ACe350703a955d164261c79f0433f86b92'
    auth_token = '51bec6acf105b178f5b7c1f395e0f8c4'
    client1 = Client(account_sid, auth_token)
    message = client1.messages \
                  .create(
                      body=c,
                      from_='+13345398215',
                      to='+916380361993'
                      )






