import os
import datetime
from flask import Flask, render_template, request
from flask_gravatar import Gravatar
from dotenv import load_dotenv
from peewee import *
from playhouse.shortcuts import model_to_dict

load_dotenv()
app = Flask(__name__)


gravatar = Gravatar(app,
                    size=100,
                    rating='g',
                    default='identicon',
                    force_default=False,
                    force_lower=False,
                    use_ssl=False,
                    base_url=None)


mydb = MySQLDatabase(os.getenv("MYSQL_DATABASE"),user=os.getenv("MYSQL_USER"),password=os.getenv("MYSQL_PASSWORD"),host=os.getenv("MYSQL_HOST"),port=3306)

class TimelinePost(Model):
    name = CharField()
    email = CharField()
    content = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)
    class Meta:
        database = mydb

mydb.connect()
mydb.create_tables([TimelinePost])

class Person:
    def __init__(self, _name, _hobbies, _workExperience, _education, _aboutMe, _travelMapURL, _profileImageURL = "./static/img/logo.jpg", _summary = "", _tagline = ""):
        self.name = _name
        self.hobbies = _hobbies
        self.workExperience = _workExperience
        self.education = _education
        self.aboutMe = _aboutMe
        self.travelMapURL = _travelMapURL
        self.profileImageURL = _profileImageURL
        self.summary = _summary
        self.tagline = _tagline

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
                , "./static/img/luis/profile.jpg"
                , "Software Engineer, Network Engineer, Cybersecurity Engineer, Database Administrator, Outdoor Enthusiast"
                , "Here's a cool tagline!")

    person = Luis
    return person

@app.route('/')
def index():
    return render_template('index.html', title="Luis Moraguez - Resume", person=GetPerson(), url=os.getenv("URL"))

@app.route('/portfolio-details')
def portfolioDetails():
    return render_template('portfolio-details.html', title="Luis Moraguez - Portfolio Details", person=GetPerson(), url=os.getenv("URL"))

@app.route('/timeline')
def timeline():
    data = get_time_line_post()
    timeline_posts = data['timeline_posts']

    return render_template('timeline.html', title="Timeline", timeline_posts=timeline_posts)

@app.route('/api/timeline_post', methods=['POST'])
def post_time_line_post():
    name = request.form['name']
    email = request.form['email']
    content = request.form['content']
    timeline_post = TimelinePost.create(name=name, email=email, content=content)

    return model_to_dict(timeline_post)

@app.route('/api/timeline_post', methods=['GET'])
def get_time_line_post():
    return {
        'timeline_posts': [
            model_to_dict(p)
            for p in TimelinePost.select().order_by(TimelinePost.created_at.desc())
        ]
    }

@app.route('/api/timeline_post', methods=['DELETE'])
def delete_time_line_post():
    id = request.form['id']
    deleted = TimelinePost.get(TimelinePost.id == id)
    TimelinePost.delete_by_id(id)
    return model_to_dict(deleted)