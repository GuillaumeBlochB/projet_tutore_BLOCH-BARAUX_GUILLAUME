## TC_03, password forgotten
- There's no way to return to the login page.
- It would be wise to change to an email instead of username
- It would be wise to add something like "si un utilisateur a été trouvé"

## TC_09, verifying list of options
The dropdown's options are prefiltered by the unfiltered list of results. Therefore, the status dropdown first displays "No Records Found" before the unfiltered results are loaded in.
### How to reproduce
- Login
- Access the Recruitment Page
- Click the "Status" dropdown (or any)

## TC_10, verifying presence of results in recruitment after filtering
The results are randomly generated. It is therefore difficult to ensure results would be returned everytime. It is less a defect and more of an inconsistency.
### How to reproduce
- Login
- Access the Recruitment Page
- Filter with Job Title and/or Status
Sometimes no results will show up, sometimes not. 

## TC_11, verifying absence of results in recruitment after filtering
The results are randomly generated. It is therefore difficult to ensure no results would be returned everytime. It is less a defect and more of an inconsistency.
### How to reproduce
- Login
- Access the Recruitment Page
- Filter with Job Title and/or Status
Sometimes results will show up, sometimes not. 

## TC_14, changing password and attempting to log back in with new password
Even though the password change request goes through correctly, logging in with the new password does not work. It would appear as though the password isn't changed.
### How to reproduce
- Login
- Go to change password
- Enter current password
- Enter the same value for new password and confirm password : at least 7 characters, one number.
- Log Out
- Try to log back in with the username and new password
- The "Invalid Credentials" message will appear.
