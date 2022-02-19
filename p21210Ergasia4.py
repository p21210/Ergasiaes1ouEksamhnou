#edw  einai ta plhthh
count_win=0
count_lose=0
count_draw=0

#me auto to for ginetai h epanaluptikh diadikasia
for i in range(1,101):
	import random
	#edw ftiaxnei thn trapoula
	ARITHMOI=[i for i in range(1,11)]
	XRWMA=["C♣","S♠","H♥","D♦"]
	FIGOURES=["J","Q","K"]
	XARTIA=ARITHMOI+FIGOURES
	#edw exei tis dikes mou kartes
	DEKA=[10]
	MY_XARTIA=DEKA+FIGOURES
	#edw exei tou deuterou paikth tis kartes
	COMP_XARTIA=[i for i in range(1,10)]

	#me auto,upothetw,anakateuei olh thn kanonikh trapoula
	DECK=[]
	for i in XRWMA:
		for j in XARTIA:
			DECK.append([i,j])
	random.shuffle(DECK)

	#edw ginetai to anakatema gia ths dikes mou kartes
	MY_DECK=[]
	for i in XRWMA:
		for j in MY_XARTIA:
			MY_DECK.append([i,j])
	random.shuffle(MY_DECK)

	#edw ginetai to anakatema gia tou antipalou ths kartes
	COMP_DECK=[]
	for i in XRWMA:
		for j in COMP_XARTIA:
			COMP_DECK.append([i,j])
	random.shuffle(COMP_DECK)

	#edw briskei thn aksia ths kathe kartas
	def get_card_value(c):
		if c[1] in FIGOURES:
			return 10
		else:
			return c[1]

	#edw bgazei to score to kathe paikth		
	def sum_cards(LST):
		score=0
		for c in LST:
			score+=get_card_value(c)
		return score

	#moirase xartia
	comp_cards=[COMP_DECK[1],DECK[1],DECK[2]]
	my_cards=[MY_DECK[1],DECK[3]]

	#shmeivwsh: ebala mesa se parentheseis ta viriables giati mou ebgaze error
	comp_score=sum_cards(comp_cards)
	print (comp_cards,comp_score)
	my_score=sum_cards(my_cards) 
	print (my_cards,my_score)

	#shmeiwsh: ebala to keimeno mesa se parenthesesh giati mou ebgaze error
	if my_score>comp_score:
		print ("kerdises!")
		count_win=count_win+1
	elif comp_score>my_score:
		print ("exases")
		count_lose=count_lose+1
	else:
		print ("isopalia")
		count_draw=count_draw=count_draw+1
print ("kerdises: ",count_win)
print ("exases: ",count_lose)
print ("hrthes isopalia: ",count_draw)