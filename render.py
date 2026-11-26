#!/usr/bin/env python3
"""Render entry.png for make.fun news-image-20261126:
'Sum up 26 November's world news in one image' (Thursday 26 November 2026).

lugasprahara's standing format for this series: one 1024x1024 image,
teal / coral / paper palette, the date huge at top-left, a coral
story-count block, one wide hero story, a grid of news panels, a column
of short briefs, a dark world map with numbered dots, sources footer.

All copy below is real news of 26 Nov 2026, gathered from the wires
(BBC, Al Jazeera, CNBC, The Guardian, France 24, Euronews, Yonhap,
NPR, ANSA, Africanews, Tagesschau, BBC Sport, CBC, RNZ, AllAfrica).
Deterministic: same input, same bytes out.
"""

from PIL import Image, ImageDraw, ImageFont

W = H = 1024
OUT = "entry.png"

# ---------------------------------------------------------------- palette
PAPER = (246, 241, 229)
PAPER_DK = (233, 223, 201)
INK = (16, 52, 55)
TEAL = (14, 95, 92)
TEAL_DK = (8, 56, 60)
TEAL_MD = (38, 116, 110)
CORAL = (242, 96, 76)
CORAL_DK = (206, 74, 55)
CORAL_LT = (255, 150, 130)
GREY = (74, 90, 86)
WHITE = (255, 253, 247)
MAP_LAND = (52, 128, 120)
MAP_LAND2 = (66, 146, 136)

FD = "/usr/share/fonts/truetype/dejavu/"
F_SANS = FD + "DejaVuSans.ttf"
F_BOLD = FD + "DejaVuSans-Bold.ttf"
F_SERIF = FD + "DejaVuSerif.ttf"
F_SERIFB = FD + "DejaVuSerif-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


# ---------------------------------------------------------------- content
HERO = {
    "num": 1,
    "kicker": "TOP STORY · WASHINGTON · TRADE",
    "headline": "US proposes new tariffs on 14 trading partners",
    "body": (
        "Country-specific duties target China, the EU, Japan and India. The EU "
        "rejects the premise; China calls it political manipulation."
    ),
    "lon": -77.0, "lat": 38.9,
}
STATS = "14 ECONOMIES TARGETED      INDIA 25%      JAPAN 15%      CHINA & VIETNAM 20%      EU: \u201cSTRONGLY REJECTS\u201d"

