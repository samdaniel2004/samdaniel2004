from PIL import Image, ImageDraw, ImageFont
import os
import math

# ==========================================
# CONFIGURATION
# ==========================================

WIDTH = 1200
HEIGHT = 420

FRAME_COUNT = 48
FRAME_DURATION = 80

OUTPUT_DIR = "assets"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "pixel-game.gif")

os.makedirs(OUTPUT_DIR, exist_ok=True)


# ==========================================
# COLORS
# ==========================================

BLACK = (5, 5, 8)
DARK = (18, 18, 22)
DARKER = (12, 12, 15)

WHITE = (240, 240, 240)
LIGHT = (190, 190, 190)
GRAY = (110, 110, 110)
DARK_GRAY = (55, 55, 60)


# ==========================================
# FONT
# ==========================================

try:
    FONT_SMALL = ImageFont.truetype("DejaVuSansMono.ttf", 15)
    FONT_MEDIUM = ImageFont.truetype("DejaVuSansMono.ttf", 18)
    FONT_BIG = ImageFont.truetype("DejaVuSansMono.ttf", 23)
except:
    FONT_SMALL = ImageFont.load_default()
    FONT_MEDIUM = ImageFont.load_default()
    FONT_BIG = ImageFont.load_default()


# ==========================================
# DRAW CITY
# ==========================================

def draw_city(draw, offset):

    buildings = [
        (650, 125, 700, 270),
        (705, 85, 755, 270),
        (760, 145, 805, 270),
        (810, 65, 865, 270),
        (870, 115, 920, 270),
        (925, 90, 980, 270),
        (985, 140, 1035, 270),
        (1040, 75, 1095, 270),
        (1100, 125, 1160, 270),
    ]

    for x1, y1, x2, y2 in buildings:

        x1 -= offset
        x2 -= offset

        # Building
        draw.rectangle(
            (x1, y1, x2, y2),
            fill=DARK
        )

        # Roof
        draw.line(
            (x1, y1, x2, y1),
            fill=GRAY,
            width=2
        )

        # Windows
        for wx in range(x1 + 8, x2 - 5, 14):

            for wy in range(y1 + 12, y2 - 10, 20):

                # Some windows blink
                if (wx + wy + offset) % 4 != 0:

                    draw.rectangle(
                        (wx, wy, wx + 4, wy + 5),
                        fill=LIGHT
                    )


# ==========================================
# DRAW MOUNTAINS
# ==========================================

def draw_mountains(draw, offset):

    mountain_offset = offset // 3

    points = [
        (-200 - mountain_offset, 270),
        (20 - mountain_offset, 150),
        (170 - mountain_offset, 270),
        (350 - mountain_offset, 135),
        (500 - mountain_offset, 270),
        (680 - mountain_offset, 155),
        (850 - mountain_offset, 270),
        (1030 - mountain_offset, 135),
        (1250 - mountain_offset, 270),
    ]

    draw.polygon(
        points,
        fill=(30, 30, 35)
    )


# ==========================================
# DRAW MOON
# ==========================================

def draw_moon(draw):

    draw.ellipse(
        (965, 45, 1060, 140),
        fill=WHITE
    )

    # Small dark moon pixels
    draw.rectangle(
        (1030, 70, 1042, 80),
        fill=LIGHT
    )

    draw.rectangle(
        (1005, 110, 1015, 118),
        fill=LIGHT
    )


# ==========================================
# DRAW STARS
# ==========================================

def draw_stars(draw, frame):

    stars = [
        (100, 55),
        (190, 95),
        (310, 42),
        (430, 80),
        (535, 35),
        (625, 105),
        (745, 55),
        (865, 90),
        (1120, 50),
    ]

    for i, (x, y) in enumerate(stars):

        # Twinkle
        if (frame + i * 2) % 6 < 4:

            draw.rectangle(
                (x, y, x + 2, y + 2),
                fill=WHITE
            )


# ==========================================
# DRAW TECH PANELS
# ==========================================

def draw_panel(draw, x, y, title):

    width = 125
    height = 48

    draw.rectangle(
        (x, y, x + width, y + height),
        outline=GRAY,
        width=2
    )

    draw.text(
        (x + 12, y + 15),
        title,
        fill=WHITE,
        font=FONT_SMALL
    )


