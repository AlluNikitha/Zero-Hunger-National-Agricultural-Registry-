import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
# pyrefly: ignore [missing-import]
import folium
# pyrefly: ignore [missing-import]
from streamlit_folium import st_folium
import os
import sys

# Page Configuration - Clean, Wide & Professional
st.set_page_config(
    page_title="AgriPulse | Crop & Farmer Data Management System",
    page_icon="🌾",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Workspace Root Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data')
IMG_DIR = os.path.join(DATA_DIR, 'images')

# -------------------------------------------------------------
# LIGHT THEMES DICTIONARY (STRICTLY LIGHT THEMES, HIGH CONTRAST)
# -------------------------------------------------------------
LIGHT_THEMES = {
    "🌿 Fresh Emerald (Clean Agro Light)": {
        "name": "Fresh Emerald",
        "bg_color": "#f8fafc",
        "card_bg": "#ffffff",
        "card_border": "#e2e8f0",
        "card_shadow": "0 4px 20px -2px rgba(5, 150, 105, 0.08), 0 2px 6px -1px rgba(0, 0, 0, 0.04)",
        "text_color": "#0f172a",
        "text_muted": "#64748b",
        "brand_title": "#064e3b",
        "brand_sub": "#059669",
        "heading_gradient": "linear-gradient(135deg, #065f46 0%, #047857 100%)",
        "heading_h2": "#0f172a",
        "heading_h3": "#1e293b",
        "metric_num": "#047857",
        "accent_primary": "#059669",
        "accent_secondary": "#10b981",
        "chart_primary": "#059669",
        "chart_secondary": "#0d9488",
        "tab_bg": "#f1f5f9",
        "tab_text": "#475569",
        "tab_active_bg": "linear-gradient(135deg, #059669 0%, #10b981 100%)",
        "tab_active_color": "#ffffff",
        "hero_bg": "linear-gradient(135deg, #ecfdf5 0%, #f0fdf4 45%, #ffffff 100%)",
        "hero_border": "#a7f3d0",
        "hero_badge_bg": "#ecfdf5",
        "hero_badge_text": "#059669",
        "hero_badge_border": "#6ee7b7",
        "top_bar_bg": "#ffffff",
        "top_bar_border": "#e2e8f0"
    },
    "🌾 Golden Harvest (Sunlit Amber Light)": {
        "name": "Golden Harvest",
        "bg_color": "#fdfbf7",
        "card_bg": "#ffffff",
        "card_border": "#fde68a",
        "card_shadow": "0 4px 20px -2px rgba(180, 83, 9, 0.09), 0 2px 6px -1px rgba(0, 0, 0, 0.04)",
        "text_color": "#1c1917",
        "text_muted": "#78716c",
        "brand_title": "#78350f",
        "brand_sub": "#b45309",
        "heading_gradient": "linear-gradient(135deg, #b45309 0%, #d97706 100%)",
        "heading_h2": "#1c1917",
        "heading_h3": "#292524",
        "metric_num": "#b45309",
        "accent_primary": "#d97706",
        "accent_secondary": "#f59e0b",
        "chart_primary": "#d97706",
        "chart_secondary": "#b45309",
        "tab_bg": "#fef3c7",
        "tab_text": "#78350f",
        "tab_active_bg": "linear-gradient(135deg, #d97706, #b45309)",
        "tab_active_color": "#ffffff",
        "hero_bg": "linear-gradient(135deg, #fffbeb 0%, #fef3c7 45%, #ffffff 100%)",
        "hero_border": "#fde68a",
        "hero_badge_bg": "#fef3c7",
        "hero_badge_text": "#b45309",
        "hero_badge_border": "#fcd34d",
        "top_bar_bg": "#ffffff",
        "top_bar_border": "#fde68a"
    },
    "🌊 Nordic Breeze (Oceanic Cyan Light)": {
        "name": "Nordic Breeze",
        "bg_color": "#f0f9ff",
        "card_bg": "#ffffff",
        "card_border": "#bae6fd",
        "card_shadow": "0 4px 20px -2px rgba(2, 132, 199, 0.09), 0 2px 6px -1px rgba(0, 0, 0, 0.04)",
        "text_color": "#0c4a6e",
        "text_muted": "#64748b",
        "brand_title": "#075985",
        "brand_sub": "#0284c7",
        "heading_gradient": "linear-gradient(135deg, #0369a1 0%, #0284c7 100%)",
        "heading_h2": "#0c4a6e",
        "heading_h3": "#075985",
        "metric_num": "#0284c7",
        "accent_primary": "#0284c7",
        "accent_secondary": "#06b6d4",
        "chart_primary": "#0284c7",
        "chart_secondary": "#0369a1",
        "tab_bg": "#e0f2fe",
        "tab_text": "#0369a1",
        "tab_active_bg": "linear-gradient(135deg, #0284c7, #0369a1)",
        "tab_active_color": "#ffffff",
        "hero_bg": "linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 45%, #ffffff 100%)",
        "hero_border": "#bae6fd",
        "hero_badge_bg": "#e0f2fe",
        "hero_badge_text": "#0284c7",
        "hero_badge_border": "#7dd3fc",
        "top_bar_bg": "#ffffff",
        "top_bar_border": "#bae6fd"
    },
    "🍃 Sage & Olive (Botanical Earth Light)": {
        "name": "Sage & Olive",
        "bg_color": "#fafaf9",
        "card_bg": "#ffffff",
        "card_border": "#dcfce7",
        "card_shadow": "0 4px 20px -2px rgba(21, 128, 61, 0.08), 0 2px 6px -1px rgba(0, 0, 0, 0.04)",
        "text_color": "#1c1917",
        "text_muted": "#71717a",
        "brand_title": "#14532d",
        "brand_sub": "#15803d",
        "heading_gradient": "linear-gradient(135deg, #15803d 0%, #4d7c0f 100%)",
        "heading_h2": "#14532d",
        "heading_h3": "#166534",
        "metric_num": "#15803d",
        "accent_primary": "#15803d",
        "accent_secondary": "#65a30d",
        "chart_primary": "#15803d",
        "chart_secondary": "#4d7c0f",
        "tab_bg": "#f4f4f5",
        "tab_text": "#3f3f46",
        "tab_active_bg": "linear-gradient(135deg, #15803d, #4d7c0f)",
        "tab_active_color": "#ffffff",
        "hero_bg": "linear-gradient(135deg, #f0fdf4 0%, #f7fee7 45%, #ffffff 100%)",
        "hero_border": "#bbf7d0",
        "hero_badge_bg": "#dcfce7",
        "hero_badge_text": "#15803d",
        "hero_badge_border": "#86efac",
        "top_bar_bg": "#ffffff",
        "top_bar_border": "#dcfce7"
    },
    "🌸 Lavender Bloom (Pastel Modern Light)": {
        "name": "Lavender Bloom",
        "bg_color": "#faf5ff",
        "card_bg": "#ffffff",
        "card_border": "#e9d5ff",
        "card_shadow": "0 4px 20px -2px rgba(124, 58, 237, 0.08), 0 2px 6px -1px rgba(0, 0, 0, 0.04)",
        "text_color": "#2e1065",
        "text_muted": "#6b7280",
        "brand_title": "#4c1d95",
        "brand_sub": "#7c3aed",
        "heading_gradient": "linear-gradient(135deg, #6d28d9 0%, #7c3aed 100%)",
        "heading_h2": "#3b0764",
        "heading_h3": "#4c1d95",
        "metric_num": "#7c3aed",
        "accent_primary": "#7c3aed",
        "accent_secondary": "#ec4899",
        "chart_primary": "#7c3aed",
        "chart_secondary": "#c026d3",
        "tab_bg": "#f3e8ff",
        "tab_text": "#6b21a8",
        "tab_active_bg": "linear-gradient(135deg, #7c3aed, #6d28d9)",
        "tab_active_color": "#ffffff",
        "hero_bg": "linear-gradient(135deg, #faf5ff 0%, #f3e8ff 45%, #ffffff 100%)",
        "hero_border": "#e9d5ff",
        "hero_badge_bg": "#f3e8ff",
        "hero_badge_text": "#7c3aed",
        "hero_badge_border": "#d8b4fe",
        "top_bar_bg": "#ffffff",
        "top_bar_border": "#e9d5ff"
    }
}

# -------------------------------------------------------------
# TOP NAVIGATION BAR (WITH THEME SELECTOR & ABOUT BUTTON)
# -------------------------------------------------------------
# We place the selector at the top
theme_keys = list(LIGHT_THEMES.keys())

# Top Navbar Layout
top_col_brand, top_col_theme, top_col_about, top_col_add = st.columns(
    [3.2, 2.2, 1.1, 1.2], vertical_alignment="center"
)

with top_col_theme:
    selected_theme_key = st.selectbox(
        "Select Light Theme",
        theme_keys,
        index=0,
        key="app_theme_selector",
        label_visibility="collapsed",
        help="Switch between 5 curated high-contrast Light themes"
    )

with top_col_about:
    btn_top_about = st.button("ℹ️ About", use_container_width=True, help="Learn about the system, UN SDG 2 targets & architecture")

with top_col_add:
    btn_top_add = st.button("➕ Add Farmer", use_container_width=True, help="Register a new farmer profile")

# Active Theme Palette
t = LIGHT_THEMES[selected_theme_key]

with top_col_brand:
    st.markdown(f"""
    <div style="display: flex; align-items: center; gap: 14px; padding: 4px 0;">
        <div style="font-size: 2.3rem; line-height: 1;">🌾</div>
        <div>
            <div style="font-size: 1.55rem; font-weight: 850; color: {t['brand_title']}; letter-spacing: -0.025em; line-height: 1.2;">
                AgriPulse Platform
            </div>
            <div style="font-size: 0.84rem; color: {t['brand_sub']}; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em;">
                UN SDG 2: Zero Hunger & National Agricultural Registry
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# -------------------------------------------------------------
# DYNAMIC CSS INJECTION (FULL PALETTE TRANSFORMATION)
# -------------------------------------------------------------
st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800;900&family=Inter:wght@400;500;600;700&display=swap');

/* Hide empty Streamlit top header bar to prevent clipping */
header[data-testid="stHeader"] {{
    display: none !important;
}}

/* Universal page background & text */
html, body, .stApp, [data-testid="stAppViewContainer"], [data-testid="stMain"] {{
    font-family: 'Outfit', 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
    background-color: {t['bg_color']} !important;
    color: {t['text_color']} !important;
}}

/* Neat, spacious block container */
.block-container {{
    padding-top: 1.5rem !important;
    padding-bottom: 3.5rem !important;
    max-width: 1440px !important;
}}

/* Headings with dynamic theme gradients */
h1, [data-testid="stHeadingWithActionElements"] h1 {{
    background: {t['heading_gradient']} !important;
    -webkit-background-clip: text !important;
    -webkit-text-fill-color: transparent !important;
    font-weight: 850 !important;
    letter-spacing: -0.025em !important;
    margin-bottom: 0.5rem !important;
}}

h2, [data-testid="stHeadingWithActionElements"] h2 {{
    color: {t['heading_h2']} !important;
    font-weight: 750 !important;
    border-left: 5px solid {t['accent_primary']} !important;
    padding-left: 14px !important;
    margin-top: 1.6rem !important;
    margin-bottom: 0.8rem !important;
    font-size: 1.6rem !important;
}}

h3, [data-testid="stHeadingWithActionElements"] h3 {{
    color: {t['heading_h3']} !important;
    font-weight: 700 !important;
    margin-top: 1.2rem !important;
    font-size: 1.25rem !important;
}}

p, span, label, div {{
    color: {t['text_color']};
    line-height: 1.6;
}}

label[data-testid="stWidgetLabel"] p, .stSelectbox label, .stTextInput label, .stNumberInput label, .stSlider label {{
    font-weight: 700 !important;
    font-size: 0.92rem !important;
    color: {t['heading_h2']} !important;
}}

/* Hero Header */
.hero-header {{
    background: {t['hero_bg']} !important;
    border-radius: 20px !important;
    padding: 2.2rem 2.8rem !important;
    text-align: center !important;
    margin-top: 0.8rem !important;
    margin-bottom: 1.8rem !important;
    border: 1px solid {t['hero_border']} !important;
    box-shadow: {t['card_shadow']} !important;
}}

.hero-badge {{
    display: inline-block !important;
    background: {t['hero_badge_bg']} !important;
    color: {t['hero_badge_text']} !important;
    padding: 5px 16px !important;
    border-radius: 9999px !important;
    font-weight: 700 !important;
    font-size: 0.82rem !important;
    letter-spacing: 0.05em !important;
    text-transform: uppercase !important;
    margin-bottom: 0.75rem !important;
    border: 1px solid {t['hero_badge_border']} !important;
}}

.hero-title {{
    font-size: 2.6rem !important;
    font-weight: 900 !important;
    background: {t['heading_gradient']} !important;
    -webkit-background-clip: text !important;
    -webkit-text-fill-color: transparent !important;
    margin-bottom: 0.5rem !important;
    letter-spacing: -0.03em !important;
    line-height: 1.2 !important;
}}

.hero-subtitle {{
    font-size: 1.15rem !important;
    color: {t['text_muted']} !important;
    font-weight: 500 !important;
    max-width: 880px !important;
    margin: 0 auto !important;
    line-height: 1.6 !important;
}}

/* Metric Cards */
.metric-card {{
    background: {t['card_bg']} !important;
    border: 1px solid {t['card_border']} !important;
    border-top: 4px solid {t['accent_primary']} !important;
    border-radius: 16px !important;
    padding: 1.4rem 1.2rem !important;
    text-align: center !important;
    box-shadow: {t['card_shadow']} !important;
    transition: all 0.25s ease !important;
    height: 100% !important;
}}
.metric-card:hover {{
    transform: translateY(-3px) !important;
    box-shadow: 0 12px 28px -4px rgba(0, 0, 0, 0.12) !important;
}}
.metric-label {{
    font-size: 0.82rem !important;
    font-weight: 700 !important;
    color: {t['text_muted']} !important;
    text-transform: uppercase !important;
    letter-spacing: 0.06em !important;
    margin-bottom: 0.35rem !important;
}}
.metric-value {{
    font-size: 2.15rem !important;
    font-weight: 900 !important;
    color: {t['metric_num']} !important;
    line-height: 1.1 !important;
}}
.metric-sub {{
    font-size: 0.82rem !important;
    color: {t['text_muted']} !important;
    margin-top: 0.4rem !important;
    font-weight: 500 !important;
}}

/* Navigation Tabs */
.stTabs [data-baseweb="tab-list"] {{
    gap: 8px !important;
    background-color: {t['tab_bg']} !important;
    padding: 8px !important;
    border-radius: 16px !important;
    border: 1px solid {t['card_border']} !important;
    margin-top: 0.5rem !important;
    margin-bottom: 1.8rem !important;
}}
.stTabs [data-baseweb="tab"] {{
    height: 3.1rem !important;
    background-color: transparent !important;
    border-radius: 12px !important;
    padding: 8px 20px !important;
    font-weight: 700 !important;
    font-size: 0.94rem !important;
    border: none !important;
    transition: all 0.2s ease !important;
}}
.stTabs [data-baseweb="tab"] p, .stTabs [data-baseweb="tab"] span {{
    color: {t['tab_text']} !important;
    font-weight: 700 !important;
}}
.stTabs [data-baseweb="tab"]:hover {{
    background: rgba(0, 0, 0, 0.04) !important;
}}
.stTabs [aria-selected="true"] {{
    background: {t['tab_active_bg']} !important;
    box-shadow: 0 4px 14px rgba(0, 0, 0, 0.15) !important;
}}
.stTabs [aria-selected="true"] p, .stTabs [aria-selected="true"] span {{
    color: {t['tab_active_color']} !important;
    font-weight: 800 !important;
}}

/* All Buttons High Contrast Styling */
.stButton button, .stDownloadButton button {{
    background: {t['tab_active_bg']} !important;
    border-radius: 10px !important;
    border: none !important;
    padding: 0.65rem 1.4rem !important;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.12) !important;
    transition: all 0.2s ease !important;
}}
.stButton button p, .stButton button span, .stDownloadButton button p, .stDownloadButton button span {{
    color: #ffffff !important;
    font-weight: 700 !important;
    font-size: 0.92rem !important;
}}
.stButton button:hover, .stDownloadButton button:hover {{
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 20px rgba(0, 0, 0, 0.25) !important;
}}

/* DataFrames */
[data-testid="stDataFrame"] {{
    border-radius: 14px !important;
    overflow: hidden !important;
    border: 1px solid {t['card_border']} !important;
    box-shadow: {t['card_shadow']} !important;
    background: {t['card_bg']} !important;
}}

/* About Target Cards */
.about-card {{
    background: {t['card_bg']} !important;
    border: 1px solid {t['card_border']} !important;
    border-radius: 16px !important;
    padding: 1.6rem !important;
    box-shadow: {t['card_shadow']} !important;
    height: 100% !important;
}}
</style>
""", unsafe_allow_html=True)

# -------------------------------------------------------------
# DATA LOADING VIA PANDAS
# -------------------------------------------------------------
@st.cache_data
def load_datasets():
    if not os.path.exists(DATA_DIR):
        return None, None, None, None
    try:
        f_df = pd.read_csv(os.path.join(DATA_DIR, 'farmer_data.csv'))
        c_df = pd.read_csv(os.path.join(DATA_DIR, 'crop_data.csv'))
        m_df = pd.read_csv(os.path.join(DATA_DIR, 'market_data.csv'))
        p_df = pd.read_csv(os.path.join(DATA_DIR, 'production_data.csv'))
        return f_df, c_df, m_df, p_df
    except Exception as e:
        st.error(f"Error loading datasets: {e}")
        return None, None, None, None

farmers_df, crops_df, markets_df, production_df = load_datasets()

if farmers_df is None or crops_df is None:
    st.error(f"Dataset files not found in '{DATA_DIR}'. Please ensure CSV files exist in the 'data/' directory.")
    st.stop()

# -------------------------------------------------------------
# DIALOG 1: ABOUT SYSTEM & SDG 2 MISSION (CLICKABLE FROM TOP)
# -------------------------------------------------------------
@st.dialog("ℹ️ About AgriPulse System & UN SDG 2 Mission", width="large")
def about_system_dialog():
    st.markdown("""
    ### 🌾 AgriPulse: Centralized Agricultural Intelligence Platform
    AgriPulse is a comprehensive agricultural data management and analytics system built to advance **United Nations Sustainable Development Goal 2 (SDG 2: Zero Hunger)**.
    It unifies farmer registry demographics, precision agronomic specifications, quantitative yield analytics, and real-time APMC Mandi wholesale price discovery.
    """)
    
    st.markdown("---")
    st.markdown("#### 🎯 Core UN SDG 2 Targets Addressed:")
    
    col_d1, col_d2 = st.columns(2)
    with col_d1:
        st.info("**🎯 Target 2.1 — End Hunger & Ensure Universal Food Access**\n\nOptimizes spatial distribution of crops and provides supply transparency to curb agricultural supply chain losses.")
        st.success("**🌾 Target 2.3 — Double Productivity & Income of Smallholders**\n\nIdentifies underperforming farms with NumPy Z-Scores and pairs them with ideal soil-crop vectors to raise output.")
    with col_d2:
        st.warning("**💧 Target 2.4 — Sustainable Agriculture & Climate Resilience**\n\nMonitors irrigation infrastructure (drip, sprinkler, rainfed) and prioritizes climate-resilient pulses and millets.")
        st.error("**⚖️ Target 2.c — Fair APMC Mandi Markets & MSP Benchmarks**\n\nDetects price arbitrage across mandis and protects farmers from distress sales below the Government MSP rate.")

    st.markdown("---")
    st.markdown("#### 🛠️ Computational Engine & Technologies:")
    st.markdown(f"""
    - **Streamlit ({st.__version__})**: Reactive, modern web application with top navigation controls and 5 custom light themes.
    - **Pandas ({pd.__version__})**: High-performance relational data handling, multi-criteria filtering, grouping, and CSV export.
    - **NumPy ({np.__version__})**: Parametric distribution modeling, Gaussian curve fitting, Z-Score outlier detection, and 1,000-trial Monte Carlo stochastic simulations.
    - **Active Datasets**: `{len(farmers_df):,}` Farmers | `{len(crops_df)}` Crops | `{len(production_df):,}` Harvest Records | `{len(markets_df):,}` Mandi Price Feeds.
    """)

# -------------------------------------------------------------
# DIALOG 2: REGISTER NEW FARMER PROFILE
# -------------------------------------------------------------
@st.dialog("➕ Register New Farmer Profile", width="large")
def register_farmer_dialog():
    st.markdown("Fill in the agricultural credentials for the new farmer:")
    with st.form("add_farmer_form"):
        col_f1, col_f2 = st.columns(2)
        farmer_name = col_f1.text_input("Full Farmer Name *", placeholder="e.g. Ramesh Patel")
        farmer_gender = col_f2.selectbox("Gender", ["Male", "Female", "Other"])
        
        col_f3, col_f4 = st.columns(2)
        farmer_contact = col_f3.text_input("Contact Number (10 digits) *", placeholder="9876543210")
        farmer_state = col_f4.selectbox("State *", sorted(farmers_df['State'].unique().tolist()))
        
        col_f5, col_f6 = st.columns(2)
        farmer_district = col_f5.text_input("District *", placeholder="e.g. Ludhiana")
        farmer_village = col_f6.text_input("Village *", placeholder="e.g. Samrala")
        
        col_f7, col_f8, col_f9 = st.columns(3)
        farmer_land = col_f7.number_input("Land Area (Acres) *", min_value=0.1, max_value=200.0, value=3.5, step=0.1)
        farmer_soil = col_f8.selectbox("Dominant Soil Type", ["Alluvial", "Black (Regur)", "Red", "Sandy Loam", "Clayey", "Loam"])
        farmer_irrigation = col_f9.selectbox("Irrigation Facility", ["Tube Well / Borewell", "Canal", "Drip Irrigation", "Rainfed", "Sprinkler"])
        
        col_f10, col_f11 = st.columns(2)
        farmer_crop = col_f10.selectbox("Primary Cultivated Crop *", sorted(crops_df['Crop_Name'].unique().tolist()))
        farmer_pmkisan = col_f11.selectbox("PM-KISAN Beneficiary?", ["Yes", "No"])
        
        submit_btn = st.form_submit_button("💾 Save & Register Profile", use_container_width=True)
        if submit_btn:
            if not farmer_name or not farmer_contact or not farmer_district or not farmer_village:
                st.error("Please fill all required fields marked with an asterisk (*).")
            else:
                new_id = f"F{str(len(farmers_df) + 1).zfill(3)}"
                new_farmer = {
                    "Farmer_ID": new_id,
                    "Name": farmer_name,
                    "Gender": farmer_gender,
                    "Contact": farmer_contact,
                    "State": farmer_state,
                    "District": farmer_district,
                    "Village": farmer_village,
                    "Land_Area_Acres": farmer_land,
                    "Soil_Type": farmer_soil,
                    "Irrigation_Type": farmer_irrigation,
                    "Primary_Crop": farmer_crop,
                    "PM_Kisan_Beneficiary": farmer_pmkisan
                }
                new_df = pd.DataFrame([new_farmer])
                updated = pd.concat([farmers_df, new_df], ignore_index=True)
                updated.to_csv(os.path.join(DATA_DIR, 'farmer_data.csv'), index=False)
                st.cache_data.clear()
                st.success(f"Farmer '{farmer_name}' (ID: {new_id}) successfully enrolled!")
                st.rerun()

# Trigger dialogs from top buttons
if btn_top_about:
    about_system_dialog()

if btn_top_add:
    register_farmer_dialog()

# -------------------------------------------------------------
# HERO HEADER BANNER
# -------------------------------------------------------------
st.markdown(f"""
<div class="hero-header">
    <div class="hero-badge">🌱 UN Sustainable Development Goal 2: Zero Hunger</div>
    <div class="hero-title">Crop & Farmer Data Management System</div>
    <div class="hero-subtitle">
        A centralized agricultural data and analytics platform built with <b>Streamlit, Pandas, and NumPy</b>. 
        Empowering farmers, researchers, and agronomists with landholdings, crop intelligence, harvest yield modeling, and APMC Mandi price tracking.
    </div>
</div>
""", unsafe_allow_html=True)

# -------------------------------------------------------------
# NUMPY HIGH-LEVEL AGRO METRIC CARDS
# -------------------------------------------------------------
total_farmers = len(farmers_df)
total_crops = len(crops_df)
total_mandis = len(markets_df)

prod_array = production_df['Production_Tonnes'].to_numpy() if 'Production_Tonnes' in production_df.columns else np.array([7857])
yield_array = production_df['Yield_T_Per_Acre'].to_numpy() if 'Yield_T_Per_Acre' in production_df.columns else np.array([5.5])

total_production_tonnes = np.sum(prod_array)
mean_yield_t_acre = np.mean(yield_array)
yield_std_t_acre = np.std(yield_array)

kpi1, kpi2, kpi3, kpi4, kpi5 = st.columns(5)
with kpi1:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">👨‍🌾 Total Farmers</div>
        <div class="metric-value">{total_farmers:,}</div>
        <div class="metric-sub">Across 14 Agro-States</div>
    </div>
    """, unsafe_allow_html=True)

with kpi2:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">🌱 Crop Varieties</div>
        <div class="metric-value">{total_crops}</div>
        <div class="metric-sub">Kharif, Rabi & Zaid</div>
    </div>
    """, unsafe_allow_html=True)

