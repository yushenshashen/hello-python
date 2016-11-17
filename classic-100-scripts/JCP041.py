#!/usr/bin/env python
# -*- coding: UTF-8 -*-


class Static:
    StaticVar = 5
    def varfunc(self):
        self.StaticVar += 1
        print self.StaticVar

print Static.StaticVar

a = Static()
for i in range(3):
    a.varfunc()


class sta:
    v = 0
    def varfun(n):
        n.v += 1
        print n.v

print sta.v

a = sta()
for i in range(5):
    a.varfun()