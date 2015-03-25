#!usr/bin/python
# -*-coding:Latin-1 -*
import os

continuer = True

while continuer:

	print("	----------------------------------------------------------")
	print("	Calcul du Risque Relatif et Odds Ratios Etude CASE/CONTROL")
	print("	----------------------------------------------------------")

	variable = input ("Saisissez le nom de votre variable: ")

#ce logiciel permet de determiner les odds ratios, risque relatifs, yule coefficient
#et khi2 avec leur interpretation dans une etude cas temoin

#entree des effectifs par groupes et declaration des variables en float
	CasePos = input ("Saisissez le nombre de cas positifs: ")
	try:
		CasePos = float (CasePos)
	except ValueError:
		print('	Veuillez taper un nombre entier!')
		continue
	
	CaseNeg = input ("Saisissez le nombre de cas negatifs: ")  
	try:
		CaseNeg = float (CaseNeg)
	except ValueError:
		print('	Veuillez taper un nombre entier!')
		continue
	
	ControlPos = input ("Saisissez le nombre de temoins positifs: ")
	try:
		ControlPos = float (ControlPos)
	except ValueError:
		print(' Veuillez taper un nombre entier!')
		continue 
	
	ControlNeg = input ("Saisissez le nombre de temoins negatifs: ")
	try:
		ControlNeg = float (ControlNeg)
	except ValueError:
		print('	Veuillez taper un nombre entier!')
		continue


#calcul des variables intermediaires
	TotalCase = CasePos + CaseNeg
	print('Le nombre total de cas est = ', TotalCase)

	TotalControl = ControlPos + ControlNeg
	print('Le nombre total de temoins est = ', TotalControl)

	TotalPos = CasePos + ControlPos
	print('Le nombre total individus Positifs = ', TotalPos)

	TotalNeg = CaseNeg + ControlNeg
	print('Le nombre total individus Negatifs = ', TotalNeg)

#determination du risque relatif
	RR = (CasePos/TotalPos) / (CaseNeg/TotalNeg)
	print('Le risque relatif Case/Control est de : ', RR)

	if ControlPos !=0:
#determination du odds ratio
		OR = (CasePos/ControlPos) / (CaseNeg/ControlNeg)
		print('Odds Ratio Case/control est de : ', OR)

#intermediaire de calcul
	total = CasePos+CaseNeg+ControlPos+ControlNeg

#frequence de la maladie
	prevalence = (CasePos+CaseNeg)/total
	print('la frequence de la maladie est: ',prevalence)

#pourcentage de positivite dans le groupe case
	freqPosCase = (CasePos / (CasePos + CaseNeg)) * 100
	print('le pourcentage de positivite dans le groupe case est: ',freqPosCase, 'pourcents')

#pourcentage de positivite dans le groupe control
	freqPosControl = (ControlPos / (ControlPos + ControlNeg)) * 100
	print('le pourcentage de positivite dans le groupe controle est: ',freqPosControl, 'pourcents')


#determination du coefficient de Yule
	Yule = ((CasePos*ControlNeg)-(ControlPos*CaseNeg))/((CasePos*ControlNeg)+(ControlPos*CaseNeg))
	print('coefficient Q de Yule : ', Yule)

#boucle interpretation du coefficient de Yule
	if Yule < 0.01 and Yule > -0.01:
		print("----------intensite de liaison nulle")
	elif Yule >=0.01  and Yule <0.09:
		print("----------intensite de liaison positive negligeable")
	elif Yule >=0.1 and Yule <0.29:
		print("----------intensite de liaison positive legere")
	elif Yule >=0.3 and Yule <0.49:
		print("----------intensite de liaison positive moderee")
	elif Yule >=0.5 and Yule <0.69:
		print("----------intensite de liaison positive forte")
	elif Yule >=0.7 :
		print("----------intensite de liaison positive tres forte")  
	elif Yule >= -0.09 and Yule < -0.01:
		print("----------intensite de liaison negative negligeable")
	elif Yule >= -0.29 and Yule < -0.1:
		print("----------intensite de liaison negative legere")
	elif Yule >= -0.49 and Yule < -0.3:
		print("----------intensite de liaison negative moderee")
	elif Yule >= -0.69 and Yule < -0.5:
		print("----------intensite de liaison negative forte")
	elif Yule < -0.7:
		print("----------intensite de liaison negative tres forte") 




#determination du test de khi2
	cross = (CasePos*ControlNeg)-(ControlPos*CaseNeg)
	khi=((cross*cross)*total)/((CasePos+ControlPos)*(CaseNeg+ControlNeg)*(CasePos+CaseNeg)*(ControlPos+ControlNeg))
	print("le Khi2 est de : ", khi)

#interpretation du test de khi2
	if khi >3.841:
		print("----------le test Khi2 est SIGNIFICATIF p<0.05 !")
	else:
		print("----------le test khi2 est NON significatif !")

#interaction pour enregistrement dans fichier de sortie	

	add =  input('Souhaitez vous ajouter les donnees dans le fichier CASE_CONTROL_RESULTS (o/n)? ')
	if add == "o" or add == "O":
		
#fichier de sortie
		variable = str (variable)
		CasePos = str (CasePos)
		CaseNeg = str (CaseNeg)
		ControlPos = str (ControlPos)
		ControlNeg = str (ControlNeg)
		freqPosCase = str (freqPosCase)
		freqPosControl = str (freqPosControl)
		RR = str (RR)
		OR = str (OR)
		Yule = str (Yule)
		khi = str (khi)
	
		mon_fichier = open ("CASE_CONTROL_RESULTS.txt", "a")
		mon_fichier.write ("---------------------------------------------------------------------")
		mon_fichier.write ("\n")
		mon_fichier.write ("Etude CASE/CONTROL sur la variable: "+ variable + "\n")
		mon_fichier.write ("nombre de case positifs : "+ CasePos + "\n")
		mon_fichier.write ("nombre de case negatifs : "+ CaseNeg + "\n")
		mon_fichier.write ("nombre de control positifs : "+ ControlPos + "\n")
		mon_fichier.write ("nombre de control negatifs : "+ ControlNeg + "\n")
		mon_fichier.write ("pourcentage de positivite dans le groupe Case: " + freqPosCase + "\n")
		mon_fichier.write ("pourcentage de positivite dans le groupe Control: " + freqPosControl + "\n")
		mon_fichier.write ("Risque Relatif CASE/CONTROL: "+ RR + "\n")
		mon_fichier.write ("Odds Ratios CASE/CONTROL: "+ OR + "\n")
		mon_fichier.write ("Coefficient Q de Yule: " + Yule + "\n")
		mon_fichier.write ("Constante du Khi2 --> significatif > 3.841: " + khi + "\n")
	
		mon_fichier.close()
		


#interaction pour sortie du logiciel	

	quitter =  input('Souhaitez vous quitter le logiciel (o/n)? ')
	if quitter == "o" or quitter == "O":
		continuer = False
os.system("pause")