# ==========================================
# DRAW CHARACTER
# ==========================================

def draw_character(draw, x, ground_y, frame):

    # Walking cycle
    cycle = frame % 8

    if cycle < 4:
        leg_a = 8
        leg_b = -8
        arm_a = -5
        arm_b = 5
    else:
        leg_a = -8
        leg_b = 8
        arm_a = 5
        arm_b = -5

    # Character dimensions
    head_y = ground_y - 95
    body_y = ground_y - 70

    # Backpack
    draw.rectangle(
        (
            x - 13,
            body_y + 5,
            x + 4,
            body_y + 43
        ),
        fill=DARK_GRAY
    )

    # Backpack outline
    draw.rectangle(
        (
            x - 13,
            body_y + 5,
            x + 4,
            body_y + 43
        ),
        outline=GRAY,
        width=2
    )

    # Head
    draw.rectangle(
        (
            x + 5,
            head_y,
            x + 32,
            head_y + 27
        ),
        fill=WHITE
    )

    # Hair
    draw.rectangle(
        (
            x + 5,
            head_y,
            x + 32,
            head_y + 7
        ),
        fill=DARK
    )

    # Eye
    draw.rectangle(
        (
            x + 25,
            head_y + 11,
            x + 28,
            head_y + 14
        ),
        fill=BLACK
    )

    # Hoodie/body
    draw.rectangle(
        (
            x,
            body_y,
            x + 38,
            ground_y - 30
        ),
        fill=GRAY
    )

    # Hoodie outline
    draw.rectangle(
        (
            x,
            body_y,
            x + 38,
            ground_y - 30
        ),
        outline=LIGHT,
        width=2
    )

    # Left arm
    draw.line(
        (
            x + 4,
            body_y + 8,
            x - 10,
            body_y + 35 + arm_a
        ),
        fill=WHITE,
        width=6
    )

    # Right arm
    draw.line(
        (
            x + 34,
            body_y + 8,
            x + 48,
            body_y + 35 + arm_b
        ),
        fill=WHITE,
        width=6
    )

    # Left leg
    draw.line(
        (
            x + 10,
            ground_y - 30,
            x + 5 + leg_a,
            ground_y
        ),
        fill=LIGHT,
        width=8
    )

    # Right leg
    draw.line(
        (
            x + 29,
            ground_y - 30,
            x + 35 + leg_b,
            ground_y
        ),
        fill=LIGHT,
        width=8
    )

    # Shoes
    draw.rectangle(
        (
            x - 2 + leg_a,
            ground_y - 2,
            x + 15 + leg_a,
            ground_y + 4
        ),
        fill=WHITE
    )

    draw.rectangle(
        (
            x + 28 + leg_b,
            ground_y - 2,
            x + 45 + leg_b,
            ground_y + 4
        ),
        fill=WHITE
    )


# ==========================================
# DRAW CAT
# ==========================================

def draw_cat(draw, x, ground_y, frame):

    bob = 2 if frame % 8 < 4 else 0

    y = ground_y - 18 + bob

    # Body
    draw.rectangle(
        (x, y, x + 30, y + 14),
        fill=GRAY
    )

    # Head
    draw.rectangle(
        (x + 22, y - 7, x + 38, y + 8),
        fill=LIGHT
    )

    # Ears
    draw.polygon(
        [
            (x + 23, y - 7),
            (x + 27, y - 15),
            (x + 31, y - 7)
        ],
        fill=LIGHT
    )

    draw.polygon(
        [
            (x + 31, y - 7),
            (x + 35, y - 15),
            (x + 39, y - 7)
        ],
        fill=LIGHT
    )

    # Tail
    tail_offset = 4 if frame % 8 < 4 else -4

    draw.line(
        (
            x,
            y + 5,
            x - 13,
            y - 4 + tail_offset
        ),
        fill=LIGHT,
        width=4
    )


# ==========================================
# DRAW GROUND
# ==========================================

