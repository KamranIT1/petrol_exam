import tkinter as tk
from tkinter import *
from datetime import datetime
from tkinter import ttk
from tkinter import messagebox
import random
global_qiymetler = {
        "AI92": 1.10,
        "AI95": 1.60,
        "AI98": 2.30,
        "dizel": 1.00
}


root = tk.Tk()
header = tk.Frame(root, bg="darkblue")
header.place(relx=0, rely=0, relwidth=1, height=28)
tk.Label(header, text="Best Oil", bg="darkblue", fg="white", font=("Arial", 14, "bold"),width=120).pack(fill="x",expand=True)
root.title("BestOil")

hot_have = tk.BooleanVar()
burger_have = tk.BooleanVar()
kartof_have = tk.BooleanVar()
cola_have = tk.BooleanVar()
label_text = tk.StringVar()
label_text1 = tk.StringVar()
label_text2 = tk.StringVar()
label_text3 = tk.StringVar()
label_text4 = tk.StringVar()
entry_text2 = tk.StringVar()
entry_text3 = tk.StringVar()
entry_text4 = tk.StringVar()
entry_text1 = tk.StringVar()
benzin_var = tk.StringVar()
benzin_var1 = tk.StringVar(value=" ")
benzin_var2 = tk.StringVar()
admin_var = tk.StringVar()
admin_var2 = tk.StringVar()
hot_text = tk.StringVar(value="1.10")
burger_text = tk.StringVar(value="2.20")
kartof_text = tk.StringVar(value="3.40")
cola_text = tk.StringVar(value="1.50")
class admin:
    def __init__(self, root, admin_var, admin_var2):
        self.root = root
        self.admin_var = admin_var
        self.admin_var2 = admin_var2


        

        


    def adminpan(self):
     self.my_frame = tk.Frame(self.root)
     self.my_frame.place(relx=0.9, rely=0.1, relwidth=0.1, relheight=0.2) 

     
     
     tk.Label(self.my_frame, text="Setting").pack(fill="y", expand=True,pady=0)
     tk.Frame(self.my_frame, height=20).pack()
     tk.Button(self.my_frame, text="Admin Panel", command=self.show_login,).pack(fill="y",expand=True,pady=10)
     tk.Button(self.my_frame, text="Cixmaq", command=self.log_out).pack(fill="y", expand=True,pady=10)






    def check_login(self):

        try:
            with open("admin.txt", "r") as f:
                files = f.readlines()
            username = files[0].strip()
            password = files[1].strip()
            

            if self.admin_var.get() != username or self.admin_var2.get() != password:
             admin_var.set("")
             admin_var2.set("")
            
             raise NameError
        except NameError:
            messagebox.showerror("Xeta", "Yanlis username ve ya sifre")
        else:
          messagebox.showinfo("INFO", "Login succesfull")
          self.login_frame.destroy()
          self.dashboard_frame = tk.Frame(second_root)
          self.dashboard_frame.pack(fill="y", padx=20, expand=True)
          tk.Label(self.dashboard_frame, text="Welcome to Admin Panel!").pack()
          tk.Button(self.dashboard_frame, text="Benzin qiymetlerini deyis",command=self.benzini_deyis).pack()
          
 
          
        
 




    def show_login(self):
     global second_root
     second_root = tk.Toplevel(self.root)
     second_root.title("Admin Panel")


     self.login_frame = tk.Frame(second_root)
     self.login_frame.pack(fill="y",expand=True,padx=2)


     tk.Label(self.login_frame, text="Username").pack(padx=2,pady=1)
     tk.Entry(self.login_frame, textvariable=self.admin_var).pack(padx=2,pady=2)

     tk.Label(self.login_frame, text="Password").pack(padx=2,pady=3)
     tk.Entry(self.login_frame, textvariable=self.admin_var2, show="*").pack(padx=2,pady=4)

     tk.Button(self.login_frame, text="Login", command=self.check_login).pack(padx=2,pady=5,anchor="center")
     admin_var.set("")
     admin_var2.set("")      
     

     
     
       


        

      


    def benzini_deyis(self):
     self.entry_text1 = tk.StringVar()
     
  


     tk.Label(self.dashboard_frame,text="Qiymeti yaz").pack(expand=True,pady=160)
     tk.Entry(self.dashboard_frame,textvariable=self.entry_text1).place(x=25,y=240)


     
     self.qiymetler = {}
     self.qiymet_var_benzin = tk.BooleanVar(value=0)
     self.qiymet_var_premium = tk.BooleanVar(value=0)
     self.qiymet_var_super = tk.BooleanVar(value=0)
     self.qiymet_var_dizel =  tk.BooleanVar(value=0)
     tk.Checkbutton(self.dashboard_frame,text="AI92",variable=self.qiymet_var_benzin).place(x=50,y=80)
     tk.Checkbutton(self.dashboard_frame,text="AI95",variable=self.qiymet_var_premium).place(x=50,y=110)
     tk.Checkbutton(self.dashboard_frame,text="AI98",variable=self.qiymet_var_super).place(x=50,y=140)
     tk.Checkbutton(self.dashboard_frame,text="Dizel",variable=self.qiymet_var_dizel).place(x=50,y=170)
     tk.Button(self.dashboard_frame,text="Qiymeti tesdiqle",command=self.qiymeti_tesdiqle).pack(expand=True,pady=130,anchor="center")




     

    def qiymeti_tesdiqle(self):
     global global_qiymetler
     qiymet = float(self.entry_text1.get())
     secilenler = []
     if self.qiymet_var_benzin.get():
      global_qiymetler["AI92"] = qiymet
      secilenler.append("AI92")
     if self.qiymet_var_premium.get():
       global_qiymetler["AI95"] = qiymet
       secilenler.append("AI95")
     if self.qiymet_var_super.get():
      global_qiymetler["AI98"] = qiymet
      secilenler.append("AI98")
     if self.qiymet_var_dizel.get():
      global_qiymetler["dizel"] = qiymet
      secilenler.append("Dizel")
      print("Yenilənmiş qiymətlər:", global_qiymetler)

     if not secilenler:
        messagebox.showwarning("Diqqət", "Heç bir benzin növü seçilməyib!")
        
     return
    def log_out(self):
       root.destroy()

      



