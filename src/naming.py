""""This file is part of PLADIF.

	MIT License

	Copyright (c) 2022 - Thibault Hilaire

	Permission is hereby granted, free of charge, to any person obtaining a copy
	of this software and associated documentation files (the "Software"), to deal
	in the Software without restriction, including without limitation the rights
	to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
	copies of the Software, and to permit persons to whom the Software is
	furnished to do so, subject to the following conditions:

	The above copyright notice and this permission notice shall be included in all
	copies or substantial portions of the Software.

	THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
	IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
	FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
	AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
	LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
	OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
	SOFTWARE.


PLADIF is a simple tool that plots attrakdiff graphs from CSV files (like those from Usabilla).
It is written by Thibault Hilaire

File: naming.py
Date: Feb 2022

	some constants and naming
"""

from collections import OrderedDict

#TODO: add english (and german) translation



titles = {
	"QP": "Qualité pragmatique",
	"QHS": "Qualité hédonique - stimulation",
	"QHI": "Qualité hédonique - identification",
	"ATT": "Attrativité globale"
}
# pairs of word, ordered in the order we want them on the graph (QP, QHS, QHI and APP)
pairs = OrderedDict(
	QP1=("Technique", "Humain"),
	QP2=("Compliqué", "Simple"),
	QP3=("Pas pratique", "Pratique"),
	QP4=("Fastidieux", "Efficace"),
	QP5=("Imprévisible", "Prévisible"),
	QP6=("Confus", "Clair"),
	QP7=("Incontrôlable", "Maîtrisable"),

	QHS1=("Conventionnel", "Original"),
	QHS2=("Sans imagination", "Créatif"),
	QHS3=("Prudent", "Audacieux"),
	QHS4=("Conservateur", "Novateur"),
	QHS5=("Ennuyeux", "Captivant"),
	QHS6=("Peu exigeant", "Challenging"),
	QHS7=("Commun", "Nouveau"),

	QHI1=("M’isole", "Me sociabilise"),
	QHI2=("Amateur", "Professionnel"),
	QHI3=("De mauvais goût", "De bon goût"),
	QHI4=("Bas de gamme", "Haut de gamme"),
	QHI5=("M’exclut", "M’intègre"),
	QHI6=("Me sépare des autres", "Me rapproche des autres"),
	QHI7=("Non présentable", "Présentable"),

	ATT1=("Déplaisant", "Plaisant"),
	ATT2=("Laid", "Beau"),
	ATT3=("Désagréable", "Agréable"),
	ATT4=("Rebutant", "Attirant"),
	ATT5=("Mauvais", "Bon"),
	ATT6=("Repoussant", "Attrayant"),
	ATT7=("Décourageant", "Motivant")
)

order_short = ["QP2*", 'ATT2', 'QP3*', 'QHI3*', 'QP5*', "QHI4", "QHS2", "ATT5*", "QP6", "QHS5"]
order_long = [
	"QP1*", "QHI1", "ATT1*", "QHS1*", "QP2*", "QHI2*", "ATT2", "QP3", "ATT3*, QP4",
	"QHI3*", "QP5*", "QHI4", "QHI5", "QHI6*", "QHI7", "ATT4", "QHS2", "ATT5*",
	'QP6', "ATT6", "QHS3*", "QHS4*", "QHS5", "QHS6", "ATT7*", "QHS7*", "QP7"
]