with kpi3:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">⚖️ Total Output</div>
        <div class="metric-value">{int(total_production_tonnes):,} <span style="font-size:1.1rem;">T</span></div>
        <div class="metric-sub">NumPy Vector Sum</div>
    </div>
    """, unsafe_allow_html=True)

with kpi4:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">🌾 Avg Yield Rate</div>
        <div class="metric-value">{mean_yield_t_acre:.2f} <span style="font-size:1rem;">T/Ac</span></div>
        <div class="metric-sub">Std Dev: ±{yield_std_t_acre:.2f}</div>
    </div>
    """, unsafe_allow_html=True)

with kpi5:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">🏪 APMC Mandis</div>
        <div class="metric-value">{total_mandis}</div>
        <div class="metric-sub">Live Price Feeds</div>
    </div>
    """, unsafe_allow_html=True)

st.write("")

# -------------------------------------------------------------
# TOP NAVIGATION TABS (ABOUT PAGE IS FIRST & VISIBLE AT TOP)
# -------------------------------------------------------------
tab_about, tab_farmers, tab_crops, tab_analytics, tab_simulator, tab_mandi, tab_gis, tab_data = st.tabs([
    "ℹ️ About & SDG 2 Hub",
    "👨‍🌾 Farmer Directory",
    "🌱 Crop Explorer",
    "📊 NumPy Yield Analytics",
    "🎲 Monte Carlo Simulator",
    "💰 APMC Mandi & Arbitrage",
    "🗺️ Agricultural GIS Map",
    "📁 Raw Datasets"
])

# -------------------------------------------------------------
# TAB 1: ABOUT & SDG 2 HUB (PROMINENT AT TOP)
# -------------------------------------------------------------
with tab_about:
    st.header("About AgriPulse & UN SDG 2 Zero Hunger Mission")
    st.markdown("""
    The **AgriPulse Crop & Farmer Data Management System** is a high-performance agricultural intelligence platform engineered to advance **United Nations Sustainable Development Goal 2 (SDG 2: Zero Hunger)**.
    By bridging smallholder farming communities with quantitative agronomic analytics and transparent market intelligence, the system democratizes data across the agricultural value chain.
    """)
    
    col_a1, col_a2 = st.columns(2, gap="large")
    with col_a1:
        st.markdown(f"""
        <div class="about-card" style="border-left: 5px solid {t['accent_primary']}; margin-bottom: 1.2rem;">
            <h4 style="margin:0 0 0.4rem 0; color:{t['accent_primary']};">🎯 SDG Target 2.1: Universal Access to Safe & Nutritious Food</h4>
            <p style="margin:0; color:{t['text_muted']}; font-size:0.95rem;">
                Eliminates agricultural information asymmetry by providing real-time production, mandi arrival rates, and harvest output distribution. 
                Helps policymakers redirect surplus staple crops to food-stressed districts and reduces post-harvest supply chain spoilage.
            </p>
        </div>
        <div class="about-card" style="border-left: 5px solid {t['chart_secondary']};">
            <h4 style="margin:0 0 0.4rem 0; color:{t['chart_secondary']};">🌾 SDG Target 2.3: Doubling Agricultural Productivity of Smallholders</h4>
            <p style="margin:0; color:{t['text_muted']}; font-size:0.95rem;">
                Empowers marginal and small farmers (who represent over 80% of Indian landholdings) with NumPy-based normalized Z-Score yield benchmarking, 
                soil-crop vector matching, and precision agronomy to systematically lift per-acre output.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
    with col_a2:
        st.markdown(f"""
        <div class="about-card" style="border-left: 5px solid {t['accent_secondary']}; margin-bottom: 1.2rem;">
            <h4 style="margin:0 0 0.4rem 0; color:{t['accent_secondary']};">💧 SDG Target 2.4: Sustainable Agriculture & Climate Resilience</h4>
            <p style="margin:0; color:{t['text_muted']}; font-size:0.95rem;">
                Actively tracks water requirements, drought-tolerant millets, and sustainable micro-irrigation practices (drip and sprinkler systems) 
                to counter groundwater depletion and build climate resilience across agro-ecological zones.
            </p>
        </div>
        <div class="about-card" style="border-left: 5px solid {t['accent_primary']};">
            <h4 style="margin:0 0 0.4rem 0; color:{t['accent_primary']};">⚖️ SDG Target 2.c: Fair Agricultural Markets & Volatility Mitigation</h4>
            <p style="margin:0; color:{t['text_muted']}; font-size:0.95rem;">
                Provides transparent wholesale APMC Mandi modal price tracking compared directly against Government Minimum Support Price (MSP) benchmarks, 
                detecting inter-mandi price spreads and protecting farming households from distress sales.
            </p>
        </div>
        """, unsafe_allow_html=True)

    st.write("")
    
    st.subheader("🛠️ Technical Architecture & Computational Engine")
    st.markdown(f"""
    This system is built entirely in **Python**, utilizing three core scientific computing libraries:
    - **Streamlit ({st.__version__})**: High-visibility reactive web application with interactive tab routing, 5 selectable light themes, and real-time state management.
    - **Pandas ({pd.__version__})**: High-performance tabular data manipulation, filtering, aggregation, and export routines across 4 relational datasets.
    - **NumPy ({np.__version__})**: Advanced mathematical computing, parametric distribution fitting, Z-Score outlier detection, vector similarity matching, and Monte Carlo stochastic financial simulation.
    """)
    
    st.image(
        "https://images.unsplash.com/photo-1625246333195-78d9c38ad449?w=1600&auto=format&fit=crop&q=80",
        caption="Empowering Indian agriculture through modern scientific computing and data transparency",
        use_container_width=True
    )

