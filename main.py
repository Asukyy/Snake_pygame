import pygame
import random


# Initialisation de Pygame
pygame.init()

# Création de la fenêtre
window = pygame.display.set_mode((800, 600))
pos_x = 0
pos_y = 0
speed = 3
dir_x = 1
dir_y = 0  # Le serpent commence à se déplacer vers la droite

score = 0
snake_positions = [(pos_x, pos_y)] # liste pour stocker la position du serpent
snake_size = 1

apple_x = random.randint(0, 750)
apple_y = random.randint(0, 550)

# Charger la police de caractères
# font = pygame.font.SysFont("verdana", 30)

# Boucle principale
running = True
while running:
    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    # Mettre à jour la position de la pomme si elle a été mangée
    if pos_x >= apple_x and pos_x <= apple_x + 30 and pos_y >= apple_y and pos_y <= apple_y + 30:
        apple_x = random.randint(0, 750)
        apple_y = random.randint(0, 550)
        snake_size += 1
        score += 1
    # Mettre à jour la position du serpent
    pos_x += dir_x * speed
    pos_y += dir_y * speed
    
    # ajouter la nouvelle position du serpent à la fin de la liste
    snake_positions.append((pos_x, pos_y))
    # si la longueur de la liste dépasse la taille du serpent, supprimer la première position
    if len(snake_positions) > snake_size:
        snake_positions.pop(0)
    
    #si je presse la touche droite
    if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
        dir_x = 1
        dir_y = 0
    #si je presse la touche gauche
    if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
        dir_x = -1
        dir_y = 0
    #si je presse la touche haut
    if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
        dir_x = 0
        dir_y = -1
    #si je presse la touche bas
    if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
        dir_x = 0
        dir_y = 1
        
    #si je touche le bord droit
    if pos_x > 750:
        pos_x = 0
    #si je touche le bord gauche
    if pos_x < 0:
        pos_x = 750
    #si je touche le bord haut
    if pos_y < 0:
        pos_y = 550
    #si je touche le bord bas
    if pos_y > 550:
        pos_y = 0


    # Remplissage de la fenêtre
    window.fill((0, 0, 0))
    
    # Dessiner la pomme
    pygame.draw.rect(window, (255, 0, 0), (apple_x, apple_y, 30, 30))

    # Dessiner le serpent
    for pos in snake_positions:
        pygame.draw.rect(window, (0, 255, 0), (pos[0], pos[1], 50 , 50))

    # Afficher le score
    # score_text = font.render("Score: " + str(score), True, (255, 255, 255))
    # window.blit(score_text, (10, 10))

    # Rafraîchissement de l'écran
    pygame.display.flip()

    # 60 images par seconde
    pygame.time.Clock().tick(60)

pygame.quit()