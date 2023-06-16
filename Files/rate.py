from .__init__ import *

class RatingDialog(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Rate Me")
        self.resizable(False,False)
        self.stars = 0
        self.ico = Image.open("Icons/rate.png")
        self.photo = ImageTk.PhotoImage(self.ico)
        self.wm_iconphoto(False, self.photo)

        self.star_labels = []
        for i in range(5):
            star_label = tk.Label(self, text="★", font=("Arial", 20))
            star_label.pack(side=tk.LEFT, padx=5)
            star_label.bind("<Enter>", lambda event, index=i: self.on_star_enter(event, index))
            star_label.bind("<Leave>", self.on_star_leave)
            star_label.bind("<Button-1>", lambda event, index=i: self.on_star_click(event, index))
            self.star_labels.append(star_label)

    def on_star_enter(self, event, index):
        for i in range(index + 1):
            self.star_labels[i].config(fg="gold")

    def on_star_leave(self, event):
        self.update_stars()

    def on_star_click(self, event, index):
        self.stars = index + 1
        self.update_stars()
        tmsg.showinfo("Thank You", "Thank you for rating the application with {} stars!".format(self.stars))
        f = open("Rating&Review/ratings.txt","a")
        f.write(f"Rating : {self.stars} \n")
        f.close()
        self.destroy()

    def update_stars(self):
        for i in range(5):
            if i < self.stars:
                self.star_labels[i].config(fg="gold")
            else:
                self.star_labels[i].config(fg="black")