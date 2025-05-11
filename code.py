import pywhatkit as kit
from datetime import datetime


now = datetime.now()

def send(no, msg):
    hour = now.hour  # Specify the hour in 24-hour format
    minute = now.minute + 2  # Specify the minute
    try:
        kit.sendwhatmsg(no, msg, hour, minute)
        print("Message scheduled successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")


question_name = "What is your name? : "
question_number = "Can I get your contact number please? : "
name = input(question_name)
phone_number = "+91" + input(question_number)
message = "Hello " + name + "! Thanks for coming to my place and hope I am not boring you to death> ;)"

send(phone_number, message)