import win32com.client


def create_word(file_path):
    """Function to create word."""
    word = win32com.client.Dispatch("Word.Application")
    word.Visible = True

    doc = word.Documents.Add()

    selection = word.Selection
    selection.TypeText("Hey")
    selection.TypeParagraph()
    selection.TypeText("there")

    doc.SaveAs(file_path)

    word.Quit()


create_word(r"C:\Users\Administrator\Desktop\PythonTraining\PythonTraining_DailyTask\Day20\sample.docx")
