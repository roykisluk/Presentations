# Gemini Project Mandates: Presentation Tools

This project is dedicated to creating high-quality, beautiful Beamer presentations using a consistent philosophy and automated workflow. As Gemini, you must adhere to these foundational mandates.

## Core Philosophy: The Rhetoric of Decks

You must internalize and apply the following principles from `presentations/rhetoric_of_decks.md`:

1.  **The Three Laws**:
    *   **Beauty is function**: Clarity made visible. No decoration without function.
    *   **Cognitive load is the enemy**: One idea per slide. Two max for inseparable contrasts.
    *   **The slide serves the spoken word**: The slide is the visual anchor, not the script.
2.  **The Aristotelian Triad**:
    *   **Ethos (Credibility)**: Built through methodology, Devil's Advocate slides, and acknowledging limitations.
    *   **Pathos (Emotion)**: Built through opening hooks, stakes, and human impact.
    *   **Logos (Logic)**: Built through data viz, causal diagrams, and logical flow.
3.  **MB/MC Equivalence**: Aim for a consistent ratio of Marginal Benefit to Marginal Cost across all slides. Avoid "cliffs" in density.
4.  **Titles as Assertions**: Every slide title must state a claim (e.g., "Treatment increased distance by 61 miles") rather than just a label (e.g., "Results").
5.  **Bullets are Defeat**: Find the structure (sequence, contrast, hierarchy, causal chain) rather than relying on lists.

## Specialized Skills

This repository contains specialized instructions for Claude that you should also follow. These are located in `.claude/skills/`:

*   **`beautiful_deck`**: The end-to-end pipeline for creating a presentation. Includes audience triage, theme design, Narrative → Application → Picture → Codeblock → Technical sequencing, and multi-agent audits.
*   **`compiledeck`**: Mechanical rules for Beamer preambles, palettes, and the zero-warning compile loop.
*   **`tikz`**: Measurement-based visual collision audit for TikZ diagrams.
*   **`split-pdf`**: Methodology for summarizing papers to be used as source material.

**Mandate**: When tasked with creating or editing a presentation, you MUST follow the workflows described in these skill files.

## The Zero-Warning Compile Loop

You MUST achieve zero compile warnings (Overfull/Underfull `\hbox` and `\vbox`) for every deck you produce.
1.  **Compile**: `pdflatex -interaction=nonstopmode <deck>.tex`
2.  **Audit**: Check the `.log` file for `Overfull` or `Underfull` boxes.
3.  **Fix**: Adjust content or use `\adjustbox` until the count is exactly **0**.
4.  **Verify**: Run `/tikz` (or follow its logic) to ensure no silent visual collisions in diagrams.

## Project Structure

*   `JambroBeamerTheme/`: The default Beamer theme and graphics.
*   `presentations/`: Documentation, prompts, and examples.
*   `.claude/`: Specialized AI instructions (skills and commands).
*   `scripts/`: (To be created per-project) Standalone R/Python scripts for figure generation.
*   `figures/` and `tables/`: (To be created per-project) Output for scripts, `\input` or `\includegraphics` into the deck.

## Workflow for New Projects

1.  **Triage**: Gather audience, source content, and tone.
2.  **Design**: Create an original theme (or use the Warm Professional house style).
3.  **Outline**: Create a `<deck_name>_outline.md` following the Narrative → Technical arc. **Get user approval.**
4.  **Scripts**: Write and run standalone scripts for figures and tables first.
5.  **Draft**: Write slides following the assertions and MB/MC rules.
6.  **Audit**: Run the zero-warning compile loop and the TikZ collision audit.
7.  **Sub-Agent Review**: (Optional) Use `generalist` or `codebase_investigator` to perform rhetoric and graphics audits.
