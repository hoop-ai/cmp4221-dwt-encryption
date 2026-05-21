"""Build the CMP4221 DWT encryption presentation deliverables.

Run from the Projects folder:
    python _build/build_deck.py

Outputs:
    CMP4221 - DWT Encryption Presentation.pptx
    CMP4221 - DWT Encryption Presentation.pdf
    CMP4221 - DWT Encryption Study Deck.pptx
    CMP4221 - DWT Encryption Study Deck.pdf
"""

from __future__ import annotations

from pathlib import Path
import sys

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_CONNECTOR, MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.util import Inches, Pt


PROJECT_DIR = Path(__file__).resolve().parent.parent
MAIN_PPTX = PROJECT_DIR / "CMP4221 - DWT Encryption Presentation.pptx"
MAIN_PDF = PROJECT_DIR / "CMP4221 - DWT Encryption Presentation.pdf"
STUDY_PPTX = PROJECT_DIR / "CMP4221 - DWT Encryption Study Deck.pptx"
STUDY_PDF = PROJECT_DIR / "CMP4221 - DWT Encryption Study Deck.pdf"

SLIDE_W = 13.333
SLIDE_H = 7.5
TOTAL_MAIN = 10


def c(hex_value: str) -> RGBColor:
    hex_value = hex_value.strip("#")
    return RGBColor(int(hex_value[0:2], 16), int(hex_value[2:4], 16), int(hex_value[4:6], 16))


NAVY = c("17324D")
NAVY_2 = c("254B72")
TEAL = c("0C7C7B")
TEAL_2 = c("28A3A1")
AMBER = c("D69B20")
RED = c("B84A3A")
GREEN = c("2E8B57")
INK = c("243342")
MUTED = c("6B7785")
LINE = c("D9E1EA")
PAPER = c("F6F8FA")
PALE_TEAL = c("E8F6F5")
PALE_NAVY = c("EAF0F6")
PALE_AMBER = c("FFF4DA")
WHITE = c("FFFFFF")

FONT_TITLE = "Aptos Display"
FONT_BODY = "Aptos"
FONT_MONO = "Consolas"


