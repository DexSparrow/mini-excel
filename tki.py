from kiz import*
from tkinter import*
from op import*
from random import  randrange
from math import*


# def vidiny(a,b = "vary",c = "akondro") :
# 	if  a:
# 		prix1=int(input("Otrinona ny vidiny "+a+"? : "));
# 	if  b:
# 		prix2=int(input("Otrinona ny vidiny "+b+"? : "));
# 	if  c:
# 		prix3=int(input("Otrinona ny vidiny "+c+"? : "));

# vidiny("akoho","Godrogodro")		



# fen1 = Tk()
# tex1 = Label(fen1,text = "Bonjour",fg = 'blue')  	# fen1 n pas obligatoire il a deja une valeur par defaut et les zutres aussi sint comma ca
# tex1.pack()	# c comme fill en js
# boul = Button(fen1,text = 'Appuyez ici',command = fen1.destroy,fg = 'red')
# boul.pack() # c comme fill en js
# fen1.mainloop()

# def saryLine() :

# 	global x1,x2,y1,y2

# 	ngeza.create_line(x1,y1,x2,y2,width = 2,fill = coul)

# 	y2,y1 = y2+ 10 , y1 - 10

# def setColo() :
# 	global coul
# 	loko = ['purple','cyan','maroon','green','red','blue','orange','yellow']
# 	s = randrange(8);
# 	coul = loko[s]

# x1, y1, x2, y2 = 10, 190, 190, 10
# # coordonnées de la ligne
# coul = 'dark green'

# fany = Tk()

# ngeza = Canvas(fany,bg = "green",height = 200 ,width = 200)
# ngeza.pack(side =LEFT)

# butt1 = Button(fany,text = "Quitter",command =fany.quit )		
# butt1.pack(side = BOTTOM)
# butt2 = Button(fany,text = "Tracer une ligne",command =saryLine)		
# butt2.pack()
# butt3 = Button(fany,text = "Couleur aleatoire",command =setColo)		
# butt3.pack()

# fany.mainloop()

# fany.destroy()


#-----x-----Canvas pour tracer des simples et lignes et aussi capable d effacer
#-----x-----Une ligne precedement creer


# canvbg = "green" #c pour effacer une ligne en y superposant la couleur;


# loko = "red"
# x1,y1,x2,y2 = 100,200,300,30

# def tracer():
# 	global x1,y1,x2,y2
# 	global sx1,sy1,sx2,sy2
# 	canvas.create_line(x1,y1,x2,y2,width = 2,fill = loko);
# 	sx1,sy1,sx2,sy2 = x1,y1,x2,y2
# 	x1,y1,x2,y2 = x2,y2,x1 - 5,y1 - 10



# def couleur () :
# 	global loko
# 	col = ['purple','cyan','maroon','turquoise','red','blue','orange','yellow']
# 	s = randrange(len(col))
# 	loko = col [s];

# def effacer():
# 	global x1,y1,x2,y2
# 	x1,y1,x2,y2 =sx1,sy1,sx2,sy2 
# 	canvas.create_line(sx1,sy1,sx2,sy2,width = 2,fill = canvbg)



# ctx = Tk()

# canvas = Canvas(ctx,width=300,height=300,bg=canvbg)
# canvas.pack(side = RIGHT)
# butt_dessiner = Button(ctx,text = "Tracer",command = tracer)
# butt_dessiner.pack(side = TOP)
# butt_color = Button(ctx,text = "Choisir une couleur",command = couleur)
# butt_color.pack()
# butt_effacer = Button(ctx,text = "Effacer",command = effacer)
# butt_effacer.pack()
# butt_stop = Button(ctx,text = "Quitter",command = ctx.quit)
# butt_stop.pack(side = BOTTOM)

# ctx.mainloop()
# ctx.destroy()


# ------x----Pour creer un simple visage------x-------
# def circo(f,d,rayon):
# 	canv.create_oval(f-rayon,d-rayon,f+rayon,d+rayon,outline = "red")
# 	#x,y-r,x+r,y
	
# def liny(l,s,c,k,wi = 2):
# 		canv.create_line(l,s,c,k,width  = wi)


# def transit(x,y) :
# 	global mx,my;
# 	mx = x;
# 	my = y;


