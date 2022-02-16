import streamlit as st

import streamlit as st
import pandas as pd
import numpy as np


# TODO: think about i18n !
# >>> import locale
# >>> locale.getdefaultlocale()
# ('en_GB', 'cp1252')
# + https://lokalise.com/blog/beginners-guide-to-python-i18n/

#st.set_page_config(layout="wide")

# title
st.title("USAT: Usabilla to Attrakdiff")
st.header("Add your Usabilla files")






def remove(i):
	del st.session_state.tab[i]

# files
if 'tab' not in st.session_state:
	st.session_state.tab = []


with st.form("Add some Usabilla data"):
	file = st.file_uploader("Upload a csv file", type=['csv'], accept_multiple_files=False, help='Add here your Usabilla csv file')
	if file:
		label = st.text_input("Label for file "+file.name, help="Indicate here the label for these data")
	msg = st.empty()
	# Every form must have a submit button.
	submitted = st.form_submit_button("Submit")
	if submitted:
		if not label:
			msg.error("A label is required")
		elif not file:
			msg.error("A file is required")
		elif label in [x[1] for x in st.session_state.tab]:
			msg.error("Duplicate label")
		else:
			msg.empty()
			st.session_state.tab.append((file.name, label))

columns = st.columns((1,4,4,1))
for col, name in zip(columns, ["plot", "filename", "label", ""]):
	col.write(name)
for i, t in enumerate(st.session_state.tab):
	check = columns[0].empty()
	check.checkbox("", key='check'+str(i))
	columns[1].write(t[0])
	columns[2].write(t[1])
	bt = columns[3].empty()
	bt.button("❌", on_click=remove, args=(i,), key='del'+str(i))








# col1, col2 = st.columns(2)
# col1.file_uploader("Choose a file", accept_multiple_files=True)
# col2.text_input("totoi")
#
# col1, col2 = st.columns(2)
# col1.file_uploader("Choose", accept_multiple_files=True)
# col2.text_input("titi")
