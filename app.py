
from tkinter import *
from mydb import Database
from tkinter import messagebox
from myapi import API
class NLPapp:
    def __init__(self):
        self.root = Tk()
        self.dbo = Database()
        self.apio = API()

        self.root.title("NLP APP")
        self.root.iconbitmap('project/resources/favicon.ico')
        self.root.geometry('350x550')
        self.root.configure(bg = "#1C3277")
        self.login_gui()
        self.root.mainloop()
        print("done")

    def login_gui(self):
        self.clear()
        heading = Label(self.root , text="NLP App" , bg="#1C3277" , fg="white")
        heading.pack(pady=(25,25))
        heading.configure(font=('verdana',24,'bold'))
        
        label1 = Label(self.root , text="Enter Email", bg="#1C3277",fg="white")
        label1.pack(pady=(10,10))
        
        self.email_input = Entry(self.root , width=50)
        self.email_input.pack(pady=(5,10), ipady=4)

        label2 = Label(self.root , text="Enter Password", bg="#1C3277",fg="white")
        label2.pack(pady=(10,10))
        
        self.pass_input = Entry(self.root , width=50 , show="*")
        self.pass_input.pack(pady=(5,10), ipady=4)

        login_btn = Button(self.root , text="Login" , width=20 , height=2 , command=self.perform_login)
        login_btn.pack(pady=(10,10))

        label1 = Label(self.root , text="Not a Member", bg="#1C3277",fg="white")
        label1.pack(pady=(10,3))

        redirect_btn = Button(self.root , text="Register Now" , width = 10,height=1 , command=self.register_gui)
        redirect_btn.pack(pady=(3,10))

    def register_gui(self):
        self.clear()
        heading = Label(self.root , text="NLP App" , bg="#1C3277" , fg="white")
        heading.pack(pady=(25,25))
        heading.configure(font=('verdana',24,'bold'))

        label0 = Label(self.root , text="Enter Name", bg="#1C3277",fg="white")
        label0.pack(pady=(10,10))
        
        self.name_input = Entry(self.root , width=50)
        self.name_input.pack(pady=(5,10), ipady=4)
        
        label1 = Label(self.root , text="Enter Email", bg="#1C3277",fg="white")
        label1.pack(pady=(10,10))
        
        self.email_input = Entry(self.root , width=50)
        self.email_input.pack(pady=(5,10), ipady=4)

        label2 = Label(self.root , text="Enter Password", bg="#1C3277",fg="white")
        label2.pack(pady=(10,10))
        
        self.pass_input = Entry(self.root , width=50 , show="*")
        self.pass_input.pack(pady=(5,10), ipady=4)

        register_btn = Button(self.root , text="Register" , width=20 , height=2,command=self.perform_registration)
        register_btn.pack(pady=(10,10))

        label1 = Label(self.root , text="Already a Member", bg="#1C3277",fg="white")
        label1.pack(pady=(10,3))

        redirect_btn = Button(self.root , text="Login Now" , width = 10,height=1 , command=self.login_gui)
        redirect_btn.pack(pady=(3,10))

    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()
    
    def perform_registration(self):
        name = self.name_input.get()
        email  = self.email_input.get()
        password = self.pass_input.get()

        response = self.dbo.add_data(name,email , password)
        if response:
            messagebox.showinfo("success","Registration Successfully done. you can login now")
        else:
            messagebox.showerror("Error", "Email already exist")

    def perform_login(self):
        email = self.email_input.get()
        password = self.pass_input.get()

        response = self.dbo.check_data(email , password)
        if response:
            messagebox.showinfo("success","login successfully")
            self.home_gui()
        else:
            messagebox.showerror("Error","incorrect email/password ")
    
    def home_gui(self):
        self.clear()
        heading = Label(self.root , text="NLP App" , bg="#1C3277" , fg="white")
        heading.pack(pady=(25,25))
        heading.configure(font=('verdana',24,'bold'))
        
        sentiment_btn = Button(self.root , text="Sentiment Analysis", width = 20 , height=2,bg="#E2E4EA",fg="black",command=self.sentiment_gui)
        sentiment_btn.pack(pady=(15,10))
        sentiment_btn.configure(font=('verdana',14))
        
        ner_btn = Button(self.root , text="Name Entity Recognition",width = 20 , bg="#E2E4EA",fg="black")
        ner_btn.pack(pady=(10,10))
        ner_btn.configure(font=('verdana',14))

        emotion_btn = Button(self.root , text="Emotion Prediction",width = 20 , height=2, bg="#E2E4EA",fg="black")
        emotion_btn.pack(pady=(10,10))
        emotion_btn.configure(font=('verdana',14))
      
    
        logout_btn = Button(self.root , text = "logout" , width=9 , height=1 , command=self.perform_login)
        logout_btn.pack(pady=(10,10))

    def sentiment_gui(self):
        self.clear()
        heading = Label(self.root , text="NLP App" , bg="#1C3277" , fg="white")
        heading.pack(pady=(25,25))
        heading.configure(font=('verdana',24,'bold'))

        heading2 = Label(self.root , text="Sentiment Analysis" , bg="#1C3277" , fg="white")
        heading2.pack(pady=(25,20))
        heading2.configure(font=('verdana',20,'bold'))

        label0 = Label(self.root , text="Enter text", bg="#1C3277",fg="white")
        label0.pack(pady=(10,10))
        label0.configure(font=('verdana',12))

        self.text_input = Entry(self.root , width=50)
        self.text_input.pack(pady=(5,10), ipady=4)
        
        Analyze_btn = Button(self.root , text="Analyze Sentiment", bg="#E2E4EA",fg="black", command= self.do_sentiment_analyse)
        Analyze_btn.pack(pady=(10,10))

        self.sentiment_result = Label(self.root , text=" ", bg="#1C3277",fg="white")
        self.sentiment_result.pack(pady=(10,10))
        self.sentiment_result.configure(font=('verdana',12))
        
        goback_btn = Button(self.root , text = "Go Back" , command= self.home_gui)
        goback_btn.pack(pady=(10,10))
       
    def do_sentiment_analyse(self):
        text = self.text_input.get()
        response = self.apio.sentiment_analysis(text)

        print(response)

        self.sentiment_result["text"] = response








nlp = NLPapp()