# def cible() :
# 	i = 0
# 	r = 50
# 	while i <4:
# 		circo(mx,my,r)
# 		r += 50
# 		i += 1
# 	r = 50
# 	liny(mx- (r*i),my,mx+(r*i),my)
# 	liny(mx,my- (r*i),mx,my+(r*i))

# def centreOriginel() :
# 	global mx,my
# 	mx = smx
# 	my = smy

# def visage():
	
# 	ray = 100
# 	circo(mx,my,ray)
# 	transit(my - (3*ray/8),my - (3*ray/8))
# 	circo(mx,my,ray/5)
# 	centreOriginel()
# 	transit(my + (3*ray/8),my - (3*ray/8))
# 	circo(mx,my,ray/5)
# 	centreOriginel()

	



# cx = 500
# cy = 500
# smx = cx/2 #pour garder l origine principale puisque mx my seront modifier au cours du script
# smy = cy/2 #
# mx = cx/2
# my = cy/2
# cbg ='white'

# ctx = Tk()
# canv = Canvas(ctx,width = cx,height = cy,bg = cbg)
# canv.pack()
# butt0 = Button(text = "sortir",command =ctx.quit)
# butt0.pack(side = BOTTOM)
# butt1 = Button(text = "Appuyez",command = cible)
# butt1.pack()
# butt2 = Button(text = "Shema num 2",command = visage)
# butt2.pack()
# ctx.mainloop()
# ctx.destroy()
















#---------------------x-------------------------#
#un simple damier dynamique qui peut placer des points de maniere random#



# def recta(canb ,ivox,ivoy, lon,colo = "blue" ) :
# 	canb.create_rectangle(ivox ,ivoy,ivox + lon,ivoy + lon,fill = colo)

# def transla(xN,yN) :
# 	global mx,my
# 	mx = xN
# 	my = yN

# mx = 0
# my = 0
# smx = 0
# smy = 0

# def damier(wi =7,hei =7,coul1 = "white",coul2 = "black") :
# 	x =0
# 	i = 0
# 	f = 0
# 	y =0
# 	coul = [coul1,coul2]
# 	# ce trois la sont l eta au debut 
# 	infi = 0
# 	swit = 0
# 	temo = 0
# 	# le chiffre 0 veut dire que ca commence avec la couleur blanche

# 	while i < wi: #c la mX ca va cree un rectangle depuis x = 0 jsqua x = wi ;chaque x formera un rectangle depuis y = 0 jsqua y = hei
# 		while f < hei:#c la mY ,  ca va cree un rectangle depuis y = 0 jsqua y = hei
# 			transla(x,y)
# 			recta(mycanvas,mx,my,20,colo = coul[swit])
# 			y += 20
# 			f += 1
# 			infi += 1 #ici ca consiste juste a changer la couleur en un autre couleur que la precedente
# 			swit = infi%2

# 	#il determine la couleur qui va commencer la -x-file-x- qui n est que l inverse du -x-file-x- precedent
# 		if temo == 0:
# 			infi = 1
# 			swit = 1
# 			temo = 1	
# 		else :
# 			infi = 0
# 			swit = 0
# 			temo = 0	

# 		f = 0	
# 		x += 20
# 		y = smy	
# 		i = i + 1	
	


	

# canbg = "red"
# c = 0
# col1 = ""
# debu = 0 # c utile pour quitter la saisie du col1 et passer a la sisie du col 2
# col2 = ""
# wid = input("Entrez le sizeX de votre tableau :")
# heig = input("Entrez le sizeY de votre tableau :")
# # volo =input("Entrez la couleur de votre damier")
# # leng = len(volo)
# # while c < leng :
# # 	if volo[c] != "+" and debu == 0:
# # 		col1 += volo[c]
# # 		c += 1
# # 	else :
# # 		col2 += volo[c+1]
# # 		debu == 1
# # 		c += 1	

# def transir(xl,yl) :
# 	global mx,my
# 	mx ,my= xl,yl
# rayo = 7
# def placer() :
# 	tabo = randrange(wid)*20
# 	ry = randrange(heig)*20
# 	transir(tabo - rayo,ry -rayo)
# 	grat =  ["red","grey","green","blue","turquoise"]
# 	raz =randrange(len(grat))
# 	kolo =  grat[raz]
# 	mycanvas.create_oval(mx-rayo ,my-rayo,mx+rayo,my+rayo,outline = "white",fill = kolo)	
# print(col1," col2 =",col2)

