from Shapes import *
from colors import *
def earth():
	scale = 6  # Adjust this scale factor as needed

	draw_circle(372 * scale, 426 * scale, 202 * scale, 32 * scale, colors[4])
	draw_rectangle(180 * scale, 396 * scale, 58 * scale, 80 * scale, colors[3])
	draw_rectangle(474 * scale, 306 * scale, 58 * scale, 176 * scale, colors[3])
	draw_rectangle(300 * scale, 450 * scale, 16 * scale, 86 * scale, colors[3])
	draw_rectangle(312 * scale, 414 * scale, 70 * scale, 86 * scale, colors[3])
	draw_rectangle(426 * scale, 420 * scale, 70 * scale, 86 * scale, colors[3])
	draw_rectangle(420 * scale, 450 * scale, 70 * scale, 86 * scale, colors[3])
	draw_rectangle(420 * scale, 360 * scale, 70 * scale, 44 * scale, colors[3])
	draw_rectangle(396 * scale, 384 * scale, 70 * scale, 20 * scale, colors[3])
	draw_rectangle(390 * scale, 264 * scale, 70 * scale, 20 * scale, colors[3])
	draw_rectangle(426 * scale, 276 * scale, 70 * scale, 26 * scale, colors[3])
	draw_rectangle(204 * scale, 438 * scale, 70 * scale, 26 * scale, colors[3])
	draw_rectangle(192 * scale, 330 * scale, 40 * scale, 20 * scale, colors[3])
	draw_rectangle(216 * scale, 324 * scale, 40 * scale, 20 * scale, colors[3])
	draw_rectangle(234 * scale, 306 * scale, 40 * scale, 20 * scale, colors[3])
	draw_rectangle(210 * scale, 456 * scale, 40 * scale, 20 * scale, colors[3])
	draw_rectangle(216 * scale, 420 * scale, 40 * scale, 20 * scale, colors[3])
	draw_rectangle(420 * scale, 558 * scale, 46 * scale, 44 * scale, colors[3])
	draw_rectangle(444 * scale, 558 * scale, 46 * scale, 26 * scale, colors[3])
	draw_rectangle(384 * scale, 594 * scale, 46 * scale, 26 * scale, colors[3])
	draw_rectangle(396 * scale, 570 * scale, 46 * scale, 26 * scale, colors[3])
	draw_rectangle(378 * scale, 474 * scale, 46 * scale, 26 * scale, colors[3])
	draw_rectangle(378 * scale, 498 * scale, 46 * scale, 26 * scale, colors[3])
	draw_rectangle(396 * scale, 510 * scale, 46 * scale, 26 * scale, colors[3])
	draw_rectangle(480 * scale, 480 * scale, 46 * scale, 26 * scale, colors[3])
	draw_rectangle(408 * scale, 444 * scale, 46 * scale, 32 * scale, colors[3])
	draw_rectangle(276 * scale, 564 * scale, 46 * scale, 32 * scale, colors[3])
	draw_rectangle(240 * scale, 558 * scale, 46 * scale, 32 * scale, colors[3])
	draw_rectangle(210 * scale, 510 * scale, 46 * scale, 44 * scale, colors[3])
	draw_rectangle(276 * scale, 594 * scale, 46 * scale, 20 * scale, colors[3])
	draw_rectangle(270 * scale, 576 * scale, 46 * scale, 20 * scale, colors[3])
	draw_rectangle(228 * scale, 546 * scale, 52 * scale, 26 * scale, colors[3])
	draw_rectangle(204 * scale, 306 * scale, 52 * scale, 26 * scale, colors[3])
	draw_rectangle(216 * scale, 294 * scale, 52 * scale, 26 * scale, colors[3])
	draw_rectangle(228 * scale, 294 * scale, 52 * scale, 26 * scale, colors[3])
	draw_rectangle(228 * scale, 276 * scale, 52 * scale, 26 * scale, colors[3])
	draw_rectangle(252 * scale, 252 * scale, 52 * scale, 26 * scale, colors[3])
	draw_rectangle(252 * scale, 270 * scale, 52 * scale, 26 * scale, colors[3])
	draw_rectangle(246 * scale, 276 * scale, 52 * scale, 26 * scale, colors[3])
	draw_rectangle(246 * scale, 270 * scale, 52 * scale, 26 * scale, colors[3])
	draw_rectangle(510 * scale, 378 * scale, 52 * scale, 74 * scale, colors[3])
	draw_rectangle(450 * scale, 300 * scale, 52 * scale, 74 * scale, colors[3])
	draw_rectangle(444 * scale, 264 * scale, 52 * scale, 74 * scale, colors[3])
	draw_rectangle(414 * scale, 252 * scale, 52 * scale, 74 * scale, colors[3])
	draw_rectangle(498 * scale, 318 * scale, 52 * scale, 74 * scale, colors[3])
	draw_rectangle(474 * scale, 282 * scale, 52 * scale, 74 * scale, colors[3])


