import copy
import re
import os


def convert_citations_to_latex(text):
    r"""
    Convert Markdown-style citations [@key] to LaTeX-compatible format
    Also fixes common malformations like [@key} instead of [@key]
    Handles multiple citations: [@key1; @key2; @key3] -> \cite{key1,key2,key3}
    """
    # First, fix common malformations: [@key} -> [@key]
    text = re.sub(r'\[@([^\]]+)\}', r'[@\1]', text)
    
    # Pattern to match [@citationKey] with optional multiple keys separated by semicolons
    pattern = r"\[@([^\]]+)\]"

    def replace_citation(match):
        # Get the citation content (without brackets)
        citation_content = match.group(1)

        # Split multiple citations by semicolon and strip whitespace
        citation_keys = [key.strip() for key in citation_content.split(";")]
        
        # Remove @ prefix from each citation key
        citation_keys = [key.lstrip('@') for key in citation_keys]

        # Join with commas for LaTeX format
        latex_keys = ",".join(citation_keys)

        return f"\\cite{{{latex_keys}}}"

    # Replace all citations
    converted_text = re.sub(pattern, replace_citation, text)

    return converted_text


def replace_bold_italics(text):
    """
    Convert Markdown-style bold **text** to LaTeX \textbf{text}
    """
    bold_pattern = r"\*\*(.*?)\*\*"
    italics_pattern = r"\*(.*?)\*"
    italics_pattern_2 = r"_(.*?)_"

    def replace_bold(match):
        bold_content = match.group(1)
        return f"\\textbf{{{bold_content}}}"

    text = re.sub(bold_pattern, r"\\textbf{\1}", text)
    text = re.sub(italics_pattern, r"\\textit{\1}", text)
    text = re.sub(italics_pattern_2, r"\\textit{\1}", text)

    return text


def separate_sections(text):
    """
    Separate text into sections based on '# ' headers
    Returns a list of tuples: (section_name, section_content)
    """
    # Split by '# ' headers while keeping the header text
    sections = re.split(r"(?m)^# ", text)

    section_titles = []
    section_contents = []

    # First element is content before any header (skip if empty)
    if sections[0].strip():
        section_titles.append("intro")
        section_contents.append(sections[0].strip())

    # Process remaining sections
    for section in sections[1:]:
        # Split at first newline to separate title from content
        lines = section.split("\n", 1)
        section_name = lines[0].strip()
        section_text = lines[1].strip() if len(lines) > 1 else ""

        # Clean section name for filename (remove special characters)
        clean_name = (
            re.sub(r"[^\w\s-]", "", section_name).strip().replace(" ", "_").lower()
        )

        section_titles.append(clean_name)
        section_contents.append(section_text)

    return section_titles, section_contents


def copy_references_file(src, dest):
    """
    Copy references.bib file from src to dest
    """
    with open(src, "r", encoding="utf-8") as f_src:
        content = f_src.read()

    with open(dest, "w", encoding="utf-8") as f_dest:
        f_dest.write(content)


def save_as_section(section_name:str, section_text:str, save_folder="latex/sections"):
    filepath = os.path.join(save_folder, f"{section_name}.tex")

    text = (
        "\\documentclass[../main.tex]{subfiles}\n"
        +"\\begin{document} \n"
        + section_text
        + "\n\\end{document}"
    )

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(text)


def replace_bullet_points(text):
    """
    Convert Markdown-style bullet points to LaTeX itemize environment
    """
    lines = text.split("\n")
    in_itemize = False
    new_lines = []

    for line in lines:
        if line.startswith("- "):
            if not in_itemize:
                new_lines.append("\\begin{itemize}")
                in_itemize = True
            new_lines.append(f"\\item {line[2:].strip()}")
        else:
            if in_itemize:
                new_lines.append("\\end{itemize}")
                in_itemize = False
            new_lines.append(line)

    if in_itemize:
        new_lines.append("\\end{itemize}")

    return "\n".join(new_lines)


import re

def replace_numbered_lists(text: str) -> str:
    """
    Convert Markdown numbered lists to LaTeX enumerate environments.
    Properly handles nesting by maintaining a stack of indent levels.
    """
    lines = text.splitlines()
    out = []
    indent_stack = []  # stack of indent widths for open enumerate envs

    item_re = re.compile(r'^([ \t]*)(\d+)\.\s+(.*)$')
    other_list_re = re.compile(r'^([ \t]*)([-*+])\s+(.*)$')  # if you want to not close on bullets

    for line in lines:
        m = item_re.match(line)

        if m:
            indent, _num, content = m.groups()
            cur = len(indent.replace('\t', '    '))  # treat tabs as 4 spaces

            # Open/close environments to match current indent
            if not indent_stack:
                out.append(r'\begin{enumerate}')
                indent_stack.append(cur)
            else:
                top = indent_stack[-1]
                if cur > top:
                    out.append(r'\begin{enumerate}')
                    indent_stack.append(cur)
                elif cur < top:
                    # Close until we reach a level <= cur
                    while indent_stack and cur < indent_stack[-1]:
                        out.append(r'\end{enumerate}')
                        indent_stack.pop()
                    # If we've popped all and still need an enumerate at this indent
                    if not indent_stack:
                        out.append(r'\begin{enumerate}')
                        indent_stack.append(cur)
                    # If cur doesn't exactly match an existing level, treat as new level
                    elif cur != indent_stack[-1]:
                        out.append(r'\begin{enumerate}')
                        indent_stack.append(cur)

            out.append(rf'\item {content}')
            continue

        # Not a numbered item: decide whether to close open enumerates.
        # Close when we hit a blank line OR a non-list line.
        if indent_stack:
            is_blank = (line.strip() == "")
            is_other_list = other_list_re.match(line) is not None
            if is_blank or not is_other_list:
                while indent_stack:
                    out.append(r'\end{enumerate}')
                    indent_stack.pop()

        out.append(line)

    # Close any remaining enumerates at EOF
    while indent_stack:
        out.append(r'\end{enumerate}')
        indent_stack.pop()

    return "\n".join(out)




def handle_headings(text):
    """
    Convert ## headers to LaTeX subsections, remove deeper heading levels
    """
    # Convert ## to \subsection{}
    text = re.sub(r"(?m)^## (.+)$", r"\\subsection{\1}", text)
    # Remove ### and deeper headings
    text = re.sub(r"(?m)^#{3,}\s.*\n?", "", text)
    return text


input_file = r"C:\GitHub\obsidian\codex\bioeng\Nanotech Research Proposal.md"


with open(input_file, "r", encoding="utf-8") as f:
    raw_text = f.read()

copy_references_file(
    src=r"C:\GitHub\obsidian\references.bib", dest=r"latex\references.bib"
)


raise Exception("Manual changes needed before proceeding further")


for section_name, section_content in zip(*separate_sections(raw_text)):
    text = convert_citations_to_latex(section_content)
    text = replace_bold_italics(text)
    text = replace_bullet_points(text)
    text = replace_numbered_lists(text)
    text = handle_headings(text)
    save_as_section(section_name, text)

