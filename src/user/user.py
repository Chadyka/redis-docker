#!/usr/bin/env python3
# coding: utf-8
from user_class import User

rf = User()

# rf.register('anna', 'dinnye')
# rf.register('anna', 'dinnye')
#
# rf.register('geza', 'korte')
# rf.register('elek', 'dio')
# rf.register('tivadar', 'eper')
# rf.register('juli', 'malna')

rf.user_list()
rf.forgotten_password()
# rf.forgotten_password('elemer')
# rf.forgotten_password('anna')

token1 = rf.login('john', 'alma')
print(token1)
token2 = rf.login('juli', 'alma')
print(token2)
token3 = rf.login('juli', 'malna')
print(token3)
token7 = rf.login('juli', 'malna')
print(token7)
token4 = rf.login('tivadar', 'eper')
print(token4)
token5 = rf.login('elek', 'dio')
print(token5)
token6 = rf.login('elek', 'dio')
print(token6)

rf.logged_in_users()

print(rf.valid_token(token1))
print(rf.valid_token(token4))

rf.logout(token6)
print()
rf.logged_in_users()
