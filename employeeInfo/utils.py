


from ldap3 import Server, Connection, ALL
from .models import *
# def getUser(usermail):
#     user = User.objects.get(email=usermail)
#     context = {"user_info" : user}
#     return context

def ldapcheck(username, password):
    servername= 'LDAP://10.10.100.12:389'
    server = Server(servername, get_info=ALL)  # define an unsecure LDAP server, requesting info on DSE and schema

    # define the connection
    # connection = Connection(server, auto_bind=True, user='nusher.jamil@mblbd.com', password='Nushit@123456')  # define an ANONYMOUS connection
    connection = Connection(server, user=username, password=password)  # define an ANONYMOUS connection
    # c.search('dc=mblbd,dc=com','(mail=najmus@mblbd.com)',attributes=['displayName'])
    # c.extend.standard.who_am_i()
    # print(type(c))
    # perform the Bind operation
    if not connection.bind():
        print('error in bind ', connection.result['description'])
        return False
    else:
        connection.search('dc=mblbd,dc=com','(mail={})'.format(username),attributes=['displayName'])
        displayname = str(connection.entries[0]).split("displayName:")[-1]
        connection.unbind()
        return True



def checkAuthUser( emailadrress):
    try:
        user = User.objects.get(email=emailadrress)
        if user is not None:
            return True
        else:
            return False
    except Exception as e:
        print(e)
        return False


# def getBranchNameList():
#     queryset = Branch.objects.all()
#     branchlist =  [x.branch_name for x in queryset ]
#     return branchlist


def domainMailCheck(domainMail):
    domainMail = domainMail.lower()
    if(domainMail.endswith('@mblbd.com')):
        return domainMail

    else:
        return domainMail + '@mblbd.com'



from reportlab.lib.pagesizes import letter,landscape
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer,Table, TableStyle, HRFlowable
from reportlab.lib import colors
from reportlab.platypus import Image
from reportlab.platypus import PageBreak
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from .models import Service_request,User # replace with the name of your model

def preview_pdf(request, pk):
     # retrieve the object from the database using its primary key
    my_object = Service_request.objects.get(employee_id=pk)
    my_object_image = User.objects.get(EmployeeID=pk)
    
    # create a buffer for the PDF content
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'filename="entry_preview_{pk}.pdf"'
    
    image_path = my_object_image.signature

     # create a new PDF document
    doc = SimpleDocTemplate(response, pagesize=letter)
    
    # create a stylesheet for the document
    styles = getSampleStyleSheet()
    title_text = "Service/Access Request Form"
    title = Paragraph(title_text, styles["Title"])
    # title.wrapOn(canvas, width, height)
    # title.drawOn(canvas, x, y)

    # create a horizontal separator
    separator = HRFlowable(width="100%", thickness=1, lineCap="round", color="black", spaceBefore=5, spaceAfter=10)
    
    signature_image = Image(image_path, width=100, height=50)
    signature_image.hAlign = 'LEFT'
    signature_image.spaceBefore = 10
    signature_image.spaceAfter = 10
    signature_image.borderColor = colors.black
    signature_image.borderWidth = 1

    
    # create a list to hold the document contents
    elements = []
    
    # create a list to hold the rows of the table
    data = []
    
    # create a counter to keep track of the number of fields
    counter = 0
    
    # iterate over each column value in the object
    for field in my_object._meta.get_fields():
        # skip the primary key and related fields
        if field.name == 'id' or field.one_to_many or field.one_to_one or field.many_to_many:
            continue
        
        # retrieve the column value and convert it to a string
        value = str(getattr(my_object, field.name))
        
        # create a paragraph with the field name and value
        field_name = Paragraph(field.verbose_name.title() + ':', styles['Normal'])
        field_value = Paragraph(value, styles['Normal'])
        
        # add the field name and value to the current row
        if counter % 2 == 0:
            data.append([field_name, field_value])
        else:
            data[-1].extend([field_name, field_value])
        
        # increment the counter
        counter += 1
    
    # create the table
    table = Table(data)
    table.setStyle(TableStyle([
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('TEXTCOLOR', (0,0), (-1,-1), colors.black),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,0), 14),
        ('BOTTOMPADDING', (0,0), (-1,0), 12),
        ('BACKGROUND', (0,0), (-1,0), colors.lightgrey),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.whitesmoke, colors.white]),
        ('GRID', (0,0), (-1,-1), 0.25, colors.grey)
    ]))
    
    # add the table to the document
    # elements.append(Spacer(1, 0.5*inch))
    elements.append(title)
    elements.append(Spacer(1, 0.2*inch))
    elements.append(separator)
    elements.append(table)
    
    # add a page break
    # elements.append(PageBreak())
    elements.append(signature_image)
    
    # add any additional content to the document as needed
    # ...
    
    # add the document contents to the PDF document
    doc.build(elements)
    
    # return the PDF as the response to the request
    return response