# Speaker scripts — verbatim, designed to be read aloud at ~150 wpm.
# Total target: ~1,700 words = 10:30 at 150 wpm. Speakers usually go a bit
# faster when nervous (~165 wpm), so this lands cleanly inside 10:00 in
# practice while giving room to breathe and pause. Time budgets per slide
# match the on-deck headers.
MAIN_NOTES = {
    1: (
        "Hi everyone, I'm Abdul Rahman, and this is Maria. For our final project we "
        "picked a 2026 paper from ACM Transactions on Multimedia — published in "
        "Volume 22, Issue 3, this March — by Xu, Gao, Cao and Mou. The title is "
        "Multi-Image Encryption Scheme Based on Chaotic Pseudo-Random Signal "
        "Generator and DWT Compression. The idea is simple to state in one breath: "
        "take several color images, shrink each one using the wavelet transform we "
        "covered in class, stack them into a single 3D block, and then scramble that "
        "block using a chaotic system. I'll cover the first five slides — "
        "motivation, background, novelty and the pipeline — and Maria will take the "
        "algorithm details, the results, and the security analysis."
    ),
    2: (
        "Think about what actually happens when you send photos over a network. A "
        "single 512-by-512 color image already has about 786 thousand pixel values "
        "across the R, G and B channels. Now imagine sending ten of those images, "
        "or fifty for a medical scan batch — you're moving a lot of data, and "
        "anything in transit can be intercepted by an attacker. So the paper points "
        "out there are really two problems happening at the same time. First, "
        "transmission is heavy, which costs you bandwidth and time. Second, "
        "transmission is unsafe, which means the visible image content has to be "
        "destroyed before it leaves your device. Most existing schemes treat these "
        "as separate problems — encrypt one image, compress one image, then move on "
        "to the next. That works for a single selfie. It breaks down for batches "
        "like medical scans across hospitals, or surveillance frames between sites. "
        "The authors argue you need compression and encryption working together in "
        "one pipeline; otherwise you're paying the cost twice. Their stated goal: "
        "do both in one shot, on multiple images, and even on images of different "
        "sizes."
    ),
    3: (
        "Okay so the paper combines two tools we've already seen in this course. "
        "The first one is the Discrete Wavelet Transform, the DWT. We saw this in "
        "lecture: instead of using sines and cosines like the Fourier transform "
        "does, the DWT uses little localized waves called wavelets, and it splits "
        "an image into four sub-bands. There's LL, the low-frequency approximation "
        "— basically a smaller, blurry version of the image at half the height and "
        "half the width. Then LH, HL, and HH capture the horizontal, vertical, and "
        "diagonal edges respectively. The trick this paper uses is to keep only the "
        "LL sub-band and throw the other three away. That immediately compresses "
        "the image to one quarter of its original size, and because most of what "
        "your eye perceives lives in the low frequencies, the result is still "
        "visually recognizable. Now the second ingredient is a three-dimensional "
        "discrete chaotic map. A chaotic map is just a function you keep iterating: "
        "you plug in x, y, z, you get new x, y, z out, and you keep going. The "
        "output looks completely random, but it's fully deterministic — same "
        "starting numbers, same sequence every time. The authors fix the parameters "
        "at 0.3, 0.94, 0.9, 1.6, minus 1.8, minus 1.8, with initial state 0.1, 0.1, "
        "0.1. Change any of those by ten to the minus fifteen, and the sequence is "
        "completely different. That extreme sensitivity is exactly what makes those "
        "numbers usable as a secret encryption key."
    ),
    4: (
        "Here's the core trick of the paper, and it's worth saying clearly. Instead "
        "of encrypting each image one by one, the authors DWT-compress every image "
        "down to its LL sub-band, and then they stack all those LL sub-bands on "
        "top of each other into a single three-dimensional cube. Then they encrypt "
        "that whole cube as one single object. That's the novelty: one encryption "
        "pass, multiple images at once, even when those images have different "
        "sizes. They handle the size mismatch by padding the smaller images with "
        "zeros, so they all fit in the same cube shape — and they openly flag that "
        "padding as the main limitation."
    ),
    5: (
        "Let me walk you through the full pipeline end to end. Stage one — you take "
        "each color image, split it into R, G, and B channels, and run the DWT on "
        "each channel separately. You keep only the LL sub-band, which is where the "
        "compression actually happens; you're now at one quarter the size of the "
        "original. Stage two — you take all those LL sub-bands from all your "
        "images, and you stack them into a single three-dimensional cube the paper "
        "calls C. The width and height of the cube come from the biggest image in "
        "the batch divided by two, and the depth comes from how many images you "
        "have. Stage three is what the paper calls confusion. The chaotic map gets "
        "iterated to produce three sequences, S1, T1 and U1, and these tell the "
        "algorithm how to swap pixel positions inside the cube. So a pixel that "
        "started at position (i, j, k) ends up somewhere completely different. "
        "Stage four is diffusion. Here you don't just move pixels around, you "
        "change their values too, by XOR-ing each pixel with another chaotic "
        "sequence. After both stages you have the cipher cube D, and that's what "
        "gets transmitted across the network. The receiver, who shares the same "
        "key, runs the whole pipeline in reverse: inverse diffusion, inverse "
        "confusion, inverse DWT — and recovers the original images. That's the "
        "methodology in one breath. Maria's going to take the confusion and "
        "diffusion stages in detail next. Maria, over to you."
    ),
    6: (
        "Thanks Abdul. So I'll start with confusion. The cryptographic definition "
        "of confusion is just: change where information is, without changing what "
        "it is. Pixel values stay the same; only their spatial positions move. "
        "The way the paper does this is — they iterate the chaotic map M_h times "
        "M_w times z times, which is exactly once for every pixel in the cube. "
        "From those iterations they get three real-valued sequences, X, Y, and Z, "
        "and they post-process them using floor and mod operations to land on "
        "integer offsets in the right range. Those become S1, T1, and U1 — one "
        "offset for each axis. Then, for every single pixel at position (i, j, k), "
        "the algorithm compares each coordinate against its corresponding offset. "
        "There are nine possible cases — three coordinates, each can be bigger, "
        "smaller, or equal to its offset — and each case dictates a specific swap. "
        "If i is bigger than S1, the pixel swaps with the pixel at position i plus "
        "S1. If i is smaller, it swaps with the absolute value of i minus S1. If "
        "they're equal, the pixel doesn't move on that axis. The same logic runs "
        "for j against T1 and k against U1. After running this for every pixel, "
        "you get the confusion cube C-prime. Pixel values are unchanged, but the "
        "spatial arrangement is now driven by chaos, so visually the cube already "
        "looks like noise. The really nice property is that those offsets actually "
        "depend on the plaintext itself, which makes the scheme plaintext-aware — "
        "encrypting two different images gives you two completely different cipher "
        "cubes, even with the same key."
    ),
    7: (
        "Now diffusion. Where confusion changed positions, diffusion changes pixel "
        "values directly. The first step is to flatten the confusion cube C-prime "
        "into a one-dimensional vector, V. Then the chaotic map gets iterated "
        "again to produce three new sequences — X2, Y2, and Z2. For the very first "
        "pixel of V, the algorithm XORs it with a seed value derived from the "
        "chaotic state, so that first pixel is hidden right away. Then for every "
        "pixel after the first, the algorithm takes the index k, computes k mod 3, "
        "and uses the result — zero, one, or two — to pick which of X2, Y2, or Z2 "
        "to XOR against. So you're not just using one chaotic stream, you're "
        "cycling through three independent streams, which makes the attacker's "
        "job significantly harder. And critically, the diffusion also uses the "
        "previous output pixel as part of the XOR. That means a single bit change "
        "at the very start of the image cascades all the way through the rest, "
        "because every later output pixel depends on the one before it. After "
        "looping through the whole vector, they reshape it back into a cube — "
        "that's the cipher cube D, and that's what gets transmitted. So at this "
        "point what an attacker sees is a noise-like 3D block — uniform histogram, "
        "near-zero correlation between neighbouring pixels, no visible structure "
        "left at all. That's the whole encryption procedure: confuse the positions, "
        "diffuse the values."
    ),
    8: (
        "Right — so does it actually work? Reconstruction quality is measured with "
        "PSNR, peak signal-to-noise ratio, in decibels. Anything around 30 dB is "
        "considered visually good — most viewers can't tell the difference from "
        "the original. The paper reports 32.06 dB on average, and that's after "
        "lossy DWT compression plus a full encrypt-decrypt round trip. Compare "
        "that to four prior schemes the authors benchmark against — those land "
        "between 26.3 and 27.7 dB. So this paper is roughly 4 to 6 dB better, "
        "which on the PSNR scale is a meaningful jump because PSNR is logarithmic, "
        "not linear. Visually, in Figure 7 of the paper, you literally cannot tell "
        "the decrypted image apart from the original by eye. On the speed side, "
        "total encryption runs at about 6.15 megabytes per second on their "
        "MATLAB-on-CPU setup, which is fast enough for batch transmission "
        "scenarios. So the scheme is not just secure on paper — the recovered "
        "image is actually clean, and the encryption is fast enough to be "
        "practical."
    ),
    9: (
        "Now the security analysis — four checks, all passed. First, the chaotic "
        "sequence itself goes through the NIST randomness suite, which is the "
        "standard 15-test battery used to validate any pseudo-random generator. "
        "Every single one of the fifteen tests passes with comfortable margins. "
        "Second, differential attack analysis. They flip one single pixel of the "
        "input image and re-encrypt, then measure NPCR and UACI between the two "
        "cipher images. The ideal targets are 99.6094 percent and 33.4635 percent. "
        "The paper hits 99.65 and 33.49 percent on average across twelve test "
        "images, so right on the ideal numbers. Third, information entropy of the "
        "cipher image is 7.9994, where the theoretical maximum is exactly 8.0 — "
        "so the cipher image is statistically indistinguishable from uniform "
        "noise. And fourth, the key space is huge — well beyond what any "
        "brute-force attack can cover, even with massive computing resources. So "
        "statistical attacks, differential attacks, and brute force are all "
        "blocked by the design."
    ),
    10: (
        "One honest limitation, which the authors flag themselves: when the images "
        "in a batch have different sizes, the cube has to be padded with zeros, "
        "and that wastes space. They mark that as future work. The take-home for "
        "us is this: by combining DWT compression with a 3D chaotic map, you get "
        "encryption and compression in a single pipeline, with reconstruction "
        "quality of 32 dB and entropy basically equal to perfect noise. One "
        "pipeline, multiple images, strong security. Thanks for listening — we're "
        "happy to take questions."
    ),
}


def blank_prs() -> Presentation:
    prs = Presentation()
    prs.slide_width = Inches(SLIDE_W)
    prs.slide_height = Inches(SLIDE_H)
    return prs


def add_blank(prs: Presentation):
    return prs.slides.add_slide(prs.slide_layouts[6])


def solid_background(slide, color=WHITE) -> None:
    slide.background.fill.solid()
    slide.background.fill.fore_color.rgb = color


def set_run(run, size=18, color=INK, bold=False, italic=False, font=FONT_BODY) -> None:
    run.font.name = font
    run.font.size = Pt(size)
    run.font.color.rgb = color
    run.font.bold = bold
    run.font.italic = italic


