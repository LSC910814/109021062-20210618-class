from tkinter import  *
import hashlib #雜湊密碼處理

s256 = hashlib.sha256()


def login():
    IdData = entryID.get()
    PsData = entryPS.get()
    if len(IdData) > 0 and len(IdData) > 0:
        s256.update(PsData.encode('utf-8'))
        Pshash = s256.hexdigest() #hexdigest16進制的摘要
        s256.update(IdData.encode('utf-8'))
        Idhash = s256.hexdigest() #hexdigest16進制的摘要
        if Idhash == "3774e4a1e8529d60258f0e7be05bdea6600ecc3e870d13a83a473fde9c435b0a" and Pshash == "5515f0912ec4ca5c9537a9c29ed62372869e0f2332c58eb312bd7ca7de850456":
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

flag = True
def setBtnText(num):
    global flag
    if num == 0:
        if flag:
            btn0.config(text="O")
        else:
            btn0.config(text="X")
        btn0.config(state=DISABLED) #按鈕按過後不能使用
    elif num == 1:
        if flag:
            btn1.config(text="O")
        else:
            btn1.config(text="X")
        btn1.config(state=DISABLED)
    elif num == 2:
        if flag:
            btn2.config(text="O")
        else:
            btn2.config(text="X")
        btn2.config(state=DISABLED)
    elif num == 3:
        if flag:
            btn3.config(text="O")
        else:
            btn3.config(text="X")
        btn3.config(state=DISABLED)
    elif num == 4:
        if flag:
            btn4.config(text="O")
        else:
            btn4.config(text="X")
        btn4.config(state=DISABLED)
    elif num == 5:
        if flag:
            btn5.config(text="O")
        else:
            btn5.config(text="X")
        btn5.config(state=DISABLED)
    elif num == 6:
        if flag:
            btn6.config(text="O")
        else:
            btn6.config(text="X")
        btn6.config(state=DISABLED)
    elif num == 7:
        if flag:
            btn7.config(text="O")
        else:
            btn7.config(text="X")
        btn7.config(state=DISABLED)
    elif num == 8:
        if flag:
            btn8.config(text="O")
        else:
            btn8.config(text="X")
        btn8.config(state=DISABLED)
    flag = not flag
    
    if btn0.cget('text') == btn1.cget('text') == btn2.cget('text'):
        if btn0.cget('text') == "O":
            print("P1 is winner")
            btn0.config(state=DISABLED)  
            btn1.config(state=DISABLED) 
            btn2.config(state=DISABLED) 
            btn3.config(state=DISABLED) 
            btn4.config(state=DISABLED)  
            btn5.config(state=DISABLED)
            btn6.config(state=DISABLED) 
            btn7.config(state=DISABLED) 
            btn8.config(state=DISABLED)
        if btn0.cget('text') == "X":
            print("P2 is winner")
            btn0.config(state=DISABLED)  
            btn1.config(state=DISABLED) 
            btn2.config(state=DISABLED) 
            btn3.config(state=DISABLED) 
            btn4.config(state=DISABLED)  
            btn5.config(state=DISABLED)
            btn6.config(state=DISABLED) 
            btn7.config(state=DISABLED) 
            btn8.config(state=DISABLED)
    if btn3.cget('text') == btn4.cget('text') == btn5.cget('text'):
        if btn3.cget('text') == "O":
            print("P1 is winner")
            btn0.config(state=DISABLED)  
            btn1.config(state=DISABLED) 
            btn2.config(state=DISABLED) 
            btn3.config(state=DISABLED) 
            btn4.config(state=DISABLED)  
            btn5.config(state=DISABLED)
            btn6.config(state=DISABLED) 
            btn7.config(state=DISABLED) 
            btn8.config(state=DISABLED)
        if btn3.cget('text') == "X":
            print("P2 is winner")
            btn0.config(state=DISABLED)  
            btn1.config(state=DISABLED) 
            btn2.config(state=DISABLED) 
            btn3.config(state=DISABLED) 
            btn4.config(state=DISABLED)  
            btn5.config(state=DISABLED)
            btn6.config(state=DISABLED) 
            btn7.config(state=DISABLED) 
            btn8.config(state=DISABLED)
    if btn6.cget('text') == btn7.cget('text') == btn8.cget('text'):
        if btn6.cget('text') == "O":
            print("P1 is winner")
            btn0.config(state=DISABLED)  
            btn1.config(state=DISABLED) 
            btn2.config(state=DISABLED) 
            btn3.config(state=DISABLED) 
            btn4.config(state=DISABLED)  
            btn5.config(state=DISABLED)
            btn6.config(state=DISABLED) 
            btn7.config(state=DISABLED) 
            btn8.config(state=DISABLED)
        if btn6.cget('text') == "X":
            print("P2 is winner")
            btn0.config(state=DISABLED)  
            btn1.config(state=DISABLED) 
            btn2.config(state=DISABLED) 
            btn3.config(state=DISABLED) 
            btn4.config(state=DISABLED)  
            btn5.config(state=DISABLED)
            btn6.config(state=DISABLED) 
            btn7.config(state=DISABLED) 
            btn8.config(state=DISABLED)
    if btn0.cget('text') == btn3.cget('text') == btn6.cget('text'):
        if btn0.cget('text') == "O":
            print("P1 is winner")
            btn0.config(state=DISABLED)  
            btn1.config(state=DISABLED) 
            btn2.config(state=DISABLED) 
            btn3.config(state=DISABLED) 
            btn4.config(state=DISABLED)  
            btn5.config(state=DISABLED)
            btn6.config(state=DISABLED) 
            btn7.config(state=DISABLED) 
            btn8.config(state=DISABLED)
        if btn0.cget('text') == "X":
            print("P2 is winner")
            btn0.config(state=DISABLED)  
            btn1.config(state=DISABLED) 
            btn2.config(state=DISABLED) 
            btn3.config(state=DISABLED) 
            btn4.config(state=DISABLED)  
            btn5.config(state=DISABLED)
            btn6.config(state=DISABLED) 
            btn7.config(state=DISABLED) 
            btn8.config(state=DISABLED)
    if btn1.cget('text') == btn4.cget('text') == btn7.cget('text'):
        if btn1.cget('text') == "O":
            print("P1 is winner")
            btn0.config(state=DISABLED)  
            btn1.config(state=DISABLED) 
            btn2.config(state=DISABLED) 
            btn3.config(state=DISABLED) 
            btn4.config(state=DISABLED)  
            btn5.config(state=DISABLED)
            btn6.config(state=DISABLED) 
            btn7.config(state=DISABLED) 
            btn8.config(state=DISABLED)
        if btn1.cget('text') == "X":
            print("P2 is winner")
            btn0.config(state=DISABLED)  
            btn1.config(state=DISABLED) 
            btn2.config(state=DISABLED) 
            btn3.config(state=DISABLED) 
            btn4.config(state=DISABLED)  
            btn5.config(state=DISABLED)
            btn6.config(state=DISABLED) 
            btn7.config(state=DISABLED) 
            btn8.config(state=DISABLED)
    if btn3.cget('text') == btn5.cget('text') == btn8.cget('text'):
        if btn3.cget('text') == "O":
            print("P1 is winner")
            btn0.config(state=DISABLED)  
            btn1.config(state=DISABLED) 
            btn2.config(state=DISABLED) 
            btn3.config(state=DISABLED) 
            btn4.config(state=DISABLED)  
            btn5.config(state=DISABLED)
            btn6.config(state=DISABLED) 
            btn7.config(state=DISABLED) 
            btn8.config(state=DISABLED)
        if btn3.cget('text') == "X":
            print("P2 is winner")
            btn0.config(state=DISABLED)  
            btn1.config(state=DISABLED) 
            btn2.config(state=DISABLED) 
            btn3.config(state=DISABLED) 
            btn4.config(state=DISABLED)  
            btn5.config(state=DISABLED)
            btn6.config(state=DISABLED) 
            btn7.config(state=DISABLED) 
            btn8.config(state=DISABLED)
    if btn0.cget('text') == btn4.cget('text') == btn8.cget('text'):
        if btn0.cget('text') == "O":
            print("P1 is winner")
            btn0.config(state=DISABLED)  
            btn1.config(state=DISABLED) 
            btn2.config(state=DISABLED) 
            btn3.config(state=DISABLED) 
            btn4.config(state=DISABLED)  
            btn5.config(state=DISABLED)
            btn6.config(state=DISABLED) 
            btn7.config(state=DISABLED) 
            btn8.config(state=DISABLED)
        if btn0.cget('text') == "X":
            print("P2 is winner")
            btn0.config(state=DISABLED)  
            btn1.config(state=DISABLED) 
            btn2.config(state=DISABLED) 
            btn3.config(state=DISABLED) 
            btn4.config(state=DISABLED)  
            btn5.config(state=DISABLED)
            btn6.config(state=DISABLED) 
            btn7.config(state=DISABLED) 
            btn8.config(state=DISABLED)
    if btn2.cget('text') == btn4.cget('text') == btn6.cget('text'):
        if btn2.cget('text') == "O":
            print("P1 is winner")
            btn0.config(state=DISABLED)  
            btn1.config(state=DISABLED) 
            btn2.config(state=DISABLED) 
            btn3.config(state=DISABLED) 
            btn4.config(state=DISABLED)  
            btn5.config(state=DISABLED)
            btn6.config(state=DISABLED) 
            btn7.config(state=DISABLED) 
            btn8.config(state=DISABLED)
        if btn2.cget('text') == "X":
            print("P2 is winner")
            btn0.config(state=DISABLED)  
            btn1.config(state=DISABLED) 
            btn2.config(state=DISABLED) 
            btn3.config(state=DISABLED) 
            btn4.config(state=DISABLED)  
            btn5.config(state=DISABLED)
            btn6.config(state=DISABLED) 
            btn7.config(state=DISABLED) 
            btn8.config(state=DISABLED)
    

