#!/usr/bin/python
# -*- coding: utf-8 -*-
import math
import pygame  # Adicionado para usar o transform.scale
from code.Const import ENTITY_SPEED, ENTITY_SHOT_DELAY, WIN_HEIGHT
from code.EnemyShot import EnemyShot
from code.Entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]

        # MODIFICAÇÃO PARA O BOSS:
        if name == 'Boss':
            # Dobrar o tamanho atual da imagem (largura * 2, altura * 2)
            new_size = (self.rect.width * 2, self.rect.height * 2)
            self.surf = pygame.transform.scale(self.surf, new_size)
            # Atualizar o rect para o novo tamanho, mantendo a posição original
            self.rect = self.surf.get_rect(center=position)

    def move(self):
        # Movimento horizontal padrão (para a esquerda)
        self.rect.centerx -= ENTITY_SPEED[self.name]

        # Movimento em Zigue-zague para o Enemy3
        if self.name == 'Enemy3':
            self.rect.centery += math.sin(self.rect.centerx / 50) * 5

        # Movimento para o Boss
        elif self.name == 'Boss':
            # O Boss oscila verticalmente de forma suave
            self.rect.centery += math.sin(pygame.time.get_ticks() / 500) * 2

        # Garantir que nenhum inimigo saia das bordas verticais da tela
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > WIN_HEIGHT:
            self.rect.bottom = WIN_HEIGHT

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay <= 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            return EnemyShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))