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

def GetPerson():

    Luis = Person("Luis Moraguez"
                , [Hobby("kayaking", ["./static/img/luis/kayak.jpg"], "I love to kayak challenging paddling trails around Florida.")
                    , Hobby("running", ["./static/img/luis/running.jpg"], "I love running long distance.")
                    , Hobby("camping", ["./static/img/luis/camping.jpg"], "I love connecting with nature and camping and beautiful areas around the US.")]
                , [WorkExperience("March 2017", "April 2021", "City of Kissimmee Information Technology", "Enterprise Applications Administrator", "Responsible for implementing, maintaining, and upgrading all of the city's Enterprise Public Safety applications. Projects: Custom developed interface to send live accident data to Waze, implemented Workforce Telestaff, implemented export from OneSolutionCAD to ESO, custom developed forms and reports for various needs of Police and Fire Departments, implemented body camera system for Police, implemented SSO for body camera system, custom developed integration between OneSolutionCAD and body camera system, custom developed self-service web app for Police. Also responsible for mapping departmental workflow processes, testing the applications, working with vendors to resolve software bugs or issues, creating documentation, training staff, and evaluating new features or products.")
                    ,WorkExperience("April 2015", "March 2017", "City of Kissimmee Information Technology", "Computer Specialist", "Handled all the trouble calls from every department in the city, including public safety departments by providing onsite and remote support for users. Responsible for the configuration of new equipment purchased for each department. Responsible for handling on-call and after-hours issues from public safety departments on a rotation. Effectively communicated with 3 rd party support from hardware/software vendors, partners, and technical support. Maintained accurate documentation of hardware to be deployed or disposed of, and documentation of all interactions with users and the steps taken to resolve their issues. Maintained positive working relationships with users throughout the city departments.")]
                , [Education("Florida Polytechnic University", "May 2023", "Bachelor's of Science in Computer Science")
                    ,Education("Valencia College", "May 2017", "Associate of Science in Network Engineering")
                    ,Education("Valencia College", "May 2017", "Associate of Science in Cyber Security")]
                , "Hi everyone, my name is Luis Moraguez. I was born in raised in Kissimmee, FL. I've always had a passion for technology. I've spent the last 10+ years working professionally in the IT field, and I've recently decided to switch to Computer Science because I want to build technology to help people. When I'm not in front of the computer, I love to be outdoors!"
                , ""
                , "./static/img/luis/profile.jpg")

    person = Luis
    return person

@app.route('/')
def index():
    return render_template('index.html', title="Luis Moraguez - Resume", person=GetPerson(), url=os.getenv("URL"))

@app.route('/portfolio-details')
def portfolioDetails():
    return render_template('portfolio-details.html', title="Luis Moraguez - Portfolio Details", person=GetPerson(), url=os.getenv("URL"))
