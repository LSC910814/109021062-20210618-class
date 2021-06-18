from tkinter import  *
import hashlib #雜湊密碼處理

s256 = hashlib.sha256()
s1 = hashlib.sha1()
md5 = hashlib.md5()

def login():
    IdData = entryID.get()
    PsData = entryPS.get()
    if len(IdData) > 0 and len(IdData) > 0:
        if IdData == "h304" and PsData == "1234":
            root.deiconify() #開啟另一視窗
            top.destroy() #Login視窗摧毀
        else:
            entryID.delete(0, "end")
            entryPS.delete(0, "end")
    else:
        entryID.delete(0, "end")
        entryPS.delete(0, "end")

def leave():
    top.destroy()
    root.destroy()
    
def find():
    Guesshash = entryGuess.get()
    if len(Guesshash) > 0:
        s256.update(Guesshash.encode('utf-8'))
        Guesshash = s256.hexdigest() #hexdigest16進制的摘要
        s1.update(Guesshash.encode('utf-8'))
        Guesshash = s1.hexdigest() 
        md5.update(Guesshash.encode('utf-8'))
        Guesshash = md5.hexdigest() 
        if Guesshash == "7110eda4d09e062aa5e4a390b0a572ac0d2c0220":
            labAw.config(text="SHA-1")
        elif Guesshash == "03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4":
            labAw.config(text="SHA-256")
        elif Guesshash == "81dc9bdb52d04dc20036dbd8313ed055":
            labAw.config(text="MD5")
        elif Guesshash == "5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8":
            labAw.config(text="SHA-1")
        elif Guesshash == "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8":
            labAw.config(text="SHA-256")
        elif Guesshash == "5f4dcc3b5aa765d61d8327deb882cf99":
            labAw.config(text="MD5")
        elif Guesshash == "1f8ac10f23c5b5bc1167bda84b833e5c057a77d2":
            labAw.config(text="SHA-1")
        elif Guesshash == "bef57ec7f53a6d40beb640a780a639c83bc29ac8a9816f1fc6c5c6dcd93c4721":
            labAw.config(text="SHA-256")
        elif Guesshash == "e80b5017098950fc58aad83c8c14978e":
            labAw.config(text="MD5")
        elif Guesshash == "b1b3773a05c0ed0176787a4f1574ff0075f7521e":
            labAw.config(text="SHA-1")
        elif Guesshash == "65e84be33532fb784c48129675f9eff3a682b27168c0ea744b2cf58ee02337c5":
            labAw.config(text="SHA-256")
        elif Guesshash == "d8578edf8458ce06fbc5bb76a58c5ca4":
            labAw.config(text="MD5")




root = Tk()
root.geometry("400x400+100+100")
top = Toplevel(root) #可以把top想像成一個視窗
labID = Label(top, text="ID", anchor = E, justify = RIGHT, font =("Times", 20))
labPS = Label(top, text="Password", anchor = E, justify = RIGHT, font =("Times", 20))
entryID = Entry(top)
entryPS = Entry(top,show = '*')
btnLogin = Button(top, text="Login", command = login)
btnLeave = Button(top, text="Leave", command = leave)
labID.grid(row=0, column=0, sticky=NSEW)
entryID.grid(row=0, column=1, sticky=NSEW)
labPS.grid(row=1, column=0, sticky=NSEW)
entryPS.grid(row=1, column=1, sticky=NSEW)
btnLogin.grid(row=2, column=0, sticky=NSEW)
btnLeave.grid(row=2, column=1, sticky=NSEW)



labGuess = Label(root, text="Password", anchor = E, justify = RIGHT, font=("Arial", 20,"italic"))
entryGuess = Entry(root)
labGuess.grid(row=0, column= 0,sticky=NSEW)
entryGuess.grid(row=0, column=1, sticky=NSEW)
Btn = Button(root, text="find", command=find, anchor = CENTER, font=("Arial", 20,"italic"))
Btn.grid(row=1, column=1, sticky=NSEW)
labAw = Label(root, text="", bg='light blue', command=find())
labAw.grid(row=2, column=1, sticky=NSEW)


root.withdraw() #抽起來先不顯示
root.mainloop()