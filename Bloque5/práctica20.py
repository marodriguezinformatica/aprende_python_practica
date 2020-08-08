"""Desarrollar una función que tomando el diccionario de notas que devuelve la función creada en la Práctica 19, 
genere un pdf con las calificaciones finales del alumnado.
El pdf debe constar de 3 columnas: 
La primera columna aparecerá el número de lista del alumno o alumna.
La segunda columna contendrá el nombre y apellido.
La tercera columna contendrá la nota final."""

from práctica19 import calcula_notas
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

def imprime_notas(notas):
    w,h = A4

    pdf = canvas.Canvas("nota_final.pdf",pagesize=A4)

    linea = h - 50
    pdf.setFontSize(16)
    pdf.drawString(50,linea,"Nº")
    pdf.drawString(100,linea,"Apellidos y nombre")
    pdf.drawString(400,linea,"Nota final")

    i = 1
    pdf.setFontSize(14)
    for alumno in notas:
        linea = linea - 20
        pdf.drawString(50,linea,str(i))
        pdf.drawString(100,linea,alumno)
        pdf.drawString(400,linea,str(notas[alumno]))
        i += 1

    pdf.save()



notas = calcula_notas("calificaciones.xlsx")
imprime_notas(notas)