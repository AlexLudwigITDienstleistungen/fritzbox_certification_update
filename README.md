SSL certification update for AVM FRITZ!Box
=================

Software to update the SSL certification of any FRITZ!Box.


### Requirements
This tool requires the requests library. You can install it via the following command:

pip install requests


### Configuration
You can configure multiple boxes in the file. Each Box beginns with []. The configuration commands are not case sensitive. All Options with * are required.

[FritzBox Name]					- *Name of the box. This will be shown in the logfile.

Protocoll								- *The Protocoll you want to use. HTTP and HTTPS are supported

Hostname								- *The Hostname or IP Adress of the box. If you are using different Ports you have to add it.

Username								- The username to login to the box.

Password								- *The password to login to the box.

CertificationPath				- *Path to the public certificate.

CertificateKeyPath			- *Path to the private key.

CertificationPassword		- Password for the Keyfile.

LogFile									- The logfile where errors are written. Otherwise the errors are thrown to stdout.

Url											- *Url to login to the box. This shouldn't be changed.

LoginUrlTemplate				- *Url to generate login string. This shouldn't be changed.

LoginUrlTemplateMiddle	- *Url to send the session id to the box. This shouldn't be changed.

CertificationUrl				- *Url to upload the certification files. This shouldn't be changed.


### Usage
Call the script by a python interpreter with the configfile as first parameter.


### Error control
IF any error occurs it will be pasted to the console.