def add_text(
    slide,
    x,
    y,
    w,
    h,
    text,
    *,
    size=18,
    color=INK,
    bold=False,
    italic=False,
    font=FONT_BODY,
    align=PP_ALIGN.LEFT,
    valign=MSO_ANCHOR.TOP,
    margin=0.06,
    line_spacing=1.0,
):
    shape = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = shape.text_frame
    tf.clear()
    tf.word_wrap = True
    tf.margin_left = Inches(margin)
    tf.margin_right = Inches(margin)
    tf.margin_top = Inches(margin)
    tf.margin_bottom = Inches(margin)
    tf.vertical_anchor = valign
    lines = str(text).split("\n")
    for i, line in enumerate(lines):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = align
        p.line_spacing = line_spacing
        run = p.add_run()
        run.text = line
        set_run(run, size=size, color=color, bold=bold, italic=italic, font=font)
    return shape


def add_box(slide, x, y, w, h, *, fill=WHITE, line=LINE, radius=False, width=1.0):
    kind = MSO_SHAPE.ROUNDED_RECTANGLE if radius else MSO_SHAPE.RECTANGLE
    shape = slide.shapes.add_shape(kind, Inches(x), Inches(y), Inches(w), Inches(h))
    shape.fill.solid()
    shape.fill.fore_color.rgb = fill
    if line is None:
        shape.line.fill.background()
    else:
        shape.line.color.rgb = line
        shape.line.width = Pt(width)
    return shape


def add_card(slide, x, y, w, h, title, body, *, fill=PAPER, accent=TEAL, title_size=17, body_size=14):
    add_box(slide, x, y, w, h, fill=fill, line=LINE, radius=True)
    add_box(slide, x, y, 0.08, h, fill=accent, line=None)
    add_text(slide, x + 0.18, y + 0.12, w - 0.32, 0.35, title, size=title_size, bold=True, color=NAVY)
    add_text(slide, x + 0.18, y + 0.52, w - 0.32, h - 0.62, body, size=body_size, color=INK)


def add_bullets(slide, x, y, w, h, items, *, size=17, color=INK, bullet_color=TEAL):
    shape = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = shape.text_frame
    tf.clear()
    tf.word_wrap = True
    tf.margin_left = Inches(0.04)
    tf.margin_right = Inches(0.04)
    tf.margin_top = Inches(0.02)
    tf.margin_bottom = Inches(0.02)
    for i, item in enumerate(items):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.space_after = Pt(5)
        r1 = p.add_run()
        r1.text = "• "
        set_run(r1, size=size, color=bullet_color, bold=True)
        r2 = p.add_run()
        r2.text = item
        set_run(r2, size=size, color=color)
    return shape


def add_connector(slide, x1, y1, x2, y2, *, color=LINE, width=2.0):
    conn = slide.shapes.add_connector(
        MSO_CONNECTOR.STRAIGHT, Inches(x1), Inches(y1), Inches(x2), Inches(y2)
    )
    conn.line.color.rgb = color
    conn.line.width = Pt(width)
    return conn


def add_header(slide, n, title, speaker, section):
    solid_background(slide)
    speaker_color = NAVY if "Abdul" in speaker else TEAL
    add_text(slide, 0.5, 0.28, 8.2, 0.5, title, size=26, bold=True, color=NAVY, font=FONT_TITLE)
    add_box(slide, 9.6, 0.31, 3.15, 0.38, fill=speaker_color, line=None, radius=True)
    add_text(
        slide,
        9.68,
        0.34,
        2.99,
        0.27,
        f"{speaker} · {section}",
        size=11,
        bold=True,
        color=WHITE,
        align=PP_ALIGN.CENTER,
        margin=0,
    )
    add_box(slide, 0.5, 0.92, 12.33, 0.035, fill=LINE, line=None)
    add_footer(slide, n)


def add_footer(slide, n, total=TOTAL_MAIN):
    add_text(
        slide,
        0.5,
        7.03,
        8.9,
        0.22,
        "CMP4221 · DWT Encryption · Xu et al. · ACM TOMM 2026",
        size=9,
        color=MUTED,
        margin=0,
    )
    for i in range(total):
        fill = TEAL if i < n else LINE
        slide.shapes.add_shape(MSO_SHAPE.OVAL, Inches(10.0 + i * 0.16), Inches(7.05), Inches(0.07), Inches(0.07)).fill.solid()
        dot = slide.shapes[-1]
        dot.fill.fore_color.rgb = fill
        dot.line.fill.background()
    add_text(slide, 12.2, 7.0, 0.65, 0.22, f"{n}/{total}", size=9, color=MUTED, align=PP_ALIGN.RIGHT, margin=0)


def add_notes(slide, notes: str) -> None:
    tf = slide.notes_slide.notes_text_frame
    tf.clear()
    tf.text = notes
    for p in tf.paragraphs:
        for r in p.runs:
            set_run(r, size=12, color=INK)


def add_ref(slide, text):
    add_text(slide, 0.7, 6.62, 11.95, 0.22, f"Ref: {text}", size=9.5, color=MUTED, italic=True, margin=0)


def draw_cube(slide, x, y, w, h, *, fill=PALE_TEAL, edge=TEAL, label="3D cube"):
    add_box(slide, x + 0.28, y - 0.18, w, h, fill=c("D9EEEE"), line=edge)
    add_box(slide, x + 0.14, y - 0.09, w, h, fill=c("E2F3F2"), line=edge)
    add_box(slide, x, y, w, h, fill=fill, line=edge)
    add_text(slide, x + 0.08, y + h / 2 - 0.18, w - 0.16, 0.32, label, size=14, bold=True, color=NAVY, align=PP_ALIGN.CENTER)


def build_title_slide(prs):
    slide = add_blank(prs)
    solid_background(slide, WHITE)
    add_box(slide, 0, 0, 13.333, 7.5, fill=WHITE, line=None)
    add_box(slide, 0, 0, 4.25, 7.5, fill=NAVY, line=None)
    for i in range(8):
        add_box(slide, 0.65 + i * 0.23, 4.75 - i * 0.12, 1.7, 1.05, fill=c("214467"), line=c("456B91"))
    draw_cube(slide, 1.48, 2.25, 1.45, 1.05, fill=c("2C6F83"), edge=c("7BBFC2"), label="D")
    add_text(slide, 0.55, 0.42, 3.1, 0.4, "CMP4221 · Multimedia Systems", size=13, color=c("CFE2F3"), bold=True)
    add_text(slide, 0.55, 6.62, 3.1, 0.42, "Abdul Rahman Malak\nMaria Alftaih", size=13, color=WHITE, bold=True)
    add_text(slide, 4.75, 0.72, 7.8, 0.5, "Multi-Image Encryption with DWT + Chaotic Map", size=22, color=TEAL, bold=True)
    add_text(
        slide,
        4.72,
        1.35,
        7.9,
        1.85,
        "Compression + encryption\nin one pipeline",
        size=40,
        color=NAVY,
        bold=True,
        font=FONT_TITLE,
        line_spacing=0.9,
    )
    add_text(
        slide,
        4.78,
        3.55,
        7.5,
        0.92,
        "Xu, Gao, Cao, Mou · ACM TOMM Vol. 22 Issue 3 · March 2026\nDOI 10.1145/3769123",
        size=16,
        color=INK,
    )
    add_card(
        slide,
        4.78,
        4.96,
        7.48,
        1.14,
        "Thesis",
        "DWT shrinks each color image, the LL sub-bands are stacked into a cube, and chaos scrambles the cube into a secure cipher object.",
        fill=PALE_TEAL,
        accent=TEAL,
        title_size=15,
        body_size=12.5,
    )
    add_notes(slide, MAIN_NOTES[1])