# wid = int(wid)
# heig = int(heig)

# ctx = Tk()
# mycanvas = Canvas(ctx,width = wid*20,height = heig*20,bg = canbg)
# mycanvas.pack()
# damier(wi = wid,hei = heig,coul1 = "white",coul2 = "black")
# butt1 =Button(text = "Placer un point",command = placer)
# butt1.pack(side = LEFT)
# butt2 =Button(text = "Quitter?",command = ctx.quit)
# butt2.pack()
# ctx.mainloop()


#---------------------x-------------------------#


# Une simple calculatrice qui a l aide l interpreteur python peut interpreter un chaine de caractere automatique


# def evaluer(event):
# 	sortie.configure(text = "Valiny" + str(eval(inpu.get())))

# fenetre = Tk()

# inpu = Entry()
# inpu.bind("<Return>",evaluer) # c event touche entrer qui peut etre <Enter> aussi
# # bind veut dire en faite lier , en javascript c l equivalent de objet.addEvenListener("event",funcition(el))
# sortie = Label(fenetre)
# butt = Button(text = "Quitter",command = fenetre.quit)
# inpu.pack(side = RIGHT)
# sortie.pack()
# butt.pack(side = LEFT)

# fenetre.mainloop()
# fenetre.destroy()

# -------------x---------------------------#




# -------------x---------------------------#
# ---- decteur du positon du souris sur le frame-----#

# def positionCurseur(event):
# 		tele.configure(text = "X: "+str(event.x)+\
# 			" , Y :"+str(event.y))


# fenetre = Tk()
# info = Frame(fenetre,width = 300,height = 200,bg ="pink")
# info.bind("<Button-1>",positionCurseur)


# tele = Label()
# tele.pack()
# info.pack()

# fenetre.mainloop()

# -------------x---------------------------#







# -------------x---------------------------#
# creer un cercle la ou l user click

# def circlo(event) :
# 	fenetre.create_oval(event.x-10,event.y - 10,event.x+10,event.y + 10,fill = "black")

# ctx = Tk()

# fenetre = Canvas(width = 200,height = 300,bg = "red")
# fenetre.bind("<Button-1>",circlo)
# fenetre.pack()
# butt = Button(text  = 'Quitter',command = ctx.quit)
# butt.pack()
# ctx.mainloop()

# -------------x---------------------------#


# canbg = "red"
# c = 0
# wid = input("Entrez le sizeX de votre tableau :")
# heig = input("Entrez le sizeY de votre tableau :")
# def recta(canb ,ivox,ivoy, lon,colo = "blue" ) :
# 	canb.create_rectangle(ivox ,ivoy,ivox + lon,ivoy + lon,fill = colo)

# def transla(xN,yN) :
# 	global mx,my
# 	mx = xN
# 	my = yN

# mx = 0
# my = 0
# smx = 0
# smy = 0

# def damier(wi =7,hei =7,coul1 = "white",coul2 = "black") :
# 	x =0
# 	i = 0
# 	f = 0
# 	y =0
# 	coul = [coul1,coul2]

# 	infi = 0
# 	swit = 0
# 	temo = 0

# 	while i < wi: 
# 		while f < hei:
# 			transla(x,y)
# 			recta(mycanvas,mx,my,20,colo = coul[swit])
# 			y += 20
# 			f += 1
# 			infi += 1
# 			swit = infi%2

# 		if temo == 0:
# 			infi = 1
# 			swit = 1
# 			temo = 1	
# 		else :
# 			infi = 0
# 			swit = 0
# 			temo = 0	

# 		f = 0	
# 		x += 20
# 		y = smy	
# 		i = i + 1	
	

# rayo = 7
# def pointery(event):
# 		mycanvas.create_oval(event.x - rayo,event.y - rayo,event.x + rayo,event.y + rayo,fill = "red")

# def transir(xl,yl) :
# 	global mx,my
# 	mx ,my= xl,yl

# def placer() :
# 	tabo = randrange(wid)*20
# 	ry = randrange(heig)*20
# 	transir(tabo - rayo,ry -rayo)
# 	grat =  ["red","grey","green","blue","turquoise"]
# 	raz =randrange(len(grat))
# 	kolo =  grat[raz]
# 	mycanvas.create_oval(mx-rayo ,my-rayo,mx+rayo,my+rayo,outline = "white",fill = kolo)	

