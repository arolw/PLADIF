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

# create dummy _ fct (so that gettext can parse dict)

# language options
langOption = OrderedDict(en="English", fr="Français", de="Deutsch")

# summary
summary_info = {'en': ['filename', '# users', 'file size'], 'fr': ['nom de fichier', 'nb utilisateurs', 'taille du fichier'], 'de': ['dateiname', '# nutzer', 'dateigröße']}
summary_title = {'en': "Summary", 'fr': "Résumé", 'de': 'Zusammenfassung'}


# short or long attrakdiff
order_short = ["QP2*", 'ATT2', 'QP3*', 'QHI3*', 'QP5*', "QHI4", "QHS2", "ATT5*", "QP6", "QHS5"]
order_long = [
	"QP1*", "QHI1", "ATT1*", "QHS1*", "QP2*", "QHI2*", "ATT2", "QP3", "ATT3*", "QP4",
	"QHI3*", "QP5*", "QHI4", "QHI5", "QHI6*", "QHI7", "ATT4", "QHS2", "ATT5*",
	'QP6', "ATT6", "QHS3*", "QHS4*", "QHS5", "QHS6", "ATT7*", "QHS7*", "QP7"
]

# few words translated
i18n_average = {'en': "Average value", 'fr': "Valeur moyenne", 'de': "Mittelwert"}
i18n_dim = {'en': "Dimension", 'fr': "Dimension", 'de': "Dimension"}
plt_avrg = {'en': "Diagram of average values", 'fr': "Graphique des valeurs moyennes", 'de': "Diagramm der Mittelwerte"}
plt_pair = {'en': "Description of Word-pairs", 'fr': "Graphique des paires de mots", 'de': "Beschreibung der Wortpaare"}
plt_attr = {'en': "Portfolio-presentation", 'fr': "Portfolio des résultats", 'de': "Portfoliopräsentation"}

# categories title
categories = ["QP", "QHS", "QHI", "ATT"]
titles = {
	"QP": {'en': "Pragmatic Quality", 'fr': "Qualité Pragmatique", 'de': "Pragmatische Qualität"},
	"QHS": {'en': "Hedonic Quality - Stimulation", 'fr': "Qualité hédonique - stimulation", 'de': "Hedonische Qualität - Stimulation"},
	"QHI": {'en': "Hedonic Quality - Identify", 'fr': "Qualité hédonique - identification", 'de': "Hedonische Qualität - Identität"},
	"QH": {'en': "Hedonic Quality", 'fr': "Qualité hédonique", 'de': "Hedonische Qualität"},
	"ATT": {'en': "Attrativeness", 'fr': "Attractivité", 'de': "Attraktivität"}
}

# attrakdiff cases
QPQH = {
	(-2, 2): {'en': "too\nself-\noriented", 'fr': "trop\norienté\nvers le soi", 'de': "zu\selbst-\orientiert"},
	(0, 2): {'en': "self-\noriented", 'fr': "orienté\nvers le soi", 'de': "selbst-\orientiert"},
	(2, 2): {'en': "desired", 'fr': "désiré", 'de': "begehrt"},
	(0, 0): {'en': "neutral", 'fr': "neutre", 'de': "neutral"},
	(2, 0): {'en': "taks-\noriented", 'fr': "orienté tâche", 'de': "handlungs-\orientiert"},
	(-2, -2): {'en': "superfluous", 'fr': "superflu", 'de': "überflüssig"},
	(2, -2): {'en': "too\ntask-\noriented", 'fr': "trop\norienté\ntâche", 'de': "zu\handlungs-\orientiert"},
}

