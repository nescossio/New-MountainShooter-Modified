#!/usr/bin/python
# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod

import pygame.image

from code.Const import ENTITY_HEALTH, ENTITY_DAMAGE, ENTITY_SCORE


class Entity(ABC):
    def __init__(self, name: str, position: tuple):
        self.name = name
        self.surf = pygame.image.load('./asset/' + name + '.png').convert_alpha()
        
        # REMOÇÃO DO FUNDO VERDE:
        # Verifica se a entidade é uma das novas para aplicar o Chroma Key
        if self.name in ['Enemy3', 'Enemy3Shot', 'Boss', 'BossShot']:
            # (0, 255, 0) é o verde puro que usei no fundo das imagens
            self.surf.set_colorkey((0, 255, 0))
            
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = 0
        self.health = ENTITY_HEALTH[self.name]
        self.damage = ENTITY_DAMAGE[self.name]
        self.score = ENTITY_SCORE[self.name]
        self.last_dmg = 'None'

    @abstractmethod
    def move(self):
        pass