import ssl
import hashlib
import datetime
import requests
import io
import sys
import os
import warnings

def Main():
	#Element declaration
	strConfigLF = '\r\n'
	bolError = False
	bolProcessed = False
	bolSuppressSslWarning = False
	strConfigHostname = ''
	strConfigUsername = ''
	strConfigPassword = ''
	strConfigCertificationPath = ''
	strConfigCertificationKeyPath = ''
	strConfigCertificationPassword = ''
	strConfigCertificationUrl = ''
	strConfigUrl = ''
	strConfigLoginUrlTemplate = ''
	strConfigLoginUrlTemplateMiddle = ''
	strConfigProtocoll = ''
	strLogFile = ''
	strConfigName = ''
	#Get Command Line Arguemnt for Config file
	try:
		strConfigFile = sys.argv[1]
		if len(strConfigFile) == 0:
			raise ValueError("Config file wasn't given")
	except:
		WriteLog("Error while open Config File: No Argument given", strLogFile)
		bolError = True
	#Read Config File
	try:
		if os.path.isfile(strConfigFile) == True:
			with open(strConfigFile, 'r') as strConfig:
				for strLine in strConfig:
					if strConfigProtocoll == '':
						bolProcessed = False
					if strLine.lower().startswith('suppresssslwarning'):
						if strLine[strLine.index('=') + 1:len(strLine) - 1] == "true":
							bolSuppressSslWarning = True
						else:
							bolSuppressSslWarning = False
					elif strLine.lower().startswith('hostname='):
						strConfigHostname = strLine[strLine.index('=') + 1:len(strLine) - 1]
					elif strLine.lower().startswith('username='):
						strConfigUsername = strLine[strLine.index('=') + 1:len(strLine) - 1]
					elif strLine.lower().startswith('password='):
						strConfigPassword = strLine[strLine.index('=') + 1:len(strLine) - 1]
					elif strLine.lower().startswith('certificationpath='):
						strConfigCertificationPath = strLine[strLine.index('=') + 1:len(strLine) - 1]
					elif strLine.lower().startswith('certificationkeypath='):
						strConfigCertificationKeyPath = strLine[strLine.index('=') + 1:len(strLine) - 1]
					elif strLine.lower().startswith('logfile='):
						strLogFile = strLine[strLine.index('=') + 1:len(strLine) - 1]
					elif strLine.lower().startswith('certificationurl='):
						strConfigCertificationUrl = strLine[strLine.index('=') + 1:len(strLine) - 1]
					elif strLine.lower().startswith('loginurltemplate='):
						strConfigLoginUrlTemplate = strLine[strLine.index('=') + 1:len(strLine) - 1]
					elif strLine.lower().startswith('loginurltemplatemiddle='):
						strConfigLoginUrlTemplateMiddle = strLine[strLine.index('=') + 1:len(strLine) - 1]
					elif strLine.lower().startswith('url='):
						strConfigUrl = strLine[strLine.index('=') + 1:len(strLine) - 1]
					elif strLine.lower().startswith('certificationpassword='):
						strConfigCertificationPassword = strLine[strLine.index('=') + 1:len(strLine) - 1]
					elif strLine.lower().startswith('protocoll='):
						strConfigProtocoll = strLine[strLine.index('=') + 1:len(strLine) - 1]
					elif strLine.startswith('[') and  strLine[:len(strLine) - 1].endswith(']'):
						if strConfigName == '':
							strConfigName = strLine[1:len(strLine)-2]
						else:
							#Config complete
							if strConfigHostname == '':
								bolError = True
								WriteLog("ERROR: Hostname wasn\'t given.", strLogFile)
							if strConfigPassword == '':
								bolError = True
								WriteLog("ERROR: Password wasn\'t given.", strLogFile)
							if strConfigCertificationPath == '':
								bolError = True
								WriteLog("ERROR: CertificationPath wasn\'t given.", strLogFile)
							if strConfigCertificationKeyPath == '':
								bolError = True
								WriteLog("ERROR: CertificationKeyPath wasn\'t given.", strLogFile)
							if strConfigCertificationUrl == '':
								bolError = True
								WriteLog("ERROR: CertificationUrl wasn\'t given.", strLogFile)
							if strConfigUrl == '':
								bolError = True
								WriteLog("ERROR: Url wasn\'t given.", strLogFile)
							if strConfigLoginUrlTemplate == '':
								bolError = True
								WriteLog("ERROR: LoginUrlTemplate wasn\'t given.", strLogFile)
							if strConfigLoginUrlTemplateMiddle == '':
								bolError = True
								WriteLog("ERROR: LoginUrlTemplateMiddle wasn\'t given.", strLogFile)
							if strConfigProtocoll == '':
								bolError = True
								WriteLog("ERROR: Protocoll wasn\'t given.", strLogFile)
							if bolError == False:
								WriteLog("Change certificate for " + strConfigName, strLogFile)
								UpdateCertificate(strConfigProtocoll + strConfigHostname + strConfigUrl, bolSuppressSslWarning, strConfigProtocoll + strConfigHostname + strConfigLoginUrlTemplate, strConfigLoginUrlTemplateMiddle, strConfigUsername, strConfigPassword, strConfigLF, strConfigCertificationPath, strConfigCertificationKeyPath, strConfigCertificationPassword, strConfigProtocoll + strConfigHostname + strConfigCertificationUrl, strLogFile)
								bolSuppressSslWarning = False
								strConfigHostname = ''
								strConfigUsername = ''
								strConfigPassword = ''
								strConfigCertificationPath = ''
								strConfigCertificationKeyPath = ''
								strConfigCertificationPassword = ''
								strConfigCertificationUrl = ''
								strConfigUrl = ''
								strConfigLoginUrlTemplate = ''
								strConfigLoginUrlTemplateMiddle = ''
								strConfigProtocoll = ''
								strConfigName = strLine[1:len(strLine) - 1]
								bolProcessed = True
	except:
		WriteLog('Error while parsing config file', strLogFile)
	#Config EOF
	if bolProcessed == False:
		if strConfigHostname == '':
			bolError = True
			WriteLog("ERROR: Hostname wasn\'t given.", strLogFile)
		if strConfigPassword == '':
			bolError = True
			WriteLog("ERROR: Password wasn\'t given.", strLogFile)
		if strConfigCertificationPath == '':
			bolError = True
			WriteLog("ERROR: CertificationPath wasn\'t given.", strLogFile)
		if strConfigCertificationKeyPath == '':
			bolError = True
			WriteLog("ERROR: CertificationKeyPath wasn\'t given.", strLogFile)
		if strConfigCertificationUrl == '':
			bolError = True
			WriteLog("ERROR: CertificationUrl wasn\'t given.", strLogFile)
		if strConfigLoginUrlTemplate == '':
			bolError = True
			WriteLog("ERROR: Url wasn\'t given.", strLogFile)
		if strConfigLoginUrlTemplate == '':
			bolError = True
			WriteLog("ERROR: LoginUrlTemplate wasn\'t given.", strLogFile)
		if strConfigLoginUrlTemplateMiddle == '':
			bolError = True
			WriteLog("ERROR: LoginUrlTemplateMiddle wasn\'t given.", strLogFile)
		if strConfigProtocoll == '':
			bolError = True
			WriteLog("ERROR: Protocoll wasn\'t given.", strLogFile)
		if bolError == False:
			WriteLog("Change certificate for " + strConfigName, strLogFile)
			UpdateCertificate(strConfigProtocoll + strConfigHostname + strConfigUrl, bolSuppressSslWarning, strConfigProtocoll + strConfigHostname + strConfigLoginUrlTemplate, strConfigLoginUrlTemplateMiddle, strConfigUsername, strConfigPassword, strConfigLF, strConfigCertificationPath, strConfigCertificationKeyPath, strConfigCertificationPassword, strConfigProtocoll + strConfigHostname + strConfigCertificationUrl, strLogFile)

