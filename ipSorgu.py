import urllib.request
import os
import base64
import datetime
import tkinter as tk
from tkinter import messagebox


os.system('mkdir Output')
dir_path = os.path.dirname(os.path.realpath(__file__))

filename = dir_path + "\\Output\\Data.json"
filename = filename.replace("\\","/")

class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("IP sorgu by r00t025")
        self.geometry("200x100")
        self.resizable(False, False)
        self.create_widgets()

    def create_widgets(self):
        self.ip_label = tk.Label(self, text=" IP addresini gir:")
        self.ip_label.pack(pady=5)

        self.ip_entry = tk.Entry(self)
        self.ip_entry.pack(pady=5)

        self.query_button = tk.Button(self, text="Sorgula", command=self.query)
        self.query_button.pack(pady=5)

    def query(self):
        ip = self.ip_entry.get()
        if ip == "":
            messagebox.showerror("Hata!", "Lütfen bir ip adresi girin")
        elif ip == "owner?":
            messagebox.showinfo("Info", "𝕾𝖔𝖚𝖑𝖋𝖑𝖞 ♡#8509")
        else:
            baseUrl = "http://ip-api.com/json/{}"
            contents = urllib.request.urlopen(baseUrl.format(ip)).read()
            contents = contents.decode("utf-8")
            contents = contents.replace(", Inc",".Inc")
            contents = contents.replace(",Inc",".Inc")
            contents = contents.replace(", inc",".Inc")
            contents = contents.replace(".inc",".Inc")
            contents = contents.replace(",",",\n")
            contents = contents.replace('{','{"reqTime":"' + str(datetime.datetime.now()) + '",\n',1)
            messagebox.showinfo("Info", contents)

            contents = contents + '\n\n'

            data = ''
        
            try:
                with open(filename, "r") as file:
                    data = file.read()
                    fileNotExists = False
            except:
                fileNotExists = True
            
            if fileNotExists:
                data = contents
            else:
                data = contents + data 
    
                
                
                
                
                
                
    
            with open(filename, "w") as file:
                file.write(data)
            file.close






app = Application()
app.mainloop()
