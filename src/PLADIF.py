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


import streamlit as st
from os.path import splitext
from locale import getdefaultlocale
import matplotlib.pyplot as plt
from attrakdiff import loadCSV, plotWordPair, plotAttrakdiff, plotMeanValues


# TODO: think about i18n !
# https://lokalise.com/blog/beginners-guide-to-python-i18n/



def shortname(filename: str, maxLength: int) -> str:
	"""shorten a filename such that it doesn't exceed maxLength char
	by adding ... in the middle"""
	filename = splitext(filename)[0]
	if len(filename) > maxLength:
		return filename[0:maxLength//2-1] + "..." + filename[-maxLength//2:]
	else:
		return filename




#st.set_page_config(layout="wide")

# title
st.title("PLADIF: Plot Attrakdiff graphs from CSV files")


# sidebar (to upload files)
with st.sidebar:
	st.markdown("<h1 style='text-align: center;'>Add here your Usabilla files</h1>", unsafe_allow_html=True)
	#st.header("Add here your Usabilla files")
	# file uploader
	files = st.file_uploader("", type=['csv'], accept_multiple_files=True, help="The file must be a CSV file, with tab delimiter and UTF-16 encoding (as produced by Usabilla).")
	# error message array
	msg = st.empty()

	# spacing
	for _ in range(4):
		st.write("")

	# options
	with st.expander("Options"):
		default_lang = 1 if 'fr' in getdefaultlocale()[0].lower() else (2 if 'de' in getdefaultlocale()[0].lower() else 0)
		langOption = {"EN": "English", "FR": "Français", "DE": "Deutsch"}
		lang = st.selectbox("Choose a language", langOption.keys(), format_func=lambda x: langOption.get(x), index=default_lang, help="Change the language used in the plots.", disabled=True)
		stdOption = {0: "No", 1: "Yes at 67%", 2: "Yes at 90%", 3: "Yes at 95%"}
		std = st.selectbox("Plot confidence interval ?", stdOption.keys(), format_func=lambda x: stdOption.get(x), help="Display in the graph the confidence interval (at 67%, 90% or 95%) or not.", index=1, disabled=False)




# load the data
data = {}
try:
	data = {shortname(f.name, 20): loadCSV(f) for f in files}
except ValueError as e:
	msg.error(str(e))

if data:
	# mean values QP, QHI, QHS, ATT
	fig, ax = plt.subplots()
	plotMeanValues(fig, ax, data)
	st.pyplot(fig)
	# pair words plot
	fig, ax = plt.subplots()
	plotWordPair(fig, ax, data)
	st.pyplot(fig)
	# attrakdiff
	fig, ax = plt.subplots()
	attraldiff = plotAttrakdiff(fig, ax, data)
	st.pyplot(fig)



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
<hr/>
<div class="footer">
<p><a href="https://github.com/thilaire/PLADIF">PLADIF</a> is a small open source tool to draw attrakdiff plots, ©️ T. Hilaire, 2022.</p>
</div>
"""
st.markdown(footer, unsafe_allow_html=True)
