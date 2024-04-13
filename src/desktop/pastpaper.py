from bot import (
	pyttsx3,
	sr,
	pyautogui,
	random,
	subprocess,
	time,
)

from utils.data import (
	alevel_subjects,
	alevel_subject_names,
	variants,
	sessions,
)

def open_pdf_with_app(file_path):
    subprocess.Popen([file_path], shell=True)

def pastpaper(subjectcode, papercode):
    validation = str(subjectcode) in alevel_subject_names
    subject_name = alevel_subject_names.get(str(subjectcode), "Unknown Subject")
    session = random.choice(sessions)
    year = random.randint(15, 23)
    if validation:
        if session == "February March":
            variantcode = variants["feb_march"]
            season = "m"
            session1 = "Feb-March"
        elif session == "May June":
            variantcode = random.choice(variants["may_june"])
            season = "s"
            session1 = "May-June"

        elif session == "October November":
            variantcode = random.choice(variants["oct_nov"])
            season = "w"
            session1 = "Oct-Nov"
        qppaper = f"{subjectcode}_{season}{year}_qp_{papercode}{variantcode}"
        mspaper = f"{subjectcode}_{season}{year}_ms_{papercode}{variantcode}"
        qppath = f"C:\\Users\\Kaushik\\Documents\\Programming\\Augmented-Learning-System\\assets\\Past Papers\\{subjectcode} - {subject_name}\\20{year}\\20{year} {session1}\\{qppaper}.pdf"
        mspath = f"C:\\Users\\Kaushik\\Documents\\Programming\\Augmented-Learning-System\\assets\\Past Papers\\{subjectcode} - {subject_name}\\20{year}\\20{year} {session1}\\{mspaper}.pdf"
        open_pdf_with_app(qppath)
        time.sleep(1.5)
        open_pdf_with_app(mspath)
        speech = f"A random {subject_name.lower()} paper {papercode} has been fetched from the year {session} 20{year}"
        return speech