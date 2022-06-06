import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

class Person:
    def __init__(self, _name, _hobbies, _workExperience, _education, _aboutMe, _travelMapURL, _profileImageURL="./static/img/logo.jpg"):
        self.name = _name
        self.hobbies = _hobbies
        self.workExperience = _workExperience
        self.education = _education
        self.aboutMe = _aboutMe
        self.travelMapURL = _travelMapURL
        self.profileImageURL = _profileImageURL



class WorkExperience:
    def __init__(self, _startDate, _endDate, _organization, _role, _roleDescriptions = ""):
        self.startDate = _startDate
        self.endDate = _endDate
        self.organization = _organization
        self.role = _role
        self.roleDescription = _roleDescriptions

class Education:
    def __init__(self, _institution, _completionDate, _degree):
        self.institution = _institution
        self.completionDate = _completionDate
        self.degree = _degree

class Hobby:
    def __init__(self, _name, _pictureURLs = "", _description = ""):
        self.name = _name
        self.pictureURLs = _pictureURLs
        self.description = _description

def GetPeople():
    #TODO: fill in
    Lucas = Person("Lucas Cancio"
                , [Hobby("game development", ["./static/img/logo.jpg", "./static/img/logo.jpg"])
                    , Hobby("martial arts", ["./static/img/logo.jpg", "./static/img/logo.jpg"])
                    , Hobby("biking", ["./static/img/logo.jpg", "./static/img/logo.jpg"])]
                , [WorkExperience("May 2020", "August 2020", "TheCoderSchool", "Programming Tutor", "I tutored kids on how to program")
                    , WorkExperience("June 2021", "September 2021", "Machine Intelligence Lab @ UF", "Undergraduate Researcher", "I mainly focused on documenting a submarine's simulation software")]
                , [Education("University of Florida", "May 2023", "Bachelor's of Science in Computer Science")]
                , "A little bit about me..."
                ,"", "./static/img/logo.jpg")

    #TODO: fill in
    Luis = Person("Luis Moraguez"
                , [Hobby("game development", ["./static/img/logo.jpg", "./static/img/logo.jpg"])
                    , Hobby("martial arts", ["./static/img/logo.jpg", "./static/img/logo.jpg"])
                    , Hobby("biking", ["./static/img/logo.jpg", "./static/img/logo.jpg"])]
                , [WorkExperience("May 2020", "August 2020", "TheCoderSchool", "Programming Tutor", "I tutored kids on how to program")
                    , WorkExperience("June 2021", "September 2021", "Machine Intelligence Lab @ UF", "Undergraduate Researcher", "I mainly focused on documenting a submarine's simulation software")]
                , [Education("University of Florida", "May 2023", "Bachelor's of Science in Computer Science")]
                , "A little bit about me..."
                ,"", "./static/img/logo.jpg")
                
    #TODO: fill in
    Maurice = Person("Maurice Korish"
                , [Hobby("Model United Nations", ["./static/img/Maurice/modelun.jpg"])
                    , Hobby("Track/Cross Country", ["./static/img/Maurice/track.jpg"])
                    , Hobby("Soccer", [])]
                , [WorkExperience("January 2019", "May 2021", "FeedBot Project", "Lead Developer", "With a partner, I created a device that uses facial recognition technology to guide a robotic-feeding arm to an individual's mouth.")]
                , [Education("Stanford University", "May 2026", "Bachelor's of Science in Computer Science")]
                , "Hi! My name is Maurice Korish, and I am from New Jersey. I'm very interested in math, physics, and computer science, and I would love to work on developing technologies that can enhance our understanding of the world we live in."
                ,"", "./static/img/Maurice/maurice.jpg")

    people = [Luis, Maurice, Lucas]
    return people

@app.route('/')
def index():
    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"))


@app.route('/about')
def aboutus():
    return render_template('about.html', nameOfPage="About Us", type="About Us", people=GetPeople(),  url=os.getenv("URL"))

@app.route('/hobbies')
def hobbies():
    return render_template('hobbies.html', nameOfPage="Hobbies", type="Our Hobbies", people=GetPeople(),  url=os.getenv("URL"))