# wid = int(wid)
# heig = int(heig)

# ctx = Tk()
# mycanvas = Canvas(ctx,width = wid*20,height = heig*20,bg = canbg)
# mycanvas.bind("<Button-1>",pointery)
# mycanvas.pack()
# damier(wi = wid,hei = heig,coul1 = "white",coul2 = "black")
# butt1 =Button(text = "Placer un point",command = placer)
# butt1.pack(side = LEFT)
# butt2 =Button(text = "Quitter?",command = ctx.quit)
# butt2.pack()
# ctx.mainloop()

# -------------x---------------------------#






# -------------x---------------------------#


# ------- Damier avec placement ameliorer il y anu probleme de cartographie  ------- #

# def setColor(indexColor) :
# 	biblioDeCouleur = ["black","white"]
# 	loko = biblioDeCouleur[indexColor]
# 	return loko

# def recta(yourCanvas,theX,theY,surface = 20,loko = "white"):
# 	yourCanvas.create_rectangle(theX,theY,theX + surface,theY + surface,fill = loko)

# def bouger (x,y) :
# 	global mx,my
# 	mx = x
# 	my = y



# def damier(longueur = 10,hauteur = 10,mycanvas = ""):
# 	infini = 0
# 	temoin = 0
# 	indexColor = 0
# 	i = 0
# 	j =0
# 	x = 0
# 	y =0



# 	while i < longueur:
# 		while j < hauteur:
# 			j += 1
# 			monChoix=setColor(indexColor)
# 			bouger(x =x,y = y)
# 			recta(mycanvas,theX =mx,theY =my,surface = 20,loko = monChoix)
# 			infini += 1
# 			indexColor  = infini%2
# 			y += 20
			
			

# 		if temoin == 0 :
# 			indexColor = 1
# 			infini = 1
# 			temoin = 1
# 		else :
# 			indexColor = 0
# 			infini = 0
# 			temoin = 0

# 		j = 0	
# 		x += 20 
# 		y =0
# 		i += 1
# 		count =0		


# def placer(event):
# 	i = 0
# 	j = 0
# 	temo = 1
# 	while i < wi :
# 		if event.x >= wi*20  & event.x < (wi+1)*20 :
# 			while j < hei :
# 				if event.y >= hei*20  & event.y < (hei+1)*20 : 
# 					cible = 0
# 					print("Okay thats it")
# 					j += 1
# 				j += 1
# 			print("ca passe y")	
# 			j = 0	
# 			i += 1			

# 		else :
# 			print("ca passe else",i)
# 			j = 0
# 			i += 1
	

# wi = input("Entrez le sizeX :")
# hei = input("Entrez le sizeY :")
# wi = int(wi)
# hei = int(hei)
# ctx = Tk()

# mycanvas = Canvas(ctx,width = wi*20,height =hei*20,bg = "red")
# mycanvas.pack()
# damier(mycanvas = mycanvas,longueur = wi,hauteur = hei)
# mycanvas.bind("<Button-1>",placer)
# print("hello")
# ctx.mainloop()


# -------------x---------------------------#






# -------------x---------------------------#


 #---------- Utilisation de grid-------------

# ctx = Tk()
# txt1 = Label(text = "Nom")
# txt2 = Label(text = "Prenom")

# entree1 = Entry()
# entree2 = Entry()

# # txt1.grid(row = 0)  ca centre automatiquement le texte
# # txt2.grid(row = 1)

# txt1.grid(row = 0,sticky = E) # la place dependra de votre choix
# txt2.grid(row = 1,sticky = E)
# entree1.grid(row = 0,column = 1)
# entree2.grid(row = 1,column = 1)

# ctx.mainloop()

# -------------x---------------------------#









# -------------x---------------------------#

# Dessiner sur le canvas

# ctx = Tk()

# text0 = Label(text  = "Nom")
# text1 = Label(text  = "Prenom")
# text2 = Label(text  = "Numero")

# entree0 = Entry()
# entree1 = Entry()
# entree2 = Entry()

# mycanvas = Canvas(width = 200 ,height = 200,bg = "green")
# sary = PhotoImage(file = 'sam.png')# le canvas ne prend pas en charge les images jpeg
# mycanvas.create_image(100,400,image = sary)

# text0.grid(row = 0,sticky = E)
# text1.grid(row = 1,sticky = E)
# text2.grid(row = 2,sticky = E)