def UpdateCertificate(strUrl, bolSuppressSslWarning, strLoginUrlTemplate, strLoginUrlTemplateMiddle, strUsername, strPassword, strLF, strCertificationPath, strCertificationKeyPath, strCertificationPassword, strCertificationUrl, strLogFile):
	bolError = False
	# Get Challenge
	try:
		strContent = ""
		if bolSuppressSslWarning:
			strContent = requests.get(strUrl, verify=False).text
		else:
			strContent = requests.get(strUrl).text
	except:
		WriteLog("Error while loading the folowing URL: " + strUrl, strLogFile)
		bolError = True
	#Seperate Challenge
	try:
		strLoginUrlChallenge = strContent[strContent.index("<Challenge>") + 11:strContent.index("<Challenge>") + 19]
	except:
		try:
			strLoginUrlChallenge = strContent[strContent.index("\"challenge\":") +13:strContent.index("\"challenge\":") +21]
		except:
			WriteLog("Error while reading challenge from login page.", strLogFile)
			bolError = True
	#Generate MD5 Hash
	try:
		objMd5 = hashlib.md5()
		objMd5.update((strLoginUrlChallenge + "-" + strPassword).encode('utf-16le'))
		strMd5Hash = objMd5.hexdigest().lower()
		#Make Login Url
		strLoginUrl = strLoginUrlTemplate + strUsername + strLoginUrlTemplateMiddle + strLoginUrlChallenge + "-" + strMd5Hash
	except:
		WriteLog("Error while generating MD5 hash", strLogFile);
		bolError = True
	#Get Overview Site
	try:
		strIndexContent = ""
		if bolSuppressSslWarning:
			strIndexContent = requests.get(strLoginUrl, verify=False).text
		else:
			strIndexContent = requests.get(strLoginUrl).text
	except:
		WriteLog("Error while loading the folowing URL: " + strLoginUrlTemplate, strLogFile)
		bolError = True
	#Get SID from Overview
	try:
		strSid = strIndexContent[strIndexContent.index("?sid=") + 5:strIndexContent.index("?sid=") + 21]
	except:
		try:
			strSid = strIndexContent[strIndexContent.index("<SID>") + 5:strIndexContent.index("<SID>") + 21]
		except:
			WriteLog("Error while reading SID from overview page.",strLogFile)
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
		WriteLog("Error while loading the certification file: " + strCertificationPath, strLogFile)
		bolError = True
	try:
		strCertificationKey = open(strCertificationKeyPath, 'r').read()
	except:
		WriteLog("Error while loading the certification key file: " + strCertificationKeyPath, strLogFile)
		bolError = True
	#Generate certificate response
	if bolError == False:
		strCertData = "--" + strBoundary + strLF + 'Content-Disposition: form-data; name="sid"' + strLF + strLF + strSid + strLF + "--" + strBoundary + strLF + 'ContentDisposition: form-data; name="BoxCertPassword"' + strLF + strLF + strCertificationPassword + strLF + 'Content-Disposition: form-data; name="BoxCertImportFile"; filename="cert.pem"' + strLF + 'Content-Type: application/octet-stream' + strLF + strLF + strCertification + strLF + strCertificationKey + strLF + "--" + strBoundary + "--"
	#Send Certificate to FritzBox
	if bolError == False:
		try:
			if bolSuppressSslWarning:
				warnings.filterwarnings('ignore', 'Unverified HTTPS request')
				strCertificationAnswer = requests.post(strCertificationUrl, strCertData, arrHeaders, verify=False)
				warnings.resetwarnings()
			else:
				strCertificationAnswer = requests.post(strCertificationUrl, strCertData, arrHeaders, verify=True)
			if strCertificationAnswer.status_code == 200:
				bolError = False
				WriteLog("Certificate has been successfully updated.", strLogFile)
			else:
				WriteLog("Error while uploading the certificate: " + strCertificationAnswer.status_code + " " + strCertificationAnswer.content, strLogFile)
		except:
			WriteLog("Error while loading the folowing URL: " + strCertificationUrl, strLogFile)
	#Quit Application
	quit()

def WriteLog( strMessage, strFile ):
	if strFile == "":
		print(strMessage)
	else:
		objLogFile =open(strFile, 'a')
		objLogFile.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " " + strMessage + os.linesep)
		objLogFile.close()

Main()
