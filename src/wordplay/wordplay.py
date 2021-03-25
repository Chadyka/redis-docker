#!/usr/bin/env python3
# coding: utf-8
from class_wordplay import Wordplay

rf = Wordplay()

# rf.own_set('alma', 5)
# print(rf.own_get('alma'))

rf.new_game('a')

rf.set_word('Anna', 'alma')
rf.set_word('Anna', 'akac')
rf.set_word('Anna', 'eper')
rf.set_word('Anna', 'alma')
rf.set_word('Anna', 'aluminium')
rf.set_word('Anna', 'agar')

rf.set_word('Elek', 'agar')
rf.set_word('Elek', 'elefant')
rf.set_word('Elek', 'alma')
rf.set_word('Elek', 'aforizma')
rf.set_word('Elek', 'angolna')
rf.set_word('Elek', 'ablak')
rf.set_word('Elek', 'asztal')

rf.last_game_highscore()
print()
rf.all_time_highscore()
print()
rf.last_game_winner()
print()
rf.all_time_winner()
