import smtplib
from firebase import firebase  
firebase = firebase.FirebaseApplication('https://traffico-367f7.firebaseio.com/', None)
while(1) :
    result = firebase.get('/traffico-367f7/stud/-LNumBiYnClsyQCjIYLi/', 'Status')
    if result=="Yes" :
        server=smtplib.SMTP(host='smtp.gmail.com',port=587)
        server.starttls()
        server.login("vashok890","bulbul1997")
        str = firebase.get('/traffico-367f7/stud/-LNumBiYnClsyQCjIYLi/', 'Car no')
        msg="Your vehicle "+str+" Has been wrongly parked"
        server.sendmail("vashok890@gmail.com","vashok890@gmail.com",msg)
        firebase.put('/traffico-367f7/stud/-LNumBiYnClsyQCjIYLi','Status',"No")