# -------------------------------------------------------------
# TAB 2: FARMER DIRECTORY & LAND REGISTRY
# -------------------------------------------------------------
with tab_farmers:
    st.header("👨‍🌾 Farmer Directory & Land Registry")
    st.markdown("Search, filter, and inspect registered farmer profiles across Indian agricultural states.")
    
    col_f_filter1, col_f_filter2, col_f_filter3 = st.columns(3)
    with col_f_filter1:
        state_opts = ["All States"] + sorted(farmers_df['State'].unique().tolist())
        selected_state = st.selectbox("Filter by State", state_opts)
    with col_f_filter2:
        crop_opts = ["All Crops"] + sorted(farmers_df['Primary_Crop'].unique().tolist())
        selected_crop_filter = st.selectbox("Filter by Primary Crop", crop_opts)
    with col_f_filter3:
        search_query = st.text_input("🔍 Search by Farmer Name, ID, or Village", placeholder="e.g. Ramesh or F001")
        
    filtered_farmers = farmers_df.copy()
    if selected_state != "All States":
        filtered_farmers = filtered_farmers[filtered_farmers['State'] == selected_state]
    if selected_crop_filter != "All Crops":
        filtered_farmers = filtered_farmers[filtered_farmers['Primary_Crop'] == selected_crop_filter]
    if search_query:
        q = search_query.strip().lower()
        filtered_farmers = filtered_farmers[
            filtered_farmers['Name'].astype(str).str.lower().str.contains(q) |
            filtered_farmers['Farmer_ID'].astype(str).str.lower().str.contains(q) |
            filtered_farmers['Village'].astype(str).str.lower().str.contains(q)
        ]
        
    filtered_land = filtered_farmers['Land_Area_Acres'].to_numpy()
    f_total_land = np.sum(filtered_land) if len(filtered_land) > 0 else 0
    f_mean_land = np.mean(filtered_land) if len(filtered_land) > 0 else 0
    
    st.markdown(f"""
    **Showing {len(filtered_farmers):,} of {len(farmers_df):,} Farmers** | 
    **Total Filtered Land:** `{f_total_land:,.1f} Acres` | 
    **Mean Landholding:** `{f_mean_land:.2f} Acres`
    """)
    st.dataframe(filtered_farmers, use_container_width=True, height=450)
    
    csv_f = filtered_farmers.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Download Filtered Farmer CSV",
        data=csv_f,
        file_name="filtered_farmers_export.csv",
        mime="text/csv"
    )

