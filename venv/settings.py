class Settings():
    """Класс для хранения всех настроек игры Alien Invasion."""

    def __init__(self):
        """Инициализирует настройки игры."""
        # Параметры экрана
        self.screen_width = 640
        self.screen_height = 480
        self.background_image_path = "assets/background/space.png"
        self.caption = "Space Invasion"
        self.player_ship = "assets/ships/player.png"
        self.player_ship_left = "assets/ships/playerLeft.png"
        self.player_ship_right = "assets/ships/playerRight.png"
        self.player_shield = "assets/objects/shield/shieldBlue.png"
        self.player_speed = 3
        self.enemy_ship = "assets/objects/enemyShip.png"
        self.player_bullet = "assets/shoots/laserGreen.png"