# entree0.grid(row = 0,column = 1)
# entree1.grid(row = 1,column = 1)
# entree2.grid(row = 2,column = 1)

# mycanvas.grid(row = 1,column = 2,rowspan = 2,padx = 10,pady = 5)

# ctx.mainloop()

#------------------x-------------------# 




#------------------x-------------------# 
 # Animation un peu naze mais bon

 # Cercle commande pa r des evenement

# def bouger(xN,yN) :
# 	global x1,y1
# 	x1,y1 = x1 + xN,y1 + yN

# 	mycanvas.coords(cercle,x1-ray,y1-ray,x1+ ray,y1 + ray)

# def haut() :
# 	bouger(0,-10)
# def gauche() :
# 	bouger(-10,0)
# def bas() :
# 	bouger(0,10)
# def droite() :
# 	bouger(10,0)


# x1 = 100
# y1 = 100
# ray = 20

# ctx = Tk()
# mycanvas = Canvas(width = 200,height = 200,bg = "white")
# cercle = mycanvas.create_oval(x1-ray,y1 - ray,x1+ ray,y1 + ray,fill = "red")

# mycanvas.grid(row = 0,rowspan = 5)

# Button(text = "Haut",command = haut).grid(row = 0,column = 1)
# Button(text = "gauche",command = gauche).grid(row = 1,column = 1)
# Button(text = "bas",command = bas).grid(row = 2,column = 1)
# Button(text = "droite",command = droite).grid(row = 3,column = 1)


# Button(text = "Quitter",command = ctx.quit).grid(row = 5,column = 1)

# ctx.mainloop()




#------------------x-------------------# 

 # Deplacement au point pointer par le curseur


# def bouger(xN,yN) :
# 	global x1,y1
# 	x1,y1 = x1 + xN,y1 + yN

# 	mycanvas.coords(cercle,x1-ray,y1-ray,x1+ ray,y1 + ray)

# def deplacer(event) : # on peut âs faire xxx = event
# 	xN = event.x - x1  #distance
# 	yN = event.y -y1
# 	bouger(xN,yN)

# x1 = 100
# y1 = 100
# ray = 20

# ctx = Tk()
# mycanvas = Canvas(width = 200,height = 200,bg = "white")
# cercle = mycanvas.create_oval(x1-ray,y1 - ray,x1+ ray,y1 + ray,fill = "red")
# mycanvas.bind("<Button-1>",deplacer)
# mycanvas.grid(row = 0,rowspan = 5)

# Button(text = "Quitter",command = ctx.quit).grid(row = 0,column = 1)

# ctx.mainloop()


#------------------x-------------------# 





#------------------x-------------------# 



# deux astre qu on peut controler le deplacement par le clic du souris
# la commande s alterne entre controler l astre1 et l astre2

# def bouger(xN,yN,preuve) :
# 	global x1,y1,x2,y2
# 	if preuve == 0 :
# 		x1,y1 = x1 + xN,y1 + yN
# 		mycanvas.coords(astre1,x1-ray,y1-ray,x1+ ray,y1 + ray)
# 	else :	
# 		x2,y2 = x2 + xN,y2 + yN
# 		mycanvas.coords(astre2,x2-ray,y2-ray,x2+ ray,y2 + ray)

	

# def deplacerAstre1(event) : 
# 	xN = event.x - x1  
# 	yN = event.y -y1
# 	bouger(xN,yN,preuve = 0)
# 	text.configure(text =  "distX = " + str(sqrt( ((x2 - x1)**2) + ((y2 - y1)**2))))

# def deplacerAstre2(event) : 
# 	xN = event.x - x2  
# 	yN = event.y -y2
# 	bouger(xN,yN,preuve = 1)
# 	text.configure(text =  "distX = " + str(sqrt( ((x2 - x1)**2) + ((y2 - y1)**2))))

# def changeToAstre1() :
# 	mycanvas.bind("<Button-1>",deplacerAstre1)

# def changeToAstre2() :
# 	mycanvas.bind("<Button-1>",deplacerAstre2)

# x1 = 100
# y1 = 100

# x2 = 200
# y2 = 100


# ray = 20

# temo = 0

