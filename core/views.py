from django.shortcuts import render
# from reserve.models import Reserver
from django.conf import settings

from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives


def home(request):
    title = 'Inicio'
    return render(request, 'index.html', {
        'title': title
    })

# def index(request):
#     title='Inicio'
#     reserva = Reserver.objects.latest('id')

#     if request.method == 'POST':

#         name = request.POST['name']
#         value = request.POST['value']

#         mail = reserva.email
#         start = reserva.start_and_route
#         end = reserva.end_and_route

#         reserva.ve_name = name
#         reserva.ve_value = value

#         #reserva.save()

#         # Aqui se envia el correo, comenta este send_email si necesitas que no se envie el correo
#         send_email(mail, name, value)

#         print(f"EL email en el momento es {mail} y los datos que se añaden a la base de datos son : {name}, {value}")

#         return render(request, 'index.html',{
#             'title': title
#         })


def about(request):
    return render(request, "about.html", {
        'title': "Nosotros"
    })


def contact(request):
    return render(request, "contact.html", {
        'title': "Contacto"
    })
