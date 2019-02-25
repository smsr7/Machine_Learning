import pygame
import numpy as np
class Game:

    def reset(self,render):
        if render == 1:
            self.screen=pygame.display.set_mode([650, 450])
            self.screen.fill([0, 0, 0])
        self.ballX = 325
        self.ballY = 225
        self.board1 = 200
        self.board2 = 0
        if np.random.rand() > .5:
            self.dirX = 10
        else:
            self.dirX = -10
        if np.random.rand() > .5:
            self.dirY = 10
        else:
            self.dirY = -10


        self.done = False
        self.wl = ""
        self.returns = 0
        self.state = [self.board1, self.ballX, self.ballY, self.ballX+self.dirX, self.ballY+self.dirY]
        return self.state
    def step(self, action,render):
        self.reward = 0
        if render == 1:
            self.render1()
        self.ballx, self.bally = self.ballX, self.ballY
        self.board1, self.board2, self.ballX, self.ballY, self.reward, self.done, self.wl, self.returns = self.test(action)
        if render == 1:
            self.render2()
        self.state = [self.board1, self.ballx, self.bally, self.ballX, self.ballY]
        return self.state, self.reward, self.done, self.wl, self.returns

    def render1(self):
        pygame.draw.circle(self.screen, [0,0,0], [self.ballX,self.ballY], 5)
        pygame.draw.rect(self.screen, [0,0,0], [50, self.board1, 6, 25], 0)
        pygame.draw.rect(self.screen, [0,0,0], [600, self.ballY-25, 6, 50], 0)
    def render2(self):
        pygame.draw.circle(self.screen, [100,100,100], [self.ballX,self.ballY], 5)
        pygame.draw.rect(self.screen, [255,255,255], [50, self.board1, 6, 25], 0)
        pygame.draw.rect(self.screen, [255,255,255], [600, self.ballY-25, 6, 50], 0)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
    def test(self, action):
        if action == 1:
            self.board1 = self.board1 + 10
            #self.reward = -5
        if action == 2:
            self.board1 = self.board1 - 10
            #self.reward = -5
        if action == 0:
            self.board1 = self.board1
            self.reward = -1

        if self.ballX >= 650:
            self.reward = 500
            self.done = True
            self.wl = "win"
        if self.ballX <= 0:
            self.reward = -10
            self.done = True
            self.wl = "loss"
        if self.ballY+5 >= 450 or self.ballY-5 <= 0:
            self.dirY = self.dirY * -1

        if self.ballY <= self.board1+27 and self.ballY >= self.board1-3:
            if self.ballX - 50 < 9 and self.ballX -50 > -5:
                self.reward = 10
                self.dirX = self.dirX * -1
                self.returns = self.returns + 1
        if self.board1 > 450 or self.board1 < 25:
            self.reward = -10

        if self.ballY <= self.ballY or self.ballY-5 >= self.ballY:
            if self.ballX - 600 < 10 and self.ballX - 600 > -1:
                self.dirX = self.dirX * -1
        self.ballY = self.ballY + self.dirY
        self.ballX = self.ballX + self.dirX
        return self.board1, self.board2, self.ballX, self.ballY, self.reward, self.done, self.wl, self.returns
