import streamlit as st
import numpy as np
import plotly.graph_objects as go

st.title("3D 폭죽 분산 궤적")

# 시간
t = np.linspace(0, 3, 50)

# 폭죽이 터지는 위치
x0, y0, z0 = 0, 0, 10

# 각 파티클의 초기 이동 방향 (시각화용 임의 값)
directions = [
    (2.0, 1.5, 3.0),
    (-1.8, 2.0, 2.5),
    (0.8, -2.0, 3.5)
]

colors = ["red", "orange", "blue"]

fig = go.Figure()

for i, (vx, vy, vz) in enumerate(directions):

    # 폭죽처럼 퍼졌다가 아래로 떨어지는 궤적
    x = x0 + vx * t
    y = y0 + vy * t
    z = z0 + vz * t - 2.5 * t**2

    fig.add_trace(go.Scatter3d(
        x=x,
        y=y,
        z=z,
        mode="lines+markers",
        name=f"파티클 {i+1}",
        line=dict(
            color=colors[i],
            width=6
        ),
        marker=dict(
            size=3,
            color=colors[i]
        )
    ))

# 폭발 시작점
fig.add_trace(go.Scatter3d(
    x=[x0],
    y=[y0],
    z=[z0],
    mode="markers",
    name="폭죽 폭발 지점",
    marker=dict(
        size=10,
        color="yellow",
        symbol="diamond"
    )
))

fig.update_layout(
    scene=dict(
        xaxis_title="X",
        yaxis_title="Y",
        zaxis_title="높이",
        aspectmode="data"
    ),
    height=650
)

st.plotly_chart(fig, use_container_width=True)