# ctx = Tk()
# mycanvas = Canvas(width = 200,height = 200,bg = "white")
# astre1 = mycanvas.create_oval(x1-ray,y1 - ray,x1+ ray,y1 + ray,fill = "red")
# astre2 = mycanvas.create_oval(x2-ray,y2 - ray,x2+ ray,y2 + ray,fill = "green")
	
# text = Label(text = "distX = " + str(sqrt( ((x2 - x1)**2) + ((y2 - y1)**2))))

# mycanvas.grid(row = 0,rowspan = 5)
# mycanvas.bind("<Button-1>",deplacerAstre1)

# text.grid(row = 6,column = 0)

# Button(text = "Astre1",command = changeToAstre1).grid(row = 0,column = 1)
# Button(text = "Astre2",command = changeToAstre2).grid(row = 1,column = 1)
# Button(text = "Quitter",command = ctx.quit).grid(row = 6,column = 1)

# ctx.mainloop()

#------------------x-------------------# 







#------------------x-------------------#

#Deux astre avec leur charge intercheangeable(+ et -)
# ll		pole = "positif"
# 	else :
# 		polaz11 =mycanvas.create_line(x1 ,y1- nineTY ,x1  ,y1+nineTY,width = 2,fill = canvBg)
# 		# on efface le polaz1 et polaz11 pour en creer une nouveau
# 		polaz1 =mycanvas.create_line(x1 - nineTY,y1 ,x1 +nineTY ,y1,width = 2,fill = canvBg)

# 		#on redefinit le polaz1 et le polaz11 qui peut etre traiter par bouger()

# 		polaz11 =mycanvas.create_line(x1 ,y1- nineTY ,x1  ,y1+nineTY,width = 2,fill = bg1)
# 		polaz1 =mycanvas.create_line(x1 - nineTY,y1 ,x1 +nineTY ,y1,width = 2,fill = colory)
# 		pole = "negatif"	
		
	
# def changePola2(colory = "black") :
# 	global pole,polaz2,polaz22
# 	if pole == "negatif":
# 		polaz2 =mycanvas.create_line(x2 - nineTY,y2 ,x2 +nineTY ,y2,width = 2,fill = canvBg)
# 		# on efface le polaz2 et polaz22 pour en creer une nouveau
# 		polaz22 = mycanvas.create_line(x2 ,y2- nineTY ,x2  ,y2+nineTY,width = 2,fill = canvBg)

# 		#on redefinit le polaz2 et le polaz22 qui peut etre traiter par bouger()

# 		polaz2 =mycanvas.create_line(x2 - nineTY,y2 ,x2 +nineTY ,y2,width = 2,fill = colory)
# 		polaz22 = mycanvas.create_line(x2 ,y2- nineTY ,x2  ,y2+nineTY,width = 2,fill = colory)
# 		pole = "positif"
# 	else :
# 		polaz22 = mycanvas.create_line(x2 ,y2- nineTY ,x2  ,y2+nineTY,width = 2,fill = canvBg)
# 		# on efface le polaz2 et polaz22 pour en creer une nouveau
# 		polaz2 = mycanvas.create_line(x2 - nineTY,y2 ,x2 +nineTY ,y2,width = 2,fill = canvBg)

# 		#on redefinit le polaz2 et le polaz22 qui peut etre traiter par bouger()
		
# 		polaz22 = mycanvas.create_line(x2 ,y2- nineTY ,x2  ,y2+nineTY,width = 2,fill = bg2)
# 		polaz2 = mycanvas.create_line(x2 - nineTY,y2 ,x2 +nineTY ,y2,width = 2,fill = colory)
# 		pole = "negatif"

# def deplacerAstre1(event) : 
# 	xN = event.x - x1  
# 	yN = event.y -y1
# 	bouger(xN,yN,preuve = 0)
# 	text.configure(text =  "distX = " + str(sqrt( ((x2 - x1)**2) + ((y2 - y1)**2))))

# def deplacerAstre2(event) : 
# 	xN = event.x - x2  
# 	yN = event.y -y2
# 	bouger(xN,yN,preuve = 1)
# 	text.configure(text =  "distX = " + str(sqrt( ((x2 - x1)**2) + ((y2 - y1)**2))))

# def changeToAstre1() :
# 	mycanvas.bind("<Button-1>",deplacerAstre1)

# def changeToAstre2() :
# 	mycanvas.bind("<Button-1>",deplacerAstre2)

# x1 = 100
# y1 = 100

