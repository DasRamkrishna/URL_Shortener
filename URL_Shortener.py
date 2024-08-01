# Install the library ( pip install pyshorteners )

import pyshorteners

long_url = input("Enter the long URL: ").strip()
short_url = pyshorteners.Shortener().tinyurl.short(long_url)
print(f" The Short URL: {short_url}")