a = admin(root,admin_var,admin_var2)
a.adminpan()

 






class Food:
    def __init__(self, hot_have, burger_have, kartof_have, cola_have,
                 hot_text, burger_text, kartof_text, cola_text):
        
        self.hot_have = hot_have
        self.burger_have = burger_have
        self.kartof_have = kartof_have
        self.cola_have = cola_have
        self.__hot_text = hot_text
        self.__burger_text = burger_text
        self.__kartof_text = kartof_text
        self.__cola_text = cola_text

netice_text = tk.StringVar()
def manat_sec():
    entry_text3.set("")

def litr_sec():
    entry_text2.set("")



def benzin_secimi_et(event):
    global global_qiymetler
    secim = benzin_var.get()
    if secim in global_qiymetler:
        entry_text1.set(str(global_qiymetler[secim]))


class Cafe:
    def __init__(self, entry_text1, entry_text2, entry_text3, benzin_var1, label_text):
        self.entry_text1 = entry_text1
        self.entry_text2 = entry_text2
        self.entry_text3 = entry_text3
        self.benzin_var1 = benzin_var1
        self.label_text = label_text
    def hesablaz(self):
     qiymet = float(self.entry_text1.get())  
     secim1 = self.benzin_var1.get()   
     try:
       
         #litri tapmag ucun
         if secim1 == "Manat":
            manat = float(self.entry_text2.get())
            litr = manat // qiymet
            self.label_text.set(f"{litr} L")
            #manati tapmag ucun
         elif secim1 == "Litr":
          litr = float(self.entry_text3.get())
          manat  = litr * qiymet
          self.label_text.set(f"{manat}AZN")
          tk.Label(root, textvariable=manat)
         else:
          self.label_text.set("0 AZN")
     except ValueError:
      self.label_text.set("0 AZN")

