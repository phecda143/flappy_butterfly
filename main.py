import pygame
import sys


class StartMenu:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        pygame.init()

        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Стартовое меню")

        self.background_image = pygame.image.load("game_background.png")
        self.background_image = pygame.transform.scale(self.background_image, (self.width, self.height))

        # фоновая музыка
        pygame.mixer.music.load("355d5c2bfbdf8e8.mp3")
        pygame.mixer.music.play(-1)

        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)

        # Шрифт
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

            start_button = pygame.Rect(self.width // 2 - 100, self.height // 2 - 50, 200, 50)
            settings_button = pygame.Rect(self.width // 2 - 129, self.height // 2 + 50, 250, 50)
            exit_button = pygame.Rect(self.width // 2 - 100, self.height // 2 + 150, 200, 50)
            pygame.draw.rect(self.screen, self.WHITE, start_button)
            self.draw_text("START", self.BLACK, self.width // 2, self.height // 2 - 25)
            pygame.draw.rect(self.screen, self.WHITE, settings_button)
            self.draw_text("SETTINGS", self.BLACK, self.width // 2, self.height // 2 + 75)
            pygame.draw.rect(self.screen, self.WHITE, exit_button)
            self.draw_text("EXIT", self.BLACK, self.width // 2, self.height // 2 + 175)

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    if start_button.collidepoint(mouse_pos):
                        print("Нажата кнопка Старт")
                    elif settings_button.collidepoint(mouse_pos):
                        print("Нажата кнопка Настройки")
                    elif exit_button.collidepoint(mouse_pos):
                        pygame.quit()
                        sys.exit()


if __name__ == "__main__":
    menu = StartMenu(800, 600)
    menu.show_menu()
