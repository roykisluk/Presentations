# Presentation Tools Workflow

This repository is an AI-powered factory for creating beautiful, rhetorically effective Beamer presentations. It combines the **Rhetoric of Decks** philosophy with automated workflows and specialized AI skills.

---

## 🛠 Project Components

*   **`.claude/`**: Specialized AI skills (in markdown format) that codify the presentation-creation pipeline.
*   **`presentations/`**: The intellectual foundation, detailed guides, and examples.
    *   `rhetoric_of_decks.md`: Practical principles for effective decks.
    *   `examples/`: Real-world examples of the philosophy in action.

---

## 🚀 How to Start a New Presentation

When starting a new session with Gemini or Claude, follow these steps:

1.  **Context Loading**: Tell the AI: "I want to create a new presentation. Follow the philosophy in `presentations/rhetoric_of_decks.md` and the `beautiful_deck` skill in `.claude/skills/`."
2.  **Triage**: The AI should ask you questions about your audience, content, and desired tone.
3.  **Outline**: Approve the `_outline.md` file the AI generates before it starts writing slides.
4.  **Figure Generation**: If your deck needs charts, the AI should write and run standalone scripts (R, Python, or Stata) to generate them.
5.  **Compile Loop**: The AI will iteratively compile and fix warnings until the output is perfect.

---

## 🎯 The Aristotelian Goals

Every deck in this repository aims to balance:
*   **Ethos**: Credibility and authority.
*   **Pathos**: Emotional engagement and stakes.
*   **Logos**: Logical rigor and data.

**Key Rule**: Slide titles must be **assertions**, not labels. "Treatment increased wages" instead of "Results".

---

## 🏗 Directory Structure for a Finished Deck

```text
[project-name]/
├── [project-name].tex       # Main source
├── [project-name].pdf       # Final compiled output
├── [project-name]_outline.md # Approved outline
├── scripts/                # Standalone figure/table scripts
├── figures/                # Output PDFs of charts
└── tables/                 # Output LaTeX fragments
```

---

## 🤝 AI Guidance

*   **Gemini**: Refer to `GEMINI.md` for specific mandates and tool usage.
*   **Claude**: Skills in `.claude/skills/` are designed for Claude Code but applicable to all LLMs.
