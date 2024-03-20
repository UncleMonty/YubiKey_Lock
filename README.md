# yubikey_lock

What to Include in your README
1. Project Title 

   Yubikey Lock

3. Project Description

    Motivation:
        I wanted to use my Yubikey token with my Microsoft Account (MSA) on my local hosts.
        As of wwriting this (20-March-2024), this is not a feature for MSAs to be used on Windows when logging onto a host.
        I wanted this application to function similairiy to using a Common Access Card (CAC) or a Personal Identity Verfication (PIV) token.
        
    What the application does:
        The application is a proof of concept for Yubikey token's for MSAs.
        A Yubikey's serial number (SN) would be bounded to a Windows account (regardless if it was an MSA or lcoal account).
          1) The program checks the presence of Yubikey (By Product ID)
          2) Then the program checks for that Yubikey's SN.
          3) The detected SN must match at least 1 of "EXPECTED_SERIAL_#" variables coded into the file, else the appplication locks the screen.
          4) The application then checks for the username logging in/currently logged in.
          5) The detected username must match the "EXPECTED_USER" variable coded into the file, else the appplication locks the screen.
          6) If both constraints are met, the user can log on or reamined logged on.
          7) The program checks for these constraints every 1 second.
       If you remove the Yubikey from its USB port, it will lock the screen within 1 second. 
        
    What technmoglies were used:
        Windows 11
        Visual Studio Code
        Copilot
        Chat GPT
        Python 3.+

3. Table of Contents (Optional)
If your README is very long, you might want to add a table of contents to make it easy for users to navigate to different sections easily. It will make it easier for readers to move around the project with ease.

4. How to Install and Run the Project
If you are working on a project that a user needs to install or run locally in a machine like a "POS", you should include the steps required to install your project and also the required dependencies if any.

Provide a step-by-step description of how to get the development environment set and running.

5. How to Use the Project
Provide instructions and examples so users/contributors can use the project. This will make it easy for them in case they encounter a problem – they will always have a place to reference what is expected.

You can also make use of visual aids by including materials like screenshots to show examples of the running project and also the structure and design principles used in your project.

Also if your project will require authentication like passwords or usernames, this is a good section to include the credentials.

6. Include Credits
If you worked on the project as a team or an organization, list your collaborators/team members. You should also include links to their GitHub profiles and social media too.

Also, if you followed tutorials or referenced a certain material that might help the user to build that particular project, include links to those here as well.

This is just a way to show your appreciation and also to help others get a first hand copy of the project.
