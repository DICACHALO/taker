
import io  
from reportlab.platypus import SimpleDocTemplate, Paragraph, TableStyle  
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle 
from reportlab.lib import colors  
from reportlab.lib.pagesizes import letter, landscape
from reportlab.platypus import Table, SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT, TA_CENTER
from proyecto.models import Project, User_Project
from requeriments.models import RF, RnF
from .data import rf_data, rnf_data, ipo, team_data
from django.shortcuts import HttpResponse
from specification.models import SRF



def pdf(request, pk=None):  

   pk = 17
   response = HttpResponse(content_type='application/pdf')  
   buff = io.BytesIO()  
   doc = SimpleDocTemplate(buff,  
               pagesize=landscape(letter),  
               rightMargin=40,  
               leftMargin=40,  
               topMargin=60,  
               bottomMargin=18,  
               )  
   categorias = []  
   styles = getSampleStyleSheet()  
   project = Project.objects.filter(id=pk)
   for item in project:
    header = Paragraph(item.title, styles['Title'])  
    categorias.append(header)
    header = Paragraph(item.description, styles['Heading1'])  
    categorias.append(header)
   categorias.append(Spacer(1, 12))  

   header = Paragraph("Requerimientos Funcionales ", styles['Heading2']) 
   categorias.append(Spacer(1, 12))   
   categorias.append(header) 
   headings = ('Título', 'Descripción', 'Prioridad', 'Estado', 'Costo') 
   rf = RF.objects.filter(project=pk) 
   rnf = RnF.objects.filter(project=pk)
   srf = SRF.objects.filter(project=pk)
   team = User_Project.objects.filter(project=pk)
   todascategorias = []
   styles = getSampleStyleSheet()
   styleN = styles["BodyText"]
   styleN.alignment = TA_LEFT
   styleBH = styles["Normal"]
   styleBH.alignment = TA_CENTER

   todascategorias = rf_data(rf, styleN, styleBH)

   t = Table([headings] + todascategorias)  
   t.setStyle(TableStyle(  
     [  
       ('GRID', (0, 0), (4, -1), 1, colors.dodgerblue),  
       ('LINEBELOW', (0, 0), (-1, 0), 2, colors.darkblue),  
       ('BACKGROUND', (0, 0), (-1, 0), colors.dodgerblue)  
     ]  
   ))  
                    
   categorias.append(t) 
   categorias.append(Spacer(1, 12))

   header = Paragraph("IPO (Input, Process y Output)", styles['Heading3']) 
   categorias.append(header) 
   headings = ('Entradas', 'Proceso', 'Salidas') 
   todascategorias = ipo(srf, styleN, styleBH)
   t = Table([headings] + todascategorias)  
   t.setStyle(TableStyle(  
     [  
       ('GRID', (0, 0), (3, -1), 1, colors.dodgerblue),  
       ('LINEBELOW', (0, 0), (-1, 0), 2, colors.darkblue),  
       ('BACKGROUND', (0, 0), (-1, 0), colors.dodgerblue)  
     ]  
   ))  
                    
   categorias.append(t) 


   categorias.append(Spacer(1, 12))  
   categorias.append(Spacer(1, 12))
   categorias.append(Spacer(1, 12))  

   header = Paragraph("Requerimientos no Funcionales ", styles['Heading2']) 
   categorias.append(header) 
   headings = ('Título', 'Descripción', 'Prioridad', 'Estado','Tipo', 'Costo') 
   todascategorias = rnf_data(rnf, styleN, styleBH)

   t = Table([headings] + todascategorias)  
   t.setStyle(TableStyle(  
     [  
       ('GRID', (0, 0), (5, -1), 1, colors.dodgerblue),  
       ('LINEBELOW', (0, 0), (-1, 0), 2, colors.darkblue),  
       ('BACKGROUND', (0, 0), (-1, 0), colors.dodgerblue)  
     ]  
   ))  
                    
   categorias.append(t) 
   categorias.append(Spacer(1, 12)) 



   styles=getSampleStyleSheet()
   styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
   ptext = 'Quisque non urna tortor. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Nunc eu diam risus. Duis luctus interdum elit nec vulputate. Donec vulputate, sem et pretium rhoncus, dolor purus laoreet est, at congue orci velit imperdiet quam. Fusce non risus in turpis efficitur finibus in et ipsum. Nunc pellentesque metus sit amet enim egestas vehicula. Nullam pharetra blandit magna, non tincidunt eros ultrices a. Vivamus lobortis lectus odio, vel luctus justo condimentum nec. Praesent maximus faucibus felis at ultricies. Ut a facilisis risus. Nulla ultricies neque sed ultrices facilisis. Phasellus iaculis imperdiet tellus, ut vulputate arcu porttitor in.'
   categorias.append(Paragraph(ptext, styles["Justify"]))
   categorias.append(Spacer(1, 12))

   header = Paragraph("Interesador (Opcional)", styles['Heading2']) 
   categorias.append(header) 
   headings = ('Usuario', 'Cargo', 'Firma') 
   todascategorias = team_data(team, styleN, styleBH)
   t = Table([headings] + todascategorias)  
   t.setStyle(TableStyle(  
     [  
       ('GRID', (0, 0), (3, -1), 1, colors.dodgerblue),  
       ('LINEBELOW', (0, 0), (-1, 0), 2, colors.darkblue),  
       ('BACKGROUND', (0, 0), (-1, 0), colors.dodgerblue)  
     ]  
   ))  
                    
   categorias.append(t) 

   doc.build(categorias)  
   response.write(buff.getvalue())  
   buff.close()  
   return response  

