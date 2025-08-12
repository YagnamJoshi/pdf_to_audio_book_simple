import PyPDF2
import pyttsx3
import os


class PdfToAudioBook:
    def __init__(self,pdf_file_path):
        """_summary_

        Args:
            pdf_file_path (String): PDF file path
        """
        self.pdf_file_path = pdf_file_path
        with open(self.pdf_file_path,"rb") as pdf_file:
            reader = PyPDF2.PdfReader(pdf_file)
            self.text = ""
            for page in reader.pages:
                self.text+=page.extract_text()+'\n'
        
    def getText(self):
        """_summary_

        Returns:
            String: Text retrived from PDF file
        """
        return self.text
    
    def get_audio(self,audio_book_name,audio_book_path):
        """_summary_

        Args:
            audio_book_name (String): name of audio book
            audio_book_path (String): path you want your audio book to be stored at 
        """
        engine = pyttsx3.init()
        output_file = os.path.join(audio_book_path, audio_book_name)
        engine.save_to_file(self.text,output_file)
        engine.runAndWait()
        print(f"Audio Book created at {output_file}!")

