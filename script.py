import smtplib
from email.mime.text import MIMEText

# Configurações do servidor SMTP
smtp_server = 'server.smtp.com'
smtp_port = 587
smtp_username = 'mail@example.com'
smtp_password = '1234'

# Configurações do e-mail
sender = 'spoofer@example.com'
receiver = 'victim@example.com'
subject = 'Assunto do E-mail'
message = 'Conteúdo do E-mail'

# Criação do objeto MIMEText com o conteúdo do e-mail
msg = MIMEText(message)
msg['Subject'] = subject
msg['From'] = sender
msg['To'] = receiver

try:
    # Conexão com o servidor SMTP
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        # Habilita o modo de depuração (opcional)
        server.set_debuglevel(1)

        # Inicia a conexão TLS (STARTTLS)
        server.starttls()

        # Autenticação no servidor SMTP
        server.login(smtp_username, smtp_password)

        # Envio do e-mail
        server.send_message(msg)

    print('E-mail enviado com sucesso!')
except Exception as e:
    print('Falha ao enviar o e-mail:', str(e))
