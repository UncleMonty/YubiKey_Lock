# yubikey_lock

TABLE OF CONTENTS

1) Project Title
2) Project Description
3) What technologies were used
4) How to Install and Run the Project
5) How to Use the Project
6) Credits

######################################

1. Project Title

   - Yubikey Lock

3. Project Description

- Motivation:
   
  - I wanted to use my Yubikey token with my Microsoft Account (MSA) on my local hosts.
  - As of writing this (20-March-2024), this is not a feature for MSAs to be used on Windows when logging onto a host.
  - I wanted this application to function similarly to using a Common Access Card (CAC) or a Personal Identity Verification (PIV) token.

- What the application does:
  
   - The application is a proof of concept for Yubikey token's for MSAs.
   - A Yubikey's serial number (SN) would be bounded to a Windows account (regardless if it was an MSA or local account).
   
      1) The program checks the presence of Yubikey (By Product ID).
      2) Then the program checks for that Yubikey's SN.
      3) The detected SN must match at least 1 of "EXPECTED_SERIAL_#" variables coded into the file, else the application locks the screen.
      4) The application then checks for the username logging in/currently logged in.
      5) The detected username must match the "EXPECTED_USER" variable coded into the file, else the application locks the screen.
      6) If both constraints are met, the user can log on or remained logged on.
      7) The program checks for these constraints every 1 second.

   - If you remove the Yubikey from its USB port, it will lock the screen within 1 second. 

3. What technologies were used:
   
   - Windows 11
   - Visual Studio Code
   - Copilot
   - Chat GPT
   - Python 3.11+

4. How to Install and Run the Project

   - FAILSAFE: Configure a local admin account that uses the Yubikey login (https://www.yubico.com/products/computer-login-tools/).
      1) This is going to serve as a failsafe in case the application is misconfigured.
      2) Confirm that this local administrator can read/write to C:\Users\%USER%; Make sure you can access your intended MSA account and its Startup folder.
   
   - Download/Configuration
   
      1) While logged into your MSA, move to the tools\1_yubikey_username folder of this project and run the "1_yubikey_username.lnk" file.
      2) This will open a window that provides what Windows sees as your username.
      3) While logged into your MSA, move to the tools\2_yubikey_sn folder of this project and run the "2_yubikey_sn.lnk" file.
      4) This will open a window that provides what Yubikey SN(s) Windows detects.
      5) Open up the "yubi_lock.pyw" file in either a Python Interpreter or a text editor.
      6) Replace the values for your SN(s) and username respectively, and uncomment/comment out the lines needed for your instance.
      7) Save your “yubi_lock.pyw" file.

5. How to Use the Project
   
   1) Copy your modified "yubi_lock.pyw" file.
   2) Navigate to C:\Users\%USER%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup.
   3) alternatively press: "win + r", and type: "shell:startup".
   4) Paste your modified "yubikey_lock.pyw" as a SHORTCUT.
   5) Reboot your device and attempt to login with your YubiKey on your MSA.

7. Credits

   This is currently a solo project developed by UncleMonty.
   https://github.com/UncleMonty.
