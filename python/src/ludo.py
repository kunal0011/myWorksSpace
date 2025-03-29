# --- Ludo Game using Pygame ---
# Final Version: Added Home Entry Squares to Safe Squares

import pygame
import random
import sys
import time
import math
import traceback

# --- Constants ---
WIDTH, HEIGHT = 850, 700
BOARD_OFFSET_X = 25
BOARD_OFFSET_Y = 25
BOARD_SIZE = 650
SQUARE_SIZE = BOARD_SIZE // 15

# Colors
WHITE=(255,255,255); BLACK=(0,0,0); RED=(200,0,0); GREEN=(0,150,0); YELLOW=(200,200,0); BLUE=(0,0,200)
LIGHT_RED=(255,150,150); LIGHT_GREEN=(150,255,150); LIGHT_YELLOW=(255,255,150); LIGHT_BLUE=(150,150,255)
GREY=(180,180,180); DARK_GREY=(100,100,100); GOLD=(200,165,0); BOARD_COLOR=(245,245,220); BORDER_COLOR=(50,50,50)
HIGHLIGHT_YELLOW=(255,255,0); DISABLED_COLOR_FG=(100,100,100); DISABLED_COLOR_BG=(160,160,160); DICE_SIDE_COLOR=(210,210,210)
YARD_MARKER_COLOR = (200, 200, 200)

# Function to darken a color slightly
def darken_color(color, factor=0.7):
    return tuple(max(0, int(c * factor)) for c in color)

# Player Info
PLAYER_COLORS = [RED, GREEN, YELLOW, BLUE]; PLAYER_NAMES = ["Red", "Green", "Yellow", "Blue"]; LIGHT_PLAYER_COLORS = [LIGHT_RED, LIGHT_GREEN, LIGHT_YELLOW, LIGHT_BLUE]
DARKER_PLAYER_COLORS = [darken_color(c, 0.6) for c in PLAYER_COLORS]
DARKEST_PLAYER_COLORS = [darken_color(c, 0.4) for c in PLAYER_COLORS]

# Game States
STATE_ROLL_DICE=0; STATE_SELECT_TOKEN=1; STATE_ANIMATING=2; STATE_GAME_OVER=3

# Animation Constants
ANIMATION_DURATION=0.4; DICE_ANIM_DURATION=0.3; HIGHLIGHT_PULSE_SPEED=2.5; PERSPECTIVE_OFFSET_X=8; PERSPECTIVE_OFFSET_Y=8

# --- Path Definitions ---
MAIN_PATH=[(6,1),(6,2),(6,3),(6,4),(6,5),(5,6),(4,6),(3,6),(2,6),(1,6),(0,6),(0,7),(0,8),(1,8),(2,8),(3,8),(4,8),(5,8),(6,9),(6,10),(6,11),(6,12),(6,13),(6,14),(7,14),(8,14),(8,13),(8,12),(8,11),(8,10),(8,9),(9,8),(10,8),(11,8),(12,8),(13,8),(14,8),(14,7),(14,6),(13,6),(12,6),(11,6),(10,6),(9,6),(8,5),(8,4),(8,3),(8,2),(8,1),(8,0),(7,0),(6,0)]
HOME_STRETCHES={RED:[(7,1),(7,2),(7,3),(7,4),(7,5),(7,6)], GREEN:[(1,7),(2,7),(3,7),(4,7),(5,7),(6,7)], YELLOW:[(7,13),(7,12),(7,11),(7,10),(7,9),(7,8)], BLUE:[(13,7),(12,7),(11,7),(10,7),(9,7),(8,7)]}
START_INDICES = { RED: 0, GREEN: 13, YELLOW: 26, BLUE: 39 }

# --- SAFE_SQUARES_INDICES Updated to include home entry squares ---
SAFE_SQUARES_INDICES = [
    8, 21, 34, 47, # Standard star squares
    13, 26, 39, 0  # Squares just before turning into home stretch
]

YARD_POS_OFFSETS = [(1.5 + 0.75, 1.5 + 0.75), (1.5 + 0.75, 1.5 + 2.25), (1.5 + 2.25, 1.5 + 0.75), (1.5 + 2.25, 1.5 + 2.25)]
YARD_CENTERS_GRID = { RED: (0, 0), GREEN: (0, 9), YELLOW: (9, 9), BLUE: (9, 0) }
HOME_CENTERS_GRID = { RED: (7, 7), GREEN: (7, 7), YELLOW: (7, 7), BLUE: (7, 7) }

# --- Helper Functions ---
def lerp(a, b, t): return a + (b - a) * t
def ease_in_out_cubic(t): return 4 * t**3 if t < 0.5 else 1 - pow(-2 * t + 2, 3) / 2
def get_screen_coords(grid_row, grid_col):
    try: x = BOARD_OFFSET_X + float(grid_col) * SQUARE_SIZE + SQUARE_SIZE / 2.0; y = BOARD_OFFSET_Y + float(grid_row) * SQUARE_SIZE + SQUARE_SIZE / 2.0; return int(round(x)), int(round(y))
    except Exception as e: print(f"Err get_screen_coords: {e}"); traceback.print_exc(); return BOARD_OFFSET_X, BOARD_OFFSET_Y