# x2 = 200
# y2 = 100


# ray = 20

# temo = 0
# pole = "negatif"
# nineTY = ((ray*5)/10) # 50% du rayon

# bg1 = "red"
# bg2 = "green"

# canvBg = "white"

# ctx = Tk()
# mycanvas = Canvas(width = 500,height = 500,bg = canvBg)
# astre1 = mycanvas.create_oval(x1-ray,y1 - ray,x1+ ray,y1 + ray,fill = bg1)
# astre2 = mycanvas.create_oval(x2-ray,y2 - ray,x2+ ray,y2 + ray,fill = bg2)
	
# polaz1 =mycanvas.create_line(x1 - nineTY,y1 ,x1 +nineTY ,y1,width = 2,fill = "black")
# polaz11 =mycanvas.create_line(x1 ,y1 - nineTY,x1 ,y1+nineTY ,width = 2,fill = bg1)
# polaz2 =mycanvas.create_line(x2 - nineTY,y2 ,x2+nineTY ,y2,width = 2,fill = "black")
# polaz22 =mycanvas.create_line(x2 ,y2 - nineTY,x2 ,y2+nineTY ,width = 2,fill = "black")

# text = Label(text = "distX = " + str(sqrt( ((x2 - x1)**2) + ((y2 - y1)**2))))

# mycanvas.grid(row = 0,rowspan = 5)
# mycanvas.bind("<Button-1>",deplacerAstre1)

# text.grid(row = 6,column = 0)

# Button(text = "Astre1",command = changeToAstre1).grid(row = 0,column = 1)
# Button(text = "ChangerPole1",command = changePola1).grid(row = 1,column = 1)
# Button(text = "Astre2",command = changeToAstre2).grid(row = 2,column = 1)
# Button(text = "ChangerPole2",command = changePola2).grid(row = 3,column = 1)
# Button(text = "Quitter",command = ctx.quit).grid(row = 6,column = 1)

# ctx.mainloop()




#------------------x-------------------#

#Ca marche pas encore je m rappele du methode utilise par canvas#


# i = 0
# count = 0
# def bouger(distX = 0,distY = 0) :
# 	global x1,y1,i,count

# 	if count < 2 :
# 		count += 1
# 		bouger(i,0)
# 		return

# 	else :
# 		x1,y1 = x1 + distX, y1 + distY
# 		mycanvas.coords(ball,x1 - ray, y1 -ray ,x1 + ray, y1 + ray)
# 		i += 0.5
# 		count = 0
# 		if i == 10:
# 			pass
# 		else :	
# 			bouger(i,0)




# x1 = 50
# y1 = 50
# ballBg = "red"
# ray = 30


# ctx = Tk()

# mycanvas = Canvas(width = 200,height = 200,bg = "white")
# mycanvas.grid(row = 0,rowspan = 6)
# ball = mycanvas.create_oval(x1 - ray, y1 -ray ,x1 + ray, y1 + ray,fill = ballBg)

# butt = Button(text = "Bouger",command = bouger)
# butt99 = Button(text = "Quittez", command = ctx.quit)

# butt.grid(row = 0,column = 1)
# butt99.grid(row = 5,column = 1)

# ctx.mainloop()

#------------------x-------------------#







#------------------x-------------------#
#------------------x-------------------#
#------------------x-------------------#
#------------------x-------------------#

# Ceci est une copie colle de lecon #

