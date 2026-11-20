from django.shortcuts import render

def contexto(pagina):
    return {'pagina_actual':pagina,'nombre':'Cefora Rebeca Tum Cuxulic','semestre':'Cuarto semestre','github':'https://github.com/Rebeca-cefy-web'}

def inicio(request): return render(request,'portafolio/inicio.html',contexto('inicio'))
def sobre_mi(request): return render(request,'portafolio/sobre_mi.html',contexto('sobre_mi'))
def habilidades(request): return render(request,'portafolio/habilidades.html',contexto('habilidades'))
def proyectos(request): return render(request,'portafolio/proyectos.html',contexto('proyectos'))
def contacto(request): return render(request,'portafolio/contacto.html',contexto('contacto'))
def error_404_demo(request): return render(request,'portafolio/404.html',contexto('404'))
def error_404(request,exception): return render(request,'portafolio/404.html',contexto('404'),status=404)
