from django.shortcuts import render
from mysql.connector import connect, Error



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
            curs.execute(f'insert into profile values ("{name}", "{lname}", "{password}", "{phone}", "", "{age}", "{level}", "nophoto.png", "{slug}", {active})')
            conn.commit()
    except Error as err:
        print(err)
        return render(req, 'signIO/sinO.html', {'error': True})
    
    context = {
        'error': False,
        'slug': slug,
    }

    return render(req, 'main/index.html', context)


