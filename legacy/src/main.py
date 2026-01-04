# /// script
# dependencies = ["pygame-ce"]
# ///
"""
Space Gravity – Land Safely! / ŰRMISSZIÓ – Segíts a Nave!
Educational space lander game for 7-year-olds.
Compatible with pygbag for web deployment.
"""

import asyncio
import pygame
import random
from enum import Enum

# ============================================
# CONSTANTS
# ============================================

SCREEN_WIDTH = 960
SCREEN_HEIGHT = 540
FPS = 60

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
LIGHT_GRAY = (200, 200, 200)
DARK_GRAY = (64, 64, 64)
RED = (255, 80, 80)
GREEN = (80, 255, 80)
BLUE = (80, 150, 255)
YELLOW = (255, 255, 80)
ORANGE = (255, 180, 80)

# Planet colors
COLOR_MOON = (180, 180, 190)
COLOR_MARS = (200, 100, 60)
COLOR_EARTH = (60, 140, 200)

# Physics
GRAVITY_SCALE = 0.15
THRUST_POWER = 15.0 * GRAVITY_SCALE
FUEL_RATE = 18.0

# Lander
LANDER_WIDTH = 30
LANDER_HEIGHT = 40
START_X = SCREEN_WIDTH // 2
START_Y = 80

# Landing pad
PAD_WIDTH = 140
PAD_HEIGHT = 15
PAD_X = SCREEN_WIDTH // 2 - PAD_WIDTH // 2
PAD_Y = SCREEN_HEIGHT - 50

# Planets config
PLANETS = {
    "moon": {"gravity": 1.6 * GRAVITY_SCALE, "fuel": 100, "safe_speed": 55, "color": COLOR_MOON},
    "mars": {"gravity": 3.7 * GRAVITY_SCALE, "fuel": 130, "safe_speed": 45, "color": COLOR_MARS},
    "earth": {"gravity": 9.8 * GRAVITY_SCALE, "fuel": 160, "safe_speed": 35, "color": COLOR_EARTH},
}

# ============================================
# TRANSLATIONS
# ============================================

TEXTS = {
    "hu": {
        "title": "ŰRMISSZIÓ – Segíts Leszállni!",
        "start": "Játék",
        "level_select": "Pálya",
        "credits": "Infó",
        "back": "Vissza",
        "moon": "Hold",
        "mars": "Mars",
        "earth": "Föld",
        "altitude": "Magasság",
        "speed": "Sebesség",
        "fuel": "Üzemanyag",
        "success": "Sikeres Landolás!",
        "score": "Pontszám",
        "play_again": "Újra",
        "failure": "Próbáld Újra!",
        "too_fast": "Túl gyorsan!",
        "out_of_fuel": "Elfogyott az üzemanyag!",
        "missed_pad": "Rossz helyre!",
        "controls": "SPACE = felfelé tolás",
        "lang_toggle": "L = nyelv",
    },
    "en": {
        "title": "SPACE GRAVITY – Land Safely!",
        "start": "Play",
        "level_select": "Level",
        "credits": "Info",
        "back": "Back",
        "moon": "Moon",
        "mars": "Mars",
        "earth": "Earth",
        "altitude": "Altitude",
        "speed": "Speed",
        "fuel": "Fuel",
        "success": "Perfect Landing!",
        "score": "Score",
        "play_again": "Again",
        "failure": "Try Again!",
        "too_fast": "Too fast!",
        "out_of_fuel": "Out of fuel!",
        "missed_pad": "Missed the pad!",
        "controls": "SPACE = thrust up",
        "lang_toggle": "L = language",
    },
}

def txt(lang, key):
    return TEXTS.get(lang, TEXTS["en"]).get(key, key)

# ============================================
# GAME STATE
# ============================================

class State(Enum):
    MENU = 1
    LEVEL_SELECT = 2
    CREDITS = 3
    PLAYING = 4
    SUCCESS = 5
    FAILURE = 6

# ============================================
# LANDER CLASS
# ============================================

