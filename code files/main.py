import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import os
from pdfToAudioBook import PdfToAudioBook

class PDFToAudioGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF to Audiobook Converter")
        self.root.geometry("600x600")
        
        self.pdf_path = None
        self.audio_save_path = None

        # PDF Select Button
        self.btn_select_pdf = tk.Button(root, text="Select PDF", command=self.select_pdf)
        self.btn_select_pdf.pack(pady=10)

        # Text Display
        self.text_display = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=70, height=20)
        self.text_display.pack(padx=10, pady=10)

        # Audio Name Entry
        tk.Label(root, text="Audiobook File Name (with .wav extension):").pack()
        self.audio_name_entry = tk.Entry(root, width=40)
        self.audio_name_entry.pack(pady=5)

        # Save Path Button
        self.btn_save_path = tk.Button(root, text="Select Save Location", command=self.select_save_path)
        self.btn_save_path.pack(pady=5)

        # Convert Button
        self.btn_convert = tk.Button(root, text="Convert to Audio", command=self.convert_to_audio)
        self.btn_convert.pack(pady=10)

    def select_pdf(self):
        """Select a PDF file and display its text"""
        file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
        if file_path:
            self.pdf_path = file_path
            try:
                converter = PdfToAudioBook(self.pdf_path)
                text = converter.getText()
                self.text_display.delete(1.0, tk.END)
                self.text_display.insert(tk.END, text)
            except Exception as e:
                messagebox.showerror("Error", f"Failed to read PDF: {e}")

    def select_save_path(self):
        """Choose where to save the audiobook"""
        folder_path = filedialog.askdirectory()
        if folder_path:
            self.audio_save_path = folder_path

    def convert_to_audio(self):
        """Convert the extracted PDF text to audio"""
        if not self.pdf_path:
            messagebox.showwarning("No PDF", "Please select a PDF file first.")
            return
        if not self.audio_save_path:
            messagebox.showwarning("No Save Path", "Please select a location to save the audiobook.")
            return
        audio_name = self.audio_name_entry.get().strip()
        if not audio_name:
            messagebox.showwarning("No File Name", "Please enter a name for your audiobook.")
            return
        try:
            converter = PdfToAudioBook(self.pdf_path)
            converter.get_audio(audio_name, self.audio_save_path)
            messagebox.showinfo("Success", f"Audiobook created successfully at {os.path.join(self.audio_save_path, audio_name)}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to create audiobook: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = PDFToAudioGUI(root)
    root.mainloop()
