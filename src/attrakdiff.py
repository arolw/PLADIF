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

File: attrakdiff.py
Date: Feb 2022

	Plot functions
"""


from typing import Dict, List, TypeVar
from pandas import read_excel, DataFrame, read_csv
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from scipy import stats
from math import sqrt
from io import BytesIO
import pandas as pd
import gettext

from naming import titles, order_long, order_short, pairs


def interval(data, alpha):
	"""Apply Student's t-distribution to get the confidence interval around the mean
	according to alpha (alpha=0.05 for a 95% confidence interval)
	returns the mean (center of the interval) and the interval (center of the interval)
	"""
	mean = data.mean()
	#return mean, (mean-data.std()/sqrt(2), mean+data.std()/sqrt(2))
	return mean, stats.t.interval(alpha, len(data)-1, loc=mean, scale=stats.sem(data))
	#return mean, (mean-1.895*stats.sem(data)/sqrt(len(data)-1), mean+1.895*stats.sem(data)/sqrt(len(data)-1))




def loadCSV(file: BytesIO):
	"""Load the data from an (already open) excel file
	The data is normalize in [-3,3]
	Return a dataframe"""
	# read the excel file into a dataframe
	Tab = read_csv(file, index_col=0, encoding="UTF-16", delimiter='\t') # encoding=None, encoding_errors="replace"
	# drop all the columns after the URL column
	try:
		url_index = Tab.columns.get_loc("URL")
	except KeyError:
		raise ValueError(_("The csv file is not a valid Usabilla one (does not contain a 'URL' column) !"))
	Tab.drop(columns=Tab.columns[url_index:], inplace=True)
	# check the size and rename the columns
	if len(Tab.columns) not in [len(order_short), len(order_long)]:
		raise ValueError(_("The csv file is not a valid Usabilla one (doesn not have %d or %d useful columns)") % (len(order_short), len(order_long)))
	Tab.columns = order_short if len(Tab.columns) == len(order_short) else order_long
	# normalize data in [-3,3]
	for col, serie in Tab.items():
		if '*' in col:
			Tab[col] = 4-Tab[col]   # reverse from 3 to -3
		else:
			Tab[col] = Tab[col]-4   # from -3 to 3
	# remove the '*' and sort the columns (same order as the ordered dictionary `pairs`
	Tab.columns = [(st[:-1] if '*' in st else st) for st in Tab.columns]
	d = {k: v for v, k in enumerate(pairs)}
	Tab = Tab.reindex(columns=sorted(Tab.columns, key=d.get))
	return Tab


def cat2dict(data: DataFrame) -> Dict[str, List[str]]:
	"""Returns the dictionary of the categories used
	Ex: {'QP': ['QP1','QP2'], 'ATT': ['ATT1']} """

	# groups categories
	return {name: [col for col in data.columns if name in col] for name in titles.keys()}


def plotMeanValues(fig: plt.Figure, ax: plt.Axes, datas: Dict[str, DataFrame]):
	"""Returns the dataFrame with the mean values"""
	cat = cat2dict(datas[next(iter(datas))])
	data = DataFrame.from_dict({name: {name: dF[cat].mean().mean() for name, cat in cat.items()} for name, dF in datas.items()})
	data = data.reindex(cat.keys())
	data.plot(ax=ax, grid=True, marker='o', xlabel=_('Dimension'), ylabel=_('Valeur moyenne'), ylim=[-3, 3])
	plt.setp(ax.get_xticklabels(), y=0.5)
	return data



def plotWordPair(fig: plt.Figure, ax: plt.Axes, datas: Dict[str, DataFrame]):
	#
	columns = datas[next(iter(datas))].columns
	plt.plot([0, 0], [len(columns) + 0.5, 0.5], 'k')
	# plot each line
	dd = DataFrame.from_dict({name: {col: dF[col].mean().T for col in columns} for name, dF in datas.items()})
	for name, data in datas.items():
		val = data.mean().T
		plt.plot(val, range(len(val), 0, -1), 's-')
	# set axes, etc.
	labelsL = [pairs[col][0] for col in datas[next(iter(datas))].T.index] + [""]
	labelsR = [pairs[col][1] for col in datas[next(iter(datas))].T.index] + [""]
	labelsL.reverse()
	labelsR.reverse()
	ax.set_yticks(range(len(labelsL)), labels=labelsL)
	ax.set_ylim(len(columns)+0.5, 0.5)
	axR = ax.twinx()
	axR.set_yticks(range(len(labelsR)), labels=labelsR)
	axR.set_ylim(len(columns)+0.5, 0.5)
	plt.xlim([-3, 3])

	ax.grid(visible=True)
	ax.set_box_aspect(1.25)

	return dd





def plotAttrakdiff(fig: plt.Figure, ax: plt.Axes, datas: Dict[str, DataFrame], alpha):
	plt.xlim([-3, 3])
	plt.ylim([-3, 3])
	ax.xaxis.set_ticks([-3, -1, 1, 3])
	ax.yaxis.set_ticks([-3, -1, 1, 3])
	plt.grid()
	plt.text(-2, 2, _("too\nself-\noriented"), alpha=0.5, ha='center', va='center')
	plt.text(0, 2, _("self-\noriented"), alpha=0.5, ha='center', va='center')
	plt.text(2, 2, _("desired"), alpha=0.5, ha='center', va='center')
	plt.text(0, 0, _("neutral"), alpha=0.5, ha='center', va='center')
	plt.text(2, 0, _("taks-\noriented"), alpha=0.5, ha='center', va='center')
	plt.text(-2, -2, _("superfluous"), alpha=0.5, ha='center', va='center')
	plt.text(2, -2, _("too\ntask-\noriented"), alpha=0.5, ha='center', va='center')
	plt.xlabel(_("Pragmatic Quality"))
	plt.ylabel(_("Hedonic Quality"))

	cat = cat2dict(datas[next(iter(datas))])
	attr = {}
	for name, data in datas.items():
		QH = data[cat["QHI"]+cat["QHS"]]
		QP = data[cat["QP"]]

		pd.options.display.max_rows = 999
		print("QP=", QP.stack())
		print("QH=", QH.stack())

		x, ix = interval(QP.stack(), alpha)
		y, iy = interval(QH.stack(), alpha)

		print("x=", x, "  ix=", ix)
		print("y=", x, "  iy=", iy)
		plt.plot(x, y, 'o')
		if alpha:
			ax.add_patch(Rectangle((ix[0], iy[0]), ix[1]-ix[0], iy[1]-iy[0], fill=True, alpha=0.2))
		attr[name] = {"QP":x, "QH":y}

	return pd.DataFrame.from_dict(attr)

# plt.style.use('default')
#
# T = loadData({"mars 21": "exp1.xlsx", "sept 21": "exp2.xlsx"})
# plotMeanValues(T)
# plotWordPair(T)
# plotAttrakdiff(T)

if __name__ == '__main__':
	X = loadCSV("../test/test.csv")
	#fig, ax = plt.subplots()
	#plotWordPair({'toto': X})
	fig, ax = plt.subplots()
	plotWordPair(fig, ax, {'toto': X})
	plt.show()