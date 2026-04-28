from rich.syntax import Syntax

# -----------------------------
# LANGUAGE DETECTION
# -----------------------------

def detect_lang(code):
    if "<html" in code or "<!DOCTYPE" in code:
        return "html"
    elif "function" in code or "console.log" in code:
        return "javascript"
    elif "import" in code or "def " in code:
        return "python"
    return "python"

# -----------------------------
# SYNTAX HIGHLIGHT
# -----------------------------

def highlight(code):
    lang = detect_lang(code)
    return Syntax(code, lang, theme="monokai", line_numbers=True)
