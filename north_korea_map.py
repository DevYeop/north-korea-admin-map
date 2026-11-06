import json
from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st


st.set_page_config(page_title="북한 행정구역 지도")
st.title("북한 행정구역 지도")

boundary_file = Path(__file__).with_name("geoBoundaries-PRK-ADM2_simplified.geojson")
try:
    geojson = json.loads(boundary_file.read_text(encoding="utf-8"))
except (OSError, ValueError):
    st.error(f"경계 데이터를 읽을 수 없습니다. 앱 폴더의 {boundary_file.name} 파일을 확인해 주세요.")
    st.stop()

# 경계는 고유 ID로 연결하고, 지도에 표시할 이름은 원본 지명을 사용합니다.
regions = pd.DataFrame(feature["properties"] for feature in geojson["features"])
st.caption(f"2019년 기준 시·군급 행정구역 {len(regions)}개 · 마우스를 올리면 지명이 표시됩니다.")

fig = px.choropleth_map(
    regions,
    geojson=geojson,
    locations="shapeID",
    featureidkey="properties.shapeID",
    hover_name="shapeName",
    color_discrete_sequence=["#397BB5"],
    map_style="white-bg",
    center={"lat": 40.4, "lon": 127.4},
    zoom=5.25,
    opacity=1,
    height=510,
)
fig.update_traces(
    hovertemplate="%{hovertext}<extra></extra>",
    marker_line_color="#EAF4FF",
    marker_line_width=0.7,
)
fig.update_layout(showlegend=False, margin=dict(l=0, r=0, t=0, b=0))
st.plotly_chart(fig, width="stretch", alt=f"북한 시·군급 행정구역 {len(regions)}개의 경계 지도")
st.caption(
    "경계 출처 [geoBoundaries](https://www.geoboundaries.org/) · "
    "[World Food Programme, OCHA ROAP](https://data.humdata.org/dataset/dpr-korea-administrative-boundaries) · "
    "CC BY 3.0 IGO"
)