def build_problem_slide(prs):
    slide = add_blank(prs)
    add_header(slide, 2, "Sending color images is slow AND unsafe", "Abdul · 1:00", "Problem")
    add_text(slide, 0.72, 1.25, 11.6, 0.36, "The paper is solving two costs at once: transmission size and confidentiality.", size=18, color=INK)
    cards = [
        ("Bandwidth", "A 512×512 RGB image has 786,432 channel values. A batch of images gets heavy fast.", NAVY),
        ("Confidentiality", "If images are intercepted, the visible content must be destroyed before transmission.", TEAL),
        ("Multi-image scale", "One-image-at-a-time encryption is awkward for batches like medical scans or surveillance frames.", AMBER),
    ]
    for i, (title, body, accent) in enumerate(cards):
        add_card(slide, 0.72 + i * 4.05, 2.0, 3.55, 2.15, title, body, fill=PAPER, accent=accent, title_size=18, body_size=15)
    add_box(slide, 1.1, 4.75, 11.15, 0.9, fill=PALE_AMBER, line=c("E8D4A6"), radius=True)
    add_text(slide, 1.35, 4.95, 10.65, 0.42, "Goal: compress AND encrypt multiple images in one pass.", size=24, color=NAVY, bold=True, align=PP_ALIGN.CENTER)
    add_ref(slide, "Section 1, Introduction")
    add_notes(slide, MAIN_NOTES[2])


def build_ingredients_slide(prs):
    slide = add_blank(prs)
    add_header(slide, 3, "Two ingredients: DWT and chaos", "Abdul · 1:30", "Background")
    add_text(slide, 0.75, 1.18, 5.1, 0.35, "DWT compression", size=20, color=NAVY, bold=True)
    x0, y0, box = 0.95, 1.75, 1.45
    subbands = [("LL", "approximation\nkeep this", PALE_TEAL), ("LH", "horizontal\nedges", PALE_NAVY), ("HL", "vertical\nedges", PALE_NAVY), ("HH", "diagonal\nedges", PALE_AMBER)]
    for idx, (name, desc, fill) in enumerate(subbands):
        x = x0 + (idx % 2) * (box + 0.08)
        y = y0 + (idx // 2) * (box + 0.08)
        add_box(slide, x, y, box, box, fill=fill, line=TEAL if name == "LL" else LINE, radius=False, width=2 if name == "LL" else 1)
        add_text(slide, x + 0.08, y + 0.22, box - 0.16, 0.35, name, size=26, color=NAVY, bold=True, align=PP_ALIGN.CENTER)
        add_text(slide, x + 0.1, y + 0.78, box - 0.2, 0.46, desc, size=11, color=INK, align=PP_ALIGN.CENTER)
    add_text(slide, 0.82, 5.2, 4.35, 0.55, "Keep LL only → half width × half height = 1/4 size", size=17, color=INK, bold=True)
    add_text(slide, 6.55, 1.18, 5.2, 0.35, "3D chaotic pseudo-random signal", size=20, color=NAVY, bold=True)
    add_box(slide, 6.58, 1.72, 5.65, 2.3, fill=PAPER, line=LINE, radius=True)
    points = [(0.4, 1.5), (0.9, 0.8), (1.25, 1.8), (1.75, 0.55), (2.25, 1.2), (2.65, 0.75), (3.1, 1.65), (3.55, 0.95), (4.0, 1.35), (4.5, 0.52)]
    for i in range(len(points) - 1):
        add_connector(slide, 6.85 + points[i][0], 1.98 + points[i][1], 6.85 + points[i + 1][0], 1.98 + points[i + 1][1], color=TEAL_2, width=1.6)
    for x, y in points:
        dot = slide.shapes.add_shape(MSO_SHAPE.OVAL, Inches(6.81 + x), Inches(1.94 + y), Inches(0.09), Inches(0.09))
        dot.fill.solid()
        dot.fill.fore_color.rgb = TEAL
        dot.line.fill.background()
    add_card(slide, 6.58, 4.38, 5.65, 1.28, "Key idea", "Looks random to an attacker, but repeats exactly for the receiver who knows the initial values and parameters.", fill=PALE_TEAL, accent=TEAL, title_size=16, body_size=14)
    add_ref(slide, "Fig. 5 (DWT decomposition) · Fig. 1 (chaotic phase diagram)")
    add_notes(slide, MAIN_NOTES[3])


def build_novelty_slide(prs):
    slide = add_blank(prs)
    add_header(slide, 4, "Novelty: encrypt the cube, not the images", "Abdul · 0:30", "Novelty")
    add_text(slide, 0.78, 1.2, 11.8, 0.48, "The novelty is not DWT alone or chaos alone. It is the multi-image cube strategy.", size=19, color=INK)
    for i, label in enumerate(["Image 1", "Image 2", "Image 3"]):
        add_box(slide, 1.0, 2.05 + i * 0.75, 1.35, 0.5, fill=PALE_NAVY, line=NAVY_2, radius=True)
        add_text(slide, 1.12, 2.16 + i * 0.75, 1.1, 0.2, label, size=12, color=NAVY, bold=True, align=PP_ALIGN.CENTER, margin=0)
    add_connector(slide, 2.55, 2.85, 4.05, 2.85, color=MUTED, width=2)
    add_text(slide, 2.78, 2.45, 1.1, 0.35, "DWT\nLL only", size=12, color=MUTED, align=PP_ALIGN.CENTER)
    draw_cube(slide, 4.3, 2.15, 1.75, 1.25, fill=PALE_TEAL, edge=TEAL, label="cube C")
    add_connector(slide, 6.35, 2.85, 7.85, 2.85, color=MUTED, width=2)
    add_text(slide, 6.58, 2.45, 1.0, 0.35, "one\npass", size=12, color=MUTED, align=PP_ALIGN.CENTER)
    draw_cube(slide, 8.1, 2.15, 1.75, 1.25, fill=PALE_AMBER, edge=AMBER, label="cipher D")
    add_card(slide, 1.0, 4.5, 3.55, 1.05, "1/4 size", "DWT keeps only LL, so each channel becomes half height by half width.", fill=PALE_TEAL, accent=TEAL)
    add_card(slide, 4.9, 4.5, 3.55, 1.05, "Different sizes", "The cube uses the largest dimensions and pads smaller images with zeros.", fill=PAPER, accent=AMBER)
    add_card(slide, 8.8, 4.5, 3.1, 1.05, "Single object", "Encrypt the whole stack instead of one image at a time.", fill=PALE_NAVY, accent=NAVY)
    add_ref(slide, "Innovations list, Section 1")
    add_notes(slide, MAIN_NOTES[4])


def build_pipeline_slide(prs):
    slide = add_blank(prs)
    add_header(slide, 5, "Methodology: DWT → stack → confusion → diffusion", "Abdul → Maria · 1:30", "Method")
    stages = [
        ("1", "DWT compression", "Each R,G,B channel → keep LL only\nimage shrinks to 1/4 size", TEAL),
        ("2", "Stack into cube C", "All compressed LL sub-bands\nsize from largest image", NAVY),
        ("3", "Confusion", "Chaotic offsets swap\npixel positions", AMBER),
        ("4", "Diffusion", "XOR changes values\noutput cipher cube D", RED),
    ]
    for i, (num, title, body, accent) in enumerate(stages):
        x = 0.72 + i * 3.13
        add_box(slide, x, 1.65, 2.65, 3.0, fill=PAPER, line=LINE, radius=True)
        add_box(slide, x + 0.18, 1.86, 0.52, 0.52, fill=accent, line=None, radius=True)
        add_text(slide, x + 0.32, 1.98, 0.22, 0.18, num, size=14, color=WHITE, bold=True, align=PP_ALIGN.CENTER, margin=0)
        add_text(slide, x + 0.18, 2.55, 2.24, 0.38, title, size=16, color=NAVY, bold=True, align=PP_ALIGN.CENTER)
        add_text(slide, x + 0.25, 3.08, 2.1, 0.82, body, size=13, color=INK, align=PP_ALIGN.CENTER)
        if i < len(stages) - 1:
            add_connector(slide, x + 2.72, 3.1, x + 3.0, 3.1, color=MUTED, width=2.2)
    add_box(slide, 2.15, 5.28, 9.1, 0.9, fill=PALE_TEAL, line=TEAL, radius=True)
    add_text(slide, 2.35, 5.45, 8.7, 0.46, "Transmit D. Receiver runs diffusion, confusion, and DWT recovery in reverse.", size=17, color=NAVY, bold=True, align=PP_ALIGN.CENTER)
    add_ref(slide, "Fig. 4 (encryption flow chart) · Fig. 7 (visual results)")
    add_notes(slide, MAIN_NOTES[5])


def draw_pixel_grid(slide, x, y, labels, *, accent=TEAL):
    cell = 0.32
    for r in range(5):
        for col in range(5):
            fill = WHITE
            txt = ""
            if (r, col) in labels:
                txt = labels[(r, col)][0]
                fill = labels[(r, col)][1]
            add_box(slide, x + col * cell, y + r * cell, cell, cell, fill=fill, line=LINE)
            if txt:
                add_text(slide, x + col * cell + 0.03, y + r * cell + 0.07, cell - 0.06, 0.12, txt, size=8, bold=True, color=NAVY, align=PP_ALIGN.CENTER, margin=0)
    outline = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE,
        Inches(x - 0.03),
        Inches(y - 0.03),
        Inches(cell * 5 + 0.06),
        Inches(cell * 5 + 0.06),
    )
    outline.fill.background()
    outline.line.color.rgb = accent
    outline.line.width = Pt(1.5)