# def move():
# 	"déplacement de la balle"
# 	global x1, y1, dx, dy, flag
# 	x1, y1 = x1 +dx, y1 + dy
# 	if x1 >210:
# 		x1, dx, dy = 210, 0, 15
# 	if y1 >210:
# 		y1, dx, dy = 210, -15, 0
# 	if x1 <10:
# 		x1, dx, dy = 10, 0, -15
# 	if y1 <10:
# 		y1, dx, dy = 10, 15, 0
# 	can1.coords(oval1,x1,y1,x1+30,y1+30)
# 	if flag >0:
# 		fen1.after(50,move) # ce comme setInerval en js canvas
# 	# => boucler après 50 millisecondes
# def stop_it():
# 	"arrêt de l'animation"
# 	global flag
# 	flag =0
# def start_it():
# 	"démarrage de l'animation"
# 	global flag
# 	if flag ==0:# ca empeche l acceleration du balle car si on retirait cette condition la fonction move va s incrementer 
# 	# pour ne lancer qu’une seule boucle
# 		flag =1 #ce ligne la est tres necessaire pour une animation continue et fluide
# 		move()
# #========== Programme principal =============
# # les variables suivantes seront utilisées de manière globale :
# x1, y1 = 10, 10
# # coordonnées initiales
# dx, dy = 15, 0
# # 'pas' du déplacement
# flag =0
# # commutateur
# # Création du widget principal ("parent") :
# fen1 = Tk()
# fen1.title("Exercice d'animation avec Tkinter")
# # création des widgets "enfants" :
# can1 = Canvas(fen1,bg='dark grey',height=250, width=250)
# can1.pack(side=LEFT, padx =5, pady =5)
# oval1 = can1.create_oval(x1, y1, x1+30, y1+30, width=2, fill='red')
# bou1 = Button(fen1,text='Quitter', width =8, command=fen1.quit)
# bou1.pack(side=BOTTOM)
# bou2 = Button(fen1, text='Démarrer', width =8, command=start_it)
# bou2.pack()
# bou3 = Button(fen1, text='Arrêter', width =8, command=stop_it)
# bou3.pack()
# # démarrage du réceptionnaire d'événements (boucle principale) :
# fen1.mainloop()


#------------------x-------------------#
#------------------x-------------------#
#------------------x-------------------#
#-------------------x-------------------------#




# L angle est exprime en radian

# pi = math.pi
def bouge():
	global angle,xi,yi,x1,y1,xi1,yi1,xi2,yi2,x2,y2,x3,y3

	angle = angle + pi/200
	xi = (sin(angle))*rayC
	yi = (cos(angle))*rayC

	xi1 = (sin(angle))*rayC1
	yi1 = (cos(angle))*rayC1



	xi2 = (sin(angle))*rayC2
	yi2 = (cos(angle))*rayC2


	x1 = cx + yi
	y1 = cy - xi

	x2 = cx + yi1
	y2 = cy - xi1

	x3 = cx + yi2
	y3 = cy - xi2

	mycanvas.coords(balle,x1 - ray,y1 - ray , x1 + ray ,y1 + ray)
	mycanvas.coords(balle1,x2 - ray,y2 - ray , x2 + ray ,y2 + ray )
	mycanvas.coords(balle2,x3 - ray,y3 - ray , x3 + ray ,y3 + ray )

	if aona == 1 :
		mycanvas.after(10,go)
	else :
		pass

def go() :
	global aona
	aona = 1
	bouge()

def stop():
	global aona
	aona = 0
	print("stop")


pi = 3.1415926543141592654314159265431415926543
canBg = "white"
ballBg = "red"
canvWi = 1000
canvHei = 1000
rayC = 150
rayC1= 300
rayC2= 400

cx = canvWi/2 
cy = canvHei/2 

# Ball
angle = pi/3
xi = (sin(angle))*rayC
yi = (cos(angle))*rayC

xi1 = (sin(angle))*rayC1
yi1 = (cos(angle))*rayC1



xi2 = (sin(angle))*rayC2
yi2 = (cos(angle))*rayC2

x1 = cx + yi
y1 = cy - xi

x2 = cx + yi1
y2 = cy - xi1

x3 = cx + yi2
y3 = cy - xi2

aona = 1

ctx = Tk()

ray = 30
ray1 = 100
rayx = 2

mycanvas = Canvas(width = canvWi , height = canvHei, bg = canBg)


centre = mycanvas.create_oval(cx - rayx,cy - rayx , cx + rayx ,cy + rayx ,fill = ballBg)
balle = mycanvas.create_oval(x1 - ray,y1 - ray , x1 + ray ,y1 + ray ,fill = ballBg)
balle1 = mycanvas.create_oval(x2 - ray,y2 - ray , x2 + ray ,y2 + ray ,fill = ballBg)
balle2 = mycanvas.create_oval(x3 - ray,y3 - ray , x3 + ray ,y3 + ray ,fill = ballBg)

mycanvas.grid(row = 0,rowspan = 20)

butt1 = Button(text = "Alefa" ,command = go).grid(row = 0,column = 1)
butt2 = Button(text = "Mijanona",command = stop).grid(row = 1,column = 1)
butt2 = Button(text = "Quitter",command = ctx.quit).grid(row = 5,column = 1)


ctx.mainloop()


