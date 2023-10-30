"""
Função principal do jogo.
"""


from inicializa_tela_jogo import inicializa
from game_loop import game_loop 

if __name__ == '__main__':
    w, s = inicializa()
    game_loop(w, s) 