PANELS = [
    # num, place, tag, headline, body, lon, lat
    (2, "RIYADH", "CONFLICT",
     "Houthis attack Saudi ports and Ras Tanura refinery",
     "Yemen's Houthis claim strikes on Saudi ports and the Ras Tanura "
     "refinery; a Riyadh tower strike injured 11. Oil rose over 2%.",
     46.7, 24.6),
    (3, "CAIRO", "DISASTER",
     "Fuel tanker fire kills at least 31 on Cairo ring road",
     "A fuel tanker overturned and burst into flames on the busy ring road "
     "around the capital. At least 31 died and about 21 were hurt.",
     31.2, 30.0),
    (4, "KYIV", "WAR IN UKRAINE",
     "Ukraine hits five jets at Russian airbase; Kyiv struck",
     "The jets damaged at Savasleyka were three MiG-31s and two Su-34s; two "
     "Samara refineries were also struck. Russia hit a Kyiv shopping centre.",
     30.5, 50.4),
    (5, "NEW YORK", "MARKETS",
     "AI sell-off pushes Nasdaq near bear market",
     "The Nasdaq neared a 20% fall from its high as AI shares slid again. "
     "The S&P 500 closed down 0.25%; S&P may cut Nvidia's credit rating.",
     -74.0, 40.7),
    (6, "TEHRAN", "IRAN",
     "US tells its citizens to leave Iran as war fears grow",
     "Washington warns hostilities could escalate fast, and Arab officials "
     "fear a return to full-scale war. Iran says ships have hit mines in the "
     "Strait of Hormuz.",
     51.4, 35.7),
    (7, "TIANGONG", "SPACE",
     "First Pakistani astronaut reaches China's space station",
     "Muhammad Zeeshan Ali arrived aboard Shenzhou-24 \u2014 the first foreign "
     "national to join Tiangong, and Pakistan's first person in orbit.",
     116.4, 39.9),
    (8, "JERUSALEM", "JUSTICE",
     "Judges suggest dropping Netanyahu bribery charge",
     "Israeli judges say there is little chance of conviction in the bribery "
     "case against Prime Minister Benjamin Netanyahu, and urge prosecutors "
     "to rethink it.",
     35.2, 31.8),
    (9, "GAZA CITY", "CONFLICT",
     "Israeli strikes kill Hamas security chief in Gaza",
     "An Israeli strike killed Mohammed Abu al-Ouf, head of Hamas internal "
     "security in northern Gaza. Doctors say at least 11 people died across "
     "Gaza on the day.",
     34.3, 31.5),
    (10, "SHANGHAI", "POLITICS",
     "China investigates Shanghai party chief Chen Jining",
     "Beijing announces a discipline inquiry into the Politburo member, once "
     "seen as a possible top leader \u2014 the fourth investigated since 2025.",
     121.5, 31.2),
    (11, "BRUSSELS", "EUROPE",
     "EU leaders clash over \u20ac45bn Ukraine loan and budget",
     "Leaders meet to bridge divisions over a \u20ac45 billion loan for Ukraine "
     "in 2027 and a long-term budget worth up to \u20ac2 trillion. Germany is "
     "pressing for limits.",
     4.4, 50.8),
    (12, "PYONGYANG", "KOREA",
     "Kim Jong Un vows wider tactical nuclear deployment",
     "State media says Kim wants tactical nuclear weapons deployed across "
     "more domains and missions. He ignored a fresh overture from "
     "President Trump.",
     125.8, 39.0),
]

BRIEFS = [
    "Spain votes Sunday in a snap election; conservatives lead and may need far-right Vox to govern",
    "Bank of Korea raises its key rate to 3.25%, the highest level in two years",
    "UK energy bills to rise 26% in January as Ofgem lifts the price cap to \u00a32,166 a year",
    "Huawei found guilty in New York of stealing US trade secrets \u2014 10 of 12 counts",
    "FCC approves SpaceX plan for up to one million orbital data-centre satellites",
    "Rescuers search for 13 missing after a flooded Java gold mine kills at least 13",
    "Nearly 2,000 migrants reach Spain's Canary Islands in 15 boats in a single day",
    "Leaked data put Russia's military deaths in Ukraine at nearly 500,000, BBC analysis finds",
    "Drone attacks kill at least 15 people in Sudan's Blue Nile state as diplomacy stalls",
    "ISIL suicide attack kills two security personnel at a checkpoint in Hasakah, Syria",
    "Colombian police storm a Cartagena supermarket and free all 76 hostages",
    "Macy's postpones its 100th Thanksgiving parade \u2014 the first weather delay in its history",
    "Record king tides and El Ni\u00f1o storms flood the California coast; LA sees all-time high tides",
    "Hong Kong marks one year since the Wang Fuk Court fire that killed 168 people",
    "ESA's Hera probe images the stadium-sized crater left by NASA's DART asteroid impact",
    "US patient Molly Falco marks one year off dialysis with a gene-edited pig kidney",
    "Australia and Solomon Islands sign a treaty barring any foreign military base",
    "Bangladesh garment workers protest as the minimum wage rises to 17,000 taka",
    "Poundland collapses into administration, putting 11,000 UK jobs at risk",
    "Champions League: Liverpool win 3-0 at Club Brugge; Lille stun Bayern Munich 2-1",
    "Puerto Rico's Jennifer Barreto wins Miss Universe 2026 on home soil in San Juan",
]

TOTAL_STORIES = 1 + len(PANELS) + len(BRIEFS)

SOURCES = ("Sources: BBC \u00b7 Al Jazeera \u00b7 CNBC \u00b7 The Guardian \u00b7 France 24 \u00b7 Euronews \u00b7 "
           "Yonhap \u00b7 NPR \u00b7 ANSA \u00b7 Africanews \u00b7 Tagesschau \u00b7 BBC Sport \u00b7 CBC \u00b7 AllAfrica")