cafe = Cafe(entry_text1, entry_text2, entry_text3, benzin_var1, label_text)



def hesablak():
    try:
     if hot_have.get() == True and int(label_text1.get()) > 0:
         toplam_hotdog = int(label_text1.get()) * float(hot_text.get())
     else:
         toplam_hotdog = 0

     if burger_have.get() == True and int(label_text2.get()) > 0:
         toplam_burger = int(label_text2.get()) * float(burger_text.get())
     else:
         toplam_burger = 0

     if kartof_have.get() == True and int(label_text3.get()) > 0:
         toplam_kartof = int(label_text3.get()) * float(kartof_text.get())
     else:
         toplam_kartof = 0

     if cola_have.get() == True and int(label_text4.get()) > 0:
         toplam_cola = int(label_text4.get()) * float(cola_text.get())
     else:
         toplam_cola = 0
    except ValueError:
     messagebox.showinfo("Error","Eded daxil edin")
    sum_text = toplam_burger + toplam_cola + toplam_hotdog + toplam_kartof
    netice_text.set(f"{sum_text} AZN")
def check_select():
         if hot_have.get() == True:
          button1.config(state="normal")
          button2.config(state="disabled")
          button3.config(state="disabled")
          button4.config(state="disabled")

         elif burger_have.get():
          button2.config(state="normal")
          button1.config(state="disabled")
          button3.config(state="disabled")
          button4.config(state="disabled")
    
         elif kartof_have.get():
          button3.config(state="normal")
          button1.config(state="disabled")
          button2.config(state="disabled")
          button4.config(state="disabled")

         elif cola_have.get():
          button4.config(state="normal")
          button1.config(state="disabled")
          button2.config(state="disabled")
          button3.config(state="disabled")

        



   



def umumi_mebleg(): 
 
 try:
    
    yanacaq_mebleg = entry_text3.get()
    kafe_mebleg = netice_text.get()
    yanacaq_mebleg2 = entry_text2.get()
    
    if yanacaq_mebleg == "":
        yanacaq_mebleg = 0
        entry_text3.set(0)

    if yanacaq_mebleg2 == "":
        yanacaq_mebleg2 = 0
        entry_text2.set(0)
    x = float(yanacaq_mebleg)
    y = float(kafe_mebleg.split()[0])
    z = float(yanacaq_mebleg2)
    toplam = x + y + z
    return toplam



 except ValueError:
    messagebox.showerror("Xeta","Hesablana bilmedi")






def qebz_penceresi(toplam):
    pencere = tk.Toplevel(root)
    pencere.title("Qəbz")
    pencere.geometry("350x250")
    qebz_nomresi = random.randint(100000,999999)
    tarix = datetime.now().strftime("%d.%m.%Y")
    saat = datetime.now().strftime("%H:%M")
    message = f"""
 BEST OIL
----------------------------------------------
    Tarix: {tarix}
----------------------------------------------
    Saat:  {saat}
----------------------------------------------
    sizin qebz nomreniz: {qebz_nomresi}
----------------------------------------------
    Odenilen mebleg: {toplam}
----------------------------------------------
    Teshekkur edirik bizi secdiyinize gore
----------------------------------------------
    """

    tk.Label(pencere, text=message, font=("Arial", 12), fg="Gray").grid(row=6 , column=20,padx=373)
    qr_code = tk.PhotoImage(file="image.png").subsample(4, 4)
    qr_label = tk.Label(pencere, image=qr_code, bg="white")
    qr_label.image = qr_code 
    qr_label.grid(row=11,column=20,padx=373)
    with open(f"{tarix}", "a") as f:
       f.write(f"{message}")
    

def hesabla_ve_goster():
    cafe.hesablaz()
    hesablak()
    toplam1 = umumi_mebleg()

    #fis cixartma
    tk.Label(root, text=f"Umumi mebleg: {toplam1} AZN", font=("Arial", 12)).place(relx=0.5, rely=0.8, anchor="center")
    if toplam1 is not None:
      if str(toplam1) not in ['" " ', "0", "None"]:
       qebz_penceresi(toplam1)
      else:
       messagebox.showwarning("Xeta", "Ugursuz emeliyyat")
    tk.Label(root,text=toplam1)
 





tk.Label(root, text="Benzin").place(x=27,y=80)
combo = ttk.Combobox(root, textvariable=benzin_var, values=("AI92", "AI95", "AI98", "dizel"), state="readonly")
combo.place(x=97,y=80)
combo.bind("<<ComboboxSelected>>", benzin_secimi_et)

tk.Label(root, text="Qiymet").place(x=25,y=110)
tk.Entry(root, textvariable=entry_text1, state="disabled", width=16).place(x=105,y=112)

tk.Label(root, text="Benzin secimi",font=("Arial",12)).place(x=27,y=40)
tk.Radiobutton(root, text="Manat", variable=benzin_var1, value="Manat", command=manat_sec).place(x=20,y=160)
tk.Entry(root, textvariable=entry_text2, width=10).place(x=125,y=165)
tk.Label(root, text="AZN").place(x=230,y=165)

tk.Radiobutton(root, text="Litr", variable=benzin_var1, value="Litr", command=litr_sec).place(x=25,y=190)
tk.Entry(root, textvariable=entry_text3, width=10).place(x=125,y=194)
tk.Label(root, text="L").place(x=230,y=194)

tk.Button(root, text="Petrol Hesabla", command=cafe.hesablaz).place(x=100,y=250)
tk.Label(root, textvariable=label_text).place(x=100,y=332)

tk.Label(root, text="Kafe Hesabla", font=("Arial", 12)).place(x=600,y=60)

tk.Label(root, text="Mehsul").place(x=600,y=100)
tk.Label(root, text="Qiymet").place(x=740,y=100)
tk.Label(root, text="Eded").place(x=880,y=100)

tk.Checkbutton(root, text="Hot-Dog", variable=hot_have,command=check_select).place(x=600,y=130)
tk.Entry(root, textvariable=hot_text, state="disabled", width=10).place(x=740,y=133)
button1 = tk.Entry(root, textvariable=label_text1, width=10)
button1.place(x=880,y=132)

tk.Checkbutton(root, text="Burger", variable=burger_have,command=check_select).place(x=600,y=160)
tk.Entry(root, textvariable=burger_text, state="disabled", width=10).place(x=740,y=163)
button2 = tk.Entry(root, textvariable=label_text2, width=10)
button2.place(x=880,y=162)

tk.Checkbutton(root, text="Kartof-Fri", variable=kartof_have,command=check_select).place(x=600,y=190)
tk.Entry(root, textvariable=kartof_text, state="disabled", width=10).place(x=740,y=193)


button3 = tk.Entry(root, textvariable=label_text3, width=10,)
button3.place(x=880,y=192)

tk.Checkbutton(root, text="Coca-Cola", variable=cola_have,command=check_select).place(x=600,y=220)
tk.Entry(root, textvariable=cola_text, state="disabled", width=10).place(x=740,y=223)
button4 = tk.Entry(root, textvariable=label_text4, width=10)
button4.place(x=880,y=222)

tk.Button(root, text="Kafe Hesabla", command=hesablak).place(x=813,y=272)
tk.Label(root, textvariable=netice_text).place(x=833,y=322)





tk.Button(root, text="Umumi hesabla", command=hesabla_ve_goster).place(x=503,y=382)


tk.mainloop()