from pathlib import Path

def resume_page():
    return Path("resume.html").read_text()

app.route("/resume", "GET", resume_page)