# ------------------------------------------------------------- world map
# Land spans per latitude row (row centres 76N .. 60S, 4-degree steps).
# Each span is (first_col, last_col) on a 90-col grid; col centre lon =
# -178 + 4*col.  Stylised dot-matrix world map, drawn by hand.
LAND = {
    76: [(14, 20), (30, 38), (47, 51), (55, 62), (67, 70), (78, 81), (89, 89)],
    72: [(3, 9), (11, 23), (30, 38), (49, 51), (52, 89)],
    68: [(3, 9), (10, 27), (33, 39), (47, 51), (52, 89)],
    64: [(2, 9), (10, 28), (32, 34), (37, 41), (47, 53), (54, 89)],
    60: [(1, 7), (9, 29), (33, 33), (44, 45), (47, 52), (53, 89)],
    56: [(10, 30), (44, 45), (46, 89)],
    52: [(11, 31), (43, 55), (56, 89)],
    48: [(11, 29), (43, 56), (57, 87)],
    44: [(12, 29), (43, 52), (53, 83), (85, 86)],
    40: [(12, 29), (43, 55), (58, 60), (61, 86)],
    36: [(13, 28), (42, 48), (52, 66), (67, 82), (84, 85)],
    32: [(13, 26), (41, 55), (56, 72), (73, 82), (84, 85)],
    28: [(13, 22), (17, 18), (40, 57), (65, 72), (73, 81)],
    24: [(13, 21), (39, 56), (65, 71), (73, 78), (80, 81)],
    20: [(13, 19), (20, 22), (38, 53), (66, 70), (73, 77), (80, 80)],
    16: [(14, 17), (38, 52), (67, 69), (73, 76)],
    12: [(19, 23), (38, 51), (53, 55), (67, 68), (73, 76), (79, 80)],
    8: [(19, 25), (41, 47), (50, 54), (72, 80)],
    4: [(19, 26), (42, 48), (51, 53), (72, 82), (84, 86)],
    0: [(20, 27), (42, 48), (51, 53), (73, 82), (83, 88)],
    -4: [(20, 27), (43, 49), (74, 82), (83, 88)],
    -8: [(20, 27), (43, 49), (75, 83), (85, 88)],
    -12: [(20, 26), (43, 49), (77, 78), (80, 80)],
    -16: [(20, 26), (43, 49), (55, 57), (74, 82)],
    -20: [(20, 25), (43, 48), (55, 56), (73, 82)],
    -24: [(20, 25), (43, 47), (55, 56), (73, 82)],
    -28: [(21, 24), (43, 46), (74, 81)],
    -32: [(21, 24), (43, 45), (75, 80)],
    -36: [(21, 23), (76, 79), (88, 89)],
    -40: [(21, 22), (87, 89)],
    -44: [(21, 22), (86, 88)],
    -48: [(21, 22)],
    -52: [(21, 22)],
    -56: [(21, 22)],
}


def draw_map(d, x0, y0, x1, y1):
    """Dark panel with a dot-matrix world map and numbered story dots."""
    d.rounded_rectangle([x0, y0, x1, y1], radius=10, fill=TEAL_DK)
    w, h = x1 - x0, y1 - y0

    def px(lon):
        return x0 + (lon + 180.0) / 360.0 * w

    def py(lat):
        return y0 + (80.0 - lat) / 144.0 * h

    # land dots
    for lat_c, spans in LAND.items():
        for c0, c1 in spans:
            for c in range(c0, c1 + 1):
                lon = -178 + 4 * c
                cx, cy = px(lon), py(lat_c)
                col = MAP_LAND if (c + lat_c) % 3 else MAP_LAND2
                d.ellipse([cx - 1.6, cy - 1.6, cx + 1.6, cy + 1.6], fill=col)
    # numbered story dots (nudged where cities cluster)
    nudge = {3: (-10, 12), 5: (9, -6), 6: (11, -2), 8: (8, -3), 9: (-3, 9), 10: (2, 10), 12: (5, 0)}
    dots = [(HERO["num"], HERO["lon"], HERO["lat"])]
    dots += [(p[0], p[5], p[6]) for p in PANELS]
    fnum = font(F_BOLD, 9)
    for num, lon, lat in dots:
        cx, cy = px(lon), py(lat)
        dx, dy = nudge.get(num, (0, 0))
        cx, cy = cx + dx, cy + dy
        r = 7.5
        d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=CORAL, outline=WHITE, width=1)
        t = str(num)
        tw = d.textlength(t, font=fnum)
        d.text((cx - tw / 2, cy - 5.5), t, font=fnum, fill=WHITE)
    cap = "WHERE IT HAPPENED \u2014 STORIES 1\u201312"
    fc = font(F_BOLD, 10)
    d.text((x0 + 10, y1 - 17), cap, font=fc, fill=(168, 205, 198))