# -------------------------------------------------------------
# TAB 3: CROP EXPLORER & AGRONOMIC INTELLIGENCE
# -------------------------------------------------------------
with tab_crops:
    st.header("🌱 Crop Explorer & Agronomic Intelligence")
    st.markdown("Select any crop to view its agronomic profile, verified cultivation photography, MSP rates, and growth specifications.")
    
    crop_list = sorted(crops_df['Crop_Name'].unique().tolist())
    selected_crop_name = st.selectbox(
        "🌾 Select Crop to Inspect:",
        crop_list,
        index=0
    )
    
    crop_row = crops_df[crops_df['Crop_Name'] == selected_crop_name].iloc[0]
    
    col_img, col_details = st.columns([1, 1.3], gap="large")
    
    with col_img:
        st.subheader(f"{crop_row.get('Icon', '🌱')} {crop_row['Crop_Name']} Photo")
        
        crop_id = crop_row.get('Crop_ID', '')
        local_path = os.path.join(IMG_DIR, f"crop_{crop_id}.jpg")
        
        unsplash_backups = {
            'C01': 'https://images.unsplash.com/photo-1536304993881-ff6e9eefa2a6?w=800&auto=format&fit=crop&q=80',
            'C02': 'https://images.unsplash.com/photo-1574323347407-f5e1ad6d020b?w=800&auto=format&fit=crop&q=80',
            'C03': 'https://images.unsplash.com/photo-1551754655-cd27e38d2076?w=800&auto=format&fit=crop&q=80',
            'C04': 'https://images.unsplash.com/photo-1605000797499-95a51c5269ae?w=800&auto=format&fit=crop&q=80',
            'C05': 'https://images.unsplash.com/photo-1594489428504-5c0c480a15fd?w=800&auto=format&fit=crop&q=80',
            'C06': 'https://images.unsplash.com/photo-1508746829417-e6f548d8d6ed?w=800&auto=format&fit=crop&q=80',
            'C07': 'https://images.unsplash.com/photo-1599940824399-b87987ceb72a?w=800&auto=format&fit=crop&q=80',
            'C08': 'https://images.unsplash.com/photo-1567401893414-76b7b1e5a7a5?w=800&auto=format&fit=crop&q=80',
            'C09': 'https://images.unsplash.com/photo-1515543237350-b3eea1ec8082?w=800&auto=format&fit=crop&q=80',
            'C10': 'https://images.unsplash.com/photo-1546069901-ba9599a7e63c?w=800&auto=format&fit=crop&q=80',
            'C11': 'https://images.unsplash.com/photo-1627920769842-6887c6df05ca?w=800&auto=format&fit=crop&q=80',
            'C12': 'https://images.unsplash.com/photo-1615485290382-441e4d049cb5?w=800&auto=format&fit=crop&q=80',
            'C13': 'https://images.unsplash.com/photo-1518977676601-b53f82aba655?w=800&auto=format&fit=crop&q=80',
            'C14': 'https://images.unsplash.com/photo-1592924357228-91a4daadcfea?w=800&auto=format&fit=crop&q=80',
            'C15': 'https://images.unsplash.com/photo-1618512496248-a07fe83aa8cb?w=800&auto=format&fit=crop&q=80',
            'C16': 'https://images.unsplash.com/photo-1543257580-7269da773bf5?w=800&auto=format&fit=crop&q=80',
            'C17': 'https://images.unsplash.com/photo-1597848212624-a19eb35e2651?w=800&auto=format&fit=crop&q=80',
            'C18': 'https://images.unsplash.com/photo-1588252303782-cb80119abd6d?w=800&auto=format&fit=crop&q=80',
        }
        
        if os.path.exists(local_path):
            st.image(local_path, caption=f"Cultivation of {crop_row['Crop_Name']} ({crop_row['Category']})", use_container_width=True)
        elif crop_id in unsplash_backups:
            st.image(unsplash_backups[crop_id], caption=f"{crop_row['Crop_Name']} (Online HD)", use_container_width=True)
        else:
            st.image("https://images.unsplash.com/photo-1592417817098-8f3d6eb22509?w=800", caption=f"{crop_row['Crop_Name']}", use_container_width=True)

    with col_details:
        st.subheader(f"Agronomic Profile: {crop_row['Crop_Name']}")
        st.markdown(f"*{crop_row.get('Description', 'Key Indian agricultural commodity.')}*")
        
        msp_val = crop_row.get('MSP_Per_Quintal', 0)
        
        col_spec1, col_spec2, col_spec3 = st.columns(3)
        with col_spec1:
            st.metric("Category", str(crop_row['Category']))
            st.metric("Water Need", str(crop_row['Water_Requirement']))
        with col_spec2:
            st.metric("Growing Season", str(crop_row['Season']))
            st.metric("Optimal Soil", str(crop_row['Optimal_Soil']))
        with col_spec3:
            st.metric("Govt MSP Rate", f"₹{int(msp_val):,}/Qtl")
            st.metric("Growth Period", f"{crop_row.get('Growth_Period_Days', '90-120')} Days")
            
        st.write("")
        col_c_sub1, col_c_sub2 = st.columns(2)
        with col_c_sub1:
            st.markdown(f"**🌡️ Ideal Temperature:** `{crop_row.get('Ideal_Temp_C', '20-30')} °C`")
        with col_c_sub2:
            st.markdown(f"**🌧️ Ideal Rainfall:** `{crop_row.get('Ideal_Rainfall_MM', '500-1000')} mm`")

    st.write("---")
    st.subheader("🖼️ All 18 Agricultural Crops Gallery")
    crop_cols = st.columns(6)
    for i, cname in enumerate(crop_list):
        col_idx = i % 6
        with crop_cols[col_idx]:
            icon = crops_df[crops_df['Crop_Name'] == cname]['Icon'].values[0] if 'Icon' in crops_df.columns else "🌱"
            st.markdown(f"**{icon} {cname}**")

    st.write("---")
    st.subheader("🧠 NumPy Vectorized Soil-Crop Match Recommender")
    st.markdown("Find the optimal crop varieties for any farm parcel using **NumPy weighted feature vector dot products** matching soil suitability, irrigation availability, and seasonality.")
    
    col_rec1, col_rec2, col_rec3 = st.columns(3)
    with col_rec1:
        rec_soil = st.selectbox("Parcel Soil Type:", ["Alluvial", "Black (Regur)", "Red", "Sandy Loam", "Clayey", "Loam"], index=0)
    with col_rec2:
        rec_water = st.selectbox("Water / Irrigation Capacity:", ["Low", "Medium", "High"], index=1)
    with col_rec3:
        rec_season = st.selectbox("Target Season:", ["Any", "Kharif", "Rabi", "Zaid"], index=0)
        
    water_levels = {'Low': 1, 'Medium': 2, 'High': 3}
    user_w = water_levels.get(rec_water, 2)
    weights = np.array([0.45, 0.30, 0.25])
    
    rec_results = []
    for _, r in crops_df.iterrows():
        soil_match = 1.0 if rec_soil.lower() in str(r['Optimal_Soil']).lower() else 0.4
        crop_w = water_levels.get(r['Water_Requirement'], 2)
        w_diff = abs(user_w - crop_w)
        w_score = 1.0 - (w_diff * 0.3)
        if rec_season == 'Any' or rec_season.lower() in str(r['Season']).lower():
            season_score = 1.0
        else:
            season_score = 0.3
            
        features = np.array([soil_match, w_score, season_score])
        match_pct = np.clip(np.sum(weights * features) * 100, 10.0, 99.5)
        rec_results.append({
            'Crop_Name': r['Crop_Name'],
            'Icon': r.get('Icon', '🌱'),
            'Category': r['Category'],
            'Season': r['Season'],
            'Water_Requirement': r['Water_Requirement'],
            'Optimal_Soil': r['Optimal_Soil'],
            'MSP_Per_Quintal': r.get('MSP_Per_Quintal', 0),
            'Match_Score': round(float(match_pct), 1)
        })
        
    rec_df = pd.DataFrame(rec_results).sort_values(by='Match_Score', ascending=False)
    
    st.markdown("#### 🌟 Top Recommended Crops:")
    top_c1, top_c2, top_c3 = st.columns(3)
    for idx, col in enumerate([top_c1, top_c2, top_c3]):
        if idx < len(rec_df):
            top_crop = rec_df.iloc[idx]
            with col:
                st.markdown(f"""
                <div class="metric-card" style="border-top: 4px solid {t['accent_primary']}; text-align:left;">
                    <div style="font-size:1.6rem; margin-bottom:0.2rem;">{top_crop['Icon']} <b>{top_crop['Crop_Name']}</b></div>
                    <div style="font-size:1.35rem; font-weight:900; color:{t['accent_primary']}; margin-bottom:0.4rem;">{top_crop['Match_Score']}% Compatibility</div>
                    <div style="font-size:0.85rem; color:{t['text_muted']};"><b>Category:</b> {top_crop['Category']}</div>
                    <div style="font-size:0.85rem; color:{t['text_muted']};"><b>Season:</b> {top_crop['Season']}</div>
                    <div style="font-size:0.85rem; color:{t['text_muted']};"><b>Govt MSP:</b> ₹{int(top_crop['MSP_Per_Quintal']):,}/Qtl</div>
                </div>
                """, unsafe_allow_html=True)
                
    st.write("")
    st.dataframe(rec_df[['Crop_Name', 'Category', 'Season', 'Water_Requirement', 'Optimal_Soil', 'MSP_Per_Quintal', 'Match_Score']], use_container_width=True)