def build_confusion_slide(prs):
    slide = add_blank(prs)
    add_header(slide, 6, "Confusion: scrambling pixel POSITIONS", "Maria · 1:30", "Method")
    add_bullets(
        slide,
        0.72,
        1.28,
        5.9,
        2.35,
        [
            "Iterate chaotic map once per cube pixel.",
            "Generate coordinate offsets S1, T1, U1.",
            "Compare each pixel coordinate with its offset.",
            "Pixel values stay the same; positions move.",
            "Offsets depend on plaintext, so the scheme is plaintext-aware.",
        ],
        size=15,
    )
    add_text(slide, 7.15, 1.25, 2.0, 0.25, "Before", size=15, bold=True, color=NAVY, align=PP_ALIGN.CENTER)
    add_text(slide, 10.05, 1.25, 2.0, 0.25, "After confusion", size=15, bold=True, color=NAVY, align=PP_ALIGN.CENTER)
    draw_pixel_grid(slide, 7.32, 1.75, {(1, 1): ("A", PALE_TEAL), (3, 3): ("B", PALE_AMBER)}, accent=TEAL)
    draw_pixel_grid(slide, 10.22, 1.75, {(3, 3): ("A", PALE_TEAL), (1, 1): ("B", PALE_AMBER)}, accent=AMBER)
    add_connector(slide, 9.25, 2.55, 10.0, 2.55, color=MUTED, width=2)
    add_box(slide, 7.1, 4.15, 5.0, 1.35, fill=PAPER, line=LINE, radius=True)
    add_text(slide, 7.32, 4.35, 4.56, 0.86, "Rule idea: if a coordinate is larger/smaller/equal to its chaotic offset, swap with the corresponding target coordinate. Across i, j, k, this creates nine cases.", size=13, color=INK)
    add_ref(slide, "Section 4.1.2 · Equations (8)-(10)")
    add_notes(slide, MAIN_NOTES[6])


def build_diffusion_slide(prs):
    slide = add_blank(prs)
    add_header(slide, 7, "Diffusion: XOR with a chaotic stream", "Maria · 1:30", "Method")
    add_bullets(
        slide,
        0.72,
        1.28,
        5.35,
        2.25,
        [
            "Flatten C-prime into vector V.",
            "First pixel XORs with a chaotic seed.",
            "For later pixels, index mod 3 selects X2, Y2, or Z2.",
            "Previous encrypted pixel is reused.",
            "One bit change cascades through the rest.",
        ],
        size=15,
    )
    add_box(slide, 6.55, 1.35, 5.75, 1.45, fill=PALE_NAVY, line=NAVY_2, radius=True)
    add_text(slide, 6.8, 1.78, 5.25, 0.28, "D[k] = V[k]  XOR  chaos[k mod 3]  XOR  D[k-1]", size=18, color=NAVY, bold=True, font=FONT_MONO, align=PP_ALIGN.CENTER)
    nodes = [("V[k]", PALE_TEAL), ("chaos", PALE_AMBER), ("D[k-1]", PALE_NAVY), ("D[k]", c("E9F7ED"))]
    positions = [(6.68, 3.55), (8.12, 3.55), (9.56, 3.55), (11.0, 3.55)]
    for idx, ((label, fill), (x, y)) in enumerate(zip(nodes, positions)):
        add_box(slide, x, y, 1.0, 0.75, fill=fill, line=TEAL if idx != 1 else AMBER, radius=True)
        add_text(slide, x + 0.07, y + 0.24, 0.86, 0.18, label, size=13, color=NAVY, bold=True, align=PP_ALIGN.CENTER, margin=0)
        if idx < len(nodes) - 1:
            add_text(slide, x + 1.02, y + 0.24, 0.38, 0.18, "XOR", size=8.5, color=MUTED, bold=True, align=PP_ALIGN.CENTER, margin=0)
    add_box(slide, 0.9, 4.7, 11.3, 0.82, fill=PALE_TEAL, line=TEAL, radius=True)
    add_text(slide, 1.15, 4.9, 10.8, 0.28, "Confusion hides where pixels are. Diffusion hides what pixel values are.", size=19, color=NAVY, bold=True, align=PP_ALIGN.CENTER)
    add_ref(slide, "Section 4.1.3 · Equations (11)-(13)")
    add_notes(slide, MAIN_NOTES[7])


