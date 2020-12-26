
from pwsecret import get_secret_key
from pwmenu import menu, create, find, find_accounts
# menu
# 1. Create new password for a site
# 2. Find password for a site
# 3. Find all sites connected to the same email

secret = get_secret_key()

passw = input('Please provide the master password to start using HeraPass: ')

if passw == secret:
    print('it Matched !! You\'re inside the Password Database')

else:
    print('Error, Try Again')
    exit()

choice = menu()
while choice != 'Q':
    if choice == '1':
        create()
    if choice == '2':
        find_accounts()
    if choice == '3':
        find()
    else:
        choice = menu()
exit()
