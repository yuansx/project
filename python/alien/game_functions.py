import sys
import pygame
from bullet import Bullet
from alien import Alien

def fire_bullet(ai_settings, screen, ship, bullets):
    if len(bullets) < ai_settings.bullet_allowed:
        bullet = Bullet(ai_settings, screen, ship)
        bullets.add(bullet)

def check_keydown_events(ai_settings, screen, ship, bullets, event):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()

def check_keyup_events(ship, event):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ai_settings, screen, ship, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(ai_settings, screen, ship, bullets, event)
        elif event.type == pygame.KEYUP:
            check_keyup_events(ship, event)

def update_screen(ai_settings, screen, ship, aliens, bullets):
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    aliens.draw(screen)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    pygame.display.flip()

def check_bullet_alien_collisions(ai_settings, screen, bullets, aliens, ship):
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if len(aliens) == 0:
        bullets.empty()
        create_fleet(ai_settings, screen, aliens, ship)

def update_bullet(ai_settings, screen, bullets, aliens, ship):
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    bullets.update()
    check_bullet_alien_collisions(ai_settings, screen, bullets, aliens, ship)

def get_number_aliens_x(screen_width, alien_width):
    available_space_x = screen_width - 2 * alien_width
    return int(available_space_x / (2 * alien_width))

def get_number_aliens_rows(screen_height, alien_height, ship_height):
    available_space_y = screen_height - 3 * alien_height - ship_height
    return int(available_space_y / (2 * alien_height))

def create_alien(ai_settings, screen, aliens, num, row):
    alien = Alien(ai_settings, screen)
    alien.x = alien.rect.width + 2 * alien.rect.width * num
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row
    alien.rect.x = alien.x
    aliens.add(alien)

def create_fleet(ai_settings, screen, aliens, ship):
    alien = Alien(ai_settings, screen)
    numbers = get_number_aliens_x(ai_settings.screen_width, alien.rect.width)
    number_rows = get_number_aliens_rows(ai_settings.screen_height, alien.rect.height, ship.rect.height)

    for row in range(number_rows):
        for num in range(numbers):
            create_alien(ai_settings, screen, aliens, num, row)

def change_fleet_direction(aliens):
    for alien in aliens.sprites():
        alien.rect.y += alien.ai_settings.alien_drop_speed
    alien.ai_settings.alien_direct_right = not alien.ai_settings.alien_direct_right

def check_fleet_edges(aliens):
    for alien in aliens.copy():
        if alien.check_edges():
            return True
    return False

def ship_hit(ai_settings, screen, aliens, ship, stats):
    if stats.ships_left > 0:
        stats.ships_left -= 1
        ship.center_ship(screen)
        aliens.empty()
        create_fleet(ai_settings, screen, aliens, ship)
    else:
        stats.game_active = False
def update_alien(ai_settings, screen, aliens, ship, stats):
    if check_fleet_edges(aliens):
        change_fleet_direction(aliens)
    aliens.update()
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, screen, aliens, ship, stats)