# -------------------------------------------------------------
# TAB 4: NUMPY YIELD ANALYTICS & STATISTICAL Z-SCORES
# -------------------------------------------------------------
with tab_analytics:
    st.header("📊 NumPy Statistical Agronomic Engine")
    st.markdown("Advanced quantitative analysis powered by **NumPy mathematical routines**: parametric distributions, fitted normal curves, and normalized Z-Score outlier detection.")
    
    crop_names = ["All Crops"] + sorted(production_df['Crop_Name'].unique().tolist())
    selected_analytics_crop = st.selectbox("Select Crop for NumPy Statistical Decomposition:", crop_names)
    
    if selected_analytics_crop == "All Crops":
        target_prod_df = production_df.copy()
    else:
        target_prod_df = production_df[production_df['Crop_Name'] == selected_analytics_crop].copy()
        
    yields = target_prod_df['Yield_T_Per_Acre'].to_numpy()
    
    if len(yields) > 0:
        y_mean = np.mean(yields)
        y_median = np.median(yields)
        y_std = np.std(yields)
        y_var = np.var(yields)
        y_ptp = np.ptp(yields)
        p25, p50, p75, p90, p95 = np.percentile(yields, [25, 50, 75, 90, 95])
        cv_percent = (y_std / y_mean) * 100 if y_mean > 0 else 0
        
        stat_c1, stat_c2, stat_c3, stat_c4 = st.columns(4)
        with stat_c1:
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-label">Mean ± Std Dev</div>
                <div class="metric-value">{y_mean:.2f} <span style="font-size:1.1rem;">± {y_std:.2f}</span></div>
                <div class="metric-sub">Variance (σ²): {y_var:.2f}</div>
            </div>
            """, unsafe_allow_html=True)
            
        with stat_c2:
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-label">Median & Quartiles</div>
                <div class="metric-value">{y_median:.2f} <span style="font-size:1.1rem;">T/Ac</span></div>
                <div class="metric-sub">P25: {p25:.2f} | P75: {p75:.2f}</div>
            </div>
            """, unsafe_allow_html=True)
            
        with stat_c3:
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-label">Yield Volatility (CV%)</div>
                <div class="metric-value">{cv_percent:.1f}%</div>
                <div class="metric-sub">Range (PTP): {y_ptp:.2f} T/Ac</div>
            </div>
            """, unsafe_allow_html=True)
            
        with stat_c4:
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-label">90th Percentile (Elite)</div>
                <div class="metric-value">{p90:.2f} <span style="font-size:1.1rem;">T/Ac</span></div>
                <div class="metric-sub">Top 5% Benchmark: {p95:.2f}</div>
            </div>
            """, unsafe_allow_html=True)
            
        st.write("")
        
        col_fig_dist, col_fig_z = st.columns(2)
        with col_fig_dist:
            st.subheader(f"Yield Distribution & Gaussian Fit ({selected_analytics_crop})")
            fig_dist = px.histogram(
                target_prod_df,
                x='Yield_T_Per_Acre',
                nbins=25,
                marginal="box",
                template="plotly_white",
                color_discrete_sequence=[t['chart_primary']],
                labels={'Yield_T_Per_Acre': 'Yield (Tonnes / Acre)'}
            )
            
            x_range = np.linspace(np.min(yields) * 0.8, np.max(yields) * 1.1, 200)
            if y_std > 0:
                gaussian_pdf = (1 / (y_std * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x_range - y_mean) / y_std) ** 2)
                bin_width = (np.max(yields) - np.min(yields)) / 25 if len(yields) > 1 else 1
                scaled_curve = gaussian_pdf * len(yields) * bin_width
                fig_dist.add_trace(go.Scatter(
                    x=x_range,
                    y=scaled_curve,
                    mode='lines',
                    name='NumPy Gaussian Fit',
                    line=dict(color=t['chart_secondary'], width=3, dash='solid')
                ))
                
            fig_dist.update_layout(
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                margin=dict(t=30, b=20, l=20, r=20),
                legend=dict(orientation="h", y=1.1, x=0.5, xanchor="center")
            )
            st.plotly_chart(fig_dist, use_container_width=True)
            
        with col_fig_z:
            st.subheader("Farmer Yield Z-Score Benchmark Rating")
            prod_merged = production_df.merge(
                farmers_df[['Farmer_ID', 'Name', 'State', 'Soil_Type', 'Irrigation_Type']],
                on='Farmer_ID',
                how='left'
            )
            
            crop_means = prod_merged.groupby('Crop_Name')['Yield_T_Per_Acre'].transform(lambda s: np.mean(s.to_numpy()))
            crop_stds = prod_merged.groupby('Crop_Name')['Yield_T_Per_Acre'].transform(lambda s: np.std(s.to_numpy()))
            prod_merged['Z_Score'] = (prod_merged['Yield_T_Per_Acre'] - crop_means) / np.where(crop_stds > 0, crop_stds, 1.0)
            
            conditions = [
                prod_merged['Z_Score'] > 1.0,
                prod_merged['Z_Score'] < -1.0
            ]
            choices = ["🌟 High Performer (Z > 1.0)", "⚠️ Underperforming (Z < -1.0)"]
            prod_merged['Performance_Tier'] = np.select(conditions, choices, default="✅ On Benchmark (-1.0 to 1.0)")
            
            tier_counts = prod_merged['Performance_Tier'].value_counts().reset_index()
            tier_counts.columns = ['Tier', 'Farmer_Count']
            
            fig_z = px.pie(
                tier_counts,
                names='Tier',
                values='Farmer_Count',
                hole=0.45,
                template="plotly_white",
                color='Tier',
                color_discrete_map={
                    "🌟 High Performer (Z > 1.0)": t['accent_primary'],
                    "✅ On Benchmark (-1.0 to 1.0)": t['chart_secondary'],
                    "⚠️ Underperforming (Z < -1.0)": "#dc2626"
                }
            )
            fig_z.update_layout(
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                margin=dict(t=30, b=20, l=20, r=20),
                legend=dict(orientation="h", y=-0.1)
            )
            st.plotly_chart(fig_z, use_container_width=True)
            
        st.write("---")
        st.subheader("🎯 Prioritized Extension Farms (Z < -1.0 Outliers)")
        underperforming_farmers = prod_merged[prod_merged['Z_Score'] < -1.0][
            ['Farmer_ID', 'Name', 'State', 'Crop_Name', 'Yield_T_Per_Acre', 'Z_Score', 'Soil_Type', 'Irrigation_Type']
        ].sort_values(by='Z_Score')
        
        st.markdown(f"**Identified {len(underperforming_farmers)} farm operations currently producing > 1 standard deviation below their crop median.** These operations should be prioritized for soil health cards and subsidized micro-irrigation:")
        st.dataframe(underperforming_farmers, use_container_width=True, height=260)
        
    st.write("---")
    col_g1, col_g2 = st.columns(2)
    with col_g1:
        st.subheader("Dominant Soil Types Across India")
        soil_df = farmers_df['Soil_Type'].value_counts().reset_index()
        soil_df.columns = ['Soil_Type', 'Count']
        fig_soil = px.bar(
            soil_df,
            x='Soil_Type',
            y='Count',
            color='Soil_Type',
            template="plotly_white",
            color_discrete_sequence=px.colors.qualitative.Prism
        )
        fig_soil.update_layout(showlegend=False, paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig_soil, use_container_width=True)
        
    with col_g2:
        st.subheader("Irrigation Method Adoption")
        irrig_df = farmers_df['Irrigation_Type'].value_counts().reset_index()
        irrig_df.columns = ['Irrigation_Type', 'Count']
        fig_irrig = px.pie(
            irrig_df,
            values='Count',
            names='Irrigation_Type',
            hole=0.45,
            template="plotly_white",
            color_discrete_sequence=[t['accent_primary'], t['chart_secondary'], '#f59e0b', '#7c3aed', '#ec4899']
        )
        fig_irrig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig_irrig, use_container_width=True)

