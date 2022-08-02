from Google import Create_Service
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText # Sirve para autorizar las apis de gmail, los dos ultimos imports

CLIENTE = 'proyecto1googleapi.json'
API = 'gmail'
API_VERSION = 'v1'
SCOPES = ['https://mail.google.com/']
service = Create_Service(CLIENTE, API, API_VERSION, SCOPES)


mimeMessage = MIMEMultipart() # Procedimiento para tener una mejor organización en los emails
mimeMessage['subject'] = 'Hola este es el titulo' # Titulo
emailMsg = 'Buenas, este es el mensaje' # Mensaje
mimeMessage['to'] = 'lisandro.rodriguez.09@hotmail.com' # A que persona enviar el mensaje

mimeMessage.attach(MIMEText(emailMsg, 'plain')) # Este texto contiene texto tipo plain, sin nada modificado, sin letras de color, etcs..

raw_string = base64.urlsafe_b64encode(mimeMessage.as_bytes()).decode()

message = service.users().messages().send(userId = "me", body = {"raw": raw_string}).execute()
