import pygame
import sys

def validar_formato_cpf(cpf):
    num_cpf = cpf.replace(".").replace("-", "")
    return (len(cpf) == 14 and
            cpf[3] == "." and
            cpf[7] == "." and
            cpf[11] == "-"
            num_cpf.isdigit())
def validar_formato_cep(cep):
    num_cep = cep.replace("-", "")
    return (len(cep) == 9 and
            cep[5] == '-' and
            num_cep.isdigit())
pygame.init
SCREEN_WIDTH = 800
SCREEN_HIGH = 700
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HIGH))
pygame.display.set_caption("Formulário de Cadastro")
COLOR_INACTIVE = pygame.Color('Lightskyblue3')
COLOR_ACTIVE = pygame.color('dodgerblue2')
COLOR_TEXT = pygame.Color('black')
COLOR_ERROR = pygame.Color('red')
COLOR_SUCCESS = pygame.Color('green')
BACKGROUND_COLOR = (240, 240, 240)
FONT_LABEL = pygame.font.Font(None, 32)
FONT_INPUT = pygame.font.Font(None, 32)
FONT_MESSAGE = pygame.font.Font(None, 28)
FONT_TITLE = pygame.font.Font(None, 50)

class InputBox:
    def __init__(self)