def get_grid_coords(screen_x, screen_y):
    if not (BOARD_OFFSET_X <= screen_x < BOARD_OFFSET_X + BOARD_SIZE and BOARD_OFFSET_Y <= screen_y < BOARD_OFFSET_Y + BOARD_SIZE): return None
    try: grid_col = int((screen_x - BOARD_OFFSET_X) // SQUARE_SIZE); grid_row = int((screen_y - BOARD_OFFSET_Y) // SQUARE_SIZE); grid_col = max(0, min(grid_col, 14)); grid_row = max(0, min(grid_row, 14)); return grid_row, grid_col
    except Exception as e: print(f"Err get_grid_coords: {e}"); traceback.print_exc(); return None


# --- draw_board --- (Will draw crosses on new safe squares automatically)
def draw_board(screen):
    """Draws Ludo board - Smaller White Box, Updated Yard Markers"""
    try:
        screen.fill(BORDER_COLOR)
        pygame.draw.rect(screen, BOARD_COLOR, (BOARD_OFFSET_X, BOARD_OFFSET_Y, BOARD_SIZE, BOARD_SIZE))
        yard_size=SQUARE_SIZE*6
        pygame.draw.rect(screen,LIGHT_RED,(BOARD_OFFSET_X,BOARD_OFFSET_Y,yard_size,yard_size)); pygame.draw.rect(screen,LIGHT_GREEN,(BOARD_OFFSET_X+SQUARE_SIZE*9,BOARD_OFFSET_Y,yard_size,yard_size))
        pygame.draw.rect(screen,LIGHT_YELLOW,(BOARD_OFFSET_X+SQUARE_SIZE*9,BOARD_OFFSET_Y+SQUARE_SIZE*9,yard_size,yard_size)); pygame.draw.rect(screen,LIGHT_BLUE,(BOARD_OFFSET_X,BOARD_OFFSET_Y+SQUARE_SIZE*9,yard_size,yard_size))
        inner_box_edge_squares = 3; inner_box_size_px = SQUARE_SIZE * inner_box_edge_squares; yard_padding_px = (yard_size - inner_box_size_px) // 2; br=5
        pygame.draw.rect(screen,WHITE,(int(round(BOARD_OFFSET_X+yard_padding_px)), int(round(BOARD_OFFSET_Y+yard_padding_px)), int(round(inner_box_size_px)), int(round(inner_box_size_px))),border_radius=br)
        pygame.draw.rect(screen,WHITE,(int(round(BOARD_OFFSET_X+SQUARE_SIZE*9+yard_padding_px)), int(round(BOARD_OFFSET_Y+yard_padding_px)), int(round(inner_box_size_px)), int(round(inner_box_size_px))),border_radius=br)
        pygame.draw.rect(screen,WHITE,(int(round(BOARD_OFFSET_X+SQUARE_SIZE*9+yard_padding_px)), int(round(BOARD_OFFSET_Y+SQUARE_SIZE*9+yard_padding_px)), int(round(inner_box_size_px)), int(round(inner_box_size_px))),border_radius=br)
        pygame.draw.rect(screen,WHITE,(int(round(BOARD_OFFSET_X+yard_padding_px)), int(round(BOARD_OFFSET_Y+SQUARE_SIZE*9+yard_padding_px)), int(round(inner_box_size_px)), int(round(inner_box_size_px))),border_radius=br)

        # Draw Permanent Yard Markers
        marker_radius = SQUARE_SIZE // 2 - 7
        for player_color, base_pos in YARD_CENTERS_GRID.items():
            base_r, base_c = base_pos
            for offset_r, offset_c in YARD_POS_OFFSETS:
                marker_r, marker_c = base_r + offset_r, base_c + offset_c
                marker_x, marker_y = get_screen_coords(marker_r, marker_c)
                pygame.draw.circle(screen, YARD_MARKER_COLOR, (marker_x, marker_y), marker_radius, 2)

        # Main Path & Safe Squares
        for index, (r, c) in enumerate(MAIN_PATH):
            x_px, y_px = get_screen_coords(r, c); rect = pygame.Rect(x_px - SQUARE_SIZE//2, y_px - SQUARE_SIZE//2, SQUARE_SIZE, SQUARE_SIZE)
            fill_color = WHITE; is_start_sq = False
            for color_idx, (player_color_const, start_index) in enumerate(START_INDICES.items()):
                if index == start_index: fill_color = LIGHT_PLAYER_COLORS[color_idx]; is_start_sq = True; break
            pygame.draw.rect(screen, fill_color, rect)
            if index in SAFE_SQUARES_INDICES: # Draw cross on ALL safe squares
                 cross_size = SQUARE_SIZE * 0.4; half_cross = int(cross_size // 2); line_thickness = 3
                 pygame.draw.line(screen, GOLD, (x_px - half_cross, y_px), (x_px + half_cross, y_px), line_thickness)
                 pygame.draw.line(screen, GOLD, (x_px, y_px - half_cross), (x_px, y_px + half_cross), line_thickness)
            pygame.draw.rect(screen, DARK_GREY, rect, 1) # Border

        # Home Stretch & Center Triangle
        center_r, center_c = 7, 7; cr_px, cc_px = get_screen_coords(center_r, center_c)
        triangle_points = { RED: [(BOARD_OFFSET_X+SQUARE_SIZE*6, BOARD_OFFSET_Y+SQUARE_SIZE*6), (BOARD_OFFSET_X+SQUARE_SIZE*6, BOARD_OFFSET_Y+SQUARE_SIZE*9), (cr_px, cc_px)], GREEN: [(BOARD_OFFSET_X+SQUARE_SIZE*6, BOARD_OFFSET_Y+SQUARE_SIZE*6), (BOARD_OFFSET_X+SQUARE_SIZE*9, BOARD_OFFSET_Y+SQUARE_SIZE*6), (cr_px, cc_px)], YELLOW: [(BOARD_OFFSET_X+SQUARE_SIZE*9, BOARD_OFFSET_Y+SQUARE_SIZE*6), (BOARD_OFFSET_X+SQUARE_SIZE*9, BOARD_OFFSET_Y+SQUARE_SIZE*9), (cr_px, cc_px)], BLUE: [(BOARD_OFFSET_X+SQUARE_SIZE*6, BOARD_OFFSET_Y+SQUARE_SIZE*9), (BOARD_OFFSET_X+SQUARE_SIZE*9, BOARD_OFFSET_Y+SQUARE_SIZE*9), (cr_px, cc_px)] }
        for color, path in HOME_STRETCHES.items():
            pygame.draw.polygon(screen, color, triangle_points[color]); pygame.draw.polygon(screen, DARK_GREY, triangle_points[color], 1)
            for i, (r, c) in enumerate(path):
                x_px, y_px = get_screen_coords(r, c); rect = pygame.Rect(x_px - SQUARE_SIZE//2, y_px - SQUARE_SIZE//2, SQUARE_SIZE, SQUARE_SIZE)
                pygame.draw.rect(screen, LIGHT_PLAYER_COLORS[PLAYER_COLORS.index(color)], rect); pygame.draw.rect(screen, DARK_GREY, rect, 1)

        # Arrows
        arrow_length = SQUARE_SIZE // 3; arrow_thickness = 3; arrow_offset = 5
        for color, start_index in START_INDICES.items():
            r, c = MAIN_PATH[start_index]; x_px, y_px = get_screen_coords(r, c); arrow_color = PLAYER_COLORS[PLAYER_COLORS.index(color)]
            if color == RED: start_pos = (x_px - SQUARE_SIZE//2 + arrow_offset, y_px); end_pos = (start_pos[0] + arrow_length, y_px); head = [(end_pos[0], end_pos[1]), (end_pos[0]-5, end_pos[1]-4), (end_pos[0]-5, end_pos[1]+4)]
            elif color == GREEN: start_pos = (x_px, y_px - SQUARE_SIZE//2 + arrow_offset); end_pos = (x_px, start_pos[1] + arrow_length); head = [(end_pos[0], end_pos[1]), (end_pos[0]-4, end_pos[1]-5), (end_pos[0]+4, end_pos[1]-5)]
            elif color == YELLOW: start_pos = (x_px + SQUARE_SIZE//2 - arrow_offset, y_px); end_pos = (start_pos[0] - arrow_length, y_px); head = [(end_pos[0], end_pos[1]), (end_pos[0]+5, end_pos[1]-4), (end_pos[0]+5, end_pos[1]+4)]
            elif color == BLUE: start_pos = (x_px, y_px + SQUARE_SIZE//2 - arrow_offset); end_pos = (x_px, start_pos[1] - arrow_length); head = [(end_pos[0], end_pos[1]), (end_pos[0]-4, end_pos[1]+5), (end_pos[0]+4, end_pos[1]+5)]
            else: continue
            pygame.draw.line(screen, arrow_color, start_pos, end_pos, arrow_thickness); pygame.draw.polygon(screen, arrow_color, head)
    except Exception as e: print(f"Error drawing board: {e}"); traceback.print_exc()


# --- Token Class --- (Unchanged)
class Token:
    def __init__(self, player_index, token_index):
        self.player_index = player_index; self.token_index = token_index; self.color = PLAYER_COLORS[player_index]
        self.state = 'yard'; self.path_pos = -1; self.grid_pos = (0,0)
        self.is_animating = False; self.anim_start_screen_pos = (0, 0); self.anim_end_screen_pos = (0, 0); self.anim_start_time = 0
        self.current_screen_pos = (0, 0); self.anim_target_path_pos = -1; self.anim_target_state = ''; self.anim_target_grid_pos = (0,0)
        try: self.grid_pos = self._get_yard_pos(); self.current_screen_pos = get_screen_coords(self.grid_pos[0], self.grid_pos[1])
        except Exception as e: print(f"Err init token {player_index}-{token_index}: {e}"); traceback.print_exc()
    def _get_yard_pos(self): yard_base_r, yard_base_c = YARD_CENTERS_GRID[self.color]; offset_r, offset_c = YARD_POS_OFFSETS[self.token_index]; return (float(yard_base_r) + offset_r, float(yard_base_c) + offset_c)
    def _get_home_pos(self): return HOME_CENTERS_GRID[self.color]
    def draw(self, screen, highlight_radius=0):
        draw_pos = self.current_screen_pos; radius = SQUARE_SIZE // 2 - 6
        try:
            pygame.draw.circle(screen, self.color, draw_pos, radius)
            inner_radius = int(radius * 0.6); light_r = min(self.color[0] + 50, 255); light_g = min(self.color[1] + 50, 255); light_b = min(self.color[2] + 50, 255); inner_color = (light_r, light_g, light_b)
            pygame.draw.circle(screen, inner_color, draw_pos, inner_radius)
            pygame.draw.circle(screen, BLACK, draw_pos, radius, 2)
        except Exception as e: print(f"Err draw token {self.player_index}-{self.token_index}: {e}"); traceback.print_exc()
        if highlight_radius > 0: pygame.draw.circle(screen, HIGHLIGHT_YELLOW, draw_pos, highlight_radius, 3)
    def update_animation(self, current_time):
        if not self.is_animating: return False
        elapsed_time = current_time - self.anim_start_time; progress = min(elapsed_time / ANIMATION_DURATION, 1.0); eased_progress = ease_in_out_cubic(progress)
        self.current_screen_pos = (int(round(lerp(self.anim_start_screen_pos[0], self.anim_end_screen_pos[0], eased_progress))), int(round(lerp(self.anim_start_screen_pos[1], self.anim_end_screen_pos[1], eased_progress))))
        if progress >= 1.0: self.is_animating = False; self.path_pos = self.anim_target_path_pos; self.state = self.anim_target_state; self.grid_pos = self.anim_target_grid_pos; self.current_screen_pos = self.anim_end_screen_pos; return True
        return False
    def _update_logical_pos(self, target_path_pos, target_state):
         try:
             target_grid_pos = (0,0)
             if target_state == 'yard': target_grid_pos = self._get_yard_pos()
             elif target_state == 'home': target_grid_pos = self._get_home_pos()
             elif target_state == 'path':
                 path_idx = target_path_pos
                 if 0 <= path_idx < len(MAIN_PATH): target_grid_pos = MAIN_PATH[path_idx]
                 elif len(MAIN_PATH) <= path_idx < len(MAIN_PATH) + len(HOME_STRETCHES[self.color]): home_idx = path_idx - len(MAIN_PATH); target_grid_pos = HOME_STRETCHES[self.color][home_idx]
                 else: raise ValueError(f"Invalid path_pos {path_idx}")
             else: raise ValueError(f"Unknown target state: {target_state}")
             return target_grid_pos
         except Exception as e: print(f"Err update target grid: {e}"); traceback.print_exc(); return self.grid_pos
    def move_to_start(self):
        if self.state == 'yard': target_state = 'path'; target_path_pos = START_INDICES[self.color]; self.start_animation(target_path_pos, target_state)
    def send_home(self): target_state = 'yard'; target_path_pos = -1; self.start_animation(target_path_pos, target_state)
    def start_animation(self, target_path_pos, target_state):
        if self.is_animating: return
        self.anim_target_path_pos = target_path_pos; self.anim_target_state = target_state; self.anim_target_grid_pos = self._update_logical_pos(target_path_pos, target_state)
        self.anim_start_screen_pos = self.current_screen_pos; self.anim_end_screen_pos = get_screen_coords(self.anim_target_grid_pos[0], self.anim_target_grid_pos[1])
        self.anim_start_time = time.time(); self.is_animating = True
    def calculate_target_pos(self, dice_value):
        if self.state != 'path': return -1, self.state
        try: current_path_index=self.path_pos; target_path_index=-1; target_state=self.state; player_start_index=START_INDICES[self.color]; home_stretch_len=len(HOME_STRETCHES[self.color]); main_path_len=len(MAIN_PATH); home_entry_idx_on_main=(player_start_index - 1 + main_path_len)%main_path_len
        except: return -1,self.state
        if current_path_index < main_path_len: steps_to_pass_entry = (home_entry_idx_on_main - current_path_index + main_path_len) % main_path_len + 1; home_stretch_target_index = dice_value - steps_to_pass_entry; target_state = 'path'; target_path_index = (main_path_len + home_stretch_target_index) if dice_value >= steps_to_pass_entry and home_stretch_target_index < home_stretch_len else (100 if dice_value >= steps_to_pass_entry and home_stretch_target_index == home_stretch_len else (-2 if dice_value >= steps_to_pass_entry else (current_path_index + dice_value) % main_path_len)); target_state=('home' if target_path_index==100 else target_state)
        else: current_home_stretch_index = current_path_index - main_path_len; target_home_stretch_index = current_home_stretch_index + dice_value; target_state = 'path'; target_path_index = (main_path_len + target_home_stretch_index) if target_home_stretch_index < home_stretch_len else (100 if target_home_stretch_index == home_stretch_len else -2); target_state=('home' if target_path_index==100 else target_state)
        return target_path_index, target_state
    def get_path_indices_for_move(self, dice_value):
        if self.state != 'path' or dice_value <= 0: return None
        indices = []; current_path_idx = self.path_pos; main_path_len = len(MAIN_PATH); home_stretch_len = len(HOME_STRETCHES[self.color]); player_start_idx = START_INDICES[self.color]; home_entry_idx_on_main = (player_start_idx - 1 + main_path_len) % main_path_len
        for i in range(1, dice_value + 1):
            step_path_idx = -1; step_state = 'path'
            if current_path_idx < main_path_len: steps_to_pass_entry=(home_entry_idx_on_main - current_path_idx + main_path_len) % main_path_len + 1; home_stretch_step_idx = i - steps_to_pass_entry; step_path_idx = (main_path_len + home_stretch_step_idx) if i >= steps_to_pass_entry and home_stretch_step_idx < home_stretch_len else (100 if i >= steps_to_pass_entry and home_stretch_step_idx == home_stretch_len else (-2 if i >= steps_to_pass_entry else (current_path_idx + i) % main_path_len))
            else: current_home_idx=current_path_idx - main_path_len; home_stretch_step_idx = current_home_idx + i; step_path_idx = (main_path_len + home_stretch_step_idx) if home_stretch_step_idx < home_stretch_len else (100 if home_stretch_step_idx == home_stretch_len else -2)
            if step_path_idx >= 0: indices.append(step_path_idx)
            elif step_path_idx == -2: break
        return indices
    def check_path_clear(self, dice_value, all_tokens): # Indentation Corrected
        move_path_indices = self.get_path_indices_for_move(dice_value);
        if not move_path_indices: return True
        for path_idx in move_path_indices[:-1]:
            temp_grid_pos = None; is_home_stretch_step = False
            try:
                 if 0 <= path_idx < len(MAIN_PATH): temp_grid_pos = MAIN_PATH[path_idx]
                 elif len(MAIN_PATH) <= path_idx < len(MAIN_PATH) + len(HOME_STRETCHES[self.color]): home_idx = path_idx - len(MAIN_PATH); temp_grid_pos = HOME_STRETCHES[self.color][home_idx]; is_home_stretch_step = True
            except IndexError: continue
            if not temp_grid_pos: continue
            opponents_at_step = sum(1 for t in all_tokens if t.player_index != self.player_index and t.state == 'path' and t.grid_pos == temp_grid_pos)
            if opponents_at_step >= 2:
                is_safe = False
                if not is_home_stretch_step and path_idx < len(MAIN_PATH) and path_idx in SAFE_SQUARES_INDICES: # Use updated list
                    is_safe = True
                if not is_safe:
                    return False
        return True
    def can_move(self, dice_value, all_tokens):
        try:
            if self.state == 'yard':
                if dice_value == 6: start_path_idx = START_INDICES[self.color]; start_grid_pos = MAIN_PATH[start_path_idx]; own_tokens_at_start = sum(1 for t in all_tokens if t.player_index == self.player_index and t.state == 'path' and t.grid_pos == start_grid_pos); return own_tokens_at_start < 2
                else: return False
            if self.state == 'home': return False
            if self.state == 'path':
                target_path_index, target_state = self.calculate_target_pos(dice_value);
                if target_path_index < 0: return False
                if target_state != 'home':
                    target_grid_pos = self._update_logical_pos(target_path_index, target_state);
                    if not target_grid_pos: return False
                    own_tokens_at_target = sum(1 for t in all_tokens if t != self and t.player_index == self.player_index and t.state == 'path' and t.grid_pos == target_grid_pos)
                    if own_tokens_at_target >= 2: return False
                if not self.check_path_clear(dice_value, all_tokens): return False
                return True
            return False
        except Exception as e: print(f"Err can_move: {e}"); traceback.print_exc(); return False
    def initiate_move(self, dice_value, all_tokens):
        if not self.can_move(dice_value, all_tokens): return False
        try:
            if self.state == 'yard' and dice_value == 6: self.move_to_start(); return True
            if self.state == 'path': target_path_index, target_state = self.calculate_target_pos(dice_value); self.start_animation(target_path_index, target_state); return True
            return False
        except Exception as e: print(f"Err initiate_move: {e}"); traceback.print_exc(); return False
    def check_capture_at_target(self, all_tokens):
        if self.anim_target_state != 'path': return False
        target_grid_pos = self.anim_target_grid_pos; target_path_idx = self.anim_target_path_pos; is_safe_square = False; is_on_home_stretch = False
        if target_path_idx < len(MAIN_PATH): is_safe_square = target_path_idx in SAFE_SQUARES_INDICES # Use updated list
        elif target_path_idx < len(MAIN_PATH) + len(HOME_STRETCHES[self.color]): is_on_home_stretch = True
        if is_safe_square or is_on_home_stretch: return False
        opponents_at_target = [t for t in all_tokens if t.player_index != self.player_index and t.state == 'path' and t.grid_pos == target_grid_pos]
        return len(opponents_at_target) == 1
    def perform_capture_at_target(self, all_tokens):
         if self.state != 'path': return
         target_grid_pos = self.grid_pos; target_path_idx = self.path_pos; is_safe_square = False; is_on_home_stretch = False
         if target_path_idx < len(MAIN_PATH): is_safe_square = target_path_idx in SAFE_SQUARES_INDICES # Use updated list
         elif target_path_idx < len(MAIN_PATH) + len(HOME_STRETCHES[self.color]): is_on_home_stretch = True
         if is_safe_square or is_on_home_stretch: return
         captured_token = None; opponent_count = 0
         for t in all_tokens:
             if t.player_index != self.player_index and t.state == 'path' and t.grid_pos == target_grid_pos: opponent_count += 1; captured_token = t
         if opponent_count == 1 and captured_token: print(f"!!! Capture by {PLAYER_NAMES[self.player_index]}!"); captured_token.send_home()


# --- Dice Class --- (Unchanged)
class Dice:
    def __init__(self, x, y, size, player_index):
        self.x = x; self.y = y; self.size = size; self.player_index = player_index
        self.value = 1; self.rect = pygame.Rect(x, y, size + PERSPECTIVE_OFFSET_X, size + PERSPECTIVE_OFFSET_Y)
        self.top_face_rect = pygame.Rect(x + PERSPECTIVE_OFFSET_X // 2, y + PERSPECTIVE_OFFSET_Y // 2, size, size)
        self.is_rolling = False; self.roll_start_time = 0; self.display_value = 1; self.disabled = True
    def roll(self):
        if self.is_rolling or self.disabled: return False
        self.value = random.randint(1, 6); self.is_rolling = True; self.roll_start_time = time.time(); print(f"Dice {self.player_index} rolled: {self.value}"); return True
    def update_animation(self, current_time):
        if not self.is_rolling: return False
        elapsed = current_time - self.roll_start_time
        if elapsed >= DICE_ANIM_DURATION: self.is_rolling = False; self.display_value = self.value; return True
        else: self.display_value = random.randint(1, 6); return False
    def draw(self, screen):
        try:
            base_x, base_y = self.x, self.y; size = self.size; off_x, off_y = PERSPECTIVE_OFFSET_X, PERSPECTIVE_OFFSET_Y
            top_back_left=(base_x, base_y); top_back_right=(base_x + size, base_y); top_front_left=(base_x + off_x, base_y + off_y); top_front_right=(base_x + size + off_x, base_y + off_y)
            bottom_back_left=(base_x, base_y + size); bottom_front_left=(base_x + off_x, base_y + size + off_y); bottom_front_right=(base_x + size + off_x, base_y + size + off_y)
            if self.disabled: top_face_col = DISABLED_COLOR_BG; side_face_col_1 = DISABLED_COLOR_BG; side_face_col_2 = DISABLED_COLOR_BG; border_col = DISABLED_COLOR_FG; dot_col = DISABLED_COLOR_FG
            else: top_face_col = LIGHT_PLAYER_COLORS[self.player_index]; side_face_col_1 = DARKER_PLAYER_COLORS[self.player_index]; side_face_col_2 = DARKEST_PLAYER_COLORS[self.player_index]; border_col = BLACK; dot_col = BLACK
            pygame.draw.polygon(screen, side_face_col_1, [top_back_right, top_front_right, bottom_front_right, (base_x + size, base_y + size)])
            pygame.draw.polygon(screen, side_face_col_2, [top_front_left, top_front_right, bottom_front_right, bottom_front_left])
            top_face_draw_rect = pygame.Rect(base_x + off_x//2, base_y + off_y//2, size, size); pygame.draw.rect(screen, top_face_col, top_face_draw_rect)
            line_width = 1; pygame.draw.rect(screen, border_col, top_face_draw_rect, line_width)
            pygame.draw.line(screen, border_col, top_face_draw_rect.topleft, top_back_left, line_width); pygame.draw.line(screen, border_col, top_face_draw_rect.topright, top_back_right, line_width)
            pygame.draw.line(screen, border_col, top_face_draw_rect.bottomleft, bottom_front_left, line_width); pygame.draw.line(screen, border_col, top_back_left, (base_x, base_y + size), line_width)
            pygame.draw.line(screen, border_col, top_back_right, (base_x + size, base_y + size), line_width); pygame.draw.line(screen, border_col, bottom_front_left, (base_x, base_y + size), line_width)
            pygame.draw.line(screen, border_col, (base_x + size, base_y + size) , bottom_front_right, line_width)
            dot_radius = self.size // 10; dot_positions = { 1: [(0.5, 0.5)], 2: [(0.25, 0.25), (0.75, 0.75)], 3: [(0.25, 0.25), (0.5, 0.5), (0.75, 0.75)], 4: [(0.25, 0.25), (0.75, 0.25), (0.25, 0.75), (0.75, 0.75)], 5: [(0.25, 0.25), (0.75, 0.25), (0.5, 0.5), (0.25, 0.75), (0.75, 0.75)], 6: [(0.25, 0.25), (0.75, 0.25), (0.25, 0.5), (0.75, 0.5), (0.25, 0.75), (0.75, 0.75)] }
            current_val_to_draw = self.display_value
            if current_val_to_draw in dot_positions:
                for pos_rel in dot_positions[current_val_to_draw]: dot_x = top_face_draw_rect.left + int(pos_rel[0] * size); dot_y = top_face_draw_rect.top + int(pos_rel[1] * size); pygame.draw.circle(screen, dot_col, (dot_x, dot_y), dot_radius)
        except Exception as e: print(f"Err draw dice {self.player_index}: {e}"); traceback.print_exc()


# --- Main Game --- (Uses updated drawing/constants)
def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("PyLudo - Final Centered") # Updated caption
    clock = pygame.time.Clock()
    font_large=pygame.font.Font(None, 42); font_medium=pygame.font.Font(None, 34); font_small=pygame.font.Font(None, 26); font_tiny=pygame.font.Font(None, 18)
    if not font_small: print("WARN: Font loading issue."); font_small=pygame.font.SysFont(None, 26)

    tokens = []; player_tokens = [[] for _ in range(4)]
    try:
        for p_idx in range(4):
            for t_idx in range(4): tokens.append(Token(p_idx, t_idx)); player_tokens[p_idx].append(tokens[-1])
    except Exception as e: print(f"Token creation error: {e}"); traceback.print_exc(); pygame.quit(); return

    dice_set = []; dice_size = 45; dice_margin = 15
    dice_set.append(Dice(BOARD_OFFSET_X + dice_margin, BOARD_OFFSET_Y + dice_margin, dice_size, 0)) # Red
    dice_set.append(Dice(BOARD_OFFSET_X + BOARD_SIZE - dice_size - dice_margin - PERSPECTIVE_OFFSET_X, BOARD_OFFSET_Y + dice_margin, dice_size, 1)) # Green
    dice_set.append(Dice(BOARD_OFFSET_X + BOARD_SIZE - dice_size - dice_margin - PERSPECTIVE_OFFSET_X, BOARD_OFFSET_Y + BOARD_SIZE - dice_size - dice_margin - PERSPECTIVE_OFFSET_Y, dice_size, 2)) # Yellow
    dice_set.append(Dice(BOARD_OFFSET_X + dice_margin, BOARD_OFFSET_Y + BOARD_SIZE - dice_size - dice_margin - PERSPECTIVE_OFFSET_Y, dice_size, 3)) # Blue

    current_player_index = 0; game_state = STATE_ROLL_DICE; current_dice_roll = 0
    winner = -1; message = "Roll the dice!"; consecutive_sixes = 0
    turn_switched = True; last_click_time = 0
    post_animation_info = {'captured': False, 'is_win': False, 'rolled_value': 0}
    highlight_radius = 0

    running = True
    while running:
        current_time = time.time(); delta_time = clock.tick(60) / 1000.0
        for i, dice_instance in enumerate(dice_set): dice_instance.disabled = (i != current_player_index)
        active_token_animation = any(t.is_animating for t in tokens)
        active_dice_animation = dice_set[current_player_index].is_rolling
        is_animating = active_token_animation or active_dice_animation

        # Event Handling (Unchanged)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: running = False
            if not is_animating and event.type == pygame.MOUSEBUTTONDOWN and current_time - last_click_time > 0.2:
                last_click_time = current_time; mouse_pos = event.pos
                if winner != -1: continue
                if game_state == STATE_ROLL_DICE:
                    for dice_instance in dice_set:
                         if not dice_instance.disabled and dice_instance.rect.collidepoint(mouse_pos):
                              if dice_instance.roll(): game_state = STATE_ANIMATING; message = "Rolling..."; turn_switched = False; break
                elif game_state == STATE_SELECT_TOKEN:
                    clicked_token = None; min_dist_sq = (SQUARE_SIZE * 0.7)**2
                    movable_tokens = [t for t in player_tokens[current_player_index] if t.can_move(current_dice_roll, tokens)]
                    for token in movable_tokens:
                         token_screen_x, token_screen_y = token.current_screen_pos
                         dist_sq = (mouse_pos[0] - token_screen_x)**2 + (mouse_pos[1] - token_screen_y)**2
                         if dist_sq < min_dist_sq:
                             if clicked_token is None or dist_sq < min_dist_sq: clicked_token = token; min_dist_sq = dist_sq
                    if clicked_token:
                        if clicked_token.initiate_move(current_dice_roll, tokens): post_animation_info['captured'] = clicked_token.check_capture_at_target(tokens); post_animation_info['rolled_value'] = current_dice_roll; game_state = STATE_ANIMATING; message = "Moving..."
                    else: message = "Click your highlighted tokens."

        # Update Animations & Game Logic (Unchanged)
        active_dice = dice_set[current_player_index]
        if active_dice.is_rolling:
            if active_dice.update_animation(current_time):
                current_dice_roll = active_dice.value; consecutive_sixes = (consecutive_sixes + 1) if current_dice_roll == 6 else 0
                if consecutive_sixes == 3: message = "3 sixes! Forfeit."; current_player_index=(current_player_index + 1)%4; consecutive_sixes=0; game_state=STATE_ROLL_DICE; turn_switched=True; message="Roll the dice!"
                else:
                    movable_tokens = [t for t in player_tokens[current_player_index] if t.can_move(current_dice_roll, tokens)]
                    if movable_tokens: game_state = STATE_SELECT_TOKEN; message = f"Select token to move {current_dice_roll}."
                    else: message = f"No moves for {current_dice_roll}."; turn_switched = True; game_state = STATE_ROLL_DICE; current_player_index = (current_player_index + 1) % 4 if current_dice_roll != 6 else current_player_index; consecutive_sixes = 0 if current_dice_roll != 6 else consecutive_sixes; message = "Roll the dice!" if current_dice_roll != 6 else "Roll again!"
        token_animation_finished_this_frame = False; finished_token = None
        for token in tokens:
            if token.is_animating:
                if token.update_animation(current_time): token_animation_finished_this_frame = True; finished_token = token
        if token_animation_finished_this_frame and finished_token:
             if post_animation_info['captured']: finished_token.perform_capture_at_target(tokens)
             player_home_count = sum(1 for t in player_tokens[finished_token.player_index] if t.state == 'home')
             if player_home_count == 4: winner = finished_token.player_index; game_state = STATE_GAME_OVER; message = f"Player {PLAYER_NAMES[winner]} Wins!"
             else:
                 if not any(t.is_animating for t in tokens):
                     rolled_value = post_animation_info['rolled_value']; was_capture = post_animation_info['captured']
                     if rolled_value == 6 or was_capture: message = "Extra turn!"; game_state = STATE_ROLL_DICE; turn_switched = True
                     else: current_player_index = (current_player_index + 1) % 4; game_state = STATE_ROLL_DICE; consecutive_sixes = 0; turn_switched = True; message = "Roll the dice!"
             post_animation_info = {'captured': False, 'is_win': False, 'rolled_value': 0}

        # --- Drawing ---
        screen.fill(GREY); draw_board(screen) # Board uses updated logic

        # Draw Tokens (Yard tokens use updated offsets via _get_yard_pos)
        highlight_radius = 0
        if game_state == STATE_SELECT_TOKEN:
             base_radius = SQUARE_SIZE // 2 - 1; pulse_offset = (math.sin(current_time * HIGHLIGHT_PULSE_SPEED) + 1) / 2
             highlight_radius = int(base_radius + pulse_offset * 4)
             highlight_indices = [i for i, token in enumerate(tokens) if token.player_index == current_player_index and token.can_move(current_dice_roll, tokens)]
        else: highlight_indices = []
        for i, token in enumerate(tokens): token.draw(screen, highlight_radius if i in highlight_indices else 0)

        # Draw 4 Dice
        for dice_instance in dice_set: dice_instance.draw(screen)

        # Draw UI Elements (Unchanged Layout)
        ui_x_start = BOARD_OFFSET_X + BOARD_SIZE + 15; ui_width = WIDTH - ui_x_start - 15
        player_box_height = 50; player_box_rect = pygame.Rect(ui_x_start + (ui_width - 180)//2, BOARD_OFFSET_Y + 20, 180, player_box_height)
        pygame.draw.rect(screen, LIGHT_PLAYER_COLORS[current_player_index], player_box_rect, border_radius=5); pygame.draw.rect(screen, PLAYER_COLORS[current_player_index], player_box_rect, 3, border_radius=5)
        turn_text = font_medium.render(f"{PLAYER_NAMES[current_player_index]}'s Turn", True, BLACK); turn_rect = turn_text.get_rect(center=player_box_rect.center); screen.blit(turn_text, turn_rect)
        message_area_y = player_box_rect.bottom + 30
        current_msg_str = ""; msg_color = BLACK; msg_font = font_small
        if winner != -1: current_msg_str = message; msg_color = GOLD; msg_font = font_large
        else:
            if game_state == STATE_ROLL_DICE: current_msg_str = "Click your dice!" if turn_switched else "Roll again!"
            elif game_state == STATE_SELECT_TOKEN: current_msg_str = message
            elif game_state == STATE_ANIMATING: current_msg_str = message
            else: current_msg_str = message
        max_msg_width = ui_width - 20; words = current_msg_str.split(' '); lines = []; current_line = ""
        for word in words: test_line = current_line + word + " "; test_surf = msg_font.render(test_line, True, msg_color); width = test_surf.get_width(); test_surf = None;
        if width <= max_msg_width: current_line = test_line
        else: lines.append(current_line.strip()); current_line = word + " "
        lines.append(current_line.strip()); line_y_offset = 0
        for line in lines: message_text = msg_font.render(line, True, msg_color); msg_rect = message_text.get_rect(midtop=(ui_x_start + ui_width // 2 , message_area_y + line_y_offset)); screen.blit(message_text, msg_rect); line_y_offset += msg_font.get_height()
        info_y = message_area_y + line_y_offset + 15; info_str = ""
        if game_state == STATE_SELECT_TOKEN: info_str += f"Roll: {current_dice_roll}  "
        if consecutive_sixes > 0: info_str += f"Sixes: {consecutive_sixes}"
        info_text = font_tiny.render(info_str.strip(), True, DARK_GREY); info_rect = info_text.get_rect(midtop=(ui_x_start + ui_width // 2, info_y)); screen.blit(info_text, info_rect)

        pygame.display.flip()

    pygame.quit()

if __name__ == '__main__':
    try: main()
    except Exception as e: print("\n--- UNHANDLED EXCEPTION ---"); traceback.print_exc(); input("Press Enter...")