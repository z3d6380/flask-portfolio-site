import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

class Person:
    def __init__(self, _name, _hobbies, _workExperience, _education, _aboutSelf, _travelMapURL):
        self.name = _name
        self.hobbies = _hobbies
        self.workExperience = _workExperience
        self.education = _education
        self.aboutSelf = _aboutSelf
        self.travelMapURL = _travelMapURL


class WorkExperience:
    def __init__(self, _startDate, _endDate, _organization, _roleDescriptions):
        self.startDate = _startDate
        self.endDate = _endDate
        self.organization = _organization
        self.roleDescription = _roleDescriptions

class Education:
    def __init__(self, _institution, _completionDate, _degree):
        self.institution = _institution
        self.completionDate = _completionDate
        self.degree = _degree

class Hobby:
    def __init__(self, _hobbyName, _pictures = "", _description = ""):
        self.hobbyName = _hobbyName
        self.pictures = _pictures
        self.description = _description

def GetPeople():
    #TODO: fill in
    Lucas = Person("Lucas Cancio"
                , [Hobby("game development"), Hobby("martial arts"), Hobby("biking")]
                , [WorkExperience("May 2020", "August 2020", "TheCoderSchool", "Programming Tutor")
                    , WorkExperience("June 2021", "September 2021", "Machine Intelligence Lab @ UF", "Undergraduate Researcher")]
                , [Education("University of Florida", "May 2023", "Bachelor's of Science in Computer Science")]
                , "A little bit about me...",
                "***TEMP IMAGE URL")
    #TODO: fill in
    Luis = Person("Luis Moraguez"
                , [Hobby("game development"), Hobby("martial arts"), Hobby("biking")]
                , [WorkExperience("May 2020", "August 2020", "TheCoderSchool", "Programming Tutor")
                    , WorkExperience("June 2021", "September 2021", "Machine Intelligence Lab @ UF", "Undergraduate Researcher")]
                , [Education("University of Florida", "May 2023", "Bachelor's of Science in Computer Science")]
                , "A little bit about me...",
                "***TEMP IMAGE URL")
    #TODO: fill in
    Maurice = Person("Maurice Korish"
                , [Hobby("game development"), Hobby("martial arts"), Hobby("biking")]
                , [WorkExperience("May 2020", "August 2020", "TheCoderSchool", "Programming Tutor")
                    , WorkExperience("June 2021", "September 2021", "Machine Intelligence Lab @ UF", "Undergraduate Researcher")]
                , [Education("University of Florida", "May 2023", "Bachelor's of Science in Computer Science")]
                , "A little bit about me...",
                "***TEMP IMAGE URL")

    people = [Luis, Maurice, Lucas]
    return people

@app.route('/')
def index():
    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"))


@app.route('/aboutus')
def aboutus():
    return render_template('templatetest.html', nameOfPage="About Us", type="About Us", people=GetPeople(),  url=os.getenv("URL"))

@app.route('/hobbies')
def hobbies():
    return render_template('templatetest.html', nameOfPage="Hobbies", type="Our Hobbies", people=GetPeople(),  url=os.getenv("URL"))
