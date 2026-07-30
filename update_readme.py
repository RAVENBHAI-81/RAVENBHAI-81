from datetime import datetime, timezone, timedelta
import re

# Bangladesh timezone (UTC+6)
BD_TZ = timezone(timedelta(hours=6))
now = datetime.now(BD_TZ)

# Format time nicely
time_str = now.strftime("%B %d, %Y — %I:%M %p (BD)")

# Days since you started coding — set your start date here
start_date = datetime(2023, 10, 1, tzinfo=BD_TZ)
days_coding = (now - start_date).days

# Rotating quotes — add your own if you want!
quotes = [
    "Build it. Break it. Fix it. Repeat.",
    "Code is the closest thing to magic in the real world.",
    "The best tool is the one you built yourself.",
    "Automate the boring. Focus on what matters.",
    "Every expert was once a beginner with a terminal open.",
    "Clean code is not written by following rules. It is written by someone who cares.",
    "If it can be scripted, it should be scripted.",
    "Ship it, then improve it.",
    "The quieter you become, the more you can hear the bugs.",
    "Real devs debug at midnight.",
]

# Pick quote based on day of year so it changes daily
quote = quotes[now.timetuple().tm_yday % len(quotes)]

# Build the new live block
live_block = f"""<!-- LIVE_START -->
> 🕐 **Last Updated:** `{time_str}`
>
> 💡 **Quote:** *{quote}*
>
> 📅 **Days Coding:** `{days_coding} days and counting`
<!-- LIVE_END -->"""

# Read README
with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()

# Replace between markers
new_content = re.sub(
    r"<!-- LIVE_START -->.*?<!-- LIVE_END -->",
    live_block,
    content,
    flags=re.DOTALL
)

# Write back
with open("README.md", "w", encoding="utf-8") as f:
    f.write(new_content)

print(f"✅ Updated! Time: {time_str} | Days: {days_coding} | Quote: {quote}")
