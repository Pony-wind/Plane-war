import pygame
import sys
from plane_sprites import *


class PlaneGame(object):
    """飞机大战主游戏"""

    # 游戏初始化
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("冲吧！(作者：Pony)")
        # 1.创建游戏的窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        # 2.创建游戏的时钟
        self.clock = pygame.time.Clock()
        # 3.调用私有方法，创建精灵和精灵组
        self.__creat_sprites()
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 500)
        pygame.time.set_timer(HERO_FIER_EVENT, 500)

    # 创建精灵
    def __creat_sprites(self):
        # 创建背景精灵
        bg1 = Background()
        bg2 = Background(True)
        self.back_group = pygame.sprite.Group(bg1, bg2)

        # 创建敌机精灵组
        self.enemy_group = pygame.sprite.Group()

        # 创建英雄精灵和精灵组
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)

    # 游戏主函数
    def start_game(self):
        while True:
            # 1.设置帧率
            self.clock.tick(FPS)
            # 2.事件监听
            self.__event_handler()
            # 3.碰撞检测
            self.__check_collide()
            # 4.更新/绘制精灵组
            self.__updata_sprites()
            # 5.更新显示
            pygame.display.update()

    # 事件监听
    def __event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()
            elif event.type == CREATE_ENEMY_EVENT:
                enemy1 = Enemy()
                self.enemy_group.add(enemy1)
            elif event.type == HERO_FIER_EVENT:
                self.hero.fire()
        # 监听英雄飞机运动
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_RIGHT]:
            self.hero.speed = 5
        elif keys_pressed[pygame.K_LEFT]:
            self.hero.speed = -5
        # elif keys_pressed[pygame.K_UP]:
        #     self.hero.
        else:
            self.hero.speed = 0

    # 碰撞检测
    def __check_collide(self):
        # 子弹摧毁敌机
        pygame.sprite.groupcollide(self.enemy_group, self.hero.bullets, True, True)
        # 敌机撞毁英雄
        enemies = pygame.sprite.spritecollide(self.hero, self.enemy_group, True)
        if len(enemies) > 0:
            self.hero.kill()
            PlaneGame.__game_over()

    # 更新精灵
    def __updata_sprites(self):
        # 更新背景精灵组
        self.back_group.update()
        self.back_group.draw(self.screen)
        # 更新敌机精灵组
        self.enemy_group.update()
        self.enemy_group.draw(self.screen)
        # 更新英雄精灵组
        self.hero_group.update()
        self.hero_group.draw(self.screen)
        # 更新子弹精灵组
        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)

    # 游戏结束
    @staticmethod
    def __game_over():
        pygame.quit()
        sys.exit()


# 游戏入口
if __name__ == '__main__':
    # 创建游戏对象
    player = PlaneGame()
    # 开始游戏
    player.start_game()
