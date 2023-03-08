import re

email = 'petyh_lalalaka@mail.ru'
email1 = '.petyh_lalalaka@mail.ru'
email2 = 'petyh_la.lalaka@mail.ru'
email3 = 'petyh_lalalaka@mail.ru-'
email4 = 'petyh_lalalaka@-mail.ru'
email5 = 'petyh_lalalaka@mail-.ru'


def check_email(x):
    pattern = r'(^[^.]+[a-zA-Z0-9.!#%&\'*=?^_{|}~]+[^.]+@[^-]+[a-zA-Z0-9-][^-]+\.[a-zA-Z0-9-]+[^-]+$)'
    if re.match(pattern, x) is not None:
        print(f'{x} Email confirmed')
    else:
        print(f'{x} Invalid email')


check_email(email)
check_email(email1)
check_email(email2)
check_email(email3)
check_email(email4)
check_email(email5)
