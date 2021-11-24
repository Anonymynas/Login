from tkinter import *
import numpy as np
import pandas as pd
from tkinter import messagebox

#List of the symptoms is listed here in list l1.

l1=['back_pain','constipation','abdominal_pain','diarrhoea','mild_fever','yellow_urine',
'yellowing_of_eyes','acute_liver_failure','fluid_overload','swelling_of_stomach',
'swelled_lymph_nodes','malaise','blurred_and_distorted_vision','phlegm','throat_irritation',
'redness_of_eyes','sinus_pressure','runny_nose','congestion','chest_pain','weakness_in_limbs',
'fast_heart_rate','pain_during_bowel_movements','pain_in_anal_region','bloody_stool',
'irritation_in_anus','neck_pain','dizziness','cramps','bruising','obesity','swollen_legs',
'swollen_blood_vessels','puffy_face_and_eyes','enlarged_thyroid','brittle_nails',
'swollen_extremeties','excessive_hunger','extra_marital_contacts','drying_and_tingling_lips',
'slurred_speech','knee_pain','hip_joint_pain','muscle_weakness','stiff_neck','swelling_joints',
'movement_stiffness','spinning_movements','loss_of_balance','unsteadiness',
'weakness_of_one_body_side','loss_of_smell','bladder_discomfort','foul_smell_of urine',
'continuous_feel_of_urine','passage_of_gases','internal_itching','toxic_look_(typhos)',
'depression','irritability','muscle_pain','altered_sensorium','red_spots_over_body','belly_pain',
'abnormal_menstruation','dischromic _patches','watering_from_eyes','increased_appetite','polyuria','family_history','mucoid_sputum',
'rusty_sputum','lack_of_concentration','visual_disturbances','receiving_blood_transfusion',
'receiving_unsterile_injections','coma','stomach_bleeding','distention_of_abdomen',
'history_of_alcohol_consumption','fluid_overload','blood_in_sputum','prominent_veins_on_calf',
'palpitations','painful_walking','pus_filled_pimples','blackheads','scurring','skin_peeling',
'silver_like_dusting','small_dents_in_nails','inflammatory_nails','blister','red_sore_around_nose',
'yellow_crust_ooze']

#List of Diseases is listed in list disease.

disease=['Fungal infection','Allergy','GERD','Chronic cholestasis','Drug Reaction',
'Peptic ulcer diseae','AIDS','Diabetes','Gastroenteritis','Bronchial Asthma','Hypertension',
' Migraine','Cervical spondylosis',
'Paralysis (brain hemorrhage)','Jaundice','Malaria','Chicken pox','Dengue','Typhoid','hepatitis A',
'Hepatitis B','Hepatitis C','Hepatitis D','Hepatitis E','Alcoholic hepatitis','Tuberculosis',
'Common Cold','Pneumonia','Dimorphic hemmorhoids(piles)',
'Heartattack','Varicoseveins','Hypothyroidism','Hyperthyroidism','Hypoglycemia','Osteoarthristis',
'Arthritis','(vertigo) Paroymsal  Positional Vertigo','Acne','Urinary tract infection','Psoriasis',
'Impetigo']

l2=[]

for i in range(0,len(l1)):
    l2.append(0)

df=pd.read_csv("D:\\New folder\\Prototype.csv")

#Replace the values in the imported file by pandas by the inbuilt function replace in pandas.

df.replace({'prognosis':{'Fungal infection':0,'Allergy':1,'GERD':2,'Chronic cholestasis':3,'Drug Reaction':4,
'Peptic ulcer diseae':5,'AIDS':6,'Diabetes ':7,'Gastroenteritis':8,'Bronchial Asthma':9,'Hypertension ':10,
'Migraine':11,'Cervical spondylosis':12,
'Paralysis (brain hemorrhage)':13,'Jaundice':14,'Malaria':15,'Chicken pox':16,'Dengue':17,'Typhoid':18,'hepatitis A':19,
'Hepatitis B':20,'Hepatitis C':21,'Hepatitis D':22,'Hepatitis E':23,'Alcoholic hepatitis':24,'Tuberculosis':25,
'Common Cold':26,'Pneumonia':27,'Dimorphic hemmorhoids(piles)':28,'Heart attack':29,'Varicose veins':30,'Hypothyroidism':31,
'Hyperthyroidism':32,'Hypoglycemia':33,'Osteoarthristis':34,'Arthritis':35,
'(vertigo) Paroymsal  Positional Vertigo':36,'Acne':37,'Urinary tract infection':38,'Psoriasis':39,
'Impetigo':40}},inplace=True)