def build_results_slide(prs):
    slide = add_blank(prs)
    add_header(slide, 8, "Findings: PSNR 32.06 dB beats prior work", "Maria · 1:00", "Findings")
    values = [32.0601, 26.2896, 27.6917, 27.3366, 27.4886]
    labels = ["This paper", "Ref. [8]", "Ref. [22]", "Ref. [46]", "Ref. [19]"]
    max_val = 34
    chart_x, chart_y, chart_w, chart_h = 0.95, 1.45, 6.25, 3.8
    add_text(slide, chart_x, 1.12, chart_w, 0.25, "PSNR comparison (dB)", size=16, color=NAVY, bold=True)
    for i, (label, val) in enumerate(zip(labels, values)):
        y = chart_y + i * 0.62
        add_text(slide, chart_x, y + 0.08, 1.25, 0.18, label, size=10.5, color=INK, align=PP_ALIGN.RIGHT, margin=0)
        bar_w = 4.35 * (val / max_val)
        fill = TEAL if i == 0 else c("9EB3C7")
        add_box(slide, chart_x + 1.45, y, bar_w, 0.35, fill=fill, line=None, radius=True)
        add_text(slide, chart_x + 1.55 + bar_w, y + 0.06, 0.62, 0.13, f"{val:.2f}", size=9.5, color=INK, margin=0)
    metrics = [("32.0601 dB", "reconstruction PSNR"), ("1/4", "compressed size"), ("6.1529 MB/s", "encryption speed")]
    for i, (num, label) in enumerate(metrics):
        add_box(slide, 7.75, 1.55 + i * 1.25, 4.25, 0.95, fill=PAPER if i != 0 else PALE_TEAL, line=LINE, radius=True)
        add_text(slide, 8.0, 1.75 + i * 1.25, 1.85, 0.28, num, size=21, color=TEAL if i != 1 else AMBER, bold=True, margin=0)
        add_text(slide, 9.85, 1.81 + i * 1.25, 1.95, 0.22, label, size=12.5, color=INK, margin=0)
    add_ref(slide, "Table 2 (PSNR) · Fig. 7 (visuals) · Table 10 (speed)")
    add_notes(slide, MAIN_NOTES[8])


def build_security_slide(prs):
    slide = add_blank(prs)
    add_header(slide, 9, "Security: NIST · NPCR · UACI · IE all green", "Maria · 1:00", "Findings")
    rows = [
        ("NIST randomness", "15 tests", "15 / 15 passed", GREEN),
        ("NPCR", "target 99.6094%", "99.6533%", GREEN),
        ("UACI", "target 33.4635%", "33.4887%", GREEN),
        ("Information entropy", "max 8.0", "7.9994", GREEN),
        ("Key space", "brute force", "huge", GREEN),
    ]
    x, y = 0.85, 1.45
    widths = [2.45, 2.2, 2.05, 1.0]
    heads = ["Security check", "Target / meaning", "Result", "Status"]
    add_box(slide, x, y, sum(widths), 0.48, fill=NAVY, line=None)
    cur = x
    for head, w in zip(heads, widths):
        add_text(slide, cur + 0.08, y + 0.14, w - 0.16, 0.13, head, size=10.5, color=WHITE, bold=True, margin=0)
        cur += w
    for idx, row in enumerate(rows):
        yy = y + 0.48 + idx * 0.62
        fill = WHITE if idx % 2 == 0 else PAPER
        add_box(slide, x, yy, sum(widths), 0.62, fill=fill, line=LINE)
        cur = x
        for text, w in zip(row[:3], widths[:3]):
            add_text(slide, cur + 0.08, yy + 0.2, w - 0.16, 0.16, text, size=12, color=INK if cur != x else NAVY, bold=(cur == x), margin=0)
            cur += w
        add_text(slide, cur + 0.08, yy + 0.16, widths[3] - 0.16, 0.18, "PASS", size=11, color=GREEN, bold=True, align=PP_ALIGN.CENTER, margin=0)
    add_box(slide, 9.25, 1.62, 2.95, 2.6, fill=PALE_TEAL, line=TEAL, radius=True)
    add_text(slide, 9.48, 1.9, 2.5, 0.35, "What this means", size=18, color=NAVY, bold=True, align=PP_ALIGN.CENTER)
    add_text(slide, 9.55, 2.48, 2.35, 1.15, "The cipher behaves like noise: flat histogram, low correlation, high sensitivity to tiny plaintext/key changes.", size=14, color=INK, align=PP_ALIGN.CENTER)
    add_ref(slide, "Tables 1, 5, 6, 8 · Section 6")
    add_notes(slide, MAIN_NOTES[9])


def build_takehome_slide(prs):
    slide = add_blank(prs)
    add_header(slide, 10, "Limitation and take-home", "Maria · 0:30", "Closing")
    metrics = [("32 dB", "PSNR"), ("7.9994", "entropy"), ("99.65%", "NPCR")]
    for i, (num, label) in enumerate(metrics):
        add_box(slide, 1.0 + i * 4.1, 1.35, 3.25, 1.35, fill=PALE_TEAL if i == 0 else PAPER, line=TEAL if i == 0 else LINE, radius=True)
        add_text(slide, 1.18 + i * 4.1, 1.64, 2.9, 0.42, num, size=32, color=TEAL if i != 2 else GREEN, bold=True, align=PP_ALIGN.CENTER)
        add_text(slide, 1.18 + i * 4.1, 2.22, 2.9, 0.18, label, size=13, color=MUTED, align=PP_ALIGN.CENTER, margin=0)
    add_card(slide, 1.0, 3.35, 5.35, 1.15, "Limitation", "Zero-padding wastes cube space when image sizes differ. The authors flag this for future work.", fill=PALE_AMBER, accent=AMBER, title_size=18, body_size=15)
    add_card(slide, 6.9, 3.35, 5.35, 1.15, "Take-home", "DWT + chaos gives compression and encryption in one pipeline for multiple color images.", fill=PALE_TEAL, accent=TEAL, title_size=18, body_size=15)
    add_text(slide, 1.0, 5.55, 11.3, 0.42, "Questions?", size=30, color=NAVY, bold=True, align=PP_ALIGN.CENTER, font=FONT_TITLE)
    add_ref(slide, "Section 7, Conclusion")
    add_notes(slide, MAIN_NOTES[10])


