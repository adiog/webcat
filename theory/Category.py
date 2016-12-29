# -*- coding: utf-8 -*-

"""
This file is a part of webcat project.
Copyright (c) 2016 Aleksander Gajewski <adiog@brainfuck.pl>.
"""

import hashlib
from graphviz import Digraph


class Category(object):
    def __init__(self, objects, morphisms):
        if any([len(object_label) != 1 for object_label in objects]):
            raise RuntimeError()
        else:
            self.objects = objects
        if any([len(morphism) != 2 or morphism[0] not in objects or morphism[1] not in objects for morphism in morphisms]):
            raise RuntimeError()
        else:
            self.morphisms = morphisms

    def hash(self):
        sha1 = hashlib.sha1()
        sha1.update((''.join(self.objects)).encode())
        sha1.update((''.join(self.morphisms)).encode())
        return sha1.hexdigest()

    def render(self):
        url = 'static/render/' + self.hash()
        dot = Digraph(format='svg')
        for o in self.objects:
            dot.node(o)
        dot.edges(self.morphisms)
        dot.render(url)
        return url + '.svg'
