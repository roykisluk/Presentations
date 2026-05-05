import re

with open("GIV/Presentation/test_presentation.tex", "r") as f:
    content = f.read()

# Fix \begin{frame} \label{...}
content = re.sub(r'\\begin\{frame\}\s*\\label\{([^}]+)\}', r'\\begin{frame}[label=\1]', content)

# Fix \begin{frame}[shrink] \label{...}
content = re.sub(r'\\begin\{frame\}\[shrink\]\s*\\label\{([^}]+)\}', r'\\begin{frame}[shrink, label=\1]', content)

# Fix \begin{frame}[shrink]{...} \label{...}
content = re.sub(r'\\begin\{frame\}\[shrink\]\{([^}]+)\}\s*\\label\{([^}]+)\}', r'\\begin{frame}[shrink, label=\2]{\1}', content)

# Fix \begin{frame}{...}\n    \label{...}
content = re.sub(r'\\begin\{frame\}\{([^}]+)\}\s*\\label\{([^}]+)\}', r'\\begin{frame}[label=\2]{\1}', content)

# Fix \begin{frame}[shrink]\n    \label{...}
content = re.sub(r'\\begin\{frame\}\[shrink\]\s*\\label\{([^}]+)\}', r'\\begin{frame}[shrink, label=\1]', content)

with open("GIV/Presentation/test_presentation.tex", "w") as f:
    f.write(content)
