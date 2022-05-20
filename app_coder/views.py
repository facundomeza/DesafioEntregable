from app_coder.models import Familia
from django.template import loader, Template
from django.http import HttpResponse
# Create your views here.

def agregar_miembro(self, nombre: str, edad: int, parentesco: str, fecha_de_nac):
    
    template = loader.get_template('template_familia.html')

    miembro = Familia(nombre=nombre, edad=edad, parentesco=parentesco, fecha_de_nac=fecha_de_nac)
    miembro.save()
    context_dict = {
        'miembro': miembro 
    }

    render = template.render(context_dict)
    return HttpResponse(render)