# -------------------------------------------------------------
# TAB 5: NUMPY MONTE CARLO HARVEST & REVENUE SIMULATOR
# -------------------------------------------------------------
with tab_simulator:
    st.header("🎲 NumPy Monte Carlo Harvest & Revenue Risk Simulator")
    st.markdown("""
    This quantitative simulation engine leverages **NumPy's vectorized pseudo-random number generator** (`np.random.normal`) to model 
    **1,000 synthetic harvest outcomes**, factoring in yield variance, climate risk, price volatility, and cultivation expenses.
    """)
    
    sim_col1, sim_col2 = st.columns([1, 2], gap="large")
    
    with sim_col1:
        st.subheader("⚙️ Simulation Parameters")
        sim_crop = st.selectbox("Select Target Crop:", sorted(crops_df['Crop_Name'].unique().tolist()), key="sim_crop")
        
        crop_p = production_df[production_df['Crop_Name'] == sim_crop]
        if not crop_p.empty:
            crop_yield_vals = crop_p['Yield_T_Per_Acre'].to_numpy()
            default_mean_yield = float(np.mean(crop_yield_vals))
            default_std_yield = float(np.std(crop_yield_vals)) if np.std(crop_yield_vals) > 0 else 0.4
        else:
            default_mean_yield = 3.5
            default_std_yield = 0.5
            
        crop_m = markets_df[markets_df['Crop_Name'] == sim_crop]
        if not crop_m.empty:
            crop_price_vals = crop_m['Modal_Price_Rs_Qtl'].to_numpy()
            default_base_price = float(np.mean(crop_price_vals))
            default_std_price = float(np.std(crop_price_vals)) if np.std(crop_price_vals) > 0 else 120.0
        else:
            default_base_price = 2200.0
            default_std_price = 150.0
            
        sim_acres = st.slider("Cultivated Farm Area (Acres):", min_value=1.0, max_value=50.0, value=5.0, step=0.5)
        sim_cost_per_acre = st.number_input("Estimated Cost of Cultivation (₹/Acre):", min_value=5000, max_value=150000, value=25000, step=1000)
        
        climate_risk = st.radio(
            "Climate / Weather Scenario:",
            ["Normal Seasonal Conditions (±1σ)", "Favorable Monsoon (+15% Yield)", "Drought / Monsoon Deficit (-25% Yield)", "Extreme Volatility (±2.5σ)"]
        )
        
        n_trials = st.select_slider("Number of Monte Carlo Trials:", options=[500, 1000, 2000, 5000], value=1000)
        
    with sim_col2:
        st.subheader("📈 Simulated Probabilistic Financial Distribution")
        
        yield_multiplier = 1.0
        std_multiplier = 1.0
        if "Favorable" in climate_risk:
            yield_multiplier = 1.15
        elif "Drought" in climate_risk:
            yield_multiplier = 0.75
            std_multiplier = 1.5
        elif "Extreme" in climate_risk:
            std_multiplier = 2.5
            
        np.random.seed(42)
        simulated_yields = np.clip(
            np.random.normal(loc=default_mean_yield * yield_multiplier, scale=default_std_yield * std_multiplier, size=n_trials),
            a_min=0.1, a_max=None
        )
        simulated_prices = np.clip(
            np.random.normal(loc=default_base_price, scale=default_std_price, size=n_trials),
            a_min=500.0, a_max=None
        )
        
        simulated_production = simulated_yields * sim_acres
        simulated_revenue = simulated_production * (simulated_prices * 10)
        total_cost = sim_acres * sim_cost_per_acre
        simulated_net_profit = simulated_revenue - total_cost
        simulated_roi = (simulated_net_profit / total_cost) * 100
        
        p5_profit, p25_profit, p50_profit, p75_profit, p95_profit = np.percentile(
            simulated_net_profit, [5, 25, 50, 75, 95]
        )
        prob_positive = np.mean(simulated_net_profit > 0) * 100
        mean_roi = np.mean(simulated_roi)
        
        mc1, mc2, mc3, mc4 = st.columns(4)
        with mc1:
            st.metric("Expected Median Profit", f"₹{int(p50_profit):,}")
        with mc2:
            st.metric("5% Value-at-Risk (VaR)", f"₹{int(p5_profit):,}")
        with mc3:
            st.metric("95% Upside Target", f"₹{int(p95_profit):,}")
        with mc4:
            st.metric("Probability of Profit", f"{prob_positive:.1f}%")
            
        sim_df = pd.DataFrame({'Net_Profit_Rs': simulated_net_profit, 'ROI_Percent': simulated_roi})
        fig_mc = px.histogram(
            sim_df,
            x='Net_Profit_Rs',
            nbins=35,
            template="plotly_white",
            color_discrete_sequence=[t['chart_primary']],
            labels={'Net_Profit_Rs': 'Simulated Net Profit (₹)'}
        )
        
        fig_mc.add_vline(x=0, line_width=2, line_dash="dash", line_color="#dc2626", annotation_text="Breakeven (₹0)")
        fig_mc.add_vline(x=p50_profit, line_width=2, line_dash="solid", line_color=t['chart_secondary'], annotation_text=f"Median: ₹{int(p50_profit):,}")
        
        fig_mc.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            margin=dict(t=25, b=20, l=20, r=20)
        )
        st.plotly_chart(fig_mc, use_container_width=True)
        
        st.caption(f"Based on **{n_trials:,} iterations** using NumPy Gaussian sampling. 90% confidence interval for net profit: **₹{int(p5_profit):,}** to **₹{int(p95_profit):,}**. Average expected ROI: **{mean_roi:.1f}%**.")

