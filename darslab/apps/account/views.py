from django.shortcuts import render
from mysql.connector import connect, Error
from apps.course.models import Course



def register(req):
    name = req.POST.get('name')
    lname = req.POST.get('family_name')
    age = req.POST.get('age')
    level = req.POST.get('level')
    password = req.POST.get('password')
    phone = req.POST.get('phone')
    slug = name + '-' + lname
    active = True
    try:
        with connect(port='3306', user='root', password='mysql12345', database='darslab', host='localhost') as conn:
            curs = conn.cursor()
            curs.execute(f'insert into profile values ("{name}", "{lname}", "{password}", "{phone}", "", "{age}", "{level}", "nophoto.png", "{slug}", "{active}")')
            conn.commit()
    except Error as err:
        return render(req, 'signIO/sinO.html', {'error': True})
    
    courses = Course.objects.all()
    context = {
        'error': False,
        'slug': slug,
        'course': courses,
    }

    return render(req, 'course/cors.html', context)


def login(req):
    username = req.POST.get('name')
    password = req.POST.get('password')

    context = {
        'find': False,
        'first': False,
        }

    with connect(port='3306', user='root', password='mysql12345', database='darslab', host='localhost') as conn:
        curs = conn.cursor()
        curs.execute('select * from account')
        for account in curs:
            if account[0] == username and account[2] == password:
                context['find'] = True
                context['person'] = account

    return render(req, 'signIO/sinI.html', context)
    
    

    
            
    

