from firebase import firebase
import urllib
import cv2
import Main
firebase = firebase.FirebaseApplication('https://traffico-367f7.firebaseio.com/', None)
#my_url="https://firebasestorage.googleapis.com/v0/b/traffico-367f7.appspot.com/o/img.png?alt=media&token=0b229b6c-2a1e-4ad7-93cd-8d75e8f93403"
my_url="https://firebasestorage.googleapis.com/v0/b/fault-detect.appspot.com/o/image?alt=media&token=e87ba44a-ce8c-45ab-96c0-e21961dd0dbb"
s1="Yes"
s2="No"
c=1
while(1) :
    try:
        loader = urllib.request.urlretrieve(my_url, "D:\Cloudrject\img.jpg")
    except urllib.error.URLError as e:
        #message = json.loads(e.read())
        #print("Connection issue")
        continue
        #print(message["error"]["message"])
    else:
        print(loader)
        break

Main.main()
my_request = urllib.request.Request(my_url, method="DELETE")
loader = urllib.request.urlopen(my_request)
#img=cv2.imread("img.jpg")
#if c==1 :
#    firebase.put('/traffico-367f7/stud/-LNumBiYnClsyQCjIYLi','Status',s1)
#else :
#    firebase.put('/traffico-367f7/stud/-LNumBiYnClsyQCjIYLi','Status',s2)