# -------------------------------------------------------------
# TAB 6: APMC MANDI & ARBITRAGE TRACKER
# -------------------------------------------------------------
with tab_mandi:
    st.header("💰 APMC Mandi Market Intelligence & Arbitrage")
    st.markdown("Real-time modal wholesale rates compared against Government Minimum Support Price (MSP) benchmarks, with inter-mandi price spread analysis.")
    
    if not markets_df.empty:
        modal_col = 'Modal_Price_Rs_Qtl' if 'Modal_Price_Rs_Qtl' in markets_df.columns else markets_df.columns[3]
        msp_col = 'MSP_Rs_Qtl' if 'MSP_Rs_Qtl' in markets_df.columns else markets_df.columns[5]
        
        mandi_groups = markets_df.groupby('Crop_Name')
        crop_names_m = []
        modal_means = []
        msp_vals = []
        price_ptps = []
        price_stds = []
        
        for cname, grp in mandi_groups:
            p_arr = grp[modal_col].to_numpy()
            msp_v = grp[msp_col].values[0] if len(grp[msp_col]) > 0 else 0
            crop_names_m.append(cname)
            modal_means.append(np.mean(p_arr))
            msp_vals.append(msp_v)
            price_ptps.append(np.ptp(p_arr))
            price_stds.append(np.std(p_arr))
            
        spread_summary = pd.DataFrame({
            'Crop_Name': crop_names_m,
            'Mean_Modal_Price': modal_means,
            'MSP_Benchmark': msp_vals,
            'Price_Spread_PTP': price_ptps,
            'Price_Std_Dev': price_stds
        }).sort_values(by='Price_Spread_PTP', ascending=False)
        
        fig_mandi = go.Figure()
        fig_mandi.add_trace(go.Bar(
            x=spread_summary['Crop_Name'],
            y=spread_summary['Mean_Modal_Price'],
            name='Wholesale Modal Price (₹/Qtl)',
            marker_color=t['chart_primary']
        ))
        fig_mandi.add_trace(go.Bar(
            x=spread_summary['Crop_Name'],
            y=spread_summary['MSP_Benchmark'],
            name='Govt MSP Benchmark (₹/Qtl)',
            marker_color=t['chart_secondary']
        ))
        fig_mandi.update_layout(
            barmode='group',
            template="plotly_white",
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
            xaxis_title="Crop Name",
            yaxis_title="Rate (₹ per Quintal)",
            margin=dict(t=40, b=20, l=20, r=20)
        )
        st.plotly_chart(fig_mandi, use_container_width=True)
        
        st.subheader("Inter-Mandi Arbitrage & Price Volatility Matrix")
        st.dataframe(spread_summary, use_container_width=True, height=300)
        
    st.subheader("Raw Mandi Rates Records")
    st.dataframe(markets_df, use_container_width=True, height=350)

