from .__init__ import *



class About(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("About")
        self.resizable(False,False)
        self.ico = Image.open("Icons/about.png")
        self.photo = ImageTk.PhotoImage(self.ico)
        self.wm_iconphoto(False, self.photo)

        about_text = """
Welcome to Notepad GUI!

Crafted with passion and dedication by Rajan Poudel, an aspiring computer coding and programming enthusiast, 
this Notepad GUI represents my initial venture into the world of software development. Fueled by a deep love 
for computers and a drive to transform functionality into reality, I embarked on this journey to create a 
user-friendly and efficient text editing application.

As a beginner in the coding realm, I eagerly embraced the challenge of constructing this GUI-based Notepad 
from the ground up. With each line of code written, I uncovered the power and creativity that programming 
offers. This project not only honed my technical skills but also ignited a passion within me to explore the 
boundless possibilities of software development.

Notepad GUI strives to provide you with a reliable and intuitive tool for all your text editing needs. Whether 
you're a student, professional, or simply someone who appreciates a clean interface, this Notepad is designed 
to make your writing experience swift and seamless. Please note that this application focuses on fundamental 
text editing features only.

My vision for this Notepad is to create a user-friendly experience that allows anyone, regardless of their 
coding expertise, to effortlessly manipulate and manage their text with confidence. I hope that this tool will 
not only assist you in your daily writing tasks but also inspire you to delve deeper into the captivating 
world of computer programming.

Thank you for joining me on this thrilling journey as I take my initial steps into the coding realm. Your 
support and feedback are invaluable to me as I continue to learn and evolve. Feel free to explore the various 
features of this Notepad GUI, and may it bring simplicity and efficiency to your writing endeavors.

Happy writing!
Rajan Poudel
        """

        help_label = tk.Label(self, text=about_text, justify=tk.LEFT)
        help_label.pack(padx=10, pady=10)