def build_main_deck() -> Presentation:
    prs = blank_prs()
    prs.core_properties.title = "CMP4221 - DWT Encryption Presentation"
    builders = [
        build_title_slide,
        build_problem_slide,
        build_ingredients_slide,
        build_novelty_slide,
        build_pipeline_slide,
        build_confusion_slide,
        build_diffusion_slide,
        build_results_slide,
        build_security_slide,
        build_takehome_slide,
    ]
    for builder in builders:
        builder(prs)
    return prs


def study_header(slide, n, title):
    solid_background(slide)
    add_text(slide, 0.55, 0.3, 10.9, 0.42, title, size=25, color=NAVY, bold=True, font=FONT_TITLE)
    add_text(slide, 11.7, 0.38, 1.0, 0.22, f"{n}/18", size=10, color=MUTED, align=PP_ALIGN.RIGHT, margin=0)
    add_box(slide, 0.55, 0.9, 12.25, 0.035, fill=LINE, line=None)


def study_slide(prs, n, title, bullets=None, cards=None, table=None, note=None):
    slide = add_blank(prs)
    study_header(slide, n, title)
    if bullets:
        add_bullets(slide, 0.85, 1.35, 11.65, 4.7, bullets, size=18)
    if cards:
        for card in cards:
            if len(card) == 8:
                x, y, w, h, title_text, body_text, fill, accent = card
                add_card(slide, x, y, w, h, title_text, body_text, fill=fill, accent=accent)
            else:
                add_card(slide, *card)
    if table:
        draw_study_table(slide, table)
    add_text(slide, 0.55, 7.02, 9.0, 0.18, "Companion study deck · not the 10-minute graded deck", size=8.5, color=MUTED, margin=0)
    add_notes(slide, note or title)
    return slide


def draw_study_table(slide, data):
    x, y = data.get("x", 0.8), data.get("y", 1.35)
    widths = data["widths"]
    row_h = data.get("row_h", 0.46)
    rows = data["rows"]
    add_box(slide, x, y, sum(widths), row_h, fill=NAVY, line=None)
    cur = x
    for head, w in zip(data["headers"], widths):
        add_text(slide, cur + 0.08, y + 0.14, w - 0.16, 0.12, head, size=10.5, color=WHITE, bold=True, margin=0)
        cur += w
    for idx, row in enumerate(rows):
        yy = y + row_h * (idx + 1)
        add_box(slide, x, yy, sum(widths), row_h, fill=WHITE if idx % 2 == 0 else PAPER, line=LINE)
        cur = x
        for text, w in zip(row, widths):
            add_text(slide, cur + 0.08, yy + 0.13, w - 0.16, 0.13, str(text), size=10.8, color=INK, margin=0)
            cur += w


