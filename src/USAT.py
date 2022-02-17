""""This file is part of USAT.

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


USAT is a simple tool that taks survey from Usabilla and plot attrakdiff plots.
It is written by Thibault Hilaire

File: USAT.py
Date: Feb 2022

	main file with the interactions
"""


import streamlit as st
import matplotlib.pyplot as plt
from attrakdiff import loadCSV, plotWordPair, plotAttrakdiff, plotMeanValues


# TODO: think about i18n !
# >>> import locale
# >>> locale.getdefaultlocale()
# ('en_GB', 'cp1252')
# + https://lokalise.com/blog/beginners-guide-to-python-i18n/



def shortname(filename: str, maxLength: int) -> str:
	"""shorten a filename such that it doesn't exceed maxLength char
	by adding ... in the middle"""
	if len(filename) > maxLength:
		return filename[0:maxLength//2-1] + "..." + filename[-maxLength//2:]
	else:
		return filename





#st.set_page_config(layout="wide")

# title
st.title("USAT: Usabilla to Attrakdiff")

# sidebar (to upload files)
with st.sidebar:
	st.header("Add here your Usabilla files")
	# file uploader
	files = st.file_uploader("", type=['csv'], accept_multiple_files=True, help="The file must be a CSV file, with tab delimiter and UTF-16 encoding (as produced by Usabilla).")
	# error message array
	msg = st.empty()

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


