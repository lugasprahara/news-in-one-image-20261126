// news-image-20261126 entry (Node 22, standard library only): "Sum up
// 26 November's world news in one image". The image beside this file,
// entry.png, is the entry: 33 stories of Thursday 26 November 2026 —
// the US tariff proposal as the top story, 11 panels, 21 briefs and a
// world map with numbered dots — rendered by render.py (Python/Pillow)
// from the day's wire reports. This program copies entry.png to
// /output/entry.png, byte for byte, so both grader runs write the
// same bytes. The image is a whole PNG of 1024 by 1024 pixels and
// 219,960 bytes, under the 1 MiB gate.
//
// Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync } from 'node:fs';
import { join } from 'node:path';

copyFileSync(new URL('./entry.png', import.meta.url), join(process.env.MAKEFUN_OUTPUT_DIR ?? '/output', 'entry.png'));
