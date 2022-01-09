from tkinter import *
from tkinter import messagebox
import platform   
import webbrowser
root=Tk()
root.geometry("780x600")
root.resizable(0,0)
ico=PhotoImage(file="icon.png")
root.iconphoto(True,ico)
root.config(bg="#ffa40b")
root.title("Website Manager")
Label(root,text="Enter the website to block",font=("font awesome",15,"bold italic"),bg="#ffa40b",fg="green").place(x=250,y=20)
ip_address="127.0.0.10"
websites=Entry(root,width=30,borderwidth=6,font=("fontawesome",15,"bold italic"),bg="green",fg="#ffa40b")
websites.place(x=180,y=60)
Label(root,text="Ex: abc123.com",font=("font awesome",15,"bold italic"),bg="#ffa40b",fg="green").place(x=300,y=100)
os=platform.system()
if((os.lower()=="linux") | (os.lower()=="darwin")):
    host_path="/etc/hosts"
elif(os.lower()=="windows"):
    host_path="c:\windows\system32\drivers\etc\hosts"
else:
    messagebox.showerror("Error","Operating System Error")
def Block():
    try:
        if(len(websites.get())==1):
            messagebox.showwarning("Input Error","Input Field Can't be Empty")
        else:
            websites_list=websites.get()
            website=list(websites_list.split(","))
            with open(host_path,"r+") as host_file:
                file_content=host_file.read()
                for web in website:
                    if web in file_content:
                        messagebox.showinfo("Already Blocked","Website already blocked")
                        pass
                    else:
                        host_file.write("\n"+ip_address+" "+web+"\n")                    
                        messagebox.showinfo("Success","Website blocked successfully ")
    except PermissionError:
        messagebox.showerror("Admin Privileges Required","Run the Program with Admin Privileges")
def unblock():
    try:
        if(len(websites.get())==1):
            messagebox.showwarning("Input Error","Input Field Can't be Empty")
        else:
            websites_list=websites.get()
            website=list(websites_list.split(","))
            with open(host_path,"r+") as host_file:
                file_content=host_file.read()
                for web in website:
                    if web in file_content:
                        a_file = open(host_path, "r")
                        url=websites.get()
                        site=f"{ip_address} {url}"
                        lines = a_file.readlines()
                        a_file.close()
                        new_file = open(host_path, "w")
                        for line in lines:
                            if line.strip("\n") != site:
                                new_file.write(line)
                        new_file.close()
                        messagebox.showinfo("Success","Site Unblocked successfully")
                    else:
                        messagebox.showwarning("Not Found","Site not found")
    except PermissionError:
        messagebox.showerror("Admin Privileges Required","Run the Program with Admin Privileges")
def exitFunction():
    root.destroy

buttonBlock=Button(root,text="BLOCK",font=("font awesome",15,"bold italic"),bg="green",fg="#ffa40b",width=7,borderwidth=5,command=Block)
buttonBlock.place(x=330,y=130)

buttonUnBlock=Button(root,text="UNBLOCK",font=("font awesome",15,"bold italic"),bg="green",fg="#ffa40b",width=7,borderwidth=5,command=unblock)
buttonUnBlock.place(x=330,y=190)

buttonClear=Button(root,text="CLEAR",font=("font awesome",15,"bold italic"),bg="green",fg="#ffa40b",width=7,borderwidth=5,command=lambda: websites.delete(0,END))
buttonClear.place(x=330,y=250)

buttonExit=Button(root,text="EXIT",font=("font awesome",15,"bold italic"),bg="green",fg="#ffa40b",width=7,borderwidth=5,command=root.destroy)
buttonExit.place(x=330,y=310)

buttonContact=Button(root,text="CONTACT",font=("font awesome",15,"bold italic"),bg="green",fg="#ffa40b",width=7,borderwidth=5,command=lambda:webbrowser.open("https://github.com/cmanjunathan45/"))
buttonContact.place(x=330,y=370)
root.mainloop()              
