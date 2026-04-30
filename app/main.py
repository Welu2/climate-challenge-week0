import streamlit as st
import plotly.express as px
from utils import load_all_data

# Page Config
st.set_page_config(page_title="COP32 | Africa Climate Dashboard", layout="wide")

# Dark Theme CSS
st.markdown("""
<style>
.stApp { background-color: #0e1117; color: white; }
[data-testid="stMetric"] {
    background-color: #000;
    border: 1px solid #333;
    padding: 15px;
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

# Title
st.title("🌍 African Climate Vulnerability Dashboard")
st.markdown("---")

# Load Data
with st.spinner("Loading data..."):
    df = load_all_data()

if df.empty:
    st.error("No data loaded. Check Drive or local files.")
    st.stop()

# --- SIDEBAR ---
st.sidebar.header("🎛️ Controls")

countries = sorted(df["Country"].unique())
selected_countries = st.sidebar.multiselect(
    "Select Countries",
    countries,
    default=countries
)

min_year, max_year = int(df["Year"].min()), int(df["Year"].max())
year_range = st.sidebar.slider("Year Range", min_year, max_year, (min_year, max_year))

# Variable selector (for exploration)
variable = st.sidebar.selectbox(
    "Extra Variable",
    ["T2M", "PRECTOTCORR", "RH2M"]
)

# Filter
filtered_df = df[
    (df["Country"].isin(selected_countries)) &
    (df["Year"].between(year_range[0], year_range[1]))
]

if filtered_df.empty:
    st.warning("No data for selected filters")
    st.stop()

# --- KPIs ---
m1, m2, m3, m4 = st.columns(4)
m1.metric("Avg Temp", f"{filtered_df['T2M'].mean():.2f}")
m2.metric("Max Temp", f"{filtered_df['T2M'].max():.2f}")
m3.metric("Countries", len(selected_countries))
m4.metric("Records", len(filtered_df))

st.markdown("### 📈 Analysis")

col1, col2 = st.columns(2)

# ✅ REQUIRED: Temperature Trend
with col1:
    fig_temp = px.line(
        filtered_df,
        x="Date",
        y="T2M",
        color="Country",
        title="🌡️ Temperature Trend (T2M)",
        template="plotly_dark"
    )
    st.plotly_chart(fig_temp, use_container_width=True)

# ✅ REQUIRED: Precipitation Boxplot
with col2:
    fig_precip = px.box(
        filtered_df,
        x="Country",
        y="PRECTOTCORR",
        color="Country",
        title="🌧️ Precipitation Distribution",
        template="plotly_dark"
    )
    st.plotly_chart(fig_precip, use_container_width=True)

# Extra exploration
st.markdown(f"### 🔍 Exploring: {variable}")
fig_extra = px.line(
    filtered_df,
    x="Date",
    y=variable,
    color="Country",
    template="plotly_dark"
)
st.plotly_chart(fig_extra, use_container_width=True)

# Stats
with st.expander("📊 Statistics"):
    st.dataframe(filtered_df.groupby("Country")[variable].describe().round(2))