# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 23:56:50 2022

@author: Musharaff
"""
import webbrowser as wb
from tkinter import *   
    
win = Tk()## win is a top or parent window
win.geometry("1700x1700")
win.configure(bg="black")
win.title("TKinter Tutor")

def tab1():
    def tab2():
        def back():
            b.destroy()
            c.destroy()
            d.destroy()
            e.destroy()
            f.destroy()
            g.destroy()
            dumy.destroy()
            back.destroy()
            nxt.destroy()
            tab1()
            
        def nxt():
            b.destroy()
            c.destroy()
            d.destroy()
            e.destroy()
            f.destroy()
            g.destroy()
            dumy.destroy()
            back.destroy()
            nxt.destroy()
            nxtpage()
            
        def b_snip():
            def back1():
                label1.destroy()
                #label2.destroy()
                back1.destroy()
                tab2()
            b.destroy()
            c.destroy()
            d.destroy()
            e.destroy()
            f.destroy()
            g.destroy()
            dumy.destroy()
            back.destroy()
            nxt.destroy()
            
            label1=Label(win, text="SYNTAX  --------->       W = Button(master, options)",foreground="white",font=("ROBOTO",25),bg="black")
            #label2=Label(win, text="\n\nOPTIONS\n\n\nactivebackground\nbd\nbg\ncommand\nactiveforeground\nfg\nfont\nheight\nimage\nhiglightcolor\njustify\npadx\npady\nunderline\nwidth\nWraplength\nstate\n\n\n")
            label1.pack()
            #label2.pack()
            
            back1=Button(win, text = "BACK",command=back1,height=2,width=10,foreground="white",font=("ROBOTO",25),bg="black")
            back1.pack()
        
        def c_snip():
            def back2():
                label2.destroy()
                back2.destroy()
                tab2()
            b.destroy()
            c.destroy()
            d.destroy()
            e.destroy()
            f.destroy()
            g.destroy()
            dumy.destroy()
            back.destroy()
            nxt.destroy()
            
            label2=Label(win, text="SYNTAX  --------->       w = CheckButton(master, option=value)",foreground="white",font=("ROBOTO",25),bg="black")
            label2.pack()
            
            back2=Button(win, text = "BACK",command=back2,height=2,width=10,foreground="white",font=("ROBOTO",25),bg="black")
            back2.pack()
            
        def d_snip():
            def back3():
                label3.destroy()
                back3.destroy()
                tab2()
            b.destroy()
            c.destroy()
            d.destroy()
            e.destroy()
            f.destroy()
            g.destroy()
            dumy.destroy()
            back.destroy()
            nxt.destroy()
            
            label3=Label(win, text="SYNTAX  --------->       W = Label(master,options)",foreground="white",font=("ROBOTO",25),bg="black")
            label3.pack()
            
            back3=Button(win, text = "BACK",command=back3,height=2,width=10,foreground="white",font=("ROBOTO",25),bg="black")
            back3.pack()
        
        def e_snip():
            def back4():
                label4.destroy()
                back4.destroy()
                tab2()
            b.destroy()
            c.destroy()
            d.destroy()
            e.destroy()
            f.destroy()
            g.destroy()
            dumy.destroy()
            back.destroy()
            nxt.destroy()
            
            label4=Label(win, text="SYNTAX  --------->      W = Radiobutton(master, options)",foreground="white",font=("ROBOTO",25),bg="black")
            label4.pack()
            
            back4=Button(win, text = "BACK",command=back4,height=2,width=10,foreground="white",font=("ROBOTO",25),bg="black")
            back4.pack()
            
        def f_snip():
            def back5():
                label5.destroy()
                back5.destroy()
                tab2()
            b.destroy()
            c.destroy()
            d.destroy()
            e.destroy()
            f.destroy()
            g.destroy()
            dumy.destroy()
            back.destroy()
            nxt.destroy()
            
            label5=Label(win, text="SYNTAX  --------->      w = Entry(master, option=value)",foreground="white",font=("ROBOTO",25),bg="black")
            label5.pack()
            
            back5=Button(win, text = "BACK",command=back5,height=2,width=10,foreground="white",font=("ROBOTO",25),bg="black")
            back5.pack()
            
        def g_snip():
            def back6():
                label6.destroy()
                back6.destroy()
                tab2()
            b.destroy()
            c.destroy()
            d.destroy()
            e.destroy()
            f.destroy()
            g.destroy()
            dumy.destroy()
            back.destroy()
            nxt.destroy()
            
            label6=Label(win, text="SYNTAX  --------->      W = Message(master,options)",foreground="white",font=("ROBOTO",25),bg="black")
            label6.pack()
            
            back6=Button(win, text = "BACK",command=back6,height=2,width=10,foreground="white",font=("ROBOTO",25),bg="black")
            back6.pack()
            
        def nxtpage():
            def nxtpage2():
                def nxtpage3():
                    def finish():
                        def pro():
                            ll.destroy()
                            pro.destroy()
                            
                            Ll1=Label(win,text="Rock Paper Scissors Game\n",font=25,foreground="white",bg="black")
                            Ll1.pack()
                            Ll2=Label(win,text="Age Calculator App\n",font=25,foreground="white",bg="black")
                            Ll2.pack()
                            Ll3=Label(win,text="Graphical Register and Login\n",font=25,foreground="white",bg="black")
                            Ll3.pack()
                            Ll4=Label(win,text="Pharmacy Management System\n",font=25,foreground="white",bg="black")
                            Ll4.pack()
                            Ll5=Label(win,text="Tic Tac Toe Game\n\n",font=25,foreground="white",bg="black")
                            Ll5.pack()
                            
                            la=Label(win,text="THANK YOU",font=("TIMES_NEW ROMAN",100),foreground="white",bg="black")
                            la.pack()
                            
                            exit_button = Button(win, text="EXIT", command=win.destroy,height=2,width=5,bg="green")
                            exit_button.pack(pady=20)
                        
                        b11.destroy()
                        b12.destroy()
                        b13.destroy()
                        b14.destroy()
                        backl.destroy()
                        finish.destroy()
                        
                        ll=Label(win,text="YOU HAVE SUCCSSFULLY LEARNT TKINTER\n PLEASE TRY OUT SOME PROJECTS\n CLICK PROJECTS BELOW TO EXPLORE THEM\n\n\n",font=("TIMES_NEW_ROMAN",40),foreground="white",bg="black")
                        ll.pack()
                        
                        pro=Button(win , text="PROJECTS",command=pro,height=5,width=50,bg="cyan")
                        pro.pack()                            
                        
                    def backl():
                        b11.destroy()
                        b12.destroy()
                        b13.destroy()
                        b14.destroy()
                        backl.destroy()
                        finish.destroy()
                        nxtpage2()
        
                    url11="https://www.youtube.com/watch?v=FqIKEW-S8W0&list=PL6gx4Cwl9DGBwibXFtPtflztSNPGuIB_d&index=12"
                    url12="https://www.youtube.com/watch?v=IB6VkXJVf0Y&list=PL6gx4Cwl9DGBwibXFtPtflztSNPGuIB_d&index=13"
                    url13="https://www.youtube.com/watch?v=O12aT42okYE&list=PL6gx4Cwl9DGBwibXFtPtflztSNPGuIB_d&index=14"
                    url14="https://www.youtube.com/watch?v=lt78_05hHSk&list=PL6gx4Cwl9DGBwibXFtPtflztSNPGuIB_d&index=15"
                    
                    def onclick3(x):
                        wb.open(x,new=2)
                        
                    b11=Button(win, text = "Python GUI with Tkinter - 11 - Adding the Status Bar",command=lambda: onclick(url11),height=5,width=50,foreground="white",bg="blue")
                    b11.pack()
                    b12=Button(win, text = "Python GUI with Tkinter - 12 - Messagebox",command=lambda: onclick(url12),height=5,width=50,foreground="white",bg="blue")
                    b12.pack()
                    b13=Button(win, text = "Python GUI with Tkinter - 13 - Shapes and Graphics",command=lambda: onclick(url13),height=5,width=50,foreground="white",bg="blue")
                    b13.pack()
                    b14=Button(win, text = "Python GUI with Tkinter - 14 - Images and Icons",command=lambda: onclick(url14),height=5,width=50,foreground="white",bg="blue")
                    b14.pack()
                    
                    backl=Button(win,text="BACK",command=backl,bg="red")
                    backl.pack()
                    
                    finish=Button(win,text="FINISH",command=finish, height=2,width=100,bg="green")
                    finish.pack()
                    
                def nxxxt():
                    b6.destroy()
                    b7.destroy()
                    b8.destroy()
                    b9.destroy()
                    b10.destroy()
                    nxxt.destroy()
                    nxxxt.destroy()
                    backk.destroy()
                    nxtpage3()
                
                def backk():
                    b6.destroy()
                    b7.destroy()
                    b8.destroy()
                    b9.destroy()
                    b10.destroy()
                    nxxt.destroy()
                    nxxxt.destroy()
                    backk.destroy()
                    nxtpage()
                    
                url6="https://www.youtube.com/watch?v=qWnE-yp6wzU&list=PL6gx4Cwl9DGBwibXFtPtflztSNPGuIB_d&index=7"
                url7="https://www.youtube.com/watch?v=XkCbinbgbdw&list=PL6gx4Cwl9DGBwibXFtPtflztSNPGuIB_d&index=8"
                url8="https://www.youtube.com/watch?v=IYHJRnVOFlw&list=PL6gx4Cwl9DGBwibXFtPtflztSNPGuIB_d&index=9"
                url9="https://www.youtube.com/watch?v=PSm-tq5M-Dc&list=PL6gx4Cwl9DGBwibXFtPtflztSNPGuIB_d&index=10"
                url10="https://www.youtube.com/watch?v=D24Vx3_IM8U&list=PL6gx4Cwl9DGBwibXFtPtflztSNPGuIB_d&index=11"
                
                def onclick2(x):
                    wb.open(x,new=2)
                
                b6=Button(win, text = "Python GUI with Tkinter - 6 - Binding Functions to Layouts",command=lambda: onclick2(url6),height=5,width=50,foreground="white",bg="blue")
                b6.pack()
                b7=Button(win, text = "Python GUI with Tkinter - 7 - Mouse Click Events",command=lambda: onclick2(url7),height=5,width=50,foreground="white",bg="blue")
                b7.pack()
                b8=Button(win, text = "Python GUI with Tkinter - 8 - Using Classes",command=lambda: onclick2(url8),height=5,width=50,foreground="white",bg="blue")
                b8.pack()
                b9=Button(win, text = "Python GUI with Tkinter - 9 - Creating Drop Down Menus",command=lambda: onclick2(url9),height=5,width=50,foreground="white",bg="blue")
                b9.pack()
                b10=Button(win, text = "Python GUI with Tkinter - 10 - Creating a Toolbar",command=lambda: onclick2(url10),height=5,width=50,foreground="white",bg="blue")
                b10.pack()
                nxxxt=Button(win, text = "NEXT",command=nxxxt,bg="green")
                nxxxt.pack()
                
                backk=Button(win,text="BACK",command=backk,bg="red")
                backk.pack()
            
                
                
                
            
            
            def nxxt():
                b1.destroy()
                b2.destroy()
                b3.destroy()
                b4.destroy()
                b5.destroy()
                nxxt.destroy()
                bback.destroy()
                l1.destroy()
                nxtpage2()
                
            def bback():
                b1.destroy()
                b2.destroy()
                b3.destroy()
                b4.destroy()
                b5.destroy()
                nxxt.destroy()
                bback.destroy()
                l1.destroy()
                tab1()
                
            b.destroy()
            c.destroy()
            d.destroy()
            e.destroy()
            f.destroy()
            g.destroy()
            dumy.destroy()
            back.destroy()
            nxt.destroy()
            
            l1=Label(win, text="Videos to learn TKinter\n\n\n\n",font=("ROBOTO",20),foreground="white",bg="black")
            l1.pack()
            
            url1="https://www.youtube.com/watch?v=RJB1Ek2Ko_Y&list=PL6gx4Cwl9DGBwibXFtPtflztSNPGuIB_d&index=2" 
            url2="https://www.youtube.com/watch?v=RTM9tiV_HoY&list=PL6gx4Cwl9DGBwibXFtPtflztSNPGuIB_d&index=3"
            url3="https://www.youtube.com/watch?v=Ko4EPJ8DDjg&list=PL6gx4Cwl9DGBwibXFtPtflztSNPGuIB_d&index=4"
            url4="https://www.youtube.com/watch?v=-nmzq3xiZ6I&list=PL6gx4Cwl9DGBwibXFtPtflztSNPGuIB_d&index=5"
            url5="https://www.youtube.com/watch?v=wNBqM28MMjs&list=PL6gx4Cwl9DGBwibXFtPtflztSNPGuIB_d&index=6"
            
           
        
            def onclick(x):
                wb.open(x,new=2)
            
            b1=Button(win, text = "Python GUI with Tkinter - 1 - Introduction",command=lambda: onclick(url1),height=5,width=50,foreground="white",bg="blue")
            b1.pack()
            b2=Button(win, text = "Python GUI with Tkinter - 2 - Organizing your Layout",command=lambda: onclick(url2),height=5,width=50,foreground="white",bg="blue")
            b2.pack()
            b3=Button(win, text = "Python GUI with Tkinter - 3 - Fitting Widgets in your Layout",command=lambda: onclick(url3),height=5,width=50,foreground="white",bg="blue")
            b3.pack()
            b4=Button(win, text = "Python GUI with Tkinter - 4 - Grid Layout",command=lambda: onclick(url4),height=5,width=50,foreground="white",bg="blue")
            b4.pack()
            b5=Button(win, text = "Python GUI with Tkinter - 5 - More on the Grid Layout",command=lambda: onclick(url5),height=5,width=50,foreground="white",bg="blue")
            b5.pack()
            nxxt=Button(win, text = "NEXT",command=nxxt,bg="green")
            nxxt.pack()
            
            bback=Button(win, text = "BACK",command=bback,bg="red")
            bback.pack()
        
        
        title.destroy()
        a.destroy()
        ext_button.destroy()
        l.destroy()

        dumy=Label(win, text = " " ,height=5,width=50,bg="black")
        dumy.grid(row=0,column=0)

        b=Button(win, text = "Button Widget snippet",command=b_snip,height=5,width=50,bg="blue",foreground="white")
        b.grid(row=2,column=2)
        
        c=Button(win, text = "Checkbutton Widget snippet",command=c_snip,height=5,width=50,bg="blue",foreground="white")
        c.grid(row=3,column=2)
        
        d=Button(win, text = "Label Widget snippet",command=d_snip,height=5,width=50,bg="blue",foreground="white")
        d.grid(row=4,column=2)
        
        e=Button(win, text = "Radiobutton Widget snippet",command=e_snip,height=5,width=50,bg="blue",foreground="white")
        e.grid(row=2,column=3)
        
        f=Button(win, text = "Entry Widget snippet",command=f_snip,height=5,width=50,bg="blue",foreground="white")
        f.grid(row=3,column=3)
        
        g=Button(win, text = "Message Widget snippet",command=g_snip,height=5,width=50,bg="blue",foreground="white")
        g.grid(row=4,column=3)
        
        back=Button(win, text = "BACK",command=back,bg="red")
        back.grid(row=5,column=2)
        
        nxt=Button(win, text = "NEXT",command=nxt,bg="green")
        nxt.grid(row=5,column=3)
    
        
    title=Label(win, text="TKINTER TUTOR",font=("ROBOTO",30),height=1,width=15,foreground="white",bg="black" )
    title.pack()
    
    a=Button(win, text = "Learn TKinter",font=("ROBOTO",30),height=4,width=25 ,command=tab2,bg="blue")
    a.pack()
    
    ext_button = Button(win, text="EXIT",font=("TIMES_NEW_ROMAN",10) ,command=win.destroy,bg="blue",height=2,width=5)
    ext_button.pack(pady=20)
    
    l=Label(win,text="Submitted to\n\t Mr.Sridhar S.K sir \n Subtmitted By\n\t\t\tA Mohammed Musharaff\n\t\t  Sachith Naik R.K\n\t\t       P Raghavendra Rao\n\t        Anirvesh M\n\t  Vinod Kumar",foreground="white",font=("ROBOTO",25),bg="black")
    l.pack()
tab1()


  
win.mainloop()  

