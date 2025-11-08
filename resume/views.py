from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.staticfiles.storage import staticfiles_storage


# Create your views here.
def home(request):
    return render (request,"home.html")

def about (request):
    return render (request,"about.html")


def projects (request):
    projects_show=[
        {
            'title': 'Rasoi Connect',
            'path': 'images/rasoi_connect.PNG',
        },
        {
            'title': 'Ecommerce',
            'path': 'images/ecommerce.PNG',
        },

        {
            'title': 'Timetable Scheduler',
            'path': 'images/timtable.PNG',
        },
        {
            'title': 'CRUD',
            'path': 'images/CRUD.PNG',
        },

         {
            'title': 'Photo Uploader',
            'path': 'images/photo_uploader.PNG',
        },
          {
            'title': 'To do list',
            'path': 'images/todolist.PNG',
        },
         {
            'title': 'Portfolio',
            'path': 'images/portfolio.PNG',
        },
                  {
            'title': 'Labour Hiring',
            'path': 'images\labour_hiring.PNG',
        },

    ]
    return render (request,"projects.html",{"projects_show": projects_show})


def experience(request):
    experience=[
        {"company":"ABC",
         "position":"python developer"},
        {"company":"ABC2",
         "position":"python developer2"},
        {"company":"ABC3",
         "position":"python developer3"}
    ]
    return render (request,"experience.html",{"experience":experience})


def certificate(request):
    return render (request, "certificate.html")


def contact(request):
    return render (request,"contact.html")

def resume(request):
    resume_path="myapp/resume.pdf"
    resume_path=staticfiles_storage.path(resume_path)
    if staticfiles_storage.exists(resume_path):
        with open(resume_path,"rb") as resume_file:
            response=HttpResponse(resume_file.read(),content_type="application/pdf")
            response['Content-Disposition']='attachment';filename="resume.pdf"
            return response
    else:
        return HttpResponse("resume not found", status=404)
def projects(request):
    projects_show = [
        {
            'title': 'Heart Disease prediction',
            'path': 'images/heart.png',
            'description': 'The Heart Disease Prediction System predicts the risk of heart disease using machine learning techniques.It analyzes medical factors such as age, gender, blood pressure, cholesterol, and heart rate',
            'github_link': 'https://github.com/Sowmyabongu/heart-disease-prediction',
            'app_link': 'https://heart-disease-prediction-mfpvmkhxkhdallunsp2wls.streamlit.app/'
        },
        {
            'title': 'breast cancer prediction',
            'path': 'images/breast.png',
            'description':'The Breast Cancer Prediction System uses machine learning algorithms to predict whether a tumor is benign or malignant based on features like cell size, texture, and shape. ',
            'github_link': 'https://github.com/Sowmyabongu/Breast-cancer-Prediction',
            'app_link': 'https://breast-cancer-prediction-enprnuhnpw9tgxgabzcvhf.streamlit.app/'
        },
    ]
    return render(request, "projects.html", {'projects_show': projects_show})

def experience(request):
    experience = [
        {
            'company': 'Data Science Intern',
            'position': 'CodTech IT Solutions Pvt. Ltd',
            'description': (
               'Completed an 8-week internship focused on data analysis, machine learning, and visualization using Python,Pandas, and Scikit-learn.I worked on collecting, analyzing, and interpreting large datasets to uncover meaningful insights. I applied machine learning techniques and data visualization tools to support data-driven decision-making and improve business outcomes.'

            ),
            'duration': 'June 2025 – August 2025'
        },
        
    ]
    return render(request, "experience.html", {'experience': experience})
