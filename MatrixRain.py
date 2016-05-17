import pygame
from pygame.locals import *
import sys
import string
import random

# Initialise screen
pygame.init()
res = (864, 480)
s = pygame.display.set_mode(res)
pygame.display.set_caption('Make it Rain')

# Create letter grid lists
f = pygame.font.Font('matrix code nfi.otf', 12)
fsize = f.size('f')
gridres = (
	int((res[0] - res[0]%fsize[0]) / fsize[0]),
	int((res[1] - res[1]%fsize[1]) / fsize[1])
	)
gridletter = []
gridcolour = []
columnstate = []
columnspeed = []
columntimer = []
letterlist = string.ascii_lowercase + string.digits

# Fill grid lists
for x in range(0, gridres[0]):
	gridletter.append([])
	gridcolour.append([])
	columnstate.append(random.randint(0, 7))
	columnspeed.append(random.randint(3, 8))
	columntimer.append(0)
	for y in range(0, gridres[1]):
		gridletter[x].append(random.choice(letterlist))
		gridcolour[x].append([0, 0, 0])

# Main loop		
while True:
	for e in pygame.event.get():
		if e.type == QUIT:
			sys.exit()
		if e.type == KEYDOWN:
			k = e.key
			if k == K_ESCAPE:
				sys.exit()
	
	# Randomly replace letters
	for n in range(0, 300):
		x = random.randint(0, gridres[0] - 1)
		y = random.randint(0, gridres[1] - 1)
		gridletter[x][y] = random.choice(letterlist)
	
	# Randomly increase columnstate
	for n in range(0, 2):
		columnstate[random.randint(0, gridres[0] - 1)] += 1
	
	# Rain logic
	for x in range(0, gridres[0]):
	
		# Vary speed of raindrops
		if columntimer[x] == columnspeed[x]:
			columntimer[x] = 0
			for y in range(gridres[1] - 1, -1, -1):
			
				# Move all colours down 1 letter
				if y != 0:
					gridcolour[x][y] = gridcolour[x][y-1][:]
					
				# Start raindrop
				elif columnstate[x] >= 9:
					
					# White tip
					if gridcolour[x][y] == [0, 0, 0]:
						gridcolour[x][y] = [240, 240, 240]
					
					# Fading white to green
					elif gridcolour[x][y][0] != 0:
						gridcolour[x][y][0] -= 40
						gridcolour[x][y][2] -= 40
						
					# Stop raindrop
					elif columnstate[x] >= 10:
					
						# Account for RGB value > 255
						if gridcolour[x][y][1] >= 235:
							gridcolour[x][y][1] -= 20
							
						# Fading green to black
						else:
							gridcolour[x][y][1] -= random.randint(-20, 60)
						
						# Account for RGB value < 0
						if gridcolour[x][y][1] <= 0:
							gridcolour[x][y][1] = 0
							columnstate[x] = -999
							
				# Reset for new raindrop
				elif (columnstate[x] < 0
						and gridcolour[x][gridres[1]-1][1] == 0):
					columnstate[x] = 0
					columnspeed[x] = random.randint(3, 8)
		
		else: columntimer[x] += 1
	
	# Erase old letters
	s.fill((0, 0, 0))
	
	# Blit new letters
	for x, y in [(x, y)	
			for x in range(0, gridres[0])
			for y in range(0, gridres[1])]:
		s.blit(f.render(gridletter[x][y], 1, gridcolour[x][y]),
			(x*fsize[0], y*fsize[1]))
		
	pygame.display.update()
	pygame.time.Clock().tick(80)