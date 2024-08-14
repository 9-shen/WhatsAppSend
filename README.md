# WhatsAppSend Script


## Table of Contents
- [Installation](#installation)
- [Requirements](#requirements)
- [WhatsAppSendSearchBar
](#WhatsAppSendSearchBar)
- [WhatsAppNewInstance](#WhatsAppNewInstance)
- [Contact](#contact)

## Installation

```bash
# WhatsApp Send
git clone https://github.com/9-shen/WhatsAppSend.git
cd WhatsAppSend
pip install -r requirements.txt
```
## Requirements
1 - Prepare your contact list.<br>
2 - Split the number file to maximum 1000 Lines <br>
    <i>You Can Use the split_file_numbers.py</i><br>
3 - We have 2 version of the script : <br>
    3.1 - WhatsApp Send Search Bar <br>
    3.2 - WhatsApp Send New Instance <br>
## WhatsAppSendSearchBar
<ul>
<li>File Name : main.py</li>
<li>Make sure before to run this file import the contact list to your phone</li>
<li>You can use vcf_contacts.py to convert Contact From Csv To Vcf</li>
<li>Then Go to your gmail or your phone and import the Vcf file</li>
<li>Refresh the contact list</li>
<li>You Need to update the pyauto_x and pyauto_y in config file</li>
</ul>

```bash
# config File ( pyauto x and y )
PYAUTO_X = 380
PYAUTO_Y = 310
```
To do This must be run the script : pyauto_screen.py <br>
and get the X,Y Position
```bash
# pyauto_screen.py
python pyauto_screen.py
```
<ul>
<li>Update these lines in main.py</li>
<ul>
<li>Line 8 : change the contacts file name *.csv</li>
<li>Line 11 : Chose the message file</li>
</ul>
<li>Update these lines in Config.py</li>
<ul>
<li>Line 2 : Put the X value</li>
<li>Line 3 : Put the Y value</li>
</ul>
</ul>

Finally run the file main.py
```bash
# main.py
python main.py
```
PS: the file will open the browser and gives you 20 seconds delay to Scan the QR Code<br>
after that the script will automatically send the messages using search bar.

## WhatsAppNewInstance
<ul>
<li>File name : send_msg.py</li>
<li>before run the file please update this Line :</li>
<ul>
    <li>Line 14 : Choose the contact list *.csv</li>
</ul>
</ul>
PS: for this script it will take message randomly from Message folder and send random message each time to avoid spamming

```bash
# send_msg.py
python send_msg.py
```
PS: the file will open the browser and gives you 20 seconds delay to scan the QR Code<br>
after that the script will open new instance each time, if the number has a whatsapp account it will choose randm message to send to, and close the current tab and open a new instance each time

## Contact
For more info : contact@9-shen.com