# -------------------------------------------------------------
# TAB 7: AGRICULTURAL GIS MAP
# -------------------------------------------------------------
with tab_gis:
    st.header("🗺️ Nationwide Agricultural GIS Belt Map")
    st.markdown("Geospatial distribution of registered farming clusters across Indian agricultural belts.")
    
    state_coords = {
        'Punjab': [30.9010, 75.8573], 'Haryana': [29.6857, 76.9905], 
        'Uttar Pradesh': [26.8467, 80.9462], 'Andhra Pradesh': [16.3067, 80.4365],
        'Telangana': [17.9689, 79.5941], 'Maharashtra': [19.9975, 73.7898],
        'Madhya Pradesh': [22.7196, 75.8577], 'Karnataka': [15.3647, 75.1240],
        'Tamil Nadu': [10.7870, 79.1378], 'Gujarat': [22.3039, 70.8022],
        'Rajasthan': [27.0238, 74.2179], 'West Bengal': [23.2324, 87.8615],
        'Bihar': [25.5941, 85.1376], 'Odisha': [21.4669, 83.9756]
    }
    
    m = folium.Map(location=[22.5, 79.0], zoom_start=5, tiles="OpenStreetMap")
    
    state_counts = farmers_df['State'].value_counts()
    for state, count in state_counts.items():
        if state in state_coords:
            folium.CircleMarker(
                location=state_coords[state],
                radius=max(8, min(25, int(count * 0.75))),
                popup=f"<b>{state}</b><br>Registered Farmers: {count}",
                tooltip=f"{state}: {count} Farmers",
                color=t['accent_primary'],
                fill=True,
                fill_color=t['accent_primary'],
                fill_opacity=0.75
            ).add_to(m)
            
    st_folium(m, width=1200, height=520)

# -------------------------------------------------------------
# TAB 8: RAW DATASETS & EXPORTER
# -------------------------------------------------------------
with tab_data:
    st.header("📁 Raw Agricultural Datasets")
    st.markdown("Browse, inspect, and export all backing tabular datasets.")
    
    data_sel = st.radio(
        "Select Dataset to Inspect:",
        ["👨‍🌾 Farmer Profiles", "🌱 Crop Varieties", "⚖️ Production Statistics", "💰 APMC Mandi Rates"],
        horizontal=True
    )
    
    if data_sel == "👨‍🌾 Farmer Profiles":
        st.dataframe(farmers_df, use_container_width=True)
        st.download_button("📥 Export Farmer CSV", farmers_df.to_csv(index=False), "farmer_data.csv", "text/csv")
    elif data_sel == "🌱 Crop Varieties":
        st.dataframe(crops_df, use_container_width=True)
        st.download_button("📥 Export Crop CSV", crops_df.to_csv(index=False), "crop_data.csv", "text/csv")
    elif data_sel == "⚖️ Production Statistics":
        st.dataframe(production_df, use_container_width=True)
        st.download_button("📥 Export Production CSV", production_df.to_csv(index=False), "production_data.csv", "text/csv")
    elif data_sel == "💰 APMC Mandi Rates":
        st.dataframe(markets_df, use_container_width=True)
        st.download_button("📥 Export Mandi CSV", markets_df.to_csv(index=False), "market_data.csv", "text/csv")