def draw_ground(draw):

    draw.rectangle(
        (0, 270, WIDTH, HEIGHT),
        fill=DARKER
    )

    draw.line(
        (0, 270, WIDTH, 270),
        fill=WHITE,
        width=3
    )

    # Ground pixels
    for x in range(0, WIDTH, 35):

        draw.rectangle(
            (x, 290, x + 14, 294),
            fill=DARK_GRAY
        )

    # Water reflection
    draw.rectangle(
        (700, 310, WIDTH, HEIGHT),
        fill=(10, 10, 13)
    )

    for i in range(8):

        y = 320 + i * 12

        draw.line(
            (750 - i * 10, y, 1110 + i * 8, y),
            fill=DARK_GRAY,
            width=2
        )


# ==========================================
# DRAW TERMINAL TEXT
# ==========================================

def draw_terminal(draw, frame):

    text = "// dream > code > create >"

    draw.text(
        (30, 380),
        text,
        fill=WHITE,
        font=FONT_MEDIUM
    )

    # Blinking cursor
    if frame % 8 < 4:

        draw.rectangle(
            (310, 379, 320, 397),
            fill=WHITE
        )


# ==========================================
# GENERATE FRAMES
# ==========================================

frames = []

for frame in range(FRAME_COUNT):

    image = Image.new(
        "RGB",
        (WIDTH, HEIGHT),
        BLACK
    )

    draw = ImageDraw.Draw(image)

    # Background animation
    offset = (frame * 5) % 600

    draw_stars(draw, frame)

    draw_moon(draw)

    # Repeating mountains
    draw_mountains(
        draw,
        offset
    )

    # City scroll
    city_offset = (frame * 2) % 400

    draw_city(
        draw,
        city_offset
    )

    draw_ground(draw)

    # --------------------------------------
    # Floating AI/Developer technology
    # --------------------------------------

    draw_panel(
        draw,
        90,
        125,
        "PYTHON"
    )

    draw_panel(
        draw,
        245,
        90,
        "AI / ML"
    )

    draw_panel(
        draw,
        400,
        120,
        "LLM + RAG"
    )

    draw_panel(
        draw,
        560,
        85,
        "GEN AI"
    )

    draw_panel(
        draw,
        720,
        120,
        "UI / UX"
    )

    # --------------------------------------
    # Character movement
    # --------------------------------------

    character_x = 250 + int(
        math.sin(frame / 12) * 5
    )

    draw_character(
        draw,
        character_x,
        270,
        frame
    )

    # Cat follows character
    draw_cat(
        draw,
        character_x - 55,
        270,
        frame
    )

    # --------------------------------------
    # GitHub-style sign
    # --------------------------------------

    draw.rectangle(
        (930, 205, 1150, 265),
        fill=DARK,
        outline=GRAY,
        width=2
    )

    draw.text(
        (950, 220),
        "BUILD • CREATE",
        fill=WHITE,
        font=FONT_MEDIUM
    )

    draw.text(
        (950, 242),
        "LEARN • IMPROVE",
        fill=LIGHT,
        font=FONT_SMALL
    )

    # --------------------------------------
    # Terminal text
    # --------------------------------------

    draw_terminal(
        draw,
        frame
    )

    # --------------------------------------
    # Pixelate slightly
    # --------------------------------------

    small = image.resize(
        (WIDTH // 2, HEIGHT // 2),
        Image.Resampling.NEAREST
    )

    image = small.resize(
        (WIDTH, HEIGHT),
        Image.Resampling.NEAREST
    )

    frames.append(image)


# ==========================================
# SAVE GIF
# ==========================================

frames[0].save(
    OUTPUT_FILE,
    save_all=True,
    append_images=frames[1:],
    duration=FRAME_DURATION,
    loop=0,
    optimize=True
)

file_size = os.path.getsize(OUTPUT_FILE) / 1024

print()
print("======================================")
print(" PIXEL GAME ANIMATION CREATED")
print("======================================")
print()
print(f"File: {OUTPUT_FILE}")
print(f"Frames: {FRAME_COUNT}")
print(f"Resolution: {WIDTH}x{HEIGHT}")
print(f"Size: {file_size:.1f} KB")
print()
print("Open the GIF to preview it.")
