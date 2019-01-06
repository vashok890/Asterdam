from firebase import firebase  
firebase = firebase.FirebaseApplication('https://traffico-367f7.firebaseio.com/', None)
data1 =  { 'Name': 'Varun A',  
          'Car no': 'KA03MF907',  
          'emailID': 'vashok890@gmail.com',
          'Status':'No'
          }
result = firebase.post('/traffico-367f7/stud/',data1)
