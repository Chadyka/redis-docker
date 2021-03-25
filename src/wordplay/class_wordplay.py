#!/usr/bin/env python3
# coding: utf-8
import redis


class Wordplay():

    def __init__(self):
        redis_host = 'localhost'
        redis_port = 6379

        self.r = redis.Redis(host=redis_host, port=redis_port)

    def own_set(self, key, value):
        self.r.set(key, value)

    def own_get(self, key):
        return self.r.get(key).decode()

    def new_game(self, first_letter):

        self.r.setex('wordplay', first_letter, 60)

        print("Game's on: " + first_letter)

        p = self.r.pipeline()

        for player in self.r.smembers('players'):
            p.delete('wp_' + player.decode())
        p.delete('players')
        p.delete('last_game_highscore')
        p.delete('all_time_highscore')
        p.execute()

    def set_word(self, player, word):
        if not(self.r.exists('wordplay')):
            print('No game running...')
        else:
            char = self.r.get('wordplay').decode()
            if char != word[:1]:
                print('Bad character.')
            else:
                if self.r.sismember('wp_' + player, word):
                    print('Already used ...')
                else:
                    print('Great, ' + player + '!', word)

                    p = self.r.pipeline()
                    p.sadd('wp_' + player, word)
                    p.sadd('players', player)
                    p.zincrby('last_game_highscore', player, 1)
                    p.zincrby('all_time_highscore', player, 1)
                    p.execute()

    def last_game_highscore(self):
        #print(self.r.zrevrange('last_game_highscore', 0, -1, withscores=True))
        for i in self.r.zrevrange('last_game_highscore', 0, -1):
            print(i.decode())
            print(i)

    def all_time_highscore(self):
        #print(self.r.zrevrange('last_game_highscore', 0, -1, withscores=True))
        for i in self.r.zrevrange('all_time_highscore', 0, -1, withscores=True):
            print(i[0].decode())
            print(i[1])

    def last_game_winner(self):
        print(self.r.zrevrange('last_game_highscore', 0, 0)[0].decode())

    def all_time_winner(self):
        print(self.r.zrevrange('all_time_highscore', 0, 0)[0].decode())