#check the df 
#print(df.head())

X= df[l1]

#print(X)

y = df[["prognosis"]]
np.ravel(y)

#print(y)

#Read a csv named Testing.csv

tr=pd.read_csv("D:\\New folder\\Prototype-1.csv")

#Use replace method in pandas.

tr.replace({'prognosis':{'Fungal infection':0,'Allergy':1,'GERD':2,'Chronic cholestasis':3,'Drug Reaction':4,
'Peptic ulcer diseae':5,'AIDS':6,'Diabetes ':7,'Gastroenteritis':8,'Bronchial Asthma':9,'Hypertension ':10,
'Migraine':11,'Cervical spondylosis':12,
'Paralysis (brain hemorrhage)':13,'Jaundice':14,'Malaria':15,'Chicken pox':16,'Dengue':17,'Typhoid':18,'hepatitis A':19,
'Hepatitis B':20,'Hepatitis C':21,'Hepatitis D':22,'Hepatitis E':23,'Alcoholic hepatitis':24,'Tuberculosis':25,
'Common Cold':26,'Pneumonia':27,'Dimorphic hemmorhoids(piles)':28,'Heart attack':29,'Varicose veins':30,'Hypothyroidism':31,
'Hyperthyroidism':32,'Hypoglycemia':33,'Osteoarthristis':34,'Arthritis':35,
'(vertigo) Paroymsal  Positional Vertigo':36,'Acne':37,'Urinary tract infection':38,'Psoriasis':39,
'Impetigo':40}},inplace=True)

X_test= tr[l1]
y_test = tr[["prognosis"]]

#print(y_test)

np.ravel(y_test)
def DecisionTree():
    
    from sklearn import tree

    clf3 = tree.DecisionTreeClassifier() 
    clf3 = clf3.fit(X,y)

    from sklearn.metrics import accuracy_score
    y_pred=clf3.predict(X_test)
    print(accuracy_score(y_test, y_pred))
    print(accuracy_score(y_test, y_pred,normalize=False))

    psymptoms = [Symptom1.get(),Symptom2.get(),Symptom3.get(),Symptom4.get(),Symptom5.get()]

    for k in range(0,len(l1)):
        for z in psymptoms:
            if(z==l1[k]):
                l2[k]=1

    inputtest = [l2]
    predict = clf3.predict(inputtest)
    predicted=predict[0]

    h='no'
    for a in range(0,len(disease)):
        if(predicted == a):
            h='yes'
            break


    if (h=='yes'):
        t1.delete("1.0", END)
        t1.insert(END, disease[a])
    else:
        t1.delete("1.0", END)
        t1.insert(END, "Not Found")


def randomforest():
    from sklearn.ensemble import RandomForestClassifier
    clf4 = RandomForestClassifier()
    clf4 = clf4.fit(X,np.ravel(y))

    # calculating accuracy 
    from sklearn.metrics import accuracy_score
    y_pred=clf4.predict(X_test)
    print(accuracy_score(y_test, y_pred))
    print(accuracy_score(y_test, y_pred,normalize=False))
    
    psymptoms = [Symptom1.get(),Symptom2.get(),Symptom3.get(),Symptom4.get(),Symptom5.get()]

    for k in range(0,len(l1)):
        for z in psymptoms:
            if(z==l1[k]):
                l2[k]=1

    inputtest = [l2]
    predict = clf4.predict(inputtest)
    predicted=predict[0]

    h='no'
    for a in range(0,len(disease)):
        if(predicted == a):
            h='yes'
            break

    if (h=='yes'):
        t2.delete("1.0", END)
        t2.insert(END, disease[a])
    else:
        t2.delete("1.0", END)
        t2.insert(END, "Not Found")


