import pygame,sys,string,random
from pygame.locals import *

pygame.init()
res=(864,480)
s=pygame.display.set_mode(res)
pygame.display.set_caption('Make it Rain')
f=pygame.font.Font('matrix code nfi.otf',12)
fsize=f.size('f')
gridres=(int((res[0]-res[0]%fsize[0])/fsize[0]),int((res[1]-res[1]%fsize[1])/fsize[1]))
gridletter=[]
gridcolour=[]
columnstate=[]
columnspeed=[]
columntimer=[]

for x in range(0,gridres[0]):
	gridletter.append([])
	gridcolour.append([])
	columnstate.append(random.randint(0,7))
	columnspeed.append(random.randint(3,8))
	columntimer.append(0)
	for y in range(0,gridres[1]):
		gridletter[x].append(random.choice(string.ascii_lowercase+string.digits))
		gridcolour[x].append([0,0,0])
	
while True:
	for e in pygame.event.get():
		if e.type==QUIT:sys.exit()
		if e.type==KEYDOWN:
			k=e.key
			if k==K_ESCAPE:sys.exit()
	
	
	for n in range(0,300):gridletter[random.randint(0,gridres[0]-1)][random.randint(0,gridres[1]-1)]=(random.choice(string.ascii_lowercase+string.digits))
	for n in range(0,2):columnstate[random.randint(0,gridres[0]-1)]+=1
	
	for x in range(0,gridres[0]):
		if columntimer[x]==columnspeed[x]:
			columntimer[x]=0
			for y in range(gridres[1]-1,-1,-1):
				if y!=0:gridcolour[x][y]=gridcolour[x][y-1][:]
				elif columnstate[x]>=9:
					if gridcolour[x][y]==[0,0,0]:gridcolour[x][y]=[240,240,240]
					elif gridcolour[x][y][0]!=0:gridcolour[x][y][0]-=40;gridcolour[x][y][2]-=40
					elif columnstate[x]>=10:
						if gridcolour[x][y][1]>=235:gridcolour[x][y][1]-=20
						else:gridcolour[x][y][1]-=random.randint(-20,60)
						if gridcolour[x][y][1]<=0:
							gridcolour[x][y][1]=0
							columnstate[x]=-999
				elif columnstate[x]<0 and gridcolour[x][gridres[1]-1][1]==0:columnstate[x]=0;columnspeed[x]=random.randint(3,8)
		else:columntimer[x]+=1
		
	s.fill((0,0,0))
	
	for x,y in [(x,y) for x in range(0,gridres[0]) for y in range(0,gridres[1])]:
		s.blit(f.render(gridletter[x][y],1,gridcolour[x][y]),(x*fsize[0],y*fsize[1]))
		
	pygame.display.update()
	pygame.time.Clock().tick(80)