class Lander:
    def __init__(self, fuel):
        self.x = START_X
        self.y = START_Y
        self.vy = 0
        self.fuel = fuel
        self.thrust = False
    
    def update(self, dt, gravity):
        self.vy += gravity * dt
        if self.thrust and self.fuel > 0:
            self.vy -= THRUST_POWER * dt
            self.fuel -= FUEL_RATE * dt
            self.fuel = max(0, self.fuel)
        self.y += self.vy * dt
    
    def check_landing(self, safe_speed):
        bottom = self.y + LANDER_HEIGHT // 2
        if bottom >= PAD_Y:
            left = self.x - LANDER_WIDTH // 2
            right = self.x + LANDER_WIDTH // 2
            if left < PAD_X + PAD_WIDTH and right > PAD_X:
                if abs(self.vy) <= safe_speed:
                    return "success"
                return "too_fast"
            return "missed_pad"
        return None
    
    def altitude(self):
        return max(0, PAD_Y - (self.y + LANDER_HEIGHT // 2))

# ============================================
# STARS BACKGROUND
# ============================================

stars = [(random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT - 120)) for _ in range(80)]

def draw_bg(screen, planet):
    screen.fill(BLACK)
    for sx, sy in stars:
        pygame.draw.circle(screen, WHITE, (sx, sy), 1)
    color = PLANETS[planet]["color"]
    pygame.draw.ellipse(screen, color, (0, SCREEN_HEIGHT - 80, SCREEN_WIDTH, 160))
    for _ in range(8):
        cx = random.randint(50, SCREEN_WIDTH - 50)
        cy = random.randint(SCREEN_HEIGHT - 70, SCREEN_HEIGHT - 20)
        pygame.draw.circle(screen, DARK_GRAY, (cx, cy), random.randint(8, 20))

# ============================================
# DRAWING FUNCTIONS
# ============================================

def draw_lander(screen, lander):
    x, y = int(lander.x), int(lander.y)
    pts = [(x, y - LANDER_HEIGHT // 2), (x - LANDER_WIDTH // 2, y + LANDER_HEIGHT // 2), (x + LANDER_WIDTH // 2, y + LANDER_HEIGHT // 2)]
    pygame.draw.polygon(screen, WHITE, pts)
    pygame.draw.polygon(screen, GRAY, pts, 2)
    pygame.draw.circle(screen, BLUE, (x, y - 5), 8)
    if lander.thrust and lander.fuel > 0:
        flame = [(x - 6, y + LANDER_HEIGHT // 2), (x, y + LANDER_HEIGHT // 2 + 18), (x + 6, y + LANDER_HEIGHT // 2)]
        pygame.draw.polygon(screen, ORANGE, flame)
        pygame.draw.polygon(screen, YELLOW, [(x - 3, y + LANDER_HEIGHT // 2), (x, y + LANDER_HEIGHT // 2 + 10), (x + 3, y + LANDER_HEIGHT // 2)])

def draw_pad(screen):
    pygame.draw.rect(screen, GRAY, (PAD_X, PAD_Y, PAD_WIDTH, PAD_HEIGHT))
    pygame.draw.rect(screen, GREEN, (PAD_X + PAD_WIDTH // 4, PAD_Y, PAD_WIDTH // 2, PAD_HEIGHT))
    pygame.draw.rect(screen, WHITE, (PAD_X, PAD_Y, PAD_WIDTH, PAD_HEIGHT), 2)

def draw_hud(screen, lander, planet, lang, font):
    pygame.draw.rect(screen, (30, 30, 40), (10, 10, 200, 110))
    pygame.draw.rect(screen, WHITE, (10, 10, 200, 110), 2)
    
    pname = txt(lang, planet)
    screen.blit(font.render(pname, True, LIGHT_GRAY), (20, 18))
    
    alt = int(lander.altitude())
    screen.blit(font.render(f"{txt(lang, 'altitude')}: {alt}", True, WHITE), (20, 42))
    
    spd = abs(int(lander.vy))
    scolor = GREEN if spd < 40 else YELLOW if spd < 70 else RED
    screen.blit(font.render(f"{txt(lang, 'speed')}: {spd}", True, scolor), (20, 66))
    
    fcolor = GREEN if lander.fuel > 30 else YELLOW if lander.fuel > 10 else RED
    screen.blit(font.render(f"{txt(lang, 'fuel')}: {int(lander.fuel)}", True, fcolor), (20, 90))

def draw_menu(screen, sel, lang, tfont, mfont):
    draw_bg(screen, "moon")
    title = txt(lang, "title")
    ts = tfont.render(title, True, WHITE)
    screen.blit(ts, (SCREEN_WIDTH // 2 - ts.get_width() // 2, 80))
    
    items = [txt(lang, "start"), txt(lang, "level_select"), txt(lang, "credits")]
    for i, item in enumerate(items):
        y = 220 + i * 70
        color = YELLOW if i == sel else WHITE
        if i == sel:
            pygame.draw.rect(screen, DARK_GRAY, (SCREEN_WIDTH // 2 - 120, y - 10, 240, 50))
            pygame.draw.rect(screen, YELLOW, (SCREEN_WIDTH // 2 - 120, y - 10, 240, 50), 2)
        ts = mfont.render(item, True, color)
        screen.blit(ts, (SCREEN_WIDTH // 2 - ts.get_width() // 2, y))
    
    ctrl = f"{txt(lang, 'controls')}  |  {txt(lang, 'lang_toggle')}"
    cs = mfont.render(ctrl, True, GRAY)
    screen.blit(cs, (SCREEN_WIDTH // 2 - cs.get_width() // 2, SCREEN_HEIGHT - 40))

def draw_level_select(screen, sel, lang, tfont, mfont):
    draw_bg(screen, "mars")
    ts = tfont.render(txt(lang, "level_select"), True, WHITE)
    screen.blit(ts, (SCREEN_WIDTH // 2 - ts.get_width() // 2, 80))
    
    planets = ["moon", "mars", "earth"]
    for i, p in enumerate(planets):
        y = 200 + i * 80
        color = YELLOW if i == sel else WHITE
        if i == sel:
            pygame.draw.rect(screen, DARK_GRAY, (SCREEN_WIDTH // 2 - 120, y - 10, 240, 60))
            pygame.draw.rect(screen, YELLOW, (SCREEN_WIDTH // 2 - 120, y - 10, 240, 60), 2)
        ts = mfont.render(txt(lang, p), True, color)
        screen.blit(ts, (SCREEN_WIDTH // 2 - ts.get_width() // 2, y))
    
    # Back option
    y = 200 + 3 * 80
    color = YELLOW if sel == 3 else GRAY
    ts = mfont.render(txt(lang, "back"), True, color)
    screen.blit(ts, (SCREEN_WIDTH // 2 - ts.get_width() // 2, y))

def draw_credits(screen, lang, tfont, mfont):
    draw_bg(screen, "earth")
    ts = tfont.render(txt(lang, "credits"), True, WHITE)
    screen.blit(ts, (SCREEN_WIDTH // 2 - ts.get_width() // 2, 80))
    
    lines = [
        "Educational Space Lander Game",
        "",
        "Teaches:",
        "- Gravity acts continuously",
        "- Braking takes time",
        "- Energy is limited",
        "",
        "Press SPACE to go back"
    ]
    for i, line in enumerate(lines):
        if line:
            ts = mfont.render(line, True, WHITE)
            screen.blit(ts, (SCREEN_WIDTH // 2 - ts.get_width() // 2, 160 + i * 35))

def draw_success(screen, score, lang, tfont, mfont):
    draw_bg(screen, "moon")
    ts = tfont.render(txt(lang, "success"), True, GREEN)
    screen.blit(ts, (SCREEN_WIDTH // 2 - ts.get_width() // 2, 150))
    
    sc = mfont.render(f"{txt(lang, 'score')}: {score}", True, YELLOW)
    screen.blit(sc, (SCREEN_WIDTH // 2 - sc.get_width() // 2, 250))
    
    pa = mfont.render(txt(lang, "play_again"), True, WHITE)
    screen.blit(pa, (SCREEN_WIDTH // 2 - pa.get_width() // 2, 350))
    
    hint = mfont.render("SPACE", True, GRAY)
    screen.blit(hint, (SCREEN_WIDTH // 2 - hint.get_width() // 2, SCREEN_HEIGHT - 40))

def draw_failure(screen, reason, lang, tfont, mfont):
    draw_bg(screen, "mars")
    ts = tfont.render(txt(lang, "failure"), True, RED)
    screen.blit(ts, (SCREEN_WIDTH // 2 - ts.get_width() // 2, 150))
    
    rs = mfont.render(txt(lang, reason), True, YELLOW)
    screen.blit(rs, (SCREEN_WIDTH // 2 - rs.get_width() // 2, 250))
    
    ta = mfont.render(txt(lang, "play_again"), True, WHITE)
    screen.blit(ta, (SCREEN_WIDTH // 2 - ta.get_width() // 2, 350))
    
    hint = mfont.render("SPACE", True, GRAY)
    screen.blit(hint, (SCREEN_WIDTH // 2 - hint.get_width() // 2, SCREEN_HEIGHT - 40))

# ============================================
# MAIN GAME LOOP
# ============================================

async def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Space Gravity – Land Safely!")
    clock = pygame.time.Clock()
    
    tfont = pygame.font.Font(None, 52)
    mfont = pygame.font.Font(None, 36)
    hfont = pygame.font.Font(None, 26)
    
    state = State.MENU
    lang = "en"
    menu_sel = 0
    level_sel = 0
    
    lander = None
    planet = "moon"
    score = 0
    fail_reason = ""
    
    prev_keys = {}
    
    running = True
    while running:
        dt = clock.tick(FPS) / 1000.0
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        keys = pygame.key.get_pressed()
        
        def just(k):
            return keys[k] and not prev_keys.get(k, False)
        
        # Language toggle
        if just(pygame.K_l):
            lang = "hu" if lang == "en" else "en"
        
        # State machine
        if state == State.MENU:
            if just(pygame.K_DOWN) or just(pygame.K_s):
                menu_sel = (menu_sel + 1) % 3
            if just(pygame.K_UP) or just(pygame.K_w):
                menu_sel = (menu_sel - 1) % 3
            if just(pygame.K_SPACE) or just(pygame.K_RETURN):
                if menu_sel == 0:  # Play (go to moon directly)
                    planet = "moon"
                    lander = Lander(PLANETS[planet]["fuel"])
                    state = State.PLAYING
                elif menu_sel == 1:  # Level select
                    level_sel = 0
                    state = State.LEVEL_SELECT
                elif menu_sel == 2:  # Credits
                    state = State.CREDITS
            draw_menu(screen, menu_sel, lang, tfont, mfont)
        
        elif state == State.LEVEL_SELECT:
            if just(pygame.K_DOWN) or just(pygame.K_s):
                level_sel = (level_sel + 1) % 4
            if just(pygame.K_UP) or just(pygame.K_w):
                level_sel = (level_sel - 1) % 4
            if just(pygame.K_SPACE) or just(pygame.K_RETURN):
                if level_sel < 3:
                    planet = ["moon", "mars", "earth"][level_sel]
                    lander = Lander(PLANETS[planet]["fuel"])
                    state = State.PLAYING
                else:
                    state = State.MENU
            if just(pygame.K_ESCAPE):
                state = State.MENU
            draw_level_select(screen, level_sel, lang, tfont, mfont)
        
        elif state == State.CREDITS:
            if just(pygame.K_SPACE) or just(pygame.K_RETURN) or just(pygame.K_ESCAPE):
                state = State.MENU
            draw_credits(screen, lang, tfont, mfont)
        
        elif state == State.PLAYING:
            lander.thrust = keys[pygame.K_SPACE] or keys[pygame.K_UP]
            lander.update(dt, PLANETS[planet]["gravity"])
            
            result = lander.check_landing(PLANETS[planet]["safe_speed"])
            if result:
                if result == "success":
                    fuel_bonus = lander.fuel * 10
                    speed_bonus = (PLANETS[planet]["safe_speed"] - abs(lander.vy)) * 200
                    score = max(0, int(fuel_bonus + speed_bonus))
                    state = State.SUCCESS
                else:
                    fail_reason = result
                    state = State.FAILURE
            
            if lander.fuel <= 0 and lander.vy > 50:
                fail_reason = "out_of_fuel"
                state = State.FAILURE
            
            if just(pygame.K_ESCAPE):
                state = State.MENU
            
            draw_bg(screen, planet)
            draw_pad(screen)
            draw_lander(screen, lander)
            draw_hud(screen, lander, planet, lang, hfont)
        
        elif state == State.SUCCESS:
            if just(pygame.K_SPACE) or just(pygame.K_RETURN):
                level_sel = 0
                state = State.LEVEL_SELECT
            draw_success(screen, score, lang, tfont, mfont)
        
        elif state == State.FAILURE:
            if just(pygame.K_SPACE) or just(pygame.K_RETURN):
                level_sel = 0
                state = State.LEVEL_SELECT
            draw_failure(screen, fail_reason, lang, tfont, mfont)
        
        prev_keys = {k: keys[k] for k in range(512) if k < len(keys) and keys[k]}
        
        pygame.display.flip()
        await asyncio.sleep(0)  # Required for pygbag
    
    pygame.quit()

if __name__ == "__main__":
    asyncio.run(main())