def NaiveBayes():
    from sklearn.naive_bayes import GaussianNB
    gnb = GaussianNB()
    gnb=gnb.fit(X,np.ravel(y))

    from sklearn.metrics import accuracy_score
    y_pred=gnb.predict(X_test)
    print(accuracy_score(y_test, y_pred))
    print(accuracy_score(y_test, y_pred,normalize=False))

    psymptoms = [Symptom1.get(),Symptom2.get(),Symptom3.get(),Symptom4.get(),Symptom5.get()]
    for k in range(0,len(l1)):
        for z in psymptoms:
            if(z==l1[k]):
                l2[k]=1

    inputtest = [l2]
    predict = gnb.predict(inputtest)
    predicted=predict[0]

    h='no'
    for a in range(0,len(disease)):
        if(predicted == a):
            h='yes'
            break

    if (h=='yes'):
        t3.delete("1.0", END)
        t3.insert(END, disease[a])
    else:
        t3.delete("1.0", END)
        t3.insert(END, "Not Found")

# GUI stuff..............................................................................
 #login GUI
def main_menu():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("500x500")
    main_screen.title("Account Login")
    Label(text="Select Your Choice", bg="blue", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Admin", height="3", width="50", command = sadmin).pack()
    Label(text="").pack()
    Button(text="User", height="3", width="50", command=suser).pack()
 
    main_screen.mainloop()
 
#admin login screen
def sadmin():
    global admin_login_screen
    admin_login_screen = Toplevel(main_screen)
    admin_login_screen.title("Login")
    admin_login_screen.geometry("300x250")
    Label(admin_login_screen, text="Please enter details below to login").pack()
    Label(admin_login_screen, text="").pack()
 
    global username_verify
    global password_verify
 
    username_verify = StringVar()
    password_verify = StringVar()
 
    global username_login_entry
    global password_login_entry
 
    Label(admin_login_screen, text="Username * ").pack()
    username_login_entry = Entry(admin_login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(admin_login_screen, text="").pack()
    Label(admin_login_screen, text="Password * ").pack()
    password_login_entry = Entry(admin_login_screen, textvariable=password_verify, show= '*')
    password_login_entry.pack()
    Label(admin_login_screen, text="").pack()
    Button(admin_login_screen, text="Login", width=10, height=1, command=admin_login_verify).pack()

#user login screen
def suser():
    global user_login_screen
    user_login_screen = Toplevel(main_screen)
    user_login_screen.title("Login")
    user_login_screen.geometry("300x250")
    Label(user_login_screen, text="Please enter details below to login").pack()
    Label(user_login_screen, text="").pack()
 
    global username_verify
    global password_verify
 
    username_verify = StringVar()
    password_verify = StringVar()
 
    global username_login_entry
    global password_login_entry
 
    Label(user_login_screen, text="Username * ").pack()
    username_login_entry = Entry(user_login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(user_login_screen, text="").pack()
    Label(user_login_screen, text="Password * ").pack()
    password_login_entry = Entry(user_login_screen, textvariable=password_verify, show= '*')
    password_login_entry.pack()
    Label(user_login_screen, text="").pack()
    Button(user_login_screen, text="Login", width=10, height=1, command=user_login_verify).pack()

#verify admin password
def admin_login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    if(username1 == 'Admin' and password1 == '1234'):
        messagebox.showinfo("", "Login To Admin")
    else:
        messagebox.showinfo("", "Incorrect Username / Password ")
        
#verify user password
def user_login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    if(username1 == 'user' and password1 == '1234'):
        user_interface()
    else:
        messagebox.showinfo("", "Incorrect Username / Password ")

        
def user_interface():
    
    user_interface = Toplevel(main_screen)
    
    Name = StringVar()

    w2 = Label(user_interface, justify=LEFT, text="Disease Predictor", fg="white", bg="black")
    w2.config(font=("Times",30,"bold italic"))
    w2.grid(row=1, column=0, columnspan=2, padx=200)

    NameLb = Label(user_interface, text="Name of the Patient :", fg="white", bg="Black")
    NameLb.config(font=("Times",15,"bold italic"))
    NameLb.grid(row=6, column=0, pady=15, sticky=W)

    S1Lb = Label(user_interface, text="Symptom 1", fg="white", bg="black")
    S1Lb.config(font=("Times",15,"bold italic"))
    S1Lb.grid(row=7, column=0, pady=10, sticky=W)

    S2Lb = Label(user_interface, text="Symptom 2", fg="White", bg="black")
    S2Lb.config(font=("Times",15,"bold italic"))
    S2Lb.grid(row=8, column=0, pady=10, sticky=W)

    S3Lb = Label(user_interface, text="Symptom 3", fg="White",bg="black")
    S3Lb.config(font=("Times",15,"bold italic"))
    S3Lb.grid(row=9, column=0, pady=10, sticky=W)

    S4Lb = Label(user_interface, text="Symptom 4", fg="white", bg="black")
    S4Lb.config(font=("Times",15,"bold italic"))
    S4Lb.grid(row=10, column=0, pady=10, sticky=W)

    S5Lb = Label(user_interface, text="Symptom 5", fg="white", bg="black")
    S5Lb.config(font=("Times",15,"bold italic"))
    S5Lb.grid(row=11, column=0, pady=10, sticky=W)


    lrLb = Label(user_interface, text="DecisionTree", fg="white", bg="black")
    lrLb.config(font=("Times",15,"bold italic"))
    lrLb.grid(row=15, column=0, pady=10,sticky=W)

    destreeLb = Label(user_interface, text="RandomForest", fg="Red", bg="Orange")
    destreeLb.config(font=("Times",15,"bold italic"))
    destreeLb.grid(row=17, column=0, pady=10, sticky=W)

    ranfLb = Label(user_interface, text="NaiveBayes", fg="White", bg="green")
    ranfLb.config(font=("Times",15,"bold italic"))
    ranfLb.grid(row=19, column=0, pady=10, sticky=W)

    OPTIONS = sorted(l1)

    NameEn = Entry(user_interface, textvariable=Name)
    NameEn.grid(row=6, column=1)

    S1 = OptionMenu(user_interface, Symptom1,*OPTIONS)
    S1.grid(row=7, column=1)

    S2 = OptionMenu(user_interface, Symptom2,*OPTIONS)
    S2.grid(row=8, column=1)

    S3 = OptionMenu(user_interface, Symptom3,*OPTIONS)
    S3.grid(row=9, column=1)

    S4 = OptionMenu(user_interface, Symptom4,*OPTIONS)
    S4.grid(row=10, column=1)

    S5 = OptionMenu(user_interface, Symptom5,*OPTIONS)
    S5.grid(row=11, column=1)


    dst = Button(user_interface, text="Prediction 1", command=DecisionTree,bg="Red",fg="yellow")
    dst.config(font=("Times",15,"bold italic"))
    dst.grid(row=8, column=3,padx=10)

    rnf = Button(user_interface, text="Prediction 2", command=randomforest,bg="White",fg="green")
    rnf.config(font=("Times",15,"bold italic"))
    rnf.grid(row=9, column=3,padx=10)

    lr = Button(user_interface, text="Prediction 3", command=NaiveBayes,bg="Blue",fg="white")
    lr.config(font=("Times",15,"bold italic"))
    lr.grid(row=10, column=3,padx=10)


    t1 = Text(user_interface, height=1, width=40,bg="Light green",fg="red")
    t1.config(font=("Times",15,"bold italic"))
    t1.grid(row=15, column=1, padx=10)

    t2 = Text(user_interface, height=1, width=40,bg="White",fg="Blue")
    t2.config(font=("Times",15,"bold italic"))
    t2.grid(row=17, column=1 , padx=10)

    t3 = Text(user_interface, height=1, width=40,bg="red",fg="white")
    t3.config(font=("Times",15,"bold italic"))
    t3.grid(row=19, column=1 , padx=10)

main_menu()