def starts(flag):
	i = 8 if flag else 9
	scale = 4 # Adjust this scale factor as needed

	triangle(114 * scale, 198 * scale, 16 * scale, 38 * scale, colors[i])
	triangle(192 * scale, 726 * scale, 16 * scale, 38 * scale, colors[i])
	triangle(1068 * scale, 948 * scale, 16 * scale, 38 * scale, colors[i])
	triangle(1068 * scale, 456 * scale, 16 * scale, 38 * scale, colors[i])
	triangle(828 * scale, 336 * scale, 16 * scale, 38 * scale, colors[i])
	triangle(690 * scale, 114 * scale, 16 * scale, 38 * scale, colors[i])
	triangle(402 * scale, 120 * scale, 16 * scale, 38 * scale, colors[i])
	triangle(402 * scale, 294 * scale, 16 * scale, 38 * scale, colors[i])
	triangle(330 * scale, 588 * scale, 16 * scale, 38 * scale, colors[i])
	triangle(330 * scale, 840 * scale, 16 * scale, 38 * scale, colors[i])
	triangle(126 * scale, 840 * scale, 16 * scale, 38 * scale, colors[i])
	triangle(126 * scale, 1068 * scale, 16 * scale, 38 * scale, colors[i])
	triangle(306 * scale, 1068 * scale, 16 * scale, 38 * scale, colors[i])
	triangle(306 * scale, 1068 * scale, -14 * scale, -4 * scale, colors[i])
	triangle(126 * scale, 1068 * scale, -14 * scale, -4 * scale, colors[i])
	triangle(126 * scale, 840 * scale, -14 * scale, -4 * scale, colors[i])
	triangle(330 * scale, 840 * scale, -14 * scale, -4 * scale, colors[i])
	triangle(1068 * scale, 948 * scale, -14 * scale, -4 * scale, colors[i])
	triangle(1068 * scale, 456 * scale, -14 * scale, -4 * scale, colors[i])
	triangle(828 * scale, 336 * scale, -14 * scale, -4 * scale, colors[i])
	triangle(402 * scale, 294 * scale, -14 * scale, -4 * scale, colors[i])
	triangle(330 * scale, 588 * scale, -14 * scale, -4 * scale, colors[i])
	triangle(192 * scale, 726 * scale, -14 * scale, -4 * scale, colors[i])
	triangle(114 * scale, 198 * scale, -14 * scale, -4 * scale, colors[i])
	triangle(402 * scale, 120 * scale, -14 * scale, -4 * scale, colors[i])
	triangle(690 * scale, 114 * scale, -14 * scale, -4 * scale, colors[i])
	triangle(822 * scale, 594 * scale, -14 * scale, -4 * scale, colors[i])
	triangle(960 * scale, 738 * scale, -14 * scale, -4 * scale, colors[i])
	triangle(1080 * scale, 630 * scale, -14 * scale, -4 * scale, colors[i])
	triangle(1080 * scale, 630 * scale, 16 * scale, -4 * scale, colors[i])
	triangle(822 * scale, 594 * scale, 16 * scale, -4 * scale, colors[i])
	triangle(960 * scale, 738 * scale, 16 * scale, -4 * scale, colors[i])
