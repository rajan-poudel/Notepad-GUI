from .__init__ import *

class HelpDialog(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Calculator Help")
        self.resizable(False,False)
        self.ico = Image.open("Icons/help.png")
        self.photo = ImageTk.PhotoImage(self.ico)
        self.wm_iconphoto(False, self.photo)

        help_text = """
Notepad Help

This Notepad GUI provides you with basic functionality to create and edit text files. It doesn't have any 
complex or premium features, keeping it simple and easy to use.

File Menu:
- New: Create a new, empty document.
- Open: Open an existing text file from your computer.
- Save: Save the current document.
- Save As: Save the current document with a new name or location.
- Save All: Save all open documents.
- Exit: Close the Notepad application.

Edit Menu:
- Cut: Remove the selected text and place it in the clipboard.
- Copy: Copy the selected text to the clipboard.
- Paste: Insert the contents of the clipboard at the current cursor position.

To use these features, follow these steps:
1. Click on the "File" menu to access file-related options.
2. Select the desired option from the dropdown menu.
3. For example, if you want to create a new document, click on "File" and then select "New." A new, empty  document will be displayed.
4. Use the Edit menu options to cut, copy, or paste text as needed.

Please note that this Notepad GUI is designed to provide a simple and straightforward text editing experience. 
It does not include advanced features such as formatting, spell checking, or syntax highlighting.

If you have any further questions or need assistance, feel free to reach out me.
        """

        help_label = tk.Label(self, text=help_text, justify=tk.LEFT)
        help_label.pack(padx=10, pady=10)