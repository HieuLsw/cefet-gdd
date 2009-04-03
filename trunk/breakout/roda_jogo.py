#!/usr/bin/env python
# -*- coding: utf8 -*-

#
# ------- CEFET Game Development Day -------
# >>> http://code.google.com/p/cefet-gdd/
#
#              Jogo: Pega Ladrão!
#
#        Orientador: Alex Tercete
#
#   Desenvolvedores: Ben Shen Deng 
#                    Glauber Rocha
#                    Rodrigo Pereira
#
#            Edição: 2009.1
#

# Inclui as bibliotecas necessárias para o projeto
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../lib'))

# Adiciona o diretório de 'resources'
import pyglet
pyglet.resource.path = ('res',)
pyglet.resource.reindex()

# Roda o jogo
#import gamelib
#gamelib.main()