def build_study_deck() -> Presentation:
    prs = blank_prs()
    prs.core_properties.title = "CMP4221 - DWT Encryption Study Deck"

    slide = add_blank(prs)
    solid_background(slide, NAVY)
    add_text(slide, 0.8, 0.7, 11.7, 0.5, "CMP4221 Companion Study Deck", size=22, color=c("BFE7E5"), bold=True)
    add_text(slide, 0.8, 1.55, 10.7, 1.25, "DWT Encryption\nbackup explanations", size=46, color=WHITE, bold=True, font=FONT_TITLE, line_spacing=0.9)
    draw_cube(slide, 9.55, 4.25, 1.8, 1.25, fill=c("2C6F83"), edge=c("8FD5D3"), label="D")
    add_text(slide, 0.82, 5.92, 10.8, 0.42, "Use this for rehearsal, defense, and Q&A. Do not present all of it in the 10-minute slot.", size=17, color=c("D7E8F6"))
    add_notes(slide, "Study deck cover.")

    study_slide(
        prs,
        2,
        "Requirement proof",
        table={
            "headers": ["Requirement", "Evidence"],
            "widths": [3.6, 8.2],
            "rows": [
                ("Journal", "ACM Transactions on Multimedia Computing, Communications, and Applications"),
                ("Year", "Crossref: online 2026-02-27; print 2026-03-31"),
                ("DOI", "10.1145/3769123"),
                ("Main deck timing", "10 slides; Abdul 1-5; Maria 6-10"),
                ("Required content", "Novelty slide 4; methodology slides 5-7; findings slides 8-9"),
            ],
        },
        note="Requirement proof slide.",
    )
    study_slide(
        prs,
        3,
        "Paper identity",
        bullets=[
            "Title: Multi-Image Encryption Scheme Based on Chaotic Pseudo-Random Signal Generator and DWT Compression.",
            "Authors: Yidan Xu, Suo Gao, Yinghong Cao, Jun Mou.",
            "Article 82, pages 1-20, ACM TOMM Vol. 22 Issue 3.",
            "Core topic: compress multiple color images, merge them into a cube, then encrypt with chaos.",
            "Do not use Options/3762860.fm.pdf as the article source; it is issue front matter.",
        ],
    )
    study_slide(
        prs,
        4,
        "Problem framing",
        cards=[
            (0.85, 1.35, 3.65, 1.35, "Bandwidth", "Multi-color images are large because every pixel has R, G, and B values.", PAPER, TEAL),
            (4.85, 1.35, 3.65, 1.35, "Security", "Visible image content must become unreadable before transmission.", PAPER, NAVY),
            (8.85, 1.35, 3.65, 1.35, "Batch use", "Multiple images need one efficient workflow instead of repeated single-image encryption.", PAPER, AMBER),
        ],
        bullets=["Exam phrase: the paper combines compression and encryption instead of treating them as separate afterthoughts."],
    )
    study_slide(
        prs,
        5,
        "DWT formula and LL-only compression",
        bullets=[
            "For each channel: [LL, LH, HL, HH] = DWT(channel).",
            "LL = low-frequency approximation. It keeps most visible structure.",
            "LH, HL, HH = detail bands. They carry edge/detail information.",
            "Keeping LL only gives half height and half width, so area becomes 1/4.",
            "Recovery is lossy, but the paper reports PSNR above 32 dB.",
        ],
    )
    study_slide(
        prs,
        6,
        "Chaotic key parameters",
        bullets=[
            "The chaotic map is deterministic: same key gives the same sequence.",
            "It is sensitive: a tiny initial-value change gives a totally different sequence.",
            "Paper parameters include a, b, c, d, k1, k2 and initial values x0, y0, z0.",
            "These sequences drive both position swaps and XOR diffusion.",
            "Security claim depends on randomness tests and key sensitivity.",
        ],
    )
    study_slide(
        prs,
        7,
        "Full pipeline recipe",
        bullets=[
            "1. Split every color image into R, G, B channels.",
            "2. Apply DWT to each channel and keep LL.",
            "3. Stack all LL data into cube C.",
            "4. Generate plaintext-related chaotic parameters.",
            "5. Confusion swaps positions; diffusion changes values.",
            "6. Transmit cipher cube D; receiver reverses the steps.",
        ],
    )
    study_slide(
        prs,
        8,
        "Cube sizing and zero-padding",
        bullets=[
            "Each compressed image has size hi/2 by wi/2 by li.",
            "The cube width and height follow the largest compressed images in the batch.",
            "Smaller images need padding so all data fits into the shared cube shape.",
            "Limitation: padding takes extra space and reduces efficiency for mixed-size batches.",
            "Future-work line: reduce extra-space utilization for more robust, less resource-intensive encryption.",
        ],
    )
    study_slide(
        prs,
        9,
        "Confusion algorithm",
        bullets=[
            "Purpose: change where pixels are.",
            "Input: plaintext cube C.",
            "Chaotic sequences become coordinate offsets S1, T1, U1.",
            "For each pixel (i, j, k), compare coordinates against offsets.",
            "Nine swap cases move pixels into new cube positions.",
            "Output: C-prime, a position-scrambled cube.",
        ],
    )
    study_slide(
        prs,
        10,
        "Diffusion algorithm",
        bullets=[
            "Purpose: change pixel values.",
            "Flatten C-prime into vector V.",
            "First value XORs with a chaotic seed.",
            "Later values use index mod 3 to select X2, Y2, or Z2.",
            "Each output also depends on the previous output, creating a cascade.",
            "Output: cipher cube D.",
        ],
    )
    study_slide(
        prs,
        11,
        "Metric: PSNR",
        bullets=[
            "PSNR = Peak Signal-to-Noise Ratio.",
            "Unit: decibels.",
            "Higher PSNR means reconstructed image is closer to the original.",
            "The paper says around 30 dB is generally acceptable visual recovery.",
            "Reported result: 32.0601 dB after compression and encryption/decryption.",
        ],
    )
    study_slide(
        prs,
        12,
        "PSNR comparison",
        table={
            "headers": ["Scheme", "PSNR (dB)"],
            "widths": [6.0, 3.0],
            "rows": [
                ("Proposed scheme", "32.0601"),
                ("Ref. [8]", "26.2896"),
                ("Ref. [22]", "27.6917"),
                ("Ref. [46]", "27.3366"),
                ("Ref. [19]", "27.4886"),
            ],
        },
    )
    study_slide(
        prs,
        13,
        "NIST randomness summary",
        bullets=[
            "NIST suite checks whether a pseudo-random generator behaves statistically random.",
            "The paper reports all 15 tests passed.",
            "Pass condition used: p-value >= 0.01 and pass rate above the accepted threshold.",
            "Presentation line: the chaotic generator passed the randomness battery.",
        ],
    )
    study_slide(
        prs,
        14,
        "Differential attack metrics",
        table={
            "headers": ["Metric", "Target", "Paper result", "Meaning"],
            "widths": [2.2, 2.4, 2.4, 4.7],
            "rows": [
                ("NPCR", "99.6094%", "99.6533%", "How many pixels change after a tiny plaintext change"),
                ("UACI", "33.4635%", "33.4887%", "Average intensity change between two cipher images"),
            ],
            "row_h": 0.64,
        },
    )
    study_slide(
        prs,
        15,
        "Information entropy",
        bullets=[
            "Information entropy measures how uniform/unpredictable the cipher pixel distribution is.",
            "The theoretical maximum for 8-bit images is 8.",
            "The paper reports 7.9994, essentially maximum entropy.",
            "Presentation line: the cipher image is statistically close to uniform noise.",
        ],
    )
    study_slide(
        prs,
        16,
        "Speed and efficiency",
        table={
            "headers": ["Step", "Time (s)", "Speed"],
            "widths": [4.2, 2.6, 3.2],
            "rows": [
                ("Confusion", "0.1124", "177.9359"),
                ("Diffusion", "3.1381", "6.3733"),
                ("Total encryption", "3.2505", "6.1529"),
            ],
        },
    )
    study_slide(
        prs,
        17,
        "Likely Q&A",
        bullets=[
            "Q: Is this lossless? A: No. DWT LL-only compression is lossy, but PSNR is still strong.",
            "Q: Why use a cube? A: It lets the method encrypt multiple images together in one object.",
            "Q: What is the main limitation? A: Zero-padding wastes space for mixed-size images.",
            "Q: Is chaos alone enough? A: No. The scheme combines confusion, diffusion, and tested randomness.",
            "Q: What is the strongest result? A: PSNR 32.0601 dB plus strong NPCR/UACI/entropy values.",
        ],
    )
    study_slide(
        prs,
        18,
        "Rehearsal checklist",
        bullets=[
            "Abdul: keep slides 3 and 5 tight; do not over-explain wavelets.",
            "Maria: define confusion and diffusion in one sentence each before details.",
            "Both: say numbers cleanly: PSNR 32.06, NPCR 99.65, UACI 33.49, entropy 7.9994.",
            "Do one timed run under 10 minutes before presenting.",
            "Use the study deck only for backup and Q&A practice.",
        ],
    )
    return prs


def export_pdf(pptx_path: Path, pdf_path: Path) -> bool:
    try:
        import pythoncom
        import win32com.client
    except ImportError:
        print(f"pywin32 not available; skipped PDF export for {pptx_path.name}", file=sys.stderr)
        return False

    pythoncom.CoInitialize()
    pp = None
    deck = None
    try:
        pp = win32com.client.Dispatch("PowerPoint.Application")
        pp.Visible = 1
        deck = pp.Presentations.Open(str(pptx_path), ReadOnly=True, Untitled=False, WithWindow=False)
        deck.SaveAs(str(pdf_path), 32)
        print(f"PDF written:  {pdf_path}")
        return True
    except Exception as exc:
        print(f"PDF conversion failed for {pptx_path.name}: {exc}", file=sys.stderr)
        return False
    finally:
        if deck is not None:
            try:
                deck.Close()
            except Exception:
                pass
        if pp is not None:
            try:
                pp.Quit()
            except Exception:
                pass
        pythoncom.CoUninitialize()


def save_decks() -> None:
    main = build_main_deck()
    main.save(MAIN_PPTX)
    print(f"PPTX written: {MAIN_PPTX}")

    study = build_study_deck()
    study.save(STUDY_PPTX)
    print(f"PPTX written: {STUDY_PPTX}")

    export_pdf(MAIN_PPTX, MAIN_PDF)
    export_pdf(STUDY_PPTX, STUDY_PDF)

    abdul_words = sum(len(MAIN_NOTES[i].split()) for i in range(1, 6))
    maria_words = sum(len(MAIN_NOTES[i].split()) for i in range(6, 11))
    print(f"Speaker-note word counts: Abdul={abdul_words}, Maria={maria_words}")


if __name__ == "__main__":
    save_decks()