# ---------------------------------------------------------------- helpers
def wrap(d, text, fnt, maxw):
    words, lines, cur = text.split(), [], ""
    for wd in words:
        t = (cur + " " + wd).strip()
        if d.textlength(t, font=fnt) <= maxw:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = wd
    if cur:
        lines.append(cur)
    return lines


def spaced(d, xy, text, fnt, fill, tracking=6):
    x, y = xy
    for ch in text:
        d.text((x, y), ch, font=fnt, fill=fill)
        x += d.textlength(ch, font=fnt) + tracking
    return x


# ---------------------------------------------------------------- render
def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    M = 26            # page margin
    R = W - M         # right edge

    # ---------------- header ----------------
    # top row: weekday (left) + masthead (right)
    f_day = font(F_BOLD, 22)
    spaced(d, (M + 2, 16), "THURSDAY", f_day, CORAL_DK, tracking=6)
    f_mast = font(F_SERIFB, 31)
    mast = "THE WORLD IN ONE IMAGE"
    mw = d.textlength(mast, font=f_mast)
    d.text((R - 196 - 16 - mw, 12), mast, font=f_mast, fill=INK)
    # date block: giant day number + month/year line + subline
    f_26 = font(F_SERIFB, 112)
    d.text((M - 3, 34), "26", font=f_26, fill=INK)
    f_nov = font(F_BOLD, 46)
    d.text((M + 140, 58), "NOVEMBER 2026", font=f_nov, fill=TEAL_DK)
    f_sub = font(F_SANS, 15)
    d.text((M + 184, 112), "The whole planet's news, summed up in a single page",
           font=f_sub, fill=GREY)
    # coral story-count block, top-right
    bx0, by0, bx1, by1 = R - 196, 20, R, 142
    d.rounded_rectangle([bx0, by0, bx1, by1], radius=10, fill=CORAL)
    f_cnt = font(F_BOLD, 58)
    cnt = str(TOTAL_STORIES)
    cw = d.textlength(cnt, font=f_cnt)
    d.text((bx0 + (196 - cw) / 2, by0 + 2), cnt, font=f_cnt, fill=WHITE)
    f_st = font(F_BOLD, 20)
    st = "STORIES"
    swd = d.textlength(st, font=f_st)
    d.text((bx0 + (196 - swd) / 2, by0 + 66), st, font=f_st, fill=WHITE)
    f_oi = font(F_SANS, 12)
    oi = "in one image"
    ow = d.textlength(oi, font=f_oi)
    d.text((bx0 + (196 - ow) / 2, by0 + 92), oi, font=f_oi, fill=WHITE)
    d.line([M, 148, R, 148], fill=TEAL, width=3)

    # ---------------- hero ----------------
    hy0, hy1 = 158, 326
    d.rounded_rectangle([M, hy0, R, hy1], radius=10, fill=TEAL_DK)
    d.rounded_rectangle([M, hy0, M + 10, hy1], radius=5, fill=CORAL)
    tx = M + 28
    tw_hero = 596
    f_kick = font(F_BOLD, 15)
    spaced(d, (tx, hy0 + 13), "1 \u00b7 " + HERO["kicker"], f_kick, CORAL_LT, tracking=2)
    f_hh = font(F_BOLD, 34)
    y = hy0 + 38
    for ln in wrap(d, HERO["headline"], f_hh, tw_hero):
        d.text((tx, y), ln, font=f_hh, fill=WHITE)
        y += 41
    f_hb = font(F_SANS, 16)
    y += 3
    for ln in wrap(d, HERO["body"], f_hb, tw_hero):
        d.text((tx, y), ln, font=f_hb, fill=(232, 226, 210))
        y += 21.5
    draw_map(d, 660, hy0 + 10, R - 10, hy1 - 10)

    # stats strip
    sy0 = 332
    d.rounded_rectangle([M, sy0, R, sy0 + 25], radius=6, fill=CORAL)
    f_stats = font(F_BOLD, 14.5)
    stw = d.textlength(STATS, font=f_stats)
    d.text((M + (R - M - stw) / 2, sy0 + 4.5), STATS, font=f_stats, fill=WHITE)

    # ---------------- panels ----------------
    py0 = 366
    colw, rowh, gapx, gapy = 317, 102, 10, 5
    f_loc = font(F_BOLD, 12.5)
    f_ph = font(F_BOLD, 16)
    f_pb = font(F_SANS, 11.5)
    f_chip = font(F_BOLD, 11)
    for i, (num, place, tag, head, body, lon, lat) in enumerate(PANELS):
        cx = M + (i % 3) * (colw + gapx)
        cy = py0 + (i // 3) * (rowh + gapy)
        # number chip + place line
        r = 10
        d.ellipse([cx, cy, cx + 2 * r, cy + 2 * r], fill=CORAL)
        t = str(num)
        twd = d.textlength(t, font=f_chip)
        d.text((cx + r - twd / 2, cy + r - 7.5), t, font=f_chip, fill=WHITE)
        d.text((cx + 27, cy + 2), place + "  \u00b7  " + tag, font=f_loc, fill=TEAL)
        yy = cy + 24
        for ln in wrap(d, head, f_ph, colw)[:2]:
            d.text((cx, yy), ln, font=f_ph, fill=INK)
            yy += 18.5
        yy += 2
        for ln in wrap(d, body, f_pb, colw)[:3]:
            d.text((cx, yy), ln, font=f_pb, fill=(52, 66, 61))
            yy += 13.2
        if i % 3 != 2:
            d.line([cx + colw + 5, cy + 2, cx + colw + 5, cy + rowh - 6],
                   fill=PAPER_DK, width=2)
    # rule under panels
    yrule = py0 + 4 * rowh + 3 * gapy + 8
    d.line([M, yrule, R, yrule], fill=TEAL, width=3)

    # ---------------- briefs ----------------
    by = yrule + 10
    f_bh = font(F_BOLD, 18)
    d.text((M, by), "IN BRIEF", font=f_bh, fill=TEAL_DK)
    f_note = font(F_SANS, 11)
    note = "Compiled from wire reports \u00b7 Thursday 26 November 2026"
    nw = d.textlength(note, font=f_note)
    d.text((R - nw, by + 5), note, font=f_note, fill=GREY)
    f_bf = font(F_SANS, 11)
    f_bn = font(F_BOLD, 11)
    cols = [BRIEFS[0:7], BRIEFS[7:14], BRIEFS[14:21]]
    yy0 = by + 27
    for ci, col in enumerate(cols):
        cx = M + ci * (colw + gapx)
        yy = yy0
        for j, b in enumerate(col):
            n = ci * 7 + j + 13
            d.text((cx, yy), str(n) + ".", font=f_bn, fill=CORAL_DK)
            for k, ln in enumerate(wrap(d, b, f_bf, colw - 24)[:2]):
                d.text((cx + 24, yy + k * 12), ln, font=f_bf, fill=(52, 66, 61))
            yy += 24

    # ---------------- footer ----------------
    f_src = font(F_SANS, 10.5)
    srw = d.textlength(SOURCES, font=f_src)
    d.text((M + (R - M - srw) / 2, 1004), SOURCES, font=f_src, fill=GREY)

    img.save(OUT, optimize=True)
    print("wrote", OUT, img.size)


if __name__ == "__main__":
    main()
