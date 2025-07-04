import pygame
import sys
import random
from datetime import date

# --- Lógica para Calcular a Idade (sem alterações) ---
def calcular_idade(ano_nascimento, mes_nascimento, dia_nascimento):
    """Calcula a idade exata de uma pessoa."""
    hoje = date.today()
    try:
        # Verifica se o ano é razoável para evitar datas muito antigas ou futuras
        if not (1900 < ano_nascimento <= hoje.year):
            return None
        nascimento = date(ano_nascimento, mes_nascimento, dia_nascimento)
    except ValueError:
        return None # Retorna None se a data for inválida (ex: 31 de Fevereiro)
    
    # Garante que a data de nascimento não é no futuro
    if nascimento > hoje:
        return None

    idade = hoje.year - nascimento.year - ((hoje.month, hoje.day) < (nascimento.month, nascimento.day))
    return idade

# --- Função Principal do Pygame (AGORA MAIS VERSÁTIL) ---
def criar_janela_resultado(status: str, mensagem_extra: str = ""):
    """Cria uma janela gráfica com Pygame para mostrar o resultado final."""
    
    pygame.init()

    # Configurações da tela
    LARGURA, ALTURA = 1920, 1080
    tela = pygame.display.set_mode((LARGURA, ALTURA))
    pygame.display.set_caption("Resultado da Verificação")

    # Cores (em formato RGB)
    BRANCO = (255, 255, 255)
    VERMELHO = (200, 0, 0)
    LARANJA_ERRO = (255, 140, 0) # Cor para a tela de erro
    
    cores_festa = [(255, 0, 128), (0, 255, 255), (255, 255, 0), (0, 255, 0), (128, 0, 255)]

    # Fontes
    fonte_titulo = pygame.font.Font(None, 90)
    fonte_subtitulo = pygame.font.Font(None, 45) # Fonte um pouco menor para mensagens de erro

    clock = pygame.time.Clock()

    rodando = True
    while rodando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                rodando = False

        # Lógica de Desenho baseada no status
        if status == "PERMITIDO":
            tela.fill(random.choice(cores_festa))
            texto_titulo = fonte_titulo.render("ACESSO PERMITIDO!", True, BRANCO)
            texto_subtitulo = fonte_subtitulo.render("Bem-vindo(a) à festa!", True, BRANCO)
            rect_titulo = texto_titulo.get_rect(center=(LARGURA / 2, ALTURA / 2 - 40))
            rect_subtitulo = texto_subtitulo.get_rect(center=(LARGURA / 2, ALTURA / 2 + 40))
            tela.blit(texto_titulo, rect_titulo)
            tela.blit(texto_subtitulo, rect_subtitulo)

        elif status == "NEGADO":
            tela.fill(VERMELHO)
            texto_titulo = fonte_titulo.render("ACESSO NEGADO", True, BRANCO)
            texto_subtitulo = fonte_subtitulo.render("Evento para maiores de 18 anos.", True, BRANCO)
            rect_titulo = texto_titulo.get_rect(center=(LARGURA / 2, ALTURA / 2 - 30))
            rect_subtitulo = texto_subtitulo.get_rect(center=(LARGURA / 2, ALTURA / 2 + 40))
            tela.blit(texto_titulo, rect_titulo)
            tela.blit(texto_subtitulo, rect_subtitulo)
            
        elif status == "ERRO":
            tela.fill(LARANJA_ERRO)
            texto_titulo = fonte_titulo.render("ERRO!", True, BRANCO)
            # Usa a mensagem de erro que foi passada para a função
            texto_subtitulo = fonte_subtitulo.render(mensagem_extra, True, BRANCO)
            rect_titulo = texto_titulo.get_rect(center=(LARGURA / 2, ALTURA / 2 - 30))
            rect_subtitulo = texto_subtitulo.get_rect(center=(LARGURA / 2, ALTURA / 2 + 40))
            tela.blit(texto_titulo, rect_titulo)
            tela.blit(texto_subtitulo, rect_subtitulo)


        pygame.display.flip()
        clock.tick(5) 

    pygame.quit()
    sys.exit()


# --- INÍCIO DO PROGRAMA ---
# (A interação inicial continua no terminal)
print("--- SISTEMA DE VERIFICAÇÃO DE IDADE ---")
try:
    ano = int(input("Ano em que nasceu (AAAA): "))
    mes = int(input("Mês em que nasceu (MM):   "))
    dia = int(input("Dia em que nasceu (DD):   "))

    idade = calcular_idade(ano, mes, dia)

    # Se a função de cálculo retornar None, significa que a data é inválida
    if idade is None:
        criar_janela_resultado("ERRO", "Data de nascimento inválida. Tente novamente.")
    else:
        print(f"\nVocê tem {idade} anos. Abrindo tela de verificação...")
        if idade >= 18:
            criar_janela_resultado("PERMITIDO")
        else:
            criar_janela_resultado("NEGADO")

# Se o usuário digitar texto em vez de número
except ValueError:
    criar_janela_resultado("ERRO", "Por favor, digite apenas números para a data.")