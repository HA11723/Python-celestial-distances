# 🌍 Planetary Distances Calculator

This Python project calculates the distance between two planets in the Solar System at given times, based on their orbital radii and periods. It is designed to simulate how the distance between any two planets changes over time as they orbit the sun.

## 🚀 Features

- Computes planet-to-planet distance over time using orbital mechanics
- Supports all 9 classical planets including Pluto
- Returns results in kilometers
- Implements both input validation and test cases
- Uses Cartesian coordinate conversion from polar orbits

## 📐 How It Works

Each planet is represented by:
- `orbital_radius` — average distance from the sun (in km)
- `orbital_period` — time to complete one orbit (in seconds)

Using these, the position of a planet at a given time `t` is calculated using:

theta = 2π * t / orbital_period
x = radius * cos(theta)
y = radius * sin(theta)

git clone https://github.com/your-username/planetary-distances.git
cd planetary-distances

python3 worksheet9.py

