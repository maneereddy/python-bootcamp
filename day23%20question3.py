#Import the required Libraries
import PyPDF2
from tkinter import *
from tkinter import filedialog
#Create an instance of tkinter frame
win= Tk()
#Set the Geometry
win.geometry("750x450")
#Create a Text Box
text= Text(win,width= 80,height=30)
text.pack(pady=20)
#Define a function to clear the text
def clear_text():
   text.delete(1.0, END)
#Define a function to open the pdf file
def open_pdf():
   file= filedialog.askopenfilename(title="Select a PDF", filetype=(("PDF    Files","*.pdf"),("All Files","*.*")))
   if file:
      #Open the PDF File
      pdf_file= PyPDF2.PdfFileReader(file)
      #Select a Page to read
      page= pdf_file.getPage(0)
      #Get the content of the Page
      content=page.extractText()
      #Add the content to TextBox
      text.insert(1.0,content)

def quit_app():
   win.destroy()

my_menu= Menu(win)
win.config(menu=my_menu)

file_menu=Menu(my_menu,tearoff=False)
my_menu.add_cascade(label="File",menu= file_menu)
file_menu.add_command(label="Open",command=open_pdf)
file_menu.add_command(label="Clear",command=clear_text)
file_menu.add_command(label="Quit",command=quit_app)
win.mainloop()