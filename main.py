import pygame
import sys

flag = True


class StartMenu:

    def __init__(self, width, height):
        self.width = width
        self.height = height

        pygame.init()

        # окно и заголовок
        if flag:
            self.screen = pygame.display.set_mode((self.width, self.height))
        else:
            pygame.display.toggle_fullscreen()
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
                        start_game = StartGame(self.width, self.height)
                        start_game.running()
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
        if flag:
            self.screen = pygame.display.set_mode((self.width, self.height))
        else:
            self.screen = pygame.display.set_mode((self.width, self.height))
            pygame.display.toggle_fullscreen()
        # фон
        self.background_image = pygame.image.load("game_background.png")
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
        global flag
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
                        if flag:
                            pygame.display.toggle_fullscreen()
                            flag = False
                        else:
                            self.screen = pygame.display.set_mode((self.width, self.height))
                            flag = True
            current_volume = pygame.mixer.music.get_volume()
            self.draw_text(str(round(current_volume, 1)), self.BLACK, self.width // 2 + 100, self.height // 2 - 75)

            pygame.display.flip()


class StartGame:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        # инициализация окна и заголовка
        if flag:
            self.screen = pygame.display.set_mode((self.width, self.height))
        else:
            self.screen = pygame.display.set_mode((self.width, self.height))
            pygame.display.toggle_fullscreen()
        # фон
        self.background_image = pygame.image.load("backgroundforgamestart.png")
        self.background_image = pygame.transform.scale(self.background_image, (self.width, self.height))

        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)

        # шрифт
        self.font = pygame.font.Font("4x4kanafont.ttf", 30)

        # кнопка для возращения на стартовое окно
        self.back_to_startmenu = pygame.Rect(0, 0, 150, 50)
        self.back_to_startmenu_text = "BACK"

        # создание уровня 1
        self.firstlvl_surf = pygame.image.load("1lvl_icon.png")
        self.firstlvl_surf = pygame.transform.scale(self.firstlvl_surf, (150, 350))
        self.firstlvl_rect = self.firstlvl_surf.get_rect(topleft=(150, 150))

        # создание уровня 2
        self.secondlvl_surf = pygame.image.load("2lvl_icon.png")
        self.secondlvl_surf = pygame.transform.scale(self.secondlvl_surf, (150, 350))
        self.secondlvl_rect = self.secondlvl_surf.get_rect(topleft=(340, 150))

        # создание уровня 3
        self.thirdlvl_surf = pygame.image.load("3lvl_icon.png")
        self.thirdlvl_surf = pygame.transform.scale(self.thirdlvl_surf, (150, 350))
        self.thirdlvl_rect = self.thirdlvl_surf.get_rect(topleft=(530, 150))

    def draw_text(self, text, color, x, y):
        text_obj = self.font.render(text, True, color)
        text_rect = text_obj.get_rect()
        text_rect.center = (x, y)
        self.screen.blit(text_obj, text_rect)

    def running(self):
        while True:
            self.screen.blit(self.background_image, (0, 0))

            # инициализация кнопок уровней
            lvl1_button = pygame.Rect(145, 145, 160, 400)
            pygame.draw.rect(self.screen, self.WHITE, lvl1_button)
            self.draw_text("1 LVL", self.BLACK, 230, 525)
            lvl2_button = pygame.Rect(335, 145, 160, 400)
            pygame.draw.rect(self.screen, self.WHITE, lvl2_button)
            self.draw_text("2 LVL", self.BLACK, 420, 525)
            lvl3_button = pygame.Rect(525, 145, 160, 400)
            pygame.draw.rect(self.screen, self.WHITE, lvl3_button)
            self.draw_text("3 LVL", self.BLACK, 610, 525)

            # отображаем уровни
            self.screen.blit(self.firstlvl_surf, self.firstlvl_rect)
            self.screen.blit(self.secondlvl_surf, self.secondlvl_rect)
            self.screen.blit(self.thirdlvl_surf, self.thirdlvl_rect)

            # инициализация кнопки и текста для возвращения
            pygame.draw.rect(self.screen, (255, 255, 255), self.back_to_startmenu)
            back_to_startmenu_button_text = self.font.render(self.back_to_startmenu_text, True, (0, 0, 0))
            self.screen.blit(back_to_startmenu_button_text, (10, 10))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    if self.back_to_startmenu.collidepoint(mouse_pos):
                        return
                    if lvl1_button.collidepoint(mouse_pos):
                        print("УРОВЕНЬ 1")
                    if lvl2_button.collidepoint(mouse_pos):
                        print("УРОВЕНЬ 2")
                    if lvl3_button.collidepoint(mouse_pos):
                        print("УРОВЕНЬ 3")
            pygame.display.update()


class Final_Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        if flag:
            self.screen = pygame.display.set_mode((self.width, self.height))
        else:
            self.screen = pygame.display.set_mode((self.width, self.height))
            pygame.display.toggle_fullscreen()

        self.background_image = pygame.image.load("game_background.png")
        self.background_image = pygame.transform.scale(self.background_image, (self.width, self.height))

        self.font = pygame.font.Font("4x4kanafont.ttf", 25)

        self.back_to_menu_button = pygame.Rect(450, 450, 300, 50)
        self.back_to_menu_text = "BACK TO MENU"

        self.start_again_button = pygame.Rect(50, 450, 300, 50)
        self.start_again_text = "START AGAIN"

        self.game_over = pygame.image.load("game_over.png")
        self.game_over = pygame.transform.scale(self.game_over, (350, 200))

    def draw_text(self, text, color, x, y):
        text_obj = self.font.render(text, True, color)
        text_rect = text_obj.get_rect()
        text_rect.center = (x, y)
        self.screen.blit(text_obj, text_rect)

    def running(self):
        while True:
            self.screen.blit(self.background_image, (0, 0))

            pygame.draw.rect(self.screen, (255, 255, 255), self.back_to_menu_button)
            back_to_menu_button_text = self.font.render(self.back_to_menu_text, True, (0, 0, 0))
            self.screen.blit(back_to_menu_button_text, (465, 460))

            pygame.draw.rect(self.screen, (255, 255, 255), self.start_again_button)
            start_again_text = self.font.render(self.start_again_text, True, (0, 0, 0))
            self.screen.blit(start_again_text, (70, 460))

            self.screen.blit(self.game_over, self.game_over.get_rect(topleft=(self.width // 2 - 175,
                                                                              self.height // 2 - 100)))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    if self.start_again_button.collidepoint(mouse_pos):
                        pass
                        # женя вставь суда игру
                    if self.back_to_menu_button.collidepoint(mouse_pos):
                        stat_menu = StartMenu(self.width, self.height)
                        stat_menu.show_menu()

            pygame.display.update()


menu = StartMenu(800, 600)
menu.show_menu()
