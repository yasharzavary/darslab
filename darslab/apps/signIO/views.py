from django.shortcuts import render


def signI(req):

    return render(req, 'signIO/sinI.html', {'first': True})

def signU(req):
    return render(req, 'signIO/sinO.html')