root = Tk()
root.geometry("400x400+100+100")
top = Toplevel(root) #可以把top想像成一個視窗
labID = Label(top, text="ID", anchor = E, justify = RIGHT, font=("Arial", 20,"italic"))
labPS = Label(top, text="Password", anchor = E, justify = RIGHT, font=("Arial", 20, "italic"))
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

root.rowconfigure(0, weight = 1) #高
root.columnconfigure(0, weight = 1) #寬
root.rowconfigure(1, weight = 1)
root.columnconfigure(1, weight = 1)
root.rowconfigure(2, weight = 1)
root.columnconfigure(2, weight = 1)

btn0 = Button(root, text="", command=lambda:setBtnText(0))#lambda函式效果
btn0.grid(row = 0, column = 0, sticky="nsew") 
btn1 = Button(root, text="", command=lambda:setBtnText(1))
btn1.grid(row = 0, column = 1, sticky="nsew")
btn2 = Button(root, text="", command=lambda:setBtnText(2))
btn2.grid(row = 0, column = 2, sticky="nsew")
btn3 = Button(root, text="", command=lambda:setBtnText(3))
btn3.grid(row = 1, column = 0, sticky="nsew")
btn4 = Button(root, text="", command=lambda:setBtnText(4))
btn4.grid(row = 1, column = 1, sticky="nsew")
btn5 = Button(root, text="", command=lambda:setBtnText(5))
btn5.grid(row = 1, column = 2, sticky="nsew")
btn6 = Button(root, text="", command=lambda:setBtnText(6))
btn6.grid(row = 2, column = 0, sticky="nsew")
btn7 = Button(root, text="", command=lambda:setBtnText(7))
btn7.grid(row = 2, column = 1, sticky="nsew")
btn8 = Button(root, text="", command=lambda:setBtnText(8))
btn8.grid(row = 2, column = 2, sticky="nsew")

root.withdraw() #抽起來先不顯示
root.mainloop()