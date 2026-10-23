from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

students= {
    "S001": {"name":"Abhi", "marks":85, "grade": "A"},
    "S002":{"name": "Punit", "marks": 74, "grade": "B"},
    "S003":{"name": "Sonu", "marks": 55, "grade": "C"},
}

class MarksSubmission(BaseModel):
    student_id : str
    marks: int
    subject: str

@app.get("/student/{student_id}")
def get_student(student_id: str):

    if student_id not in students:
        raise HTTPException(
            status_code = 404,
            detail= f"student with ID {student_id} does not exist"
        )
    return students[student_id]

@app.post("/submit-marks")
def submit_marks(submission: MarksSubmission):

    #error 1: if student_id does not in database
    if submission.student_id not in students:
        raise HTTPException(
            status_code = 404,
            detail = f"student with ID  {submission.student_id} does not found"
        )

    ##error - marks not in valid range
    if submission.marks < 0 or submission.marks > 100:
        raise HTTPException(
            status_code = 400,
            detail = {
                'error': "marks must be between 0 and 100",
                'marks_received': submission.marks,
                'fix': 'enter a valid value between 0 to 100'
            }
        )

    #error - subject name would be empty
    if submission.subject.strip() == "":
        raise HTTPException(
            status_code= 400,
            details="subject cannot be empty"
        )
    try:
        students[submission.student_id]["marks"] = submission.marks
        return{
        "message": "marks submitted succesfully",
        "student": students[submission.student_id]["name"],
        "subject": submission.subject,
        "marks": submission.marks
        }
    except Exception as e:
        raise HTTPException(
            status_code= 500,
            details = f"something went wrong on our end: {str(e)}"
        )


