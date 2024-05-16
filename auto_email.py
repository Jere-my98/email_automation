import smtplib
import csv
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

my_email = 'justinjerome401@gmail.com'
password_key = 'jftt zcca wvmr pwsr'

# SMTP Server and port no for GMAIL.com
gmail_server = "smtp.gmail.com"
gmail_port = 587

# Starting connection
my_server = smtplib.SMTP(gmail_server, gmail_port)
my_server.ehlo()
my_server.starttls()
  
# Login with your email and password
my_server.login(my_email, password_key)

with open("job_contacts.csv") as csv_file:
    jobs = csv.reader(csv_file)
    header = next(jobs, None)  # Attempt to get the header row
    
    if header is not None:
        for recruiter_name, recruiter_email, organization, job_role in jobs:
            
            recruiter_name = recruiter_name if recruiter_name else "Sir/Madam"
            
            # Create a new message object for each recipient
            message = MIMEMultipart("alternative")
            subject = f'Application for {job_role} at {organization}'.upper()
            message['Subject']=subject
            
            
            # Construct the email content
            email_text = f'''
            
Dear {recruiter_name}, 
            
I am writing to express my keen interest in the {job_role} role at {organization} and to convey my enthusiasm for contributing to your esteemed team. With a solid foundation as a Python developer and a portfolio of diverse projects, I am confident in my ability to excel in this role. 

My skill set encompasses a variety of technical proficiencies, including expertise in Python programming, web development using Flask, Django, and machine learning applications. I am enthusiastic to adapt, explore, and learn under the tutelage of experienced software craftsmen in {organization}. Moreover, my experience as a Computer Science student and a Junior Software Engineer in a start-up company (as can be observed in my resume below) has equipped me with a strong analytical mindset and the ability to adapt to dynamic environments. Whether it's collaborating with cross-functional teams or independently tackling challenges, I thrive on pushing the boundaries of what's possible and delivering high-quality results.

What truly motivates me is the opportunity to make a meaningful impact through technology. I am driven by the prospect of leveraging my skills and experience to contribute to {organization}’s mission of excellence and innovation. I am addicted to value-addition and eager to bring my passion for technology and my dedication to continuous improvement to your tech department.

Thank you for considering my application. I am excited about the possibility of joining your team and contributing to the success of {organization}.
            
I have attached my resumé below. Looking forward to hearing from you.

Thank you for your consideration.
            
Sincerely,

Jeremy Okello
            
'''
            
            # Attach the email content
            message.attach(MIMEText(email_text))

            # Attach resume
            resume_filename = 'resume.pdf'  
            with open(resume_filename, 'rb') as resume_file:
                resume_part = MIMEBase('application', 'octet-stream')
                resume_part.set_payload(resume_file.read())
                
            encoders.encode_base64(resume_part)
            resume_part.add_header('Content-Disposition', f'attachment; filename={resume_filename}')
            message.attach(resume_part)
            
            # Send the email
            my_server.sendmail(
                from_addr=my_email,
                to_addrs=recruiter_email,
                msg=message.as_string()
            )

# Quit the server
my_server.quit()
