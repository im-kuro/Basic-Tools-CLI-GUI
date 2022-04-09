# NMAP GUI MADE BY @im-kuro


import tkinter, subprocess
from tkinter import messagebox
from tkinter import *
from PIL import ImageTk, Image  

# setting basic looks 
top = Tk()
top.title("Common tools GUI -- TT: @dev_kuro GH: @im-kuro -- When running tool may seem unresponsive.")
top.geometry("800x500")

# When a user clicks the get help button on the menue
def get_help():
    messagebox.showinfo( "Report a Bug", "If you would like to report a bug please email im.kuro.business@gmail.com")

# exits the program with the button on top right
def close_app():
    exi = messagebox.askyesno( "Confirm Exit?", "[!] Are you sure you want to exit the program?")
    if exi == True:
        exit(0)
    else:
        pass
    
# module for linux (in works)
def linux_module():
    linux_frame = Frame(top)
    linux_frame = tkinter.Canvas(top,width = 2000,height = 5040, bg="red")
    linux_frame.pack()

    lin_nmap_frame = Frame(linux_frame)
    lin_nmap_frame = tkinter.Canvas(top,width = 2000,height = 5040, bg="red")

    lin_gobuster_frame = Frame(linux_frame)
    lin_gobuster_frame = tkinter.Canvas(top,width = 2000,height = 5040, bg="blue")

    lin_hashcat_frame = Frame(linux_frame)
    lin_hashcat_frame = tkinter.Canvas(top,width = 2000,height = 5040, bg="pink")

    network_frame = Frame(linux_frame) 
    network_frame = tkinter.Canvas(top,width = 800,height = 500, bg="blue")

    linux_frame.create_text(380, 100, text="Welcome to Kuro's Swiss Army Knife", fill="black", font=('Helvetica 27 bold'))
    linux_frame.create_text(380, 140, text="H4CK1NG GUI", fill="green", font=('Helvetica 30 bold'))
    img= (Image.open(r"mylogo.jpg"))   
    resized_image = img.resize((250,260), Image.ANTIALIAS)
    new_image= ImageTk.PhotoImage(resized_image)
    linux_frame.create_image(260,180, anchor=NW, image=new_image)
    def lin_nmap_module():
        def simple_nmap():
            tar = target.get()
            res = subprocess.check_output(f"nmap {tar}", shell=True)
            messagebox.showinfo( "Results", res)

        def simple_secret():
            tar = target.get()
            x = messagebox.askyesno( "Are you sure you want to continue? - [!] May seem unresponsive when runnning [!]", f"This may take a while because of the command. (~$ nmap -T1 {tar})")
            if x == True:
                res = subprocess.check_output(f"nmap -T1 {tar}", shell=True)
                messagebox.showinfo( "Results", res)
            elif x == False:
                return None

        def adv_secret():
            tar = target.get()
            x = messagebox.askyesno( "Are you sure you want to continue? - [!] May seem unresponsive when runnning [!]", f"This may take a while because of the command. (~$ sudo nmap -T1 -sU -sT {tar}). \nThis command also requrires root privlages, did you run with sudo?")
            if x == True:
                res = subprocess.check_output(f"sudo nmap -T1 -sU -sT {tar}", shell=True)
                messagebox.showinfo( "Results", res)
            elif x == False:
                return None
        def loud_hard():
            tar = target.get()
            x = messagebox.askyesno( "Are you sure you want to continue? - [!] May seem unresponsive when runnning [!]", f"This may take a while because of the command. (~$ sudo nmap -T5 -sU -sT -O {tar}). \nThis command also requrires root privlages, did you run with sudo?")
            if x == True:
                res = subprocess.check_output(f"sudo nmap -T5 -sU -sT -O {tar}", shell=True)
                messagebox.showinfo( "Results", res)
            elif x == False:
                return None
        def os_det():
            tar = target.get()
            x = messagebox.askyesno( "Are you sure you want to continue? - [!] May seem unresponsive when runnning [!]", f"This may take a while because of the command. (~$ sudo nmap -O {tar}). \nThis command also requrires root privlages, did you run with sudo?")
            if x == True:
                res = subprocess.check_output(f"sudo nmap -O {tar}", shell=True)
                messagebox.showinfo( "Results", res)
            elif x == False:
                return None
        def simple_fast_scan():
            tar = target.get()
            x = messagebox.askyesno( "Are you sure you want to continue? - [!] May seem unresponsive when runnning [!]", f"This may take a while because of the command. (~$ sudo nmap -F {tar}). \nThis command also requrires root privlages, did you run with sudo?")
            if x == True:
                res = subprocess.check_output(f"sudo nmap -F {tar}", shell=True)
                messagebox.showinfo( "Results", res)
            elif x == False:
                return None
        def loud_mass_scan():
            tar = target.get()
            x = messagebox.askyesno( "Are you sure you want to continue?  - [!] May seem unresponsive when runnning [!]", f"This may take a while because of the command. (~$ sudo nmap -T5 -sV -O -sU -sT -v -sA {tar}). \nThis command also requrires root privlages, did you run with sudo?")
            if x == True:
                res = subprocess.check_output(f"sudo nmap -T5 -sV -O -sU -sT -v -sA {tar}", shell=True)
                messagebox.showinfo( "Results", res)
            elif x == False:
                return None
        def firewall_scan():
            tar = target.get()
            x = messagebox.askyesno( "Are you sure you want to continue?  - [!] May seem unresponsive when runnning [!]" , f"This may take a while because of the command. (~$ sudo nmap -sA {tar}). \nThis command also requrires root privlages, did you run with sudo?")
            if x == True:
                res = subprocess.check_output(f"sudo nmap -sA {tar}", shell=True)
                messagebox.showinfo( "Results", res)
            elif x == False:
                return None
        def Null_Fin_xmas_snan():
            tar = target.get()
            x = messagebox.askyesno( "Are you sure you want to continue?  - [!] May seem unresponsive when runnning [!]", f"This may take a while because of the command. (~$ sudo nmap -sN -sF -sX {tar}). \nThis command also requrires root privlages, did you run with sudo?")
            if x == True:
                res1 = subprocess.check_output(f"sudo nmap -sF {tar}", shell=True)
                res2 = subprocess.check_output(f"sudo nmap -sX {tar}", shell=True)
                res3 = subprocess.check_output(f"sudo nmap -sN {tar}", shell=True)
                messagebox.showinfo( "Results", res1)
                messagebox.showinfo( "Results", res2)
                messagebox.showinfo( "Results", res3)
            elif x == False:
                return None
        def stealth_scan():
            tar = target.get()
            x = messagebox.askyesno( "Are you sure you want to continue?  - [!] May seem unresponsive when runnning [!]", f"This may take a while because of the command. (~$ sudo nmap -sS {tar}). \nThis command also requrires root privlages, did you run with sudo?")
            if x == True:
                res1 = subprocess.check_output(f"sudo nmap -sS {tar}", shell=True)
                messagebox.showinfo( "Results", res1)
            elif x == False:
                return None
        def simple_nmap_pn():
            tar = target.get()
            res = subprocess.check_output(f"nmap -Pn {tar}", shell=True)
            messagebox.showinfo( "Results", res)


        linux_frame.forget()
        lin_gobuster_frame.forget()
        lin_hashcat_frame.forget()
        network_frame.forget()
        
        lin_nmap_frame.pack()


        button1 = tkinter.Button(text='Run simple nmap scan', command=simple_nmap)
        button2 = tkinter.Button(text='Run simple secret scan', command=simple_secret)
        button3 = tkinter.Button(text='Run advanced secret scan', command=adv_secret)
        button4 = tkinter.Button(text='Run Loud and Hard scan', command=loud_hard)
        button5 = tkinter.Button(text='Run OS Detetion scan', command=os_det)
        button6 = tkinter.Button(text='Run simple fast scan', command=simple_fast_scan)
        button7 = tkinter.Button(text='Run loud and mass scan', command=loud_mass_scan)
        button8 = tkinter.Button(text='Scan for firewall', command=firewall_scan)
        button9 = tkinter.Button(text='Scan a firewall for vulns', command=Null_Fin_xmas_snan)
        button10 = tkinter.Button(text='Run a stealthy scan', command=stealth_scan)
        target = tkinter.Entry(lin_nmap_frame, width=40)



        lin_nmap_frame.create_window(280, 140, window=button1)
        lin_nmap_frame.create_window(280, 180, window=button2)
        lin_nmap_frame.create_window(280, 220, window=button3)
        lin_nmap_frame.create_window(280, 260, window=button4)
        lin_nmap_frame.create_window(280, 300, window=button5)
        lin_nmap_frame.create_window(280, 340, window=button6)
        lin_nmap_frame.create_window(480, 140, window=button7)
        lin_nmap_frame.create_window(480, 180, window=button8)
        lin_nmap_frame.create_window(480, 220, window=button9)
        lin_nmap_frame.create_window(480, 260, window=button10)
        lin_nmap_frame.create_window(380, 50, window=target)
    

        # -Pn  commands
        pnbutton1 = tkinter.Button(text='Run simple nmap scan', command=simple_nmap)
        lin_nmap_frame.create_window(280, 140, window=pnbutton1)


    def lin_gobuster_module():
        # sets commands for module
        def basic_brute():
            tar = target.get()
            word = wordlist.get()
            path = path_to_gobuster.get()
            x = messagebox.askyesno( "Are you sure you want to continue?  - [!] May seem unresponsive when runnning [!]", f"This may take a while because of the command. (~$ gobuster dir -w {wordlist} -u {tar}). \nThis command also requrires root privlages, did you run with sudo?")
            if x == True:
                res1 = subprocess.check_output(f"gobuster dir -w {word} -u {tar}", shell=True, cwd=path)
                messagebox.showinfo( "Results", res1)
            elif x == False:
                return None
        def gobuter_scan_adv():
            tar = target.get()
            word = wordlist.get()
            x = messagebox.askyesno( "Are you sure you want to continue?  - [!] May seem unresponsive when runnning [!]", f"This may take a while because of the command. (~$ gobuster dir -w {wordlist} -u {tar}). \nThis command also requrires root privlages, did you run with sudo?")
            if x == True:
                res1 = subprocess.check_output(f"gobuster dir -w {word} -u {tar}", shell=True)
                messagebox.showinfo( "Results", res1)
            elif x == False:
                return None
        # end of commands for module
        
        # forgets any other frames and packs the gobuster frame
        lin_nmap_frame.forget() 
        lin_hashcat_frame.forget()
        lin_nmap_frame.forget()
        network_frame.forget()

        lin_gobuster_frame.pack()

        target = tkinter.Entry(top, width=30,)
        wordlist = tkinter.Entry(top, width=50)
        path_to_gobuster = tkinter.Entry(top, width=60)

        lin_gobuster_frame.create_window(270, 50, window=target)
        lin_gobuster_frame.create_window(550, 50, window=wordlist)
        lin_gobuster_frame.create_window(400, 90, window=path_to_gobuster)

        target.insert(0, "Target")
        wordlist.insert(0, "Wordlist Path")
        path_to_gobuster.insert(0, "Path To Gobuster Dir")

        button1 = tkinter.Button(text='Run simple gobuster scan', command=basic_brute, width=90)
        button2 = tkinter.Button(text='Run advanced gobuster scan', command=gobuter_scan_adv, width=90)

        lin_gobuster_frame.create_window(400, 170, window=button1)
        lin_gobuster_frame.create_window(400, 210, window=button2)
        lin_gobuster_frame.mainloop()
    def lin_hashcat_module():
        # sets commands for module
        def basic_attack():
            tar = target.get()
            word = wordlist.get()
            path = path_to_gobuster.get()
            x = messagebox.askyesno( "Are you sure you want to continue?  - [!] May seem unresponsive when runnning [!]", f"This may take a while because of the command. (~$ gobuster dir -w {wordlist} -u {tar}). \nThis command also requrires root privlages, did you run with sudo?")
            if x == True:
                res1 = subprocess.check_output(f"gobuster dir -w {word} -u {tar}", shell=True, cwd=path)
                messagebox.showinfo( "Results", res1)
            elif x == False:
                return None
        def adv_attack():
            tar = target.get()
            word = wordlist.get()
            x = messagebox.askyesno( "Are you sure you want to continue?  - [!] May seem unresponsive when runnning [!]", f"This may take a while because of the command. (~$ gobuster dir -w {wordlist} -u {tar}). \nThis command also requrires root privlages, did you run with sudo?")
            if x == True:
                res1 = subprocess.check_output(f"gobuster dir -w {word} -u {tar}", shell=True)
                messagebox.showinfo( "Results", res1)
            elif x == False:
                return None
        # end of commands for module
        
        # forgets any other frames and packs the gobuster frame
        lin_gobuster_frame.forget()
        lin_nmap_frame.forget()
        linux_frame.forget()
        network_frame.forget()
        lin_hashcat_frame.pack()

        target = tkinter.Entry(top, width=30,)
        wordlist = tkinter.Entry(top, width=50)
        path_to_gobuster = tkinter.Entry(top, width=60)

        lin_hashcat_frame.create_window(270, 50, window=target)
        lin_hashcat_frame.create_window(550, 50, window=wordlist)
        lin_hashcat_frame.create_window(400, 90, window=path_to_gobuster)

        target.insert(0, "Target")
        wordlist.insert(0, "Wordlist Path")
        path_to_gobuster.insert(0, "Path To Gobuster Dir")

        button1 = tkinter.Button(text='Run simple hashcat attack', command=basic_attack, width=90)
        button2 = tkinter.Button(text='Run advanced hashcat attack', command=adv_attack, width=90)

        lin_hashcat_frame.create_window(400, 170, window=button1)
        lin_hashcat_frame.create_window(400, 210, window=button2)
        lin_hashcat_frame.mainloop()

    def network_module():
        def ping_a_ip():
            tar = target.get()
            res1 = subprocess.check_output(f"ping {tar}", shell=True)
            messagebox.showinfo( "Results", res1)
        def ifconfig():
            res1 = subprocess.check_output(f"ipconfig", shell=True)
            messagebox.showinfo( "Results", res1)
        def show_interfaces():
            res1 = subprocess.check_output(f"netsh interface show interface", shell=True)
            messagebox.showinfo( "Results", res1)   

        lin_gobuster_frame.forget()
        lin_nmap_frame.forget()
        linux_frame.forget()
        lin_hashcat_frame.forget()

        network_frame.pack()
        
        target = tkinter.Entry(top, width=50,)
        button1 = tkinter.Button(text='ping a target', command=ping_a_ip, width=40)
        button2 = tkinter.Button(text='Run ipconfig', command=ifconfig, width=40)
        button3 = tkinter.Button(text='Show active network interfaces', command=show_interfaces, width=40)

        network_frame.create_window(390, 50, window=target)
        network_frame.create_window(400, 170, window=button1)
        network_frame.create_window(400, 205, window=button2)
        network_frame.create_window(400, 240, window=button3)

        target.insert(0, "ping ip")

        network_frame.mainloop()

    

    # exit button on top right
    exit_button = tkinter.Button(top, text ="exit", command=close_app, width=10)
    exit_button.place(x=700)  

    menubar = Menu(linux_frame)

    filemenu = Menu(menubar, tearoff=0)

    filemenu.add_command(label="Nmap Dashboard", command=lin_nmap_module)
    filemenu.add_command(label="Gobuster Dashboard", command=lin_gobuster_module)
    filemenu.add_command(label="Hashcat Dashboard", command=lin_hashcat_module)
    filemenu.add_command(label="Network Config", command=network_module)
    filemenu.add_separator()
    filemenu.add_command(label="Get Help/Report Bug", command=get_help)
    filemenu.add_command(label="Exit", command=top.quit)
    menubar.add_cascade(label="More Tools", menu=filemenu)

    editmenu = Menu(menubar, tearoff=0)
    top.config(menu=menubar)
    linux_frame.mainloop()
    
    """ END OF LINUX MODULE"""

