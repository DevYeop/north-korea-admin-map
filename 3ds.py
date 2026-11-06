import streamlit as st
import numpy as np
import plotly.graph_objects as go

st.title("3D 벡터 궤적 시각화")

# 가상의 3차원 궤적 데이터 생성
t = np.linspace(0, 10 * np.pi, 300)

x = np.cos(t) * (1 + t * 0.03)
y = np.sin(t) * (1 + t * 0.03)
z = t * 0.1

# 3D 그래프 생성
fig = go.Figure()

fig.add_trace(go.Scatter3d(
    x=x,
    y=y,
    z=z,
    mode="lines+markers",  # 선 + 점
    line=dict(
        color=t,
        colorscale="Viridis",
        width=5
    ),
    marker=dict(
        size=3,
        color=t,
        colorscale="Viridis"
    ),
    name="Vector Trajectory"
))

fig.update_layout(
    title="3D Vector Trajectory",
    scene=dict(
        xaxis_title="X",
        yaxis_title="Y",
        zaxis_title="Z"
    ),
    height=650
)

st.plotly_chart(fig, use_container_width=True)
