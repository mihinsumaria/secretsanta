import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from validate_email import validate_email

def sendemail(toaddr,body): #Sends Emails	
	fromaddr = "" #Host's Email ID, host is someone who is not participating
	msg = MIMEMultipart()
	msg['From'] = fromaddr
	msg['To'] = toaddr
	msg['Subject'] = "Secret Santa Pairing" #Subject of the email
	msg.attach(MIMEText(body, 'plain'))
	 
	server = smtplib.SMTP('smtp.gmail.com', 587) #SMTP Server for GMail
	server.starttls()
	server.login("", "") #Enter host's login credentials here - Email address and password
	text = msg.as_string()
	server.sendmail(fromaddr, toaddr, text)
	server.quit()

def pairing(givers): #Pairs the gifters and the giftees
	receivers=givers[:]
	pairs=[]
	for i in givers:
		receiver=random.choice(receivers)
		while(receiver==i):
			receiver=random.choice(receivers)
		#print(i[0]+" gives "+receiver[0])
		receivers.remove(receiver)
		pairs.append((i,receiver))
	return pairs

def emailiterate(pairs): #Iterates the sending of email over multiple pairs
	for i in pairs:
		body="Happy Holidays! We have decided to do a Secret Santa, and you are a participant."
		body+=" Find out whose santa you are below.\n"
		body+="You are "+i[1][0]+"'s Santa!\n"
		body+="Gift your giftee before the end of our NYC trip.\n"
		body+="PS: I do not know what the pairings are, don't worry, this is completely anonymous."
		toaddr=i[0][1]
		sendemail(toaddr,body)
	return

def getparticipants(no_of_participants):
	givers=[]
	i=0
	while i<no_of_participants:
		name=input("Enter name of participant "+str(i+1)+": ")
		email=input("Enter email of participant "+str(i+1)+": ")
		if(validate_email(email)): #Validates email IDs
			i+=1
			givers.append([name,email])
		else:
			print("Enter a valid email ID")
	return givers

def main():
	no_of_participants=0
	while no_of_participants<3: #Minimum participants required are 3 in a secret santa
		no_of_participants=int(input("Enter the number of participants: "))
		if(no_of_participants<3):
			print("Minimum number of participants = 3")
	givers=getparticipants(no_of_participants)
	print("Pairing gifters and giftees")
	pairs=pairing(givers)
	print("Emailing santas")
	emailiterate(pairs)
	return

if __name__ == '__main__':
	main()