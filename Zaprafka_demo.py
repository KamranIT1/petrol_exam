import tkinter as tk
from tkinter import *
from datetime import datetime
from tkinter import ttk
from tkinter import messagebox
import random


root = tk.Tk()
header = tk.Frame(root, bg="darkblue", height=40)
header.grid(columnspan=10)
tk.Label(header, text="Best Oil", bg="darkblue", fg="white", font=("Arial", 14, "bold"),width=120).grid(row=5,column=20)
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
entry_text1 = tk.StringVar()
entry_text2 = tk.StringVar()
entry_text3 = tk.StringVar()
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

        self.my_frame = tk.Frame(self.root)
        self.my_frame.grid(row=3, column=9, padx=10, pady=10)
        


    def yoxla(self):
        self.my_frame = tk.Frame(self.root)
        self.my_frame.grid(row=3, column=9)
        tk.Label(self.root,text="Setting").grid(row=1,padx=300,column=9)

        tk.Button(self.my_frame, text="Admin Panel",command=self.show_login).grid(row=0, column=0, pady=10)
    def check_login(self):
        try:
            with open("admin.txt", "r") as f:
                files = f.readlines()
            username = files[0].strip()
            password = files[1].strip()

            if self.admin_var.get() != username or self.admin_var2.get() != password:
                raise NameError
        except NameError:
            messagebox.showerror("Xeta", "Yanlis username ve ya sifre")
        else:
            messagebox.showinfo("INFO", "Login succesfull")



    def show_login(self):
     second_root = tk.Toplevel(self.root)
     second_root.title("Admin Panel")
     tk.Label(second_root, text="Username").grid(row=0, column=0, padx=500)
     tk.Entry(second_root, textvariable=self.admin_var).grid(row=1, column=0, padx=500)

     tk.Label(second_root, text="Password").grid(row=2, column=0, padx=500)
     tk.Entry(second_root, textvariable=self.admin_var2, show="*").grid(row=3, column=0, padx=500)


     tk.Button(second_root, text="Daxil ol", command=self.check_login).grid(row=4, column=0, pady=5,padx=500)

app = admin(root,admin_var,admin_var2)
app.yoxla()




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
    secim = benzin_var.get()
    if secim == "AI92":
        entry_text1.set("1.10")
    elif secim == "AI95":
        entry_text1.set("1.60")
    elif secim == "AI98":
        entry_text1.set("2.30")
    elif secim == "dizel":
        entry_text1.set("1.00")

class Cafe:
    def __init__(self, entry_text1, entry_text2, entry_text3, benzin_var1, label_text):
        self.entry_text1 = entry_text1
        self.entry_text2 = entry_text2
        self.entry_text3 = entry_text3
        self.benzin_var1 = benzin_var1
        self.label_text = label_text
    def hesablaz(self):
     try:
         qiymet = float(self.entry_text1.get())  
         secim1 = self.benzin_var1.get()          
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
             raise ValueError
     except ValueError:
      messagebox.showerror("Xeta","secim edin")
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


def umumi_mebleg(): 
 
 try:
    
    yanacaq_mebleg = entry_text3.get()
    kafe_mebleg = netice_text.get()
    yanacaq_mebleg2 = entry_text2.get()
    
    if yanacaq_mebleg == '':
        yanacaq_mebleg = 0
        entry_text3.set(0)

    if yanacaq_mebleg2 == '':
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
    tk.Label(root, text=f"Umumi mebleg: {toplam1} AZN", font=("Arial", 12)).grid(row=8, column=6)
    if toplam1 is not None:
      if str(toplam1) not in ['" " ', "0", "None"]:
       qebz_penceresi(toplam1)
      else:
       messagebox.showwarning("Xeta", "Ugursuz emeliyyat")
    tk.Label(root,text=toplam1)
 





tk.Label(root, text="Benzin").grid(row=1, column=0, pady=5, padx=5)
combo = ttk.Combobox(root, textvariable=benzin_var, values=("AI92", "AI95", "AI98", "dizel"), state="readonly")
combo.grid(row=1, column=1, padx=5)
combo.bind("<<ComboboxSelected>>", benzin_secimi_et)

tk.Label(root, text="Qiymet").grid(row=2, column=0, padx=5, pady=2)
tk.Entry(root, textvariable=entry_text1, state="disabled", width=16).grid(row=2, column=1)

tk.Label(root, text="Benzin secimi",font=("Arial",12)).grid(row=3, column=0, columnspan=2, pady=5)

tk.Radiobutton(root, text="Manat", variable=benzin_var1, value="Manat", command=manat_sec).grid(row=4, column=0)
tk.Entry(root, textvariable=entry_text2, width=10).grid(row=4, column=1)
tk.Label(root, text="AZN").grid(row=4, column=0,columnspan=6)

tk.Radiobutton(root, text="Litr", variable=benzin_var1, value="Litr", command=litr_sec).grid(row=5, column=0)
tk.Entry(root, textvariable=entry_text3, width=10).grid(row=5, column=1)
tk.Label(root, text="L").grid(row=5, column=0,columnspan=6)

tk.Button(root, text="Petrol Hesabla", command=cafe.hesablaz).grid(row=6, column=1, pady=5)
tk.Label(root, textvariable=label_text).grid(row=7, column=1, pady=5)

tk.Label(root, text="Kafe Hesabla", font=("Arial", 12)).grid(row=8, column=0, pady=10)

tk.Label(root, text="Mehsul").grid(row=9, column=0)
tk.Label(root, text="Qiymet").grid(row=9, column=1)
tk.Label(root, text="Eded").grid(row=9, column=2)

tk.Checkbutton(root, text="Hot-Dog", variable=hot_have).grid(row=10, column=0)
tk.Entry(root, textvariable=hot_text, state="disabled", width=10).grid(row=10, column=1)
tk.Entry(root, textvariable=label_text1, width=10).grid(row=10, column=2)
tk.Checkbutton(root, text="Burger", variable=burger_have).grid(row=11, column=0)
tk.Entry(root, textvariable=burger_text, state="disabled", width=10).grid(row=11, column=1)
tk.Entry(root, textvariable=label_text2, width=10).grid(row=11, column=2)

tk.Checkbutton(root, text="Kartof-Fri", variable=kartof_have).grid(row=12, column=0)
tk.Entry(root, textvariable=kartof_text, state="disabled", width=10).grid(row=12, column=1)

tk.Entry(root, textvariable=label_text3, width=10).grid(row=12, column=2)

tk.Checkbutton(root, text="Coca-Cola", variable=cola_have).grid(row=13, column=0)
tk.Entry(root, textvariable=cola_text, state="disabled", width=10).grid(row=13, column=1)
tk.Entry(root, textvariable=label_text4, width=10).grid(row=13, column=2)

tk.Button(root, text="Kafe Hesabla", command=hesablak).grid(row=14, column=1, pady=10)
tk.Label(root, textvariable=netice_text).grid(row=15, column=1)



tk.Button(root, text="Umumi hesabla", command=hesabla_ve_goster).grid(row=16, column=1, pady=15)


tk.mainloop()