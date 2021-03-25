#!/usr/bin/env python3
# coding: utf-8
import uuid

import redis


class User:

    command_count = 0

    def __init__(self):
        redis_host = 'localhost'
        redis_port = 6379

        self.r = redis.Redis(host=redis_host, port=redis_port, decode_responses=True)

    def register(self, user, password):
        if self.r.hexists('users', user):
            print('User taken ...')
        else:
            self.r.hset('users', user, password)
            print('User created!')

    def user_list(self):
        for user in self.r.hkeys('users'):
            print(user, end=', ')
        print()

    def forgotten_password(self, user):
        if self.r.hexists('users', user):
            password = 'alma'
            self.r.hset('users', user, password)
            print(password)
        else:
            print('No user by this username ...')

    def __generate_token(self):
        return str(uuid.uuid4())

    def valid_token(self, token):
        return self.r.hexists('tokens', token)

    def login(self, user, password):
        curr_password = self.r.hget('users', user)
        if curr_password is None:
            print('No user like this ...')
            return ''
        else:
            if curr_password == password:
                print('Wrong password')
                return ''
            else:
                token = self.__generate_token()
                if not (self.r.hexists('tokens', token)):
                    self.r.hset('tokens', token, user)
                    return token

    def logged_in_users(self):
        print(self.r.hvals('tokens'))

    def logout(self, token):
        self.r.hdel('tokens', token)

    def command(self, token, command):
        self.r.lpush('command_list_' + token, command)
        self.r.ltrim('command_list_' + token, 0, self.command_count - 1)
        self.command_count += 1

    def command_list(self, token):
        self.r.lrange('command_list_' + token, 0, -1)
