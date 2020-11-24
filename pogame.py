import pygame

from constants import *
from screen import create_screen, update_screen
from world import create_world

#Ajouter le joueur 


def player (x, y):
    screen.blit(player, (x,y))  
    player = pygame.image.load('jeunechimpanzé')
    
#Prendre ou poser les objets 
def transfer_item(source, target, item):
    if item in source:
        source.remove(item)
        target.append(item)
    return source, target


def run_game(available_items):
    ground = ["jumelles", "couteau", "banane"]
    inventory = ["bateau", "bombe", "fleur", "moto"]
    while True:
        print("sol :", ground, "inventaire :", inventory)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                break
            elif event.type == pygame.KEYDOWN:
                if event.type == pygame.K_RETURN:
                    inventory, ground = transfer_item(inventory, ground, ordre[1])
                elif event.type == pzgame.K_SPACE:
                    ground, inventory = transfer_item(ground, inventory, ordre[1]) 
                    


if __name__ == "__main__":
    run_game(["jumelles", "couteau", "banane", "bateau", "bombe", "fleur", "moto"])


def main():
    # Création du "monde" tel que nous le définissons
    world = create_world()
    # Création des surfaces de dessin
    screen, background = create_screen(world)
    # Création d'une horloge
    clock = pygame.time.Clock()
    # Coordonnées [x, y] du joueur
    player = [0, 0]


    # Les variables qui nous permettent de savoir si notre programme est en cours d'exécution ou s'il doit se terminer.
    alive = True
    running = True

    # On met à jour ce qu'on affiche sur l'écran, et on "pousse" l'aiguille de l'horloge d'un pas.
    update_screen(screen, background, world, player)
    clock.tick()

    # Boucle "quasi" infinie, qui s'arrêtera si le joueur est mort, ou si l'arrêt du programme est demandé.
    while alive and running:
        # À chaque itération, on demande à pygame quels "évènements" se sont passés. Ces évènements sont l'interface
        # qui permet d'interragir avec l'extérieur du programme, et en particulier l'utilisateur (qui utilisera son
        # clavier.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                break
            elif event.type == pygame.KEYDOWN:
                if event.type == pygame.K_DOWN:
                    if  position[1] < HEIGHT - 1:
                        position = (position[0], position[1] + 1)
                
                elif event.type == pygame.K_UP:
                    if position[1] > 0:
                        position = (position[0], position[1] - 1)

                elif event.type == pygame.K_LEFT:
                    if position[0] > 0:
                        position = (position[0] - 1, position[1])

                elif event.type == pygame.K_RIGHT:
                    if position[0] < WIDTH - 1:
                        position = (position[0] + 1, position[1])
            

        # On met à jour ce qu'on affiche sur l'écran, et on "pousse" l'aiguille de l'horloge d'un pas.
        update_screen(screen, background, world, player)
        clock.tick()


if __name__ == "__main__":
    try:
        main()
    finally:
        pygame.quit()
