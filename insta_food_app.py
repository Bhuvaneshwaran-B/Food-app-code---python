{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "38badca5-ef0e-465b-be51-99593db27d3c",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "import pandas as pd\n",
    "\n",
    "# App Title\n",
    "st.title(\"📍 My Instagram Travel Map\")\n",
    "\n",
    "# Initialize a simple \"database\" in the app's memory\n",
    "if 'places' not in st.session_state:\n",
    "    st.session_state.places = pd.DataFrame(columns=[\"Name\", \"Area\", \"Category\", \"Map Link\"])\n",
    "\n",
    "# --- SIDEBAR: ADD NEW PLACE ---\n",
    "st.sidebar.header(\"Add New Discovery\")\n",
    "name = st.sidebar.text_input(\"Restaurant/Hotel Name\")\n",
    "area = st.sidebar.text_input(\"Area (e.g. Soho, Brooklyn, Dubai Marina)\")\n",
    "category = st.sidebar.selectbox(\"Type\", [\"Restaurant\", \"Hotel\", \"Cafe\", \"Bar\"])\n",
    "\n",
    "if st.sidebar.button(\"Save to My List\"):\n",
    "    # Generate a Google Maps search link automatically\n",
    "    search_url = f\"https://www.google.com/maps/search/?api=1&query={name.replace(' ', '+')}+{area.replace(' ', '+')}\"\n",
    "    \n",
    "    new_data = pd.DataFrame([[name, area, category, search_url]], \n",
    "                            columns=[\"Name\", \"Area\", \"Category\", \"Map Link\"])\n",
    "    \n",
    "    st.session_state.places = pd.concat([st.session_state.places, new_data], ignore_index=True)\n",
    "    st.sidebar.success(f\"Saved {name}!\")\n",
    "\n",
    "\n",
    "st.header(\"My Saved Spots\")\n",
    "\n",
    "if st.session_state.places.empty:\n",
    "    st.info(\"Your list is empty. Add something from the sidebar!\")\n",
    "else:\n",
    "    \n",
    "    areas = st.session_state.places['Area'].unique()\n",
    "    \n",
    "    for a in areas:\n",
    "        with st.expander(f\"🌆 {a.upper()}\"):\n",
    "            area_df = st.session_state.places[st.session_state.places['Area'] == a]\n",
    "            for index, row in area_df.iterrows():\n",
    "                col1, col2 = st.columns([3, 1])\n",
    "                col1.write(f\"**{row['Name']}** ({row['Category']})\")\n",
    "                col2.page_link(row['Map Link'], label=\"Navigate\", icon=\"🚗\")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
