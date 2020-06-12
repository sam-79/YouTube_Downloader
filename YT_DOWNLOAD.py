
from tkinter import *
import subprocess as sp
import youtube_dl
from tkinter import filedialog 
from tkinter import ttk
#import pafy



def root_w():
	
	self.destroy()
	root=Tk()
	root.geometry("1020x2100")
	root.resizable(height=0,width=0)
	root.title("Downloader")
	
	L1=Label(root,text="YT Downloader",font=("",10))
	L1.config(font=("",10))
	
	L2=Label(root,text="Enter Link")
	
	E1=Entry(root,text="enter")
	#url="https://youtu.be/IGQBtbKSVhY"
	url=E1.get()
	
	def save():
		
		def d_file():
			#function to dowload file
			val[n].download(filepath=save_dir)
			
			
		
		
		
		root.dir= filedialog.askdirectory()
		global save_dir
		save_dir=root.dir
		#L1=Label(root,text=save_dir)
		#L1.place(relx=0.5,rely=0.54,anchor=CENTER)
		
		if(len(save_dir)!=0):
			d_btn=Button(root,text="Download File",command=d_file)
			d_btn.place(relx=0.5,rely=0.6,anchor=CENTER)
		
	
	
	
	
	def Daudio(url):
		cmd="youtube-dl "+ url
		res=sp.call(cmd,shell=True)
		
	
	def Dvideo(url):
		
		def down(event):
			global n
			n=cb.current()
			size=round((val[n].get_filesize())/(1024*1024),2)
			
			size_lbl=Label(root,text='Size: '+str(size)+'MB')
			size_lbl.place(relx=0.5,rely=0.445,anchor=CENTER)
			
			
		
		
		
		
		
		vid=pafy.new(url)
		title_lab=Label(root,text="Hello my name is Sameer",width=30)
		
		
		
		
		
		
		
		
		
		global val
		val=vid.streams
		cb=ttk.Combobox(root,values=val,state="readonly",width=34)
		cb.bind('<<ComboboxSelected>>',down)
		
		title_lab.place(relx=0.1,rely=0.3)
		cb.place(relx=0.03,rely=0.38)
		
		#cmd="youtube-dl -x "+ url
		#res=sp.call(cmd,shell=True)
	
	
	
	
	B1=Button(root,text="Audio",command=lambda: Daudio(url))
	B2=Button(root,text="Video",command=lambda: Dvideo(url))
	B3=Button(root,text="Exit",command=exit)
	B4=Button(root,text="Select Location",command=save)
	
	
	
	
	
	# Placing of widgets 
	L1.place(anchor=CENTER,relx=0.5,rely=0.05)
	L2.place(relx=0.01,rely=0.1,height=100)
	E1.place(relx=0.48,rely=0.1,height=100)
	B1.place(relx=0.2,rely=0.2)
	B2.place(relx=0.6,rely=0.2)
	B3.place(relx=0.5,rely=0.9,anchor=CENTER)
	B4.place(relx=0.5,rely=0.51,anchor=CENTER)
	
	
	
	
	
	root.mainloop()


self=Tk()
b1=Button(self,text="Enter",command=root_w,activebackground="Black")
b1.place(anchor=N,bordermode=OUTSIDE,relx=0.5,rely=0.2,height=199)
b2=Button(self,text="Close",command=exit)
b2.place(anchor=CENTER,relheight=0.09,relx=0.5,rely=0.8)
self.mainloop()