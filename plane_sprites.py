import random
import pygame

# 窗口常量
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
FPS = 60
# 创建敌机的定时器
CREATE_ENEMY_EVENT = pygame.USEREVENT
# 英雄发射子弹事件
HERO_FIER_EVENT = pygame.USEREVENT + 1


class GameSprite(pygame.sprite.Sprite):
    """飞机大战游戏精灵"""

    def __init__(self, image_name, speed=4):
        # 定义对象的属性
        super().__init__()

        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self, *args, **kwargs):
        # 在屏幕上垂直方向运动
        self.rect.y += self.speed


class Background(GameSprite):
    """游戏背景精灵"""

    def __init__(self, is_alt=False):
        image_name = "./images/background.png"
        super().__init__(image_name)

        if is_alt == True:
            self.rect.bottom = 0

    def update(self, *args, **kwargs):
        # 调用父类方法
        super().update()
        # 判断是否移除屏幕
        if self.rect.y > SCREEN_RECT.height:
            self.rect.y = -self.rect.height


class Enemy(GameSprite):
    """敌机精灵"""

    def __init__(self):
        super().__init__("./images/enemy1.png")
        # 随机敌机速度
        self.speed = random.randint(3, 7)
        # 随机敌机出现位置
        self.rect.bottom = 0
        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0, max_x)

    def update(self):
        super().update()
        # 飞出屏幕自动删除
        if self.rect.y > SCREEN_RECT.height:
            self.kill()

    def __del__(self):
        pass


class Hero(GameSprite):
    """英雄精灵"""

    def __init__(self):
        super().__init__("./images/me1.png", 0)
        # 设置英雄飞机初始位置
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120
        # 创建子弹精灵组
        self.bullets = pygame.sprite.Group()

    def update(self):
        # 水平方向移动
        self.rect.x += self.speed
        # 判断是否飞出边界
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right

    def fire(self):
        # for i in (0,1,2):
        # 创建子弹精灵
        bullet = Bullet()
        # 设置精灵位置
        bullet.rect.y = self.rect.y - 20
        bullet.rect.centerx = self.rect.centerx
        # 将子弹精灵添加到子弹精灵组
        self.bullets.add(bullet)


class Bullet(GameSprite):
    """子弹精灵"""

    def __init__(self):
        super().__init__("./images/bullet2.png", -2)

    def updata(self):
        super().update()
        # 判断子弹是否飞出屏幕
        if self.rect.bottom < 0:
            self.kill()

    def __del__(self):
        pass