# windows module
def windows_module():  
    # sets basic info for the windows main frame  
    windows_frame = Frame(top)
    windows_frame = tkinter.Canvas(top,width = 800,height = 500, bg="red")    
    windows_frame.pack()
    # sets frames for other tools (nmap, gobuster ect.) but does not pack them
    gobuster_frame = Frame(windows_frame)
    gobuster_frame = tkinter.Canvas(top,width = 800,height = 500, bg="red")
    
    nmap_frame = Frame(windows_frame)
    nmap_frame = tkinter.Canvas(top,width = 800,height = 500, bg="red")
    
    network_frame = Frame(windows_frame) 
    network_frame = tkinter.Canvas(top,width = 800,height = 500, bg="blue")

    # front page with text and picture
    windows_frame.create_text(380, 100, text="Welcome to Kuro's Swiss Army Knife", fill="black", font=('Helvetica 20 bold'))
    windows_frame.create_text(380, 140, text="H4CK1NG GUI", fill="green", font=('Helvetica 30 bold'))
    img= (Image.open(r"mylogo.jpg"))   
    resized_image = img.resize((250,260), Image.ANTIALIAS)
    new_image= ImageTk.PhotoImage(resized_image)
    windows_frame.create_image(260,180, anchor=NW, image=new_image)

    # nmap module for windows
    def nmap_win_module():
        # commands for tool
        def simple_nmap():
            tar = target.get()
            x = messagebox.askyesno( "Are you sure you want to continue? - [!] May seem unresponsive when runnning [!]", f"This may take a while because of the command. (~$ nmap {tar})")
            print(f"Starting scan on {tar}")
            if x == True:
                res = subprocess.check_output(f"nmap {tar}", shell=True)
                messagebox.showinfo( "Results", res)
            elif x == False:
                return None
        def simple_secret():
            tar = target.get()
            x = messagebox.askyesno( "Are you sure you want to continue? - [!] May seem unresponsive when runnning [!]", f"This may take a while because of the command. (~$ nmap -T1 {tar})")
            if x == True:
                res = subprocess.check_output(f"nmap -T1 {tar}", shell=True)
                messagebox.showinfo( "Results", res)
            elif x == False:
                return None
        def adv_secret():
            tar = target.get()
            x = messagebox.askyesno( "Are you sure you want to continue? - [!] May seem unresponsive when runnning [!]", f"This may take a while because of the command. (~$ nmap -T1 -sU -sT {tar}). \nThis command also requrires root privlages, did you run with sudo?")
            if x == True:
                res = subprocess.check_output(f"nmap -T1 -sU -sT {tar}", shell=True)
                messagebox.showinfo( "Results", res)
            elif x == False:
                return None
        def loud_hard():
            tar = target.get()
            x = messagebox.askyesno( "Are you sure you want to continue? - [!] May seem unresponsive when runnning [!]", f"This may take a while because of the command. (~$ nmap -T5 -sU -sT -O {tar}). \nThis command also requrires root privlages, did you run with sudo?")
            if x == True:
                print("starting scan")
                res = subprocess.check_output(f"nmap -T5 -sU -sT -O {tar}", shell=True)
                
                messagebox.showinfo( "Results", res)
            elif x == False:
                return None
        def os_det():
            tar = target.get()
            x = messagebox.askyesno( "Are you sure you want to continue? - [!] May seem unresponsive when runnning [!]", f"This may take a while because of the command. (~$ nmap -O {tar}). \nThis command also requrires root privlages, did you run with sudo?")
            if x == True:
                res = subprocess.check_output(f"nmap -O {tar}", shell=True)
                messagebox.showinfo( "Results", res)
            elif x == False:
                return None
        def simple_fast_scan():
            tar = target.get()
            x = messagebox.askyesno( "Are you sure you want to continue? - [!] May seem unresponsive when runnning [!]", f"This may take a while because of the command. (~$ nmap -F {tar}). \nThis command also requrires root privlages, did you run with sudo?")
            if x == True:
                res = subprocess.check_output(f"nmap -F {tar}", shell=True)
                messagebox.showinfo( "Results", res)
            elif x == False:
                return None
        def loud_mass_scan():
            tar = target.get()
            x = messagebox.askyesno( "Are you sure you want to continue?  - [!] May seem unresponsive when runnning [!]", f"This may take a while because of the command. (~$ nmap -T5 -sV -O -sU -sT -v  {tar}). \nThis command also requrires root privlages, did you run with sudo?")
            if x == True:
                res = subprocess.check_output(f"nmap -T5 -sV -O -sU -sT -v  {tar}", shell=True)
                messagebox.showinfo( "Results", res)
            elif x == False:
                return None
        def firewall_scan():
            tar = target.get()
            x = messagebox.askyesno( "Are you sure you want to continue?  - [!] May seem unresponsive when runnning [!]" , f"This may take a while because of the command. (~$ nmap -sA {tar}). \nThis command also requrires root privlages, did you run with sudo?")
            if x == True:
                res = subprocess.check_output(f"nmap -sA {tar}", shell=True)
                messagebox.showinfo( "Results", res)
            elif x == False:
                return None
        def Null_Fin_xmas_snan():
            tar = target.get()
            x = messagebox.askyesno( "Are you sure you want to continue?  - [!] May seem unresponsive when runnning [!]", f"This may take a while because of the command. (~$ nmap -sN -sF -sX {tar}). \nThis command also requrires root privlages, did you run with sudo?")
            if x == True:
                res1 = subprocess.check_output(f"nmap -sF {tar}", shell=True)
                res2 = subprocess.check_output(f"nmap -sX {tar}", shell=True)
                res3 = subprocess.check_output(f"nmap -sN {tar}", shell=True)
                messagebox.showinfo( "Results", res1)
                messagebox.showinfo( "Results", res2)
                messagebox.showinfo( "Results", res3)
            elif x == False:
                return None
        def stealth_scan():
            tar = target.get()
            x = messagebox.askyesno( "Are you sure you want to continue?  - [!] May seem unresponsive when runnning [!]", f"This may take a while because of the command. (~$ nmap -sS {tar}). \nThis command also requrires root privlages, did you run with sudo?")
            if x == True:
                res1 = subprocess.check_output(f"nmap -sS {tar}", shell=True)
                messagebox.showinfo( "Results", res1)
            elif x == False:
                return None
        # end of commands for tool

        # forgets/removes any other frames and packs the frame for the tool, in this case nmap_frame
        windows_frame.forget()
        gobuster_frame.forget()
        network_frame.forget()
        nmap_frame.pack()

        # sets buttons and commands ran when clicked
        button1 = tkinter.Button(text='Run simple nmap scan', command=simple_nmap)
        button2 = tkinter.Button(text='Run simple secret scan', command=simple_secret)
        button3 = tkinter.Button(text='Run advanced secret scan', command=adv_secret)
        button4 = tkinter.Button(text='Run Loud and Hard scan', command=loud_hard)
        button5 = tkinter.Button(text='Run OS Detetion scan', command=os_det)
        button6 = tkinter.Button(text='Run simple fast scan', command=simple_fast_scan)
        button7 = tkinter.Button(text='Run loud and mass scan', command=loud_mass_scan)
        button8 = tkinter.Button(text='Scan for firewall', command=firewall_scan)
        button9 = tkinter.Button(text='Scan a firewall for vulns', command=Null_Fin_xmas_snan)
        button10 = tkinter.Button(text='Run a stealthy scan', command=stealth_scan)    


        nmap_frame.create_window(280, 140, window=button1)
        nmap_frame.create_window(280, 180, window=button2)
        nmap_frame.create_window(280, 220, window=button3)
        nmap_frame.create_window(280, 260, window=button4)
        nmap_frame.create_window(280, 300, window=button5)
        nmap_frame.create_window(280, 340, window=button6)
        nmap_frame.create_window(500, 140, window=button7)
        nmap_frame.create_window(500, 180, window=button8)
        nmap_frame.create_window(500, 220, window=button9)
        nmap_frame.create_window(500, 260, window=button10)
        target = tkinter.Entry(top, width=30,)
        
        nmap_frame.create_window(380, 50, window=target)

        # run the frame
        nmap_frame.mainloop()

    #gobuster module for windows 
    def gobuster_test():
        # sets commands for module
        def basic_brute():
            tar = target.get()
            word = wordlist.get()
            path = path_to_gobuster.get()
            x = messagebox.askyesno( "Are you sure you want to continue?  - [!] May seem unresponsive when runnning [!]", f"This may take a while because of the command. (~$ gobuster dir -w {wordlist} -u {tar}). \nThis command also requrires root privlages, did you run with sudo?")
            if x == True:
                res1 = subprocess.check_output(f"gobuster dir -w {word} -u {tar}", shell=True, cwd=path)
                messagebox.showinfo( "Results", res1)
            elif x == False:
                return None
        def gobuter_scan_adv():
            tar = target.get()
            word = wordlist.get()
            x = messagebox.askyesno( "Are you sure you want to continue?  - [!] May seem unresponsive when runnning [!]", f"This may take a while because of the command. (~$ gobuster dir -w {wordlist} -u {tar}). \nThis command also requrires root privlages, did you run with sudo?")
            if x == True:
                res1 = subprocess.check_output(f"gobuster dir -w {word} -u {tar}", shell=True)
                messagebox.showinfo( "Results", res1)
            elif x == False:
                return None
        # end of commands for module
        


        # forgets any other frames and packs the gobuster frame
        windows_frame.forget() 
        nmap_frame.forget()
        network_frame.forget()
        gobuster_frame.pack()

        target = tkinter.Entry(top, width=30,)
        wordlist = tkinter.Entry(top, width=50)
        path_to_gobuster = tkinter.Entry(top, width=60)

        gobuster_frame.create_window(270, 50, window=target)
        gobuster_frame.create_window(550, 50, window=wordlist)
        gobuster_frame.create_window(400, 90, window=path_to_gobuster)

        target.insert(0, "Target")
        wordlist.insert(0, "Wordlist Path")
        path_to_gobuster.insert(0, "Path To Gobuster Dir")

        button1 = tkinter.Button(text='Run simple gobuster scan', command=basic_brute, width=90)
        button2 = tkinter.Button(text='Run advanced gobuster scan', command=gobuter_scan_adv, width=90)

        gobuster_frame.create_window(400, 170, window=button1)
        gobuster_frame.create_window(400, 210, window=button2)
        gobuster_frame.mainloop()

    def network_checker():
        def ping_a_ip():
            tar = target.get()
            res1 = subprocess.check_output(f"ping {tar}", shell=True)
            messagebox.showinfo( "Results", res1)
        def ifconfig():
            res1 = subprocess.check_output(f"ipconfig", shell=True)
            messagebox.showinfo( "Results", res1)
        def show_interfaces():
            res1 = subprocess.check_output(f"netsh interface show interface", shell=True)
            messagebox.showinfo( "Results", res1)   

        windows_frame.forget() 
        nmap_frame.forget()
        gobuster_frame.forget()

        network_frame.pack()

        target = tkinter.Entry(top, width=50,)
        button1 = tkinter.Button(text='ping a target', command=ping_a_ip, width=40)
        button2 = tkinter.Button(text='Run ipconfig', command=ifconfig, width=40)
        button3 = tkinter.Button(text='Show active network interfaces', command=show_interfaces, width=40)

        network_frame.create_window(390, 50, window=target)
        network_frame.create_window(400, 170, window=button1)
        network_frame.create_window(400, 205, window=button2)
        network_frame.create_window(400, 240, window=button3)

        target.insert(0, "ping ip")

        network_frame.mainloop()

    # menue bar on top left
    menubar = Menu(windows_frame)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Nmap Dashboard", command=nmap_win_module)
    filemenu.add_command(label="Gobuster Dashboard",command=gobuster_test)
    filemenu.add_command(label="Network Center", command=network_checker)
    filemenu.add_command(label="Get Help/Report Bug", command=get_help)
    filemenu.add_separator()

    filemenu.add_command(label="Exit", command=top.quit)
    menubar.add_cascade(label="More Tools", menu=filemenu)
    
    editmenu = Menu(menubar, tearoff=0)
    top.config(menu=menubar)
    # runs frame
    windows_frame.mainloop()    
    
# Menue bar on top left




# checks os and runs module based off os
"""
def check_os():
    system = platform.system()
    try:
        if system == "Linux":
            print("OS DETECTED ==> LINUX")
            linux_module()
        elif system == "Windows":
            print("OS DETECTED ==> WINDOWS")
            windows_module()
        else:
            print("[!] Cant recongnize your OS.")
    except Exception as error_notice:
            print(f"[!] Looks like there was a error with the program, please contact im.kuro.business@gmail.com with the error. ERROR INFO ===> {error_notice}")
"""
linux_module()