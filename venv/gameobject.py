import pygame

class GameObject(pygame.sprite.Sprite):
    def __init__(self, group, speed = 0, x = 0, y = 0, animation_speed = 80 ):
        pygame.sprite.Sprite.__init__(self)
        """Инициализирует корабль и задает его начальную позицию."""
        self.group = group
        self.image = pygame.Surface((10, 20))
        self.speed = speed
        self.rect = pygame.Rect(0,0,0,0)
        # Устанавливаем начальные координаты
        self.start_y = y
        self.start_x = x

    def set_image(self, image):
        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.top += self.speed

    def set_speed(self, speed):
        self.speed = speed

    def get_x(self):
        return self.rect.left

    def get_y(self):
        return self.rect.top

    def get_height(self):
        return self.rect.height

    def get_widht(self):
        return self.rect.width

    def set_y(self, y):
        self.rect.top = y

    def set_x(self, x):
        self.rect.centerx = x