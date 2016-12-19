import urllib
import md5
import datetime
import requests

# Global String declaration
strUrl = 'http://fritz.box/login_sid.lua'
strLoginUrlTemplate = 'http://fritz.box/login_sid.lua?sid=0000000000000000&username='
strLoginUrlTemplateMiddle = '&response='
strUsername = '';
strPassword = 'Secure'
strLF = "\r\n"
strCertificationPath = "/etc/ssl/certs/certification.crt"
strCertificationKeyPath = "/etc/ssl/private/privatekey.key"
strCertificationPassword = ""
strCertificationUrl = "http://fritz.box/cgi-bin/firmwarecfg"
bolError = False

# Get Challenge
try:
	strContent = urllib.urlopen(strUrl).read()
except:
	print("Error while loading the folowing URL:" + strLF + strUrl)
	bolError = True
#Seperate Challenge
try:
	strLoginUrlChallenge = strContent[strContent.index("<Challenge>") + 11:strContent.index("<Challenge>") + 19]
except:
	print("Error while reading challenge from login page.")
	bolError = True
#Generate MD5 Hash
try:
	strMd5Hash = md5.new((strLoginUrlChallenge + "-" + strPassword).decode('iso-8859-1').encode('utf-16le')).hexdigest().lower()
	#Make Login Url
	strLoginUrl = strLoginUrlTemplate + strUsername + strLoginUrlTemplateMiddle + strLoginUrlChallenge + "-" + strMd5Hash
except:
	print("Error while generating MD5 hash");
	bolError = True
#Get Overview Site
try:
	strIndexContent = urllib.urlopen(strLoginUrl).read()
except:
	print("Error while loading the folowing URL:" + strLF + strLoginUrlTemplate)
	bolError = True
#Get SID from Overview
try:
	strSid = strIndexContent[strIndexContent.index("<SID>") + 5:strIndexContent.index("<SID>") + 21]
except:
	print("Error whil reading SID from overview page.")
	bolError = True
#Generate boundary
strBoundary = "---------------------------" + datetime.datetime.now().strftime("%Y%m%d%H%M%S")
#Generate Content-Type strin
strContentType = "multipart/form-data; boundary=" + strBoundary
arrHeaders = {'Content-Type': strContentType, 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0'}
#Read certification files
try:
	strCertification = open(strCertificationPath, 'r').read()
except:
	print("Error while loading the certification file:" + strLF + strCertificationPath)
	bolError = True
try:
	strCertificationKey = open(strCertificationKeyPath, 'r').read()
except:
	print("Error while loading the certification key file:" + strLF + strCertificationKeyPath)
	bolError = True
#Generate certificate response
if bolError == False:
	strCertData = "--" + strBoundary + strLF + 'Content-Disposition: form-data; name="sid"' + strLF + strLF + strSid + strLF + "--" + strBoundary + strLF + 'ContentDisposition: form-data; name="BoxCertPassword"' + strLF + strLF + strCertificationPassword + strLF + 'Content-Disposition: form-data; name="BoxCertImportFile"; filename="cert.pem"' + strLF + 'Content-Type: application/octet-stream' + strLF + strLF + strCertification + strLF + strCertificationKey + strLF + "--" + strBoundary + "--"
#Send Certificate to FritzBox
if bolError == False:
	try:
		strCertificationAnswer = requests.post(strCertificationUrl, strCertData, arrHeaders)
		if strCertificationAnswer.status_code == 200:
			bolError = False
		else:
			print("Error while uploading the certificate:" + strLF + strCertificationAnswer.content)
	except:
		print("Error while loading the folowing URL:" + strLF + strCertificationUrl)
#Quit Application
quit()
