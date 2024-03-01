from tkinter import*
import math,random,os
from tkinter import messagebox
class Bill_App:
    def __init__(self, root):
        self.root=root
        self.root.geometry('1350x700+0+0') 
        self.root.title('Billing software')
        bg_color="#000080"
        title=Label(self.root,text="Billing software",bd=12,relief=GROOVE,bg=bg_color,fg="white",font=("times new roman",30,"bold"),pady=2).pack(fill=X)
        #>>>>>>>>>> varibles <<<<<<<<<<
        self.Soap=IntVar()
        self.Face_cream=IntVar()
        self.Face_wash=IntVar()
        self.Sprey=IntVar()
        self.Gell=IntVar()
        self.Loshan=IntVar()
        
         #>>>>>>>>>> Grocery <<<<<<<<<<
        self.Rise=IntVar()
        self.Food_oil=IntVar()
        self.Dal=IntVar()
        self.Wheat=IntVar()
        self.Sugar=IntVar()
        self.Tea=IntVar()
        
         #>>>>>>>>>> Cold Drink <<<<<<<<<<
        self.maza=IntVar()
        self.coco_cola=IntVar()
        self.fruiti=IntVar()
        self.thambs_up=IntVar()
        self.pepsi=IntVar()
        self.sprite=IntVar()
        
        #>>>>>>>> Total Product Price & Tax Variable <<<<<<<<<<
        self.cosmatic_price=StringVar()
        self.grocery_price=StringVar()
        self.cold_drink_price=StringVar()
        
        self.cosmatic_Tax=StringVar()
        self.grocery_Tax=StringVar()
        self.cold_drink_Tax=StringVar()
        
        #>>>>>>> Costomer <<<<<<
        self.c_name=StringVar()
        self.c_phon=StringVar()
        self.bill_no=StringVar()
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.search_bill=StringVar()
        
        
        
        #=========== customer detail frem
        F1=LabelFrame(self.root,bd=10,relief=GROOVE,text="Customer Details",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F1.place(x=0,y=80,relwidth=1)
        
        
        cname_lbl=Label(F1,text="Customer Name",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=0,padx=20,pady=5)
        cname_text=Entry(F1,width=15,textvariable=self.c_name,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)
        
        cphon_lbl=Label(F1,text="Phone NO",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=3,padx=20,pady=5)
        cphon_text=Entry(F1,width=15,textvariable=self.c_phon,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=4,pady=5,padx=10)
        
        cbill_lbl=Label(F1,text="Bill NO",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=5,padx=20,pady=5)
        cbill_text=Entry(F1,width=15,textvariable=self.search_bill  ,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=6,pady=5,padx=10)
        
        bill_btn=Button(F1,text="search",command=self.find_bill,width=10,bd=7,font="arial 12 bold").grid(row=0,column=7,padx=10,pady=10)
        
        
        
         #>>>>>>>>>>>>Cosmatics Frame<<<<<<<<<<<
        f2=LabelFrame(self.root,bd=10,relief=GROOVE,text="Cosmetics",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        f2.place(x=5,y=180,width=325,height=380)
        
        bath_lbl=Label(f2,text="Bath Soap",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        bath_text=Entry(f2,width=10,textvariable=self.Soap,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)
           
        Face_cream_lbl=Label(f2,text="Face Cream",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        Face_cream_text=Entry(f2,width=10,textvariable=self.Face_cream,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)
          
        Face_w_lbl=Label(f2,text="Face Wash",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        Face_w_text=Entry(f2,width=10,textvariable=self.Face_wash,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)
          
        Hair_s_lbl=Label(f2,text="Hair Spray",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        Hair_s_text=Entry(f2,width=10,textvariable=self.Sprey,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)
         
        Hair_g_lbl=Label(f2,text="Hair Gell",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        Hair_g_text=Entry(f2,width=10,textvariable=self.Gell,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)
                       
        Body_lbl=Label(f2,text="Body Loshan",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        Body_text=Entry(f2,width=10,textvariable=self.Loshan,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)
                
         #>>>>>>>>>>>>Grocery Frame<<<<<<<<<<<
        f3=LabelFrame(self.root,bd=10,relief=GROOVE,text="Grocery",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        f3.place(x=300,y=180,width=325,height=380)
        
        g1_lbl=Label(f3,text="Rise",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        g1_text=Entry(f3,width=10,textvariable=self.Rise,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)
            
        g2_cream_lbl=Label(f3,text="Food oil",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        g2_cream_text=Entry(f3,width=10,textvariable=self.Food_oil,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)
          
        g3_w_lbl=Label(f3,text="Dal",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        g3_w_text=Entry(f3,width=10,textvariable=self.Dal,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)
          
        g4_lbl=Label(f3,text="Wheat",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        g4_text=Entry(f3,width=10,textvariable=self.Wheat,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)
         
        g5_lbl=Label(f3,text="Sugar",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        g5_text=Entry(f3,width=10,textvariable=self.Sugar,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)
                       
        g6_lbl=Label(f3,text="Tea",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        g6_text=Entry(f3,width=10,textvariable=self.Tea,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)
           
        #>>>>>>>>>>>>Cold drink<<<<<<<<<<<<<  
           
        f4=LabelFrame(self.root,bd=10,relief=GROOVE,text="Cold Drinks",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        f4.place(x=630,y=180,width=325,height=380) 
          
        c1_lbl=Label(f4,text="Maza",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        c1_text=Entry(f4,width=10,textvariable=self.maza,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)
            
        c2_lbl=Label(f4,text="Coco_Cola",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        c2_text=Entry(f4,width=10,textvariable=self.coco_cola,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)
          
        c3_lbl=Label(f4,text="Fruiti",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        c3_text=Entry(f4,width=10,textvariable=self.fruiti,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)
          
        c4_lbl=Label(f4,text="Thambs_Up",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        c4_text=Entry(f4,width=10,textvariable=self.thambs_up,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)
         
        c5_lbl=Label(f4,text="Pepsi",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        c5_text=Entry(f4,width=10,textvariable=self.pepsi,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)
                       
        c6_lbl=Label(f4,text="Sprite",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        c6_text=Entry(f4,width=10,textvariable=self.sprite,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)
        
        #>>>>>>>>>>Billing Area<<<<<<<<<<<
        
        F5=Frame(self.root,bd=10,relief=GROOVE)
        F5.place(x=960,y=180,width=320,height=380)
        bill_title=Label(F5,text="Bill Area",font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
        scrol_y=Scrollbar(F5,orient=VERTICAL)
        self.txtarea=Text(F5,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)
        
        #>>>>>>>>>>>ButtonFrame<<<<<<<<<<<<
        F6=LabelFrame(self.root,bd=10,relief=GROOVE,text="Bill Menu",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F6.place(x=0,y=560,relwidth=1,height=140)
        
        m1_lbl=Label(F6,text="Total Cosmatics price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=0,column=0,padx=20,pady=1,sticky="w")
        m1_text=Entry(F6,width=18,textvariable=self.cosmatic_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)
        
        m2_lbl=Label(F6,text="Total Grocery price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=1,column=0,padx=20,pady=1,sticky="w")
        m2_text=Entry(F6,width=18,textvariable=self.grocery_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=1)
        
        m3_lbl=Label(F6,text="Total Cold_drind price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=2,column=0,padx=20,pady=1,sticky="w")
        m3_text=Entry(F6,width=18,textvariable=self.cold_drink_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=1)
        
        c1_lbl=Label(F6,text="Total Cosmatics Tax",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=0,column=2,padx=20,pady=1,sticky="w")
        c1_text=Entry(F6,width=18,textvariable=self.cosmatic_Tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=1)
        
        c2_lbl=Label(F6,text="Total Grocery tax",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=1,column=2,padx=20,pady=1,sticky="w")
        c2_text=Entry(F6,width=18,textvariable=self.grocery_Tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=3,padx=10,pady=1)
        
        c3_lbl=Label(F6,text="Total Cold drind Tax",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=2,column=2,padx=20,pady=1,sticky="w")
        c3_text=Entry(F6,width=18,textvariable=self.cold_drink_Tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=3,padx=10,pady=1)
        
        btn_F=Frame(F6, bd=7,relief=GROOVE)
        btn_F.place(x=750,width=580,height=105)
        
        total_btn=Button(btn_F,command=self.total,text="Total",bg="cadetblue",fg="white",bd=5,pady=15,width=9,font="arial 12 bold").grid(row=0,column=0,padx=7,pady=5)       
        GBill_btn=Button(btn_F,text="Genrate Bill",command=self.bill_area,bg="cadetblue",fg="white",bd=5,pady=15,width=9,font="arial 12 bold").grid(row=0,column=1,padx=7,pady=5)       
        Clear_btn=Button(btn_F,text="Clear",command=self.clear_data,bg="cadetblue",fg="white",bd=5,pady=15,width=9,font="arial 12 bold").grid(row=0,column=2,padx=7,pady=5)       
        Exit_btn=Button(btn_F,text="Exit",command=self.Exit_app,bg="cadetblue",fg="white",bd=5,pady=15,width=9,font="arial 12 bold").grid(row=0,column=3,padx=7,pady=5)       
        self.welcome_bill()
        
    def total(self):
        self.c_s_p=self.Soap.get()*50
        self.c_fc_p=self.Face_cream.get()*130
        self.c_fw_p=self.Face_wash.get()*80
        self.c_hs_p=self.Sprey.get()*200
        self.c_hg_p=self.Gell.get()*150
        self.c_bl_p=self.Loshan.get()*190
        self.total_cosmatic_price=float(
                                     self.c_s_p+
                                     self.c_fc_p+
                                     self.c_fw_p+
                                     self.c_hs_p+
                                     self.c_hg_p+
                                     self.c_bl_p
                                     )
        self.cosmatic_price.set("Rs. "+str(self.total_cosmatic_price))
        self.c_tax=round((self.total_cosmatic_price*0.05),2)
        self.cosmatic_Tax.set("Rs. "+str(self.c_tax))
      
      
        self.g_r_p=self.Rise.get()*110
        self.g_f_p=self.Food_oil.get()*120
        self.g_d_p=self.Dal.get()*80
        self.g_w_p=self.Wheat.get()*240
        self.g_s_p=self.Sugar.get()*45
        self.g_t_p=self.Tea.get()*150
        self.total_grocery_price=(
                                     self.g_r_p+
                                     self.g_f_p+
                                     self.g_d_p+
                                     self.g_w_p+
                                     self.g_s_p+
                                     self.g_t_p
                                     )
        self.grocery_price.set("Rs. "+str(self.total_grocery_price))
        self.g_tax=round((self.total_grocery_price*0.05),2)
        self.grocery_Tax.set("Rs. "+str(self.g_tax))

        
        
        self.d_m_p= self.maza.get()*80
        self.d_c_p= self.coco_cola.get()*90
        self.d_f_p= self.fruiti.get()*85
        self.d_t_p= self.thambs_up.get()*90
        self.d_l_p= self.pepsi.get()*95
        self.d_s_p= self.sprite.get()*95
        self.total_Cold_Drink_price=(
                                     self.d_m_p+
                                     self.d_c_p+
                                     self.d_f_p+
                                     self.d_t_p+
                                     self.d_l_p+
                                     self.d_s_p
                                     )
        self.cold_drink_price.set("Rs. "+str(self.total_Cold_Drink_price))
        self.d_tax=round((self.total_Cold_Drink_price*0.05),2)
        self.cold_drink_Tax.set("Rs. "+str(self.d_tax))
        
        self.Total_bill=float(self.total_cosmatic_price+
                              self.total_grocery_price+
                              self.total_Cold_Drink_price+
                              self.c_tax+
                              self.g_tax+
                              self.d_tax
                            )
        
    def welcome_bill(self):
        self.txtarea.delete('1.0',END)
        self.txtarea.insert(END,"******Welcome To RS Reatail******\n")
        self.txtarea.insert(END,f"\n Bill Number: {self.bill_no.get()}")
        self.txtarea.insert(END,f"\n Customer: {self.c_name.get()}")
        self.txtarea.insert(END,f"\n Phone Number: {self.c_phon.get()} ")
        self.txtarea.insert(END,f"\n==================================")
        self.txtarea.insert(END,f"\n Products\t\tQTY\t    Price")
        self.txtarea.insert(END,f"\n==================================")
        
    def bill_area(self):
        if self.c_name.get()=="" or self.c_phon.get()=="":
            messagebox.showerror("Error","Customer details are must")
        elif self.cosmatic_price.get()=="Rs. 0.0" and self.grocery_price.get()=="Rs. 0.0" and self.cold_drink_price.get()=="Rs. 0.0":
            messagebox.showerror("Error","No Product Purchased")
            
        else:
            self.welcome_bill()
            
            #=============cosmetic==========================
            if self.Soap.get()!=0:
                self.txtarea.insert(END,f"\n Bath Soap\t\t{self.Soap.get()}\t    {self.c_s_p}")
                
            if self.Face_cream.get()!=0:
                self.txtarea.insert(END,f"\n Face Cream\t\t{self.Face_cream.get()}\t    {self.c_fc_p}")
            if self.Face_wash.get()!=0:
                self.txtarea.insert(END,f"\n Face Wash\t\t{self.Face_wash.get()}\t    {self.c_fw_p}")
            if self.Sprey.get()!=0:
                self.txtarea.insert(END,f"\n Spray\t\t{self.Sprey.get()}\t    {self.c_hs_p}")
            if self.Gell.get()!=0:
                self.txtarea.insert(END,f"\n Gell\t\t{self.Gell.get()}\t    {self.c_hg_p}")
            if self.Loshan.get()!=0:
                self.txtarea.insert(END,f"\n Loshan\t\t{self.Loshan.get()}\t    {self.c_bl_p}")
                
            #=============grocery==========================
            if self.Rise.get()!=0:
                self.txtarea.insert(END,f"\n Rice\t\t{self.Rise.get()}\t    {self.g_r_p}") 
            if self.Food_oil.get()!=0:
                self.txtarea.insert(END,f"\n Food Oil\t\t{self.Food_oil.get()}\t    {self.g_f_p}")
            if self.Dal.get()!=0:
                self.txtarea.insert(END,f"\n Daal\t\t{self.Dal.get()}\t    {self.g_d_p}")
            if self.Wheat.get()!=0:
                self.txtarea.insert(END,f"\n Wheat\t\t{self.Wheat.get()}\t    {self.g_w_p}")
            if self.Sugar.get()!=0:
                self.txtarea.insert(END,f"\n Sugar\t\t{self.Sugar.get()}\t    {self.g_s_p}")
            if self.Tea.get()!=0:
                self.txtarea.insert(END,f"\n Tea\t\t{self.Tea.get()}\t    {self.g_t_p}")
                
            #=============cold drinks==========================
            if self.maza.get()!=0:
                self.txtarea.insert(END,f"\n Maza\t\t{self.Soap.get()}\t    {self.d_m_p}")   
            if self.coco_cola.get()!=0:
                self.txtarea.insert(END,f"\n Coca Cola\t\t{self.Face_cream.get()}\t    {self.d_c_p}")
            if self.fruiti.get()!=0:
                self.txtarea.insert(END,f"\n Frooti\t\t{self.fruiti.get()}\t    {self.d_f_p}")
            if self.thambs_up.get()!=0:
                self.txtarea.insert(END,f"\n Thumbs Up\t\t{self.thambs_up.get()}\t    {self.d_t_p}")
            if self.pepsi.get()!=0:
                self.txtarea.insert(END,f"\n Pepsi\t\t{self.pepsi.get()}\t    {self.d_l_p}")
            if self.sprite.get()!=0:
                self.txtarea.insert(END,f"\n Sprite\t\t{self.sprite.get()}\t    {self.d_s_p}")
                
                
            self.txtarea.insert(END,f"\n----------------------------------")
            if self.cosmatic_Tax.get()!="Rs. 0.0":
                self.txtarea.insert(END,f"\n Cosmetic Tax\t\t\t  {self.cosmatic_Tax.get()}")
            
            
            if self.grocery_Tax.get()!="Rs. 0.0":
                self.txtarea.insert(END,f"\n Grocery Tax\t\t\t  {self.grocery_Tax.get()}")
        
            
            if self.cold_drink_Tax.get()!="Rs. 0.0":
                self.txtarea.insert(END,f"\n Cold Drink Tax\t\t\t  {self.cold_drink_Tax.get()}")
                
            self.txtarea.insert(END,f"\n----------------------------------")   
            self.txtarea.insert(END,f"\n Total Bill :\t\t\t Rs.{self.Total_bill}")
            self.txtarea.insert(END,f"\n----------------------------------")
            self.save_bill()
     
    def save_bill(self):
        op=messagebox.askyesno("Save Bill ", "Do you want to save Bill?")
        if op>0:
            self.bill_data=self.txtarea.get('1.0',END)
            f1=open("D:/python project/Billing System/Bills/"+str(self.bill_no.get())+".txt","w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved",f"Bill no. : {self.bill_no.get()} saved successfully")
            
        else:
            return
        
    def find_bill(self):
        present="no"
        for i in os.listdir("Bills/"):
            if i in os.listdir("Bills/"):
                if i.split('.')[0]==self.search_bill.get():
                    f1=open(f"Bills/{i}","r")
                    self.txtarea.delete('1.0',END)
                    for d in f1:
                        
                        self.txtarea.insert(END,d)
                    f1.close()
                    present="yes"
        if present=="no":
            messagebox.showerror("Error","Invalid bil no")            
                    
    def clear_data(self):
        
        op=messagebox.askyesno("Clear","do you really want to clear?")
        if op>0:
           
            #>>>>>>>>>> varibles <<<<<<<<<<
            self.Soap.set(0)
            self.Face_cream.set(0)
            self.Face_wash.set(0)
            self.Sprey.set(0)
            self.Gell.set(0)
            self.Loshan.set(0)
            
            #>>>>>>>>>> Grocery <<<<<<<<<<
            self.Rise.set(0)
            self.Food_oil.set(0)
            self.Dal.set(0)
            self.Wheat.set(0)
            self.Sugar.set(0)
            self.Tea.set(0)
            
            #>>>>>>>>>> Cold Drink <<<<<<<<<<
            self.maza.set(0)
            self.coco_cola.set(0)
            self.fruiti.set(0)
            self.thambs_up.set(0)
            self.pepsi.set(0)
            self.sprite.set(0)
            
            #>>>>>>>> Total Product Price & Tax Variable <<<<<<<<<<
            self.cosmatic_price.set("")
            self.grocery_price.set("")
            self.cold_drink_price.set("")
            
            self.cosmatic_Tax.set("")
            self.grocery_Tax.set("")
            self.cold_drink_Tax.set("")
            
            #>>>>>>> Costomer <<<<<<
            self.c_name.set("")
            self.c_phon.set("")
            self.bill_no.set("")
            x=random.randint(1000,9999)
            self.bill_no.set(str(x))
            self.search_bill.set("")    
            self.welcome_bill()        
        
    def Exit_app(self):
        op=messagebox.askyesno("Exit","do you really want to exit")
        if op>0:
            self.root.destroy()
        
            
                
        
    
root=Tk()
obj=Bill_App(root)
root.mainloop()
        