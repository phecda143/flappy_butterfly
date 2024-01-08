import pygame
import sys


class StartMenu:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        pygame.init()

        # окно и заголовок
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Стартовое меню")

        # загрузка фона
        self.background_image = pygame.image.load("game_background.png")
        self.background_image = pygame.transform.scale(self.background_image, (self.width, self.height))

        # фон. музыка
        pygame.mixer.music.load("355d5c2bfbdf8e8.mp3")
        pygame.mixer.music.play(-1)  # -1 чтобы музыка проигрывалась в бесконечном цикле

        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)

        # шрифт
        self.font = pygame.font.Font("4x4kanafont.ttf", 30)

    def draw_text(self, text, color, x, y):
        text_obj = self.font.render(text, True, color)
        text_rect = text_obj.get_rect()
        text_rect.center = (x, y)
        self.screen.blit(text_obj, text_rect)

    def show_menu(self):
        while True:
            self.screen.blit(self.background_image, (0, 0))

            self.draw_text("FLAPPY BUTTERFLY", self.BLACK, self.width // 1.9, self.height // 4)

            # инициализация кнопок
            start_button = pygame.Rect(self.width // 2 - 100, self.height // 2 - 50, 200, 50)
            settings_button = pygame.Rect(self.width // 2 - 129, self.height // 2 + 50, 250, 50)
            exit_button = pygame.Rect(self.width // 2 - 100, self.height // 2 + 150, 200, 50)
            pygame.draw.rect(self.screen, self.WHITE, start_button)
            self.draw_text("START", self.BLACK, self.width // 2, self.height // 2 - 25)
            pygame.draw.rect(self.screen, self.WHITE, settings_button)
            self.draw_text("SETTINGS", self.BLACK, self.width // 2, self.height // 2 + 75)
            pygame.draw.rect(self.screen, self.WHITE, exit_button)
            self.draw_text("EXIT", self.BLACK, self.width // 2, self.height // 2 + 175)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    if start_button.collidepoint(mouse_pos):
                        print("Начало игры")
                    elif settings_button.collidepoint(mouse_pos):
                        settings = Settings(self.width, self.height)
                        settings.show_settings()
                    elif exit_button.collidepoint(mouse_pos):
                        pygame.quit()
                        sys.exit()

            pygame.display.update()


class Settings:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        # инициализация окна и заголовка
        self.screen = pygame.display.set_mode((self.width, self.height))
        # фон
        self.background_image = pygame.image.load("game_background.png ")
        self.background_image = pygame.transform.scale(self.background_image, (self.width, self.height))

        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)

        # шрифт
        self.font = pygame.font.Font("4x4kanafont.ttf", 30)

        # кнопка для увеличения громкости
        self.volume_up_button = pygame.Rect(self.width // 2 - 250, self.height // 3 + 70, 200, 50)
        self.volume_up_text = "UP"

        # кнопка для уменьшения громкости
        self.volume_down_button = pygame.Rect(self.width // 2 + 30, self.height // 3 + 70, 200, 50)
        self.volume_down_text = "DOWN"

        # кнопка изменения размера окна
        self.fullscreen_button = pygame.Rect(self.width // 2 - 240, self.height // 2 + 60, 480, 50)

    def draw_text(self, text, color, x, y):
        text_obj = self.font.render(text, True, color)
        text_rect = text_obj.get_rect()
        text_rect.center = (x, y)
        self.screen.blit(text_obj, text_rect)

    def show_settings(self):
        while True:
            self.screen.blit(self.background_image, (0, 0))

            # отображаем текст SETTINGS
            self.draw_text("SETTINGS", self.BLACK, self.width // 2, self.height // 4)

            # отображаем кнопку "UP"
            pygame.draw.rect(self.screen, (255, 255, 255), self.volume_up_button)
            volume_up_button_text = self.font.render(self.volume_up_text, True, (165, 42, 42))
            self.screen.blit(volume_up_button_text, (self.width // 2 - 175, self.height // 2 - 20))

            # oтображаем кнопку "DOWN"
            pygame.draw.rect(self.screen, (255, 255, 255), self.volume_down_button)
            volume_down_button_text = self.font.render(self.volume_down_text, True, (165, 42, 42))
            self.screen.blit(volume_down_button_text, (self.width // 2 + 70, self.height // 2 - 20))

            # инициализация кнопок
            volume_button = pygame.Rect(self.width // 2 - 150, self.height // 2 - 100, 300, 50)
            fullscreen_button = pygame.Rect(self.width // 2 - 300, self.height // 2 + 60, 600, 50)
            back_button = pygame.Rect(self.width // 2 - 100, self.height // 2 + 150, 200, 50)

            pygame.draw.rect(self.screen, self.WHITE, volume_button)
            pygame.draw.rect(self.screen, self.WHITE, fullscreen_button)
            pygame.draw.rect(self.screen, self.WHITE, back_button)

            self.draw_text("VOLUME", self.BLACK, self.width // 2 - 50, self.height // 2 - 75)

            self.draw_text("SCREEN MODE: FULL/MIN", self.BLACK, self.width // 2, self.height // 2 + 85)

            self.draw_text("BACK", self.BLACK, self.width // 2, self.height // 2 + 175)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    if back_button.collidepoint(mouse_pos):
                        return

                    # проверка, была ли нажата кнопка "UP"
                    if self.volume_up_button.collidepoint(mouse_pos):
                        current_volume = pygame.mixer.music.get_volume()
                        pygame.mixer.music.set_volume(min(current_volume + 0.1, 1.0))

                        # проверка, была ли нажата кнопка "DOWN"
                    if self.volume_down_button.collidepoint(mouse_pos):
                        current_volume = pygame.mixer.music.get_volume()
                        pygame.mixer.music.set_volume(max(current_volume - 0.1, 0.0))

                    if self.fullscreen_button.collidepoint(mouse_pos):
                        pygame.display.toggle_fullscreen()
            current_volume = pygame.mixer.music.get_volume()
            self.draw_text(str(round(current_volume, 1)), self.BLACK, self.width // 2 + 100, self.height // 2 - 75)

            pygame.display.flip()


menu = StartMenu(800, 600)
menu.show_menu()
