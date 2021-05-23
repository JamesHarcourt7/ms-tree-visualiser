import pygame


class Button:

    # Button class allows user to click and perform actions within the user interface.

    def __init__(self, position, dimensions, text, t_colour, font_size, active, inactive, func):
        self.position = position
        self.dimensions = dimensions
        self.text = text
        self.t_colour = t_colour
        self.font_size = font_size
        self.active = active
        self.inactive = inactive

        self.colour = self.inactive

        self.font = pygame.font.SysFont('Comic Sans MS', self.font_size)
        self.text_image = self.font.render(self.text, 1, self.t_colour)
        self.text_rect = self.text_image.get_rect(center=[d // 2 for d in self.dimensions])

        self.image = pygame.Surface(self.dimensions)
        self.rect = self.image.get_rect(center=self.position)

        self.func = func

    def draw(self, screen):
        self.update()

        self.image.fill(self.colour)
        self.image.blit(self.text_image, self.text_rect)
        screen.blit(self.image, self.rect)

    def update(self):
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            self.colour = self.active
        else:
            self.colour = self.inactive

    def clicked(self, pos):
        if self.rect.collidepoint(pos):
            return self.func()
        return False


class TextBox:

    # TextBox object displays text to the user.

    def __init__(self, position, dimensions, text, t_colour, font_size, colour):
        self.position = position
        self.dimensions = dimensions
        self.text = text
        self.t_colour = t_colour
        self.font_size = font_size
        self.colour = colour

        self.font = pygame.font.SysFont('Comic Sans MS', self.font_size)
        self.text_image = self.font.render(self.text, 1, self.t_colour)
        self.text_rect = self.text_image.get_rect()

        self.image = pygame.Surface(self.dimensions)
        self.image.set_colorkey((250, 250, 250))
        self.rect = self.image.get_rect(center=self.position)

    def draw(self, screen):
        self.image.fill(self.colour)
        self.image.blit(self.text_image, self.text_rect)
        screen.blit(self.image, self.rect)

    def update(self, new_text):
        self.text = new_text
        self.text_image = self.font.render(self.text, 1, self.t_colour)