# pairs of word, ordered in the order we want them on the graph (QP, QHS, QHI and APP)
pairs = OrderedDict(
	QP1={
		'en': ("Technical", "Human"),
		'fr': ("Technique", "Humain"),
		'de': ("Technisch", "Menschlich")
	},
	QP2={
		'en': ("Complicated", "Simple"),
		'fr': ("Compliqué", "Simple"),
		'de': ("Kompliziert", "Menschlich")
	},
	QP3={
		'en': ("Impractical", "Pratical"),
		'fr': ("Pas pratique", "Pratique"),
		'de': ("Unpraktisch", "Praktisch")
	},
	QP4={
		'en': ("Cumbersome", "Straightforward"),
		'fr': ("Fastidieux", "Efficace"),
		'de': ("Umständlich", "Direkt")
	},
	QP5={
		'en': ("Unpredictable", "Predictable"),
		'fr': ("Imprévisible", "Prévisible"),
		'de': ("Unberechenbar", "Berechenbar")
	},
	QP6={
		'en': ("Confusing", "Clearly structured"),
		'fr': ("Confus", "Clair"),
		'de': ("Verwirrend", "Übersichtlich")
	},
	QP7={
		'en': ("Unruly", "Manageable"),
		'fr': ("Incontrôlable", "Maîtrisable"),
		'de': ("Widerspenstig", "Handhabbar")
	},
	QHS1={
		'en': ("Conventional", "Inventive"),
		'fr': ("Conventionnel", "Original"),
		'de': ("Konventionell", "Originell")
	},
	QHS2={
		'en': ("Unimaginative", "Creative"),
		'fr': ("Sans imagination", "Créatif"),
		'de': ("Phantasielos", "Kreativ")
	},
	QHS3={
		'en': ("Cautious", "Bold"),
		'fr': ("Prudent", "Audacieux"),
		'de': ("Vorsichtig", "Mutig")
	},
	QHS4={
		'en': ("Conservative", "Innovative"),
		'fr': ("Conservateur", "Novateur"),
		'de': ("Konservativ", "Innovativ")
	},
	QHS5={
		'en': ("Dull", "Captivating"),
		'fr': ("Ennuyeux", "Captivant"),
		'de': ("Lahm", "Fesselnd")
	},
	QHS6={
		'en': ("Undemanding", "Challenging"),
		'fr': ("Peu exigeant", "Challenging"),
		'de': ("Harmlos", "Herausfordernd")
	},
	QHS7={
		'en': ("Ordinary", "Novel"),
		'fr': ("Commun", "Nouveau"),
		'de': ("Herkömmlich", "Neuartig")
	},
	QHI1={
		'en': ("Isolating", "Connective"),
		'fr': ("M’isole", "Me sociabilise"),
		'de': ("Isolierend", "Verbindend")
	},
	QHI2={
		'en': ("Unprofessional", "Professional"),
		'fr': ("Amateur", "Professionnel"),
		'de': ("Laienhaft", "Fachmännisch")
	},
	QHI3={
		'en': ("Tacky", "Stylish"),
		'fr': ("De mauvais goût", "De bon goût"),
		'de': ("Stillos", "Stilvoll")
	},
	QHI4={
		'en': ("Cheap", "Premium"),
		'fr': ("Bas de gamme", "Haut de gamme"),
		'de': ("Minderwertig", "Wertvoll")
	},
	QHI5={
		'en': ("Alienating", "Integrating"),
		'fr': ("M’exclut", "M’intègre"),
		'de': ("Ausgrenzend", "Einbeziehend")
	},
	QHI6={
		'en': ("Separates me", "Bring me closer"),
		'fr': ("Me sépare des autres", "Me rapproche des autres"),
		'de': ("Trennt mich von Leuten", "Bringt mich den Leuten näher")
	},
	QHI7={
		'en': ("Unpresentable", "Presentable"),
		'fr': ("Non présentable", "Présentable"),
		'de': ("Nicht vorzeigbar", "Vorzeigbar")
	},

	ATT1={
		'en': ("Unpleasant", "Pleasant"),
		'fr': ("Déplaisant", "Plaisant"),
		'de': ("Unangenehm", "Angenehm")
	},
	ATT2={
		'en': ("Ugly", "Attractive"),
		'fr': ("Laid", "Beau"),
		'de': ("Hässlich", "Schön")
	},
	ATT3={
		'en': ("Disagreeable", "Likeable"),
		'fr': ("Désagréable", "Agréable"),
		'de': ("Unsympathisch", "Sympathisch")
	},
	ATT4={
		'en': ("Rejecting", "Inviting"),
		'fr': ("Rebutant", "Attirant"),
		'de': ("Zurückweisend", "Einladend")
	},
	ATT5={
		'en': ("Bad", "Good"),
		'fr': ("Mauvais", "Bon"),
		'de': ("Schlecht", "Gut")
	},
	ATT6={
		'en': ("Repelling", "appealing"),
		'fr': ("Repoussant", "Attrayant"),
		'de': ("Abstoßend", "Anziehend")
	},
	ATT7={
		'en': ("Discouraging", "Motivating"),
		'fr': ("Décourageant", "Motivant"),
		'de': ("Entmütigend", "Moivierend")
	}
)

