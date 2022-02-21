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
def _(x): return x

# language options
langOption = OrderedDict(en="English", fr="Français", de="Deutsch")

# categories title
titles = {
	"QP": _("Pragmatic Quality"),
	"QHS": _("Hedonic Quality - Stimulation"),
	"QHI": _("Hedonic Quality - Identify"),
	"ATT": _("Attrativeness")
}

# pairs of word, ordered in the order we want them on the graph (QP, QHS, QHI and APP)
pairs = OrderedDict(
	QP1=(_("Technical"), _("Human")),
	QP2=(_("Complicated"), _("Simple")),
	QP3=(_("Impractical"), _("Pratical")),
	QP4=(_("Cumbersome"), _("Straightforward")),
	QP5=(_("Unpredictable"), _("Predictable")),
	QP6=(_("Confusing"), _("Clearly structured")),
	QP7=(_("Unruly"), _("Manageable")),

	QHS1=(_("Conventional"), _("Inventive")),
	QHS2=(_("Unimaginative"), _("Creative")),
	QHS3=(_("Cautious"), _("Bold")),
	QHS4=(_("Conservative"), _("Innovative")),
	QHS5=(_("Dull"), _("Captivating")),
	QHS6=(_("Undemanding"), _("Challenging")),
	QHS7=(_("Ordinary"), _("Novel")),

	QHI1=(_("Isolating"), _("Connective")),
	QHI2=(_("Unprofessional"), _("Professional")),
	QHI3=(_("Tacky"), _("Stylish")),
	QHI4=(_("Cheap"), _("Premium")),
	QHI5=(_("Alienating"), _("Integrating")),
	QHI6=(_("Separates me"), _("Bring me closer")),
	QHI7=(_("Unpresentable"), _("Presentable")),

	ATT1=(_("Unpleasant"), _("Pleasant")),
	ATT2=(_("Ugly"), _("Attractive")),
	ATT3=(_("Disagreeable"), _("Likeable")),
	ATT4=(_("Rejecting"), _("Inviting")),
	ATT5=(_("Bad"), _("Good")),
	ATT6=(_("Repelling"), _("Appealing")),
	ATT7=(_("Discouraging"), _("Motivating"))
)

# short or long attrakdiff
order_short = ["QP2*", 'ATT2', 'QP3*', 'QHI3*', 'QP5*', "QHI4", "QHS2", "ATT5*", "QP6", "QHS5"]
order_long = [
	"QP1*", "QHI1", "ATT1*", "QHS1*", "QP2*", "QHI2*", "ATT2", "QP3", "ATT3*, QP4",
	"QHI3*", "QP5*", "QHI4", "QHI5", "QHI6*", "QHI7", "ATT4", "QHS2", "ATT5*",
	'QP6', "ATT6", "QHS3*", "QHS4*", "QHS5", "QHS6", "ATT7*", "QHS7*", "QP7"
]

del _
