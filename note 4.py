import cv2
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import threading
import os

# Email configuration
sender_email = "freezmymr@gmail.com"
receiver_email = "freezmymr@gmail.com"
password = "dnrw mfhm tzgl kvxv"

# instance of MIMEMultipart
msg = MIMEMultipart()

# Add sender and reciver addresses
msg['from'] = sender_email
msg['to'] = receiver_email

# Add a subject 
msg['Subject'] = "Alert people have been surfing"

# start the webcam
vid = cv2.VideoCapture(0)

# Capture a single frame from the webcam
ret, frame = vid.read()

# Save the captured frame as an image
cv2.imwrite("captured_image.jpg", frame)

# Open the captured image file
with open("captured_image.jpg", "rb") as image_file:
    # Create a MIMEImage object
    image = MIMEImage(image_file.read())
    # Attach the image to the email
    msg.attach(image)

# Connect to the SMTP server and send the email
def send_email():
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())

    print("Email sent")

# Send email in a separate thread
email_thread = threading.Thread(target=send_email)
email_thread.start()
email_thread.join()

# Release the webcam
vid.release()

# Remove the captured image file
if os.path.exists("captured_image.jpg"):
    os.remove("captured_image.jpg")

