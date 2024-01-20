import pygame
import random
import sys
import os
from pygame.locals import *

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
                        game = ButterflyGame(800, 600)
                        game.run()
                        game.save_score()
                        pygame.quit()
                        sys.exit()
                    if lvl2_button.collidepoint(mouse_pos):
                        print("УРОВЕНЬ 2")
                    if lvl3_button.collidepoint(mouse_pos):
                        print("УРОВЕНЬ 3")
            pygame.display.update()


class Final_Window:
    def __init__(self, width, height, score, bestscore):
        self.width = width
        self.height = height
        self.score = score
        self.best_score = bestscore

        if flag:
            self.screen = pygame.display.set_mode((self.width, self.height))
        else:
            self.screen = pygame.display.set_mode((self.width, self.height))
            pygame.display.toggle_fullscreen()

        self.background_image = pygame.image.load("game_background.png")
        self.background_image = pygame.transform.scale(self.background_image, (self.width, self.height))

        self.font = pygame.font.Font("4x4kanafont.ttf", 25)

        self.score_rect = pygame.Rect(self.width // 2 - 125, self.height // 2 - 250, 250, 50)
        self.bestscore_rect = pygame.Rect(self.width // 2 - 175, self.height // 2 - 170, 350, 50)

        self.back_to_menu_button = pygame.Rect(450, 450, 300, 50)
        self.back_to_menu_text = "BACK TO MENU"

        self.start_again_button = pygame.Rect(50, 450, 300, 50)
        self.start_again_text = "START AGAIN"

        self.game_over = pygame.image.load("game_over.png")
        self.game_over = pygame.transform.scale(self.game_over, (350, 200))

    def running(self):
        while True:
            self.screen.blit(self.background_image, (0, 0))

            pygame.draw.rect(self.screen, (255, 255, 255), self.score_rect)
            pygame.draw.rect(self.screen, (255, 255, 255), self.bestscore_rect)
            score = self.font.render(self.score, True, (0, 0, 0))
            best_score = self.font.render(self.best_score, True, (0, 0, 0))

            pygame.draw.rect(self.screen, (255, 255, 255), self.back_to_menu_button)
            back_to_menu_button_text = self.font.render(self.back_to_menu_text, True, (0, 0, 0))
            self.screen.blit(back_to_menu_button_text, (465, 460))

            pygame.draw.rect(self.screen, (255, 255, 255), self.start_again_button)
            start_again_text = self.font.render(self.start_again_text, True, (0, 0, 0))
            self.screen.blit(start_again_text, (70, 460))

            self.screen.blit(self.game_over, self.game_over.get_rect(topleft=(self.width // 2 - 175,
                                                                              self.height // 2 - 100)))

            self.screen.blit(score, (self.width // 2 - 85, self.height // 2 - 235))
            self.screen.blit(best_score, (self.width // 2 - 150, self.height // 2 - 160))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    if self.start_again_button.collidepoint(mouse_pos):
                        game = ButterflyGame(800, 600)
                        game.run()
                        game.save_score()
                        pygame.quit()
                        sys.exit()
                    if self.back_to_menu_button.collidepoint(mouse_pos):
                        stat_menu = StartMenu(self.width, self.height)
                        stat_menu.show_menu()

            pygame.display.update()


class ButterflyGame:
    def __init__(self, screen_width, screen_height, flag=True):
        self.SCREEN_WIDTH = screen_width
        self.SCREEN_HEIGHT = screen_height

        self.colors = [(173, 216, 230), (255, 182, 193), (128, 0, 128)]
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)

        if flag:
            self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        else:
            self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
            pygame.display.toggle_fullscreen()
        pygame.display.set_caption("Игра с бабочкой")

        self.butterfly_img = pygame.image.load("butterfly_icon.png")
        self.butterfly_img = pygame.transform.scale(self.butterfly_img, (50, 50))

        self.butterfly_rect = self.butterfly_img.get_rect()
        self.butterfly_rect.center = (100, self.SCREEN_HEIGHT // 2)

        self.obstacles = []
        self.obstacle_timer = 0
        self.butterfly_speed = 2

        self.running = True
        self.total_score = 0
        self.level = 1
        self.background_color = None
        self.obstacle_color = None
        self.color_change_interval = 5
        self.paused = False
        self.pause_button = pygame.Rect(screen_width - 100, 10, 80, 40)

        # Создание файла best_score.txt, если его нет
        if not os.path.isfile("best_score.txt"):
            with open("best_score.txt", "w") as file:
                file.write("0")

    def change_colors(self):
        if self.level <= 3 and self.total_score % self.color_change_interval == 0:
            self.background_color = random.choice(self.colors)
            self.obstacle_color = random.choice(self.colors)
            self.color_change_interval += 5

    def show_level_message(self):
        font = pygame.font.Font(None, 72)
        level_message = font.render("Уровень " + str(self.level), True, self.BLACK)
        message_rect = level_message.get_rect(center=(self.SCREEN_WIDTH // 2, self.SCREEN_HEIGHT // 2))
        self.screen.blit(level_message, message_rect)
        pygame.display.flip()
        pygame.time.delay(2000)

    def game_over(self):
        score_text = "SCORE: " + str(self.total_score)
        best_score = self.load_best_score()
        if best_score is not None:
            best_score_text = "BEST SCORE: " + str(best_score)
        else:
            best_score_text = None

        final_window = Final_Window(800, 600, score_text, best_score_text)
        final_window.running()

        pygame.display.flip()
        pygame.time.delay(3000)
    def load_best_score(self):
        best_score = None
        if os.path.isfile("best_score.txt"):
            with open("best_score.txt", "r") as file:
                best_score = int(file.read())
        return best_score

    def save_score(self):
        best_score = self.load_best_score()
        if best_score is None or self.total_score > best_score:
            with open("best_score.txt", "w") as file:
                file.write(str(self.total_score))

    def run(self):
        pygame.init()
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if self.pause_button.collidepoint(event.pos):
                        self.paused = not self.paused

            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP] and self.butterfly_rect.top > 0:
                self.butterfly_rect.y -= 1
            if keys[pygame.K_DOWN] and self.butterfly_rect.bottom < self.SCREEN_HEIGHT:
                self.butterfly_rect.y += 1

            if self.paused:
                continue

            current_time = pygame.time.get_ticks()
            if current_time - self.obstacle_timer > 2000:
                side = random.choice(["top", "bottom", "middle"])

                if side == "top":
                    obstacle_height = random.randint(50, 300)
                    obstacle = pygame.Rect(self.SCREEN_WIDTH, 0, 50, obstacle_height)
                elif side == "bottom":
                    obstacle_height = random.randint(50, 300)
                    obstacle = pygame.Rect(self.SCREEN_WIDTH, self.SCREEN_HEIGHT - obstacle_height, 50, obstacle_height)
                else:
                    obstacle_height = random.randint(50, 300)
                    obstacle_y = random.randint(0, self.SCREEN_HEIGHT - obstacle_height)
                    obstacle = pygame.Rect(self.SCREEN_WIDTH, obstacle_y, 50, obstacle_height)

                self.obstacles.append(obstacle)
                self.obstacle_timer = current_time

            for obstacle in self.obstacles:
                obstacle.x -= 1

                if obstacle.right < 0:
                    self.obstacles.remove(obstacle)
                    self.total_score += 1

            if self.total_score >= self.level * 5:
                self.level += 1
                self.obstacles.clear()
                self.show_level_message()

            butterfly_contour = self.butterfly_img.copy()
            pygame.draw.rect(butterfly_contour, self.BLACK, self.butterfly_rect, 2)

            self.change_colors()

            if self.level <= 3:
                self.screen.fill(self.colors[self.level - 1])
            else:
                self.screen.fill(self.background_color)

            for obstacle in self.obstacles:
                pygame.draw.rect(self.screen, self.BLACK, obstacle, 0)
            self.screen.blit(butterfly_contour, self.butterfly_rect)

            pygame.draw.rect(self.screen, self.WHITE, self.pause_button)
            font = pygame.font.Font(None, 36)
            pause_text = font.render("Пауза (P)", True, self.BLACK)
            self.screen.blit(pause_text, (self.SCREEN_WIDTH - 90, 20))

            font = pygame.font.Font(None, 36)
            score_text = font.render("Счет: " + str(self.total_score), True, self.BLACK)
            level_text = font.render("Уровень: " + str(self.level), True, self.BLACK)
            self.screen.blit(score_text, (10, self.SCREEN_HEIGHT - 60))
            self.screen.blit(level_text, (10, self.SCREEN_HEIGHT - 30))

            pygame.display.flip()

            for obstacle in self.obstacles:
                if self.butterfly_rect.colliderect(obstacle):
                    self.running = False

        self.save_score()
        self.game_over()


menu = StartMenu(800, 600)
menu.show_menu()
