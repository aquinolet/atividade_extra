import pyrebase


config ={
    "apiKey": "AIzaSyDC2ncKOCZj4yfW70cgBbdyYZlkNyfufDI",
    "authDomain": "login-9ce9c.firebaseapp.com",
    "projectId": "login-9ce9c",
    "storageBucket": "login-9ce9c.appspot.com",
    "messagingSenderId": "725775305998",
    "appId": "1:725775305998:web:862461cf2fdbe601139b5f",
    "measurementId": "G-ZYGJ8M0T58"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
user = auth.sign_in_with_email_and_password('aquino@gmail.com',123456)
db = firebase.database()

data = {
    "email":"leticia@gmail.com"
    }

results = db.child("users").push (data, user['idToken'])
print (results)
