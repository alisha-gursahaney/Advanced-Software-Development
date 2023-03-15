import requests
from tutorMe.models import Course
import re
from difflib import SequenceMatcher


def get_JSON_Subjects(year, semester):
    year = year[-2:]
    if semester == "Spring":
        semester = "2"
    if semester == "Fall":
        semester = "8"
    subjects = []

    url = "https://sisuva.admin.virginia.edu/psc/ihprd/UVSS/SA/s/WEBLIB_HCX_CM.H_CLASS_SEARCH.FieldFormula.IScript_ClassSearchOptions?institution=UVA01&term=1"
    url += year
    url += semester

    r = requests.get(url)
    data = r.json()

    temp = data.get("subjects")

    for sub in temp:
        subjects.append(sub['subject'])


    return subjects

def get_classes(subject_name, year, semester):
    classes = []
    data = 1
    page_num = 1
    year = year[-2:]
    if semester == "Spring":
        semester = "2"
    if semester == "Fall":
        semester = "8"

    while data != []:
        page_num_str = str(page_num)

        url = "https://sisuva.admin.virginia.edu/psc/ihprd/UVSS/SA/s/WEBLIB_HCX_CM.H_CLASS_SEARCH.FieldFormula.IScript_ClassSearch?institution=UVA01&term=1"
        year_sem_num = year + semester + "&subject="
        url += year_sem_num

        add = subject_name + "&page="
        url += add

        url += page_num_str
        r = requests.get(url)
        data = r.json()

        for cur_class in data:
            val = cur_class.get('descr')
            if val not in classes:
                classes.append(val)
        page_num += 1
    return classes



def get_classes(subject_name, year, semester):
    classes = []
    data = 1
    page_num = 1
    year = year[-2:]
    if semester == "Spring":
        semester = "2"
    if semester == "Fall":
        semester = "8"

    while data != []:
        page_num_str = str(page_num)

        url = "https://sisuva.admin.virginia.edu/psc/ihprd/UVSS/SA/s/WEBLIB_HCX_CM.H_CLASS_SEARCH.FieldFormula.IScript_ClassSearch?institution=UVA01&term=1"
        year_sem_num = year + semester + "&subject="
        url += year_sem_num

        add = subject_name + "&page="
        url += add

        url += page_num_str
        r = requests.get(url)
        data = r.json()

        for cur_class in data:
            val = cur_class.get('descr')
            if val not in classes:
                classes.append(val)
        page_num += 1
    return classes


#print(get_JSON_Subjects("2023", "Spring"))

def Searchereds(keyword):
    ClassesActual=[]
    ClassInfo=[]
    match = re.search(r'\d+', keyword)
    if match:
        number_str = match.group()  # extract the number string
        non_number_str = re.sub(r'\d+', '', keyword).strip()  # remove the number string
    else:
        number_str = ''
        non_number_str = keyword
    for item in Course.objects.all():
        ClassInfo=[item.Subject,item.course_name,item.course_number]
        Sum=0
        if  not number_str=='':
            for items in non_number_str.lower().split(" "):
                if (ClassInfo[0].lower() == items.lower()):
                    Sum += 1
                elif (ClassInfo[0].lower() != items.lower()):
                    Sum+=SequenceMatcher(None, ClassInfo[1].lower(), items.lower()).ratio()
            if (number_str == ClassInfo[2]):
                Sum +=1
            else:
                Sum += SequenceMatcher(None, number_str, item.course_number).ratio()
        else:
            if (keyword.lower() in item.course_name.lower()):
                Sum += 1
            else:
                Sum+=SequenceMatcher(None, keyword, item.course_name.lower()).ratio()
        rating=Sum
        ClassInfo.append(number_str)
        ClassInfo.append(non_number_str)
        ClassInfo.append(rating)
        ClassesActual.append(ClassInfo)
    ClassesActual.sort(key=lambda x: x[-1], reverse=True)
  # filter out items with a low relevance score
    if  number_str == '':
        threshold_score = 0.75
    else:
        threshold_score = 1.5
        # adjust this value to your liking
    ClassesActual = [course for course in ClassesActual if course[-1] >= threshold_score]
    if len(ClassesActual)>10:
        return ClassesActual[:10]
    else:
        return  ClassesActual

