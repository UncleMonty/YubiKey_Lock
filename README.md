# YubiKey_Lock

## TABLE OF CONTENTS

1) Project Title
2) Project Description
3) What technologies were used
4) How to Install and Run the Project
5) How to Use the Project
6) Credits

######################################

### 1. Project Title

   - YubiKey Lock

### 2. Project Description

- Motivation:
   
  - I wanted to use my YubiKey token with my Microsoft Account (MSA) on my local hosts.
  - As of writing this (20-March-2024), this is not a feature for MSAs to be used on Windows when logging onto a host.
  - I wanted this application to function similarly to using a Common Access Card (CAC) or a Personal Identity Verification (PIV) token.

- What the application does:
  
   - The application is a proof of concept for YubiKey token's for MSAs.
   - A YubiKey’s serial number (SN) would be bounded to a Windows account (regardless if it was an MSA or local account).
   
      1) The program checks the presence of YubiKey (By Product ID).
      2) Then the program checks for that YubiKey’s SN.
      3) The detected SN must match at least 1 of "EXPECTED_SERIAL_#" variables coded into the file, else the application locks the screen.
      4) The application then checks for the username logging in/currently logged in.
      5) The detected username must match the "EXPECTED_USER" variable coded into the file, else the application locks the screen.
      6) If both constraints are met, the user can log on or remained logged on.
      7) The program checks for these constraints every 1 second.

   - If you remove the YubiKey from its USB port, it will lock the screen within 1 second. 

### 3. What technologies were used:
   
   - Windows 11
   - Visual Studio Code
   - Copilot
   - Chat GPT
   - Python 3.11+

### 4. How to Install and Run the Project

   - FAILSAFE: Configure a local admin account that uses the YubiKey login (https://www.yubico.com/products/computer-login-tools/).
      1) This is going to serve as a failsafe in case the application is misconfigured.
      2) Confirm that this local administrator can read/write to C:\Users\%USER%; Make sure you can access your intended MSA account and its Startup folder.
      3) OPTIONAL: Create a System Restore point prior to downloading and installing the project.
   
   - Download/Configuration
   
      1) While logged into your MSA, download and extract the project.
      2) Move to the \YubiKey_Lock-main\YubiKey_Lock-main\requirements directory and run "python-3.11.8-amd64.exe".
      3) Ensure that "add python.exe to PATH" is checked.
      4) After installing python, run the "install_requirements.bat" in the \YubiKey_Lock-main\YubiKey_Lock-main\requirements directory.
      6) This batch file will run command called pip that is the standard package manager for Python, to install and manage libraries and dependencies from the requirements.txt file.
      7) Your antivirus may flag this process. You may want to action your antivirus to exclude for blocking this process.
      8) After installing both python and requirements, move to the \YubiKey_Lock-main\YubiKey_Lock-main\tools\1_yubikey_username directory of this project and run the "1_yubikey_username.lnk" file.
      9) After identifying what Windows reads as your username, move to the \YubiKey_Lock-main\tools\2_yubikey_sn directory of this project and run the "2_yubikey_sn.lnk" file.
      10) This will open a window that provides what YubiKey SN(s) Windows detects.
      11) Open up the "yubikey_lock.pyw" file in either a Python Interpreter or a text editor.
      12) Replace the values for your SN(s) and username respectively, and uncomment/comment out the lines needed for your instance.
      13) There is a section in which you will need to identify the Product_ID of your YubiKey. There is a hyperlink provided to take you to the page for this. Replace the value from that page to the code accordingly. (OPTIONAL): You can try this hyperlink as well: https://support.yubico.com/hc/en-us/articles/360013714459-How-to-Find-the-USB-Product-ID 
      14) Save your “yubikey_lock.pyw" file.

### 5. How to Use the Project
   
   1) Copy your modified "yubikey_lock.pyw" file.
   2) Navigate to C:\Users\%USER%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup.
   3) alternatively press: "win + r", and type: "shell:startup".
   4) Paste your modified "yubikey_lock.pyw" as a SHORTCUT.
   5) Reboot your device and attempt to login with your YubiKey on your MSA.

### 6. Credits

   This is currently a solo project developed by UncleMonty.
   https://github.com/UncleMonty.

   I am open to taking in technical feedback to make this project less "Proof of Concept", and more of user friendly application.
