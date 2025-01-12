import pygame
from pygame.locals import *
import random

pygame.init()

# Initialiser la fenêtre en mode fenêtre
width = 500
height = 500
screen_size = (width, height)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('Car Game')

# Colors
gray = (100, 100, 100)
green = (76, 208, 56)
red = (200, 0, 0)
white = (255, 255, 255)
yellow = (255, 232, 0)

# Road and marker sizes
road_width = 300
marker_width = 10
marker_height = 50

# Lane coordinates
left_lane = 150
center_lane = 250
right_lane = 350
lanes = [left_lane, center_lane, right_lane]

# Road and edge markers
road = (100, 0, road_width, height)
left_edge_marker = (95, 0, marker_width, height)
right_edge_marker = (395, 0, marker_width, height)

# For animating movement of the lane markers
lane_marker_move_y = 0

# Player's starting coordinates
player_x = 250
player_y = 400

# Frame settings
clock = pygame.time.Clock()
fps = 120

# Game settings
gameover = False
speed = 2
score = 0

def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.center = (x, y)
    surface.blit(text_obj, text_rect)

# Vehicle class
class Vehicle(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        pygame.sprite.Sprite.__init__(self)
        image_scale = 45 / image.get_rect().width
        new_width = image.get_rect().width * image_scale
        new_height = image.get_rect().height * image_scale
        self.image = pygame.transform.scale(image, (new_width, new_height))
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

# PlayerVehicle class
class PlayerVehicle(Vehicle):
    def __init__(self, x, y):
        image = pygame.image.load('images/car.png')
        super().__init__(image, x, y)

# Sprite groups
player_group = pygame.sprite.Group()
vehicle_group = pygame.sprite.Group()

# Create the player's car
player = PlayerVehicle(player_x, player_y)
player_group.add(player)

# Load the vehicle images
image_filenames = ['pickup_truck.png', 'semi_trailer.png', 'taxi.png', 'van.png']
vehicle_images = [pygame.image.load('images/' + img) for img in image_filenames]

# Load the crash image
crash = pygame.image.load('images/crash.png')
crash_rect = crash.get_rect()

# Menu principal
def main_menu():
    menu_running = True
    font = pygame.font.Font(pygame.font.get_default_font(), 32)
    
    while menu_running:
        screen.fill(green)
        draw_text('Car Game', font, white, screen, width // 2, height // 4)
        draw_text('1. Nouvelle Partie', font, white, screen, width // 2, height // 2 - 30)
        draw_text('2. Reglages', font, white, screen, width // 2, height // 2)
        draw_text('3. Quitter', font, white, screen, width // 2, height // 2 + 30)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == QUIT:
                menu_running = False
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_1:
                    menu_running = False
                elif event.key == K_2:
                    settings_menu()
                elif event.key == K_3:
                    pygame.quit()
                    exit()

# Menu des réglages
def settings_menu():
    global speed  
    settings_running = True
    font = pygame.font.Font(pygame.font.get_default_font(), 24)
    
    while settings_running:
        screen.fill(green)
        draw_text('Reglages', font, white, screen, width // 2, height // 4)
        draw_text('1. Augmenter vitesse: ' + str(speed), font, white, screen, width // 2, height // 2 - 60)
        draw_text('2. Diminuer vitesse: ' + str(speed), font, white, screen, width // 2, height // 2 - 30)
        draw_text('3. Retour', font, white, screen, width // 2, height // 2 + 30)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == QUIT:
                settings_running = False
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_1:  # Augmenter la vitesse
                    speed = min(10, speed + 1)  # Limiter la vitesse maximale à 10
                elif event.key == K_2:  # Diminuer la vitesse
                    speed = max(1, speed - 1)  # Limiter la vitesse minimale à 1
                elif event.key == K_3:  # Retour
                    settings_running = False

# Affichage
def game_loop():
    global gameover, speed, score, lane_marker_move_y
    running = True
    while running:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            if event.type == KEYDOWN:
                if event.key == K_LEFT and player.rect.center[0] > left_lane:
                    player.rect.x -= 100
                elif event.key == K_RIGHT and player.rect.center[0] < right_lane:
                    player.rect.x += 100
        
        # Draw the grass
        screen.fill(green)
        
        # Draw the road
        pygame.draw.rect(screen, gray, road)
        
        # Draw the edge markers
        pygame.draw.rect(screen, yellow, left_edge_marker)
        pygame.draw.rect(screen, yellow, right_edge_marker)
        
        # Affiche les lignes 
        lane_marker_move_y += speed * 2
        if lane_marker_move_y >= marker_height * 2:
            lane_marker_move_y = 0
        for y in range(marker_height * -2, height, marker_height * 2):
            pygame.draw.rect(screen, white, (left_lane + 45, y + lane_marker_move_y, marker_width, marker_height))
            pygame.draw.rect(screen, white, (center_lane + 45, y + lane_marker_move_y, marker_width, marker_height))
        
        # Affiche le joueur
        player_group.draw(screen)
        
        # Ajoute un véhicule
        if len(vehicle_group) < 2:
            add_vehicle = True
            for vehicle in vehicle_group:
                if vehicle.rect.top < vehicle.rect.height * 1.5:
                    add_vehicle = False
            if add_vehicle:
                lane = random.choice(lanes)
                image = random.choice(vehicle_images)
                vehicle = Vehicle(image, lane, height / -2)
                vehicle_group.add(vehicle)
        
        # Fais bouger les voitures
        for vehicle in vehicle_group:
            vehicle.rect.y += speed
            if vehicle.rect.top >= height:
                vehicle.kill()
                score += 1
                if score > 0 and score % 5 == 0:
                    speed += 1
        
        # Affiche les véhicules
        vehicle_group.draw(screen)
        
        # Affiche le score
        font = pygame.font.Font(pygame.font.get_default_font(), 16)
        text = font.render('Score: ' + str(score), True, white)
        text_rect = text.get_rect()
        text_rect.center = (50, 400)
        screen.blit(text, text_rect)
        
        # Check les collisions
        if pygame.sprite.spritecollide(player, vehicle_group, True):
            gameover = True
            crash_rect.center = [player.rect.center[0], player.rect.top]
        
        # Partie perdue
        if gameover:
            screen.blit(crash, crash_rect)
            pygame.draw.rect(screen, red, (0, 50, width, 100))
            draw_text('Game Over. Press Y to restart, N to quit or M for menu.', font, white, screen, width // 2, 100)
            pygame.display.update()
            
            while gameover:
                clock.tick(fps)
                for event in pygame.event.get():
                    if event.type == QUIT:
                        gameover = False
                        running = False
                    if event.type == KEYDOWN:
                        if event.key == K_y:  # Redémarrer
                            gameover = False
                            speed = 2
                            score = 0
                            vehicle_group.empty()
                            player.rect.center = [player_x, player_y]
                        elif event.key == K_n:  # Quitter
                            gameover = False
                            running = False
                        elif event.key == K_m:  # Retour au menu
                            gameover = False
                            main_menu()
                            game_loop()
        
        pygame.display.update()

main_menu()
game_loop()
pygame.quit()
