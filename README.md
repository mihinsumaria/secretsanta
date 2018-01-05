# Secret Santa
A script to send out an automated email assigning gifters to giftees for secret santa.

## Prerequesites
You need python to be installed with the following packages on your system to run the script:
* smtplib
* email
* validate_email

Use the following command to install the last one on your command line interface:
```
pip install validate_email
```

## Using the script
The host or the person who is hosting the secret santa and not participating will have to provide their gmail credentials.

On line 11 enter the host's email in the following manner:
```
fromaddr = "your_email@example.com"
```
On line 19 enter the host's gmail credentials in the following manner:
```
server.login("your_email@example.com", "your_password_here")
```
If you want to use a different gmail client apart from GMail, then on line 17 provide the SMTP server URL and port in the following manner:
```
server = smtplib.SMTP('smtp.gmail.com', 587)
```
Above is the example for GMail.

## Authors
* Mihin Sumaria

## Acknowledgements
* Rishabh Harlalka
* Tanya Sangoi
* Nishita Sheth
* Manan Shah

I ended up writing this script because some of us were separated by hundreds of miles, and could not have drawn names out of a bowl.

## Who do you talk to?
For any questions send an email at mssumaria@wpi.edu
