from django.shortcuts import render

import pyrebase


firebaseConfig = {
    'apiKey': "AIzaSyANGBWe3WlGaVRz0AlenXeL0CVB-WrTYro",
    'authDomain': "department-webapp.firebaseapp.com",
    'databaseURL': "https://department-webapp-default-rtdb.firebaseio.com",
    'projectId': "department-webapp",
    'storageBucket': "department-webapp.appspot.com",
    'messagingSenderId': "200792524960",
    'appId': "1:200792524960:web:ed6771ec8ff2bf9e86e1c5",
    'measurementId': "G-5RV1GXRFBD"
  }


fb = pyrebase.initialize_app(firebaseConfig)
db = fb.database()

def index(request):
    return render(request, "index.html")

def cse_home(request):
    return render(request, "cse.html")

def cse_syllabus(request):
    return render(request, "cse_syllabus.html")


def packages(request):
    return render(request, "packages.html")


def achievements(request):
    ach =  db.child('Achievements').get().val()
    #print('!!!!!!!!!!!!!',ach['ach1'].values())
    #print('!!!!!!!!!!!!!',ach.keys())
    achdic={}
    for i in ach.keys():
        achdic[i] = list(ach[i].values())
        #print('!!!!!!!!!!!!!',ach[i].values())
    print(achdic)
    return render(request, "achievements.html",{'achdic': achdic})

def notes(request):
    #useropt=db.child('Semester3').shallow().get()
    x= db.child('Semester3').get().val()
    #print(x.keys())


    return render(request, "notes.html",{'key':x})
