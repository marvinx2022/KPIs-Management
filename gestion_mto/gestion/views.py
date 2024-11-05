from django.shortcuts import render
from gestion.models import Parada, Week
from datetime import datetime, timedelta

import plotly.graph_objs as go
from plotly.offline import plot
from django.shortcuts import render


semanas= Week.objects.all()
nombre_semana=[semana.name for semana in semanas]
fecha_inicio=[semana.s_date for semana in semanas]
ots_programadas=[semana.ot_corr+semana.ot_prev for semana in semanas]
ots_realizadas=[semana.ot_corr_exe+semana.ot_prev_exe for semana in semanas]


x_data = nombre_semana
y_data = ots_realizadas


grafica = go.Figure()

grafica.add_trace(go.Bar(
        x=fecha_inicio,
        y=ots_programadas,
        name='Programado',
        marker_color='blue'
    ))


grafica.add_trace(go.Bar(
        x=fecha_inicio,
        y=ots_realizadas,
        name='Realizado',
        marker_color='green'
    ))



    # Guardar la gráfica como un HTML
elemento_grafico_html = plot(grafica, include_plotlyjs=False, output_type='div')


# Para efectos de definir las paradas a mostrar en el index. 
tres_meses_adelante= datetime.now()+timedelta(days=90)
proximas_paradas= Parada.objects.filter(sch_s_date__lte = tres_meses_adelante).order_by("sch_s_date")[0:3]

datos_contexto = {
    "proximas_paradas":proximas_paradas,
    'graph_html': elemento_grafico_html
}


def index(request):

    return render(request, "gestion/index.html", datos_contexto)


def paradas(request):
    return render(request, "gestion/paradas.html")


def analitica(request):
    return render(request, "gestion/analitica.html")


"""def datos(request):
    return render(request, "gestion/datos.html")"""

def datos(request):

    return render(request, 'gestion/datos.html', {'graph_html': elemento_grafico_html})