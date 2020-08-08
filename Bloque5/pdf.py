from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

w,h = A4

pdf = canvas.Canvas("prueba.pdf",pagesize=A4)

pdf.setFillColorRGB(255,0,0)
pdf.setFont("Arial",40)
pdf.drawString(50,h-50,"¡Hola mundo!")

pdf.line(50,500,100,500)
pdf.rect(300,700,50,100)
pdf.circle(100,400,80)

pdf.save()