# Smart-CLI-Dashboard-
🌍 CLI Country & Weather Dashboard
Python Winter Sprint 2026 - Advanced Project Track
Welcome to the CLI Country & Weather Dashboard! This is a backend-style Python application that integrates real-world data from multiple public APIs to provide a seamless terminal-based information hub.

🚀 The Challenge
The goal of this project was to build a functional, error-resistant dashboard that handles real-time API integration. It focuses on core backend skills: modular programming, JSON parsing, and external library management.
Key Features
Real-time Country Data: Fetches capital, region, and coordinates.
Live Weather Updates: Retrieves current temperature and wind speed based on geographical coordinates.
Interactive CLI: A user-friendly loop-based menu system.
Clean Output: Formatted terminal data (no messy JSON prints!).

📊 How It Works
The application is built using a modular approach to ensure clean, maintainable code:
fetch_country_data(country_name): Calls the REST Countries API to get the country's capital and coordinates (latitude & longitude).
fetch_weather_data(lat, lon): Uses the coordinates from the first function to get live weather from Open-Meteo.
The Dashboard Menu: A while loop that keeps the program running until the user chooses to exit.

💡 What I Learned
During this sprint, I sharpened my skills in:
API Integration: Handling GET requests and status codes.
Data Extraction: Navigating complex nested JSON objects.
Input Handling: Creating a robust user interface that doesn't crash on invalid inputs.
Created during the Python Winter Sprint 2026. Focus on understanding, not just speed. 🚀
