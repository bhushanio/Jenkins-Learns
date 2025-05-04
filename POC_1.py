import webbrowser
import os

# Define the HTML file path
html_file = "hacked_prank_fixed.html"

# Open the HTML file in the default browser
file_url = f"file://{os.path.abspath(html_file)}"
webbrowser.open(file_url)