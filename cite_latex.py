import re

def convert_citations_to_latex(text):
    """
    Convert Markdown-style citations [@key] to LaTeX-compatible format
    """
    # Pattern to match [@citationKey] with optional multiple keys separated by semicolons
    pattern = r'\[@([^\]]+)\]'
    
    def replace_citation(match):
        # Get the citation content (without brackets)
        citation_content = match.group(1)
        
        # Split multiple citations by semicolon and strip whitespace
        citation_keys = [key.strip() for key in citation_content.split(';')]
        
        # Join with commas for LaTeX format
        latex_keys = ','.join(citation_keys)
        
        return f'\\cite{{{latex_keys}}}'
    
    # Replace all citations
    converted_text = re.sub(pattern, replace_citation, text)
    
    return converted_text


def convert_boldings_to_latex(text):
    """
    Convert Markdown-style bold **text** to LaTeX \textbf{text}
    """
    pattern = r'\*\*(.*?)\*\*'
    
    def replace_bold(match):
        bold_content = match.group(1)
        return f'\\textbf{{{bold_content}}}'
    
    converted_text = re.sub(pattern, replace_bold, text)
    
    return converted_text




input_file = r"C:\GitHub\obsidian\codex\bioeng\Nanotech Research Proposal.md"
with open(input_file, "r", encoding="utf-8") as f:
    user_input = f.read()
    
text = convert_citations_to_latex(user_input)
text = convert_boldings_to_latex(text)


with open("output.md", "w", encoding="utf-8") as f:
    f.write(text)

with open("latex/subsections/output.tex", "w", encoding="utf-8") as f:
    f.write(text)