import streamlit as st
import math
import matplotlib.pyplot as plt

st.title("💧 Pipe Flow Velocity Visualization")
st.markdown("This app calculates and plots **flow velocity vs. pipe diameter** for a given flow rate.")

# --- User input section ---
st.sidebar.header("Input Parameters")
flow_rate_m3h = st.sidebar.number_input("Flow rate (m³/h)", min_value=0.01, max_value=10000.0, value=20.0, step=1.0)
min_diameter = st.sidebar.number_input("Min diameter (m)", min_value=0.005, max_value=1.0, value=0.01, step=0.005)
max_diameter = st.sidebar.number_input("Max diameter (m)", min_value=0.01, max_value=2.0, value=0.20, step=0.01)

# --- Core calculations ---
flow_rate = flow_rate_m3h / 3600.0  # Convert to m³/s

diameters = [i / 1000 for i in range(int(min_diameter * 1000), int(max_diameter * 1000) + 1, 5)]
velocities = [flow_rate / (math.pi * (d ** 2) / 4.0) for d in diameters]

# --- Display results ---
st.write(f"**Flow rate:** {flow_rate_m3h:.2f} m³/h = {flow_rate:.6f} m³/s")
st.write(f"**Diameter range:** {min_diameter:.3f} m → {max_diameter:.3f} m")

# --- Plot ---
fig, ax = plt.subplots()
ax.plot(diameters, velocities, marker="o")
ax.set_xlabel("Pipe Diameter (m)")
ax.set_ylabel("Velocity (m/s)")
ax.set_title("Flow Velocity vs. Pipe Diameter")
ax.grid(True)
st.pyplot(fig)
# --- Stripe Pay Button ---
stripe_link = "https://donate.stripe.com/00w4gz8Lhbal4DK0T58AE00"   # ← 换成你的 Payment Link

st.markdown(
    f"""
    <div style="margin:20px 0;padding:15px;border:1px solid #ccc;border-radius:10px;">
        <h3>支持我的项目 / Buy Me a Coffee ☕</h3>
        <a href="{stripe_link}" target="_blank">
            <button style="
                background-color:#4CAF50;
                color:white;
                padding:10px 20px;
                border:none;
                border-radius:8px;
                cursor:pointer;
                font-size:16px;">
                支持我 $1
            </button>
        </a>
    </div>
    """,
    unsafe_allow_html=True
)

