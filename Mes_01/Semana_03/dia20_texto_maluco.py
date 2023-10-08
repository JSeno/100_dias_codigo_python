"""
        Texto maluco
"""
import random

def historia_maluca():
    sujeitos = ['O elefante', 'Um macaco', 'O pirata', 'Um ninja', 'Um alienígena', 'A bruxa', 'O cientista louco', 'O velho careca']
    verbos = ['dançou', 'comeu', 'encontrou', 'hipnotizou', 'construiu', 'teleportou', 'transformou', 'correu']
    objetos = ['uma pizza', 'um foguete', 'um tesouro', 'um dragão', 'um portal interdimensional', 'um chapéu mágico', 'um exército de robôs', 'uma privada']

    historia = []

    for _ in range(5):
        evento = f"{random.choice(sujeitos)} {random.choice(verbos)} {random.choice(objetos)}."
        historia.append(evento)

    introducao = "Numa terra distante, onde a realidade e a loucura se misturam, aconteceu o seguinte:"
    conclusao = "E assim, a louca aventura chegou ao fim, deixando todos se perguntando o que aconteceria a seguir."

    historia = [introducao] + historia + [conclusao]

    return "\n".join(historia)

print(historia_maluca())
