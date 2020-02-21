# Exercise 9-11 Imported Admin
from users_ch9 import User, Admin, Privileges

super_user = Admin('ricky', 'bobby', 'rb@gmail.com', 'IT', 234)

super_user.privileges.show_privileges()