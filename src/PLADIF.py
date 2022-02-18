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

File: PLADIF.py
Date: Feb 2022

	main file with the interactions
"""
import pandas as pd
import streamlit as st
from tempfile import TemporaryDirectory
from os.path import join
from locale import getdefaultlocale
import matplotlib.pyplot as plt
from attrakdiff import loadCSV, plotWordPair, plotAttrakdiff, plotMeanValues


tmpFolder = TemporaryDirectory()


# TODO: think about i18n !
# https://lokalise.com/blog/beginners-guide-to-python-i18n/


def updateFileList():
	"""update the list of files
	(do not load already load file, remove from the dict the deleted files
	we need to do that to deal with the lack of information given by on_change that call that function"""
	# check the file(s) that are not yet in the dict, and load them
	newfiles = [f for f in st.session_state.csvFile if f.name not in st.session_state.data]
	if newfiles:
		for f in newfiles:
			try:
				print("LOAD "+f.name)
				st.session_state.data[f.name] = loadCSV(f)
			except ValueError as e:
				msg.error(str(e))
	# check the file(s) that are not anymore in the dict, and del them
	delfilenames = [name for name in st.session_state.data.keys() if name not in [f.name for f in st.session_state.csvFile]]
	if delfilenames:
		for name in delfilenames:
			print("DELETE "+name)
			del st.session_state.data[name]


def figure(fct):
	fig, ax = plt.subplots()
	ret = fct(fig, ax, st.session_state.data)
	st.pyplot(fig)
	imgFilename = join(tmpFolder.name, fct.__name__+".jpg")
	with open(imgFilename, 'w') as temp:
		plt.savefig(temp, format='jpg')
	with open(imgFilename, 'rb') as temp:
		st.download_button(label="Download jpeg", data=temp, file_name=fct.__name__+".jpg", mime="image/jpeg")
	return ret

# st.session_state.data stores all the data: {filename: DataFrame}
if 'data' not in st.session_state:
	st.session_state.data = {}


#st.set_page_config(layout="wide")
# title
st.title("PLADIF: Plot Attrakdiff graphs from CSV files")

# sidebar (to upload files)
with st.sidebar:
	st.markdown("<h1 style='text-align: center;'>Add here your CSV files</h1>", unsafe_allow_html=True)

	# CSV options
	with st.expander("CSV options"):
		CSVtype = {True: "Usabilla CSV file (UTF16, tab as delimiter)", False: "CSV file (UTF8 and coma as delimiter)"}
		CSV = st.selectbox("Choose a CSV type", CSVtype.keys(), format_func=lambda x: CSVtype.get(x),
			index=0, help="Choose the type of CSV file.", disabled=True)

	# file uploader
	files = st.file_uploader("", type=['csv'], accept_multiple_files=True, help="The file must be a CSV file, with tab delimiter and UTF-16 encoding (as produced by Usabilla).", on_change=updateFileList, key='csvFile')
	# error message array
	msg = st.empty()

	# spacing
	for _ in range(4):
		st.write("")

	# options
	with st.expander("Plot options"):
		default_lang = 1 if 'fr' in getdefaultlocale()[0].lower() else (2 if 'de' in getdefaultlocale()[0].lower() else 0)
		langOption = {"EN": "English", "FR": "Français", "DE": "Deutsch"}
		lang = st.selectbox("Choose a language", langOption.keys(), format_func=lambda x: langOption.get(x), index=default_lang, help="Change the language used in the plots.", disabled=True)
		stdOption = {0: "No", 1: "Yes at 67%", 2: "Yes at 90%", 3: "Yes at 95%"}
		std = st.selectbox("Plot confidence interval ?", stdOption.keys(), format_func=lambda x: stdOption.get(x), help="Display in the graph the confidence interval (at 67%, 90% or 95%) or not.", index=1, disabled=False)




# # load the data
# data = {}
# try:
# 	data = {shortname(f.name, 20): loadCSV(f) for f in files}
# except ValueError as e:
# 	msg.error(str(e))

import tempfile

if st.session_state.data:
	# mean values QP, QHI, QHS, ATT
	figure(plotMeanValues)

	# pair words plot
	figure(plotWordPair)
	# attrakdiff

	attrakdiff = figure(plotAttrakdiff)
	d = pd.DataFrame.from_dict(attrakdiff).T
	d.columns = ['QP', 'QH', 'var QP', 'var QH']
	st.table(d)




# footer
footer="""<style>
.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: white;
color: black;
text-align: center;
}
</style>
<div class="footer">
<p><a href="https://github.com/thilaire/PLADIF">PLADIF</a> is a small open source tool to draw attrakdiff plots, ©️ T. Hilaire, 2022.</p>
</div>
"""
st.markdown(footer, unsafe_allow_html=True)
