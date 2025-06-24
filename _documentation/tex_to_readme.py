#!/usr/bin/env python3
"""
LaTeX to README.md Converter

This script converts the complete LaTeX documentation into a single README.md file
that overrides the root README.md at each run.

Author: Marty Lauterbach with Claude Code
"""

import os
import re
import sys
from pathlib import Path
from typing import Dict, List, Tuple

class TexToReadmeConverter:
    def __init__(self, base_dir: str = None):
        if base_dir is None:
            base_dir = Path(__file__).parent
        self.base_dir = Path(base_dir)
        self.src_dir = self.base_dir / "src"
        self.images_dir = self.base_dir / "images"
        self.root_dir = self.base_dir.parent
        
        # Track sections and their order
        self.sections = []
        self.content = []
        
    def clean_latex_commands(self, text: str) -> str:
        """Remove or convert LaTeX commands to markdown equivalents"""
        
        # Remove common LaTeX commands
        text = re.sub(r'\\UseRawInputEncoding', '', text)
        text = re.sub(r'\\hypersetup\{[^}]*\}', '', text)
        text = re.sub(r'\\setcounter\{[^}]*\}\{[^}]*\}', '', text)
        text = re.sub(r'\\captionsetup[^}]*\{[^}]*\}', '', text)
        text = re.sub(r'\\pagenumbering\{[^}]*\}', '', text)
        text = re.sub(r'\\newpage', '', text)
        text = re.sub(r'\\onehalfspacing', '', text)
        text = re.sub(r'\\singlespacing', '', text)
        text = re.sub(r'\\addcontentsline[^}]*\{[^}]*\}\{[^}]*\}', '', text)
        text = re.sub(r'\\tableofcontents', '', text)
        text = re.sub(r'\\appendix', '', text)
        text = re.sub(r'\\printbibliography[^}]*', '', text)
        text = re.sub(r'\\tocgroup\{[^}]*\}', '', text)
        text = re.sub(r'\\vspace\{[^}]*\}', '', text)
        text = re.sub(r'\\hspace\{[^}]*\}', '', text)
        text = re.sub(r'\\centering', '', text)
        text = re.sub(r'\\flushright', '', text)
        text = re.sub(r'\\flushleft', '', text)
        
        # Convert sections
        text = re.sub(r'\\section\*\{([^}]*)\}', r'# \1', text)
        text = re.sub(r'\\section\{([^}]*)\}[^{]*', r'# \1', text)
        text = re.sub(r'\\subsection\{([^}]*)\}', r'## \1', text)
        text = re.sub(r'\\subsubsection\{([^}]*)\}', r'### \1', text)
        
        # Convert text formatting
        text = re.sub(r'\\textbf\{([^}]*)\}', r'**\1**', text)
        text = re.sub(r'\\textit\{([^}]*)\}', r'*\1*', text)
        text = re.sub(r'\\emph\{([^}]*)\}', r'*\1*', text)
        text = re.sub(r'\\texttt\{([^}]*)\}', r'`\1`', text)
        text = re.sub(r'\\code\{([^}]*)\}', r'`\1`', text)
        text = re.sub(r'\\file\{([^}]*)\}', r'`\1`', text)
        text = re.sub(r'\\mask', 'M.A.S.K.', text)
        
        # Convert quotes
        text = re.sub(r'\\enquote\{([^}]*)\}', r'"\1"', text)
        text = re.sub(r'„([^"]*)"', r'"\1"', text)
        
        # Convert lists
        text = re.sub(r'\\begin\{itemize\}', '', text)
        text = re.sub(r'\\end\{itemize\}', '', text)
        text = re.sub(r'\\begin\{enumerate\}', '', text)
        text = re.sub(r'\\end\{enumerate\}', '', text)
        text = re.sub(r'\\item\s*', '- ', text)
        
        # Convert figures with proper image path handling
        text = re.sub(r'\\begin\{figure\}[^}]*', '', text)
        text = re.sub(r'\\end\{figure\}', '', text)
        text = re.sub(r'\\begin\{flushright\}', '', text)
        text = re.sub(r'\\end\{flushright\}', '', text)
        text = re.sub(r'\\begin\{center\}', '', text)
        text = re.sub(r'\\end\{center\}', '', text)
        # Enhanced image path handling with proper formatting
        def image_replacer(match):
            img_path = match.group(1)
            
            # Fix specific known file extensions
            if 'FAWB.pdf' in img_path:
                img_path = img_path.replace('FAWB.pdf', 'FAWB.svg')
            
            # Convert relative paths to absolute from root
            if not img_path.startswith('_documentation/'):
                img_path = f'_documentation/{img_path}'
            
            # Extract filename for alt text
            filename = Path(img_path).stem
            alt_text = filename.replace('_', ' ').replace('-', ' ').title()
            
            return f'\n\n![{alt_text}]({img_path})\n'
        
        text = re.sub(r'\\includegraphics[^}]*\{([^}]*)\}', image_replacer, text)
        text = re.sub(r'\\caption\{([^}]*)\}', r'*\1*', text)
        text = re.sub(r'\\label\{[^}]*\}', '', text)
        
        # Convert tables to markdown format
        text = self.convert_tables(text)
        
        # Convert code blocks with language detection
        text = self.convert_code_blocks(text)
        
        # Remove LaTeX comments
        text = re.sub(r'%.*$', '', text, flags=re.MULTILINE)
        
        # Clean up multiple newlines
        text = re.sub(r'\n\s*\n\s*\n+', '\n\n', text)
        
        # Remove remaining backslashes and curly braces for simple cases
        text = re.sub(r'\\([a-zA-Z]+)', r'\1', text)
        text = re.sub(r'\{([^{}]*)\}', r'\1', text)
        
        # Enhanced paragraph and text formatting
        text = self.format_paragraphs(text)
        
        return text.strip()
    
    def format_paragraphs(self, text: str) -> str:
        """Format paragraphs and improve text flow"""
        # Split into paragraphs
        paragraphs = text.split('\n\n')
        formatted_paragraphs = []
        
        for para in paragraphs:
            para = para.strip()
            if not para:
                continue
            
            # Skip if it's a header, list item, or code block
            if (para.startswith('#') or para.startswith('-') or 
                para.startswith('*') or para.startswith('```') or
                para.startswith('|') or para.startswith('!')):
                formatted_paragraphs.append(para)
                continue
            
            # Clean up LaTeX artifacts
            para = re.sub(r'\\\\', ' ', para)  # Remove line breaks
            para = re.sub(r'\s+', ' ', para)    # Normalize whitespace
            para = re.sub(r'\{([^}]*)\}', r'\1', para)  # Remove simple braces
            
            # Add proper sentence spacing
            para = re.sub(r'\. +', '. ', para)
            para = re.sub(r': +', ': ', para)
            para = re.sub(r', +', ', ', para)
            
            # Handle German umlauts and special characters
            para = para.replace('ä', 'ä').replace('ö', 'ö').replace('ü', 'ü')
            para = para.replace('Ä', 'Ä').replace('Ö', 'Ö').replace('Ü', 'Ü')
            para = para.replace('ß', 'ß')
            
            if para.strip():
                formatted_paragraphs.append(para)
        
        # Join with proper spacing
        text = '\n\n'.join(formatted_paragraphs)
        
        # Clean up multiple newlines
        text = re.sub(r'\n\s*\n\s*\n+', '\n\n', text)
        text = re.sub(r'^\s+', '', text, flags=re.MULTILINE)
        
        return text
    
    def convert_tables(self, text: str) -> str:
        """Convert LaTeX tables to markdown format"""
        # Simple table conversion - handles basic tabular environments
        def table_replacer(match):
            table_content = match.group(1)
            lines = table_content.strip().split('\\\\')
            
            markdown_rows = []
            header_processed = False
            
            for line in lines:
                if '\\hline' in line:
                    continue
                    
                # Split by & and clean up
                cells = [cell.strip() for cell in line.split('&') if cell.strip()]
                if not cells:
                    continue
                    
                # Clean LaTeX formatting from cells
                clean_cells = []
                for cell in cells:
                    cell = re.sub(r'\\textbf\{([^}]*)\}', r'**\1**', cell)
                    cell = re.sub(r'\\textit\{([^}]*)\}', r'*\1*', cell)
                    cell = re.sub(r'\\[a-zA-Z]+\{([^}]*)\}', r'\1', cell)
                    clean_cells.append(cell.strip())
                
                if clean_cells:
                    markdown_rows.append('| ' + ' | '.join(clean_cells) + ' |')
                    
                    # Add header separator after first row
                    if not header_processed:
                        separator = '| ' + ' | '.join(['---'] * len(clean_cells)) + ' |'
                        markdown_rows.append(separator)
                        header_processed = True
            
            return '\n'.join(markdown_rows) + '\n'
        
        # Match table environments
        text = re.sub(r'\\begin\{table\}.*?\\begin\{tabular\}[^}]*\{[^}]*\}(.*?)\\end\{tabular\}.*?\\end\{table\}', 
                     table_replacer, text, flags=re.DOTALL)
        
        # Remove remaining table commands
        text = re.sub(r'\\begin\{table\}[^}]*', '', text)
        text = re.sub(r'\\end\{table\}', '', text)
        text = re.sub(r'\\begin\{tabular\}[^}]*', '', text)
        text = re.sub(r'\\end\{tabular\}', '', text)
        text = re.sub(r'\\hline', '', text)
        
        return text
    
    def convert_code_blocks(self, text: str) -> str:
        """Convert LaTeX code blocks to markdown format"""
        # Handle lstlisting environments
        def lstlisting_replacer(match):
            content = match.group(1).strip()
            # Try to detect language from content or context
            language = ''
            if 'def ' in content or 'import ' in content or 'class ' in content:
                language = 'python'
            elif '#include' in content or 'int main' in content:
                language = 'c'
            elif 'function' in content or 'var ' in content:
                language = 'javascript'
            
            return f'```{language}\n{content}\n```'
        
        # Convert lstlisting
        text = re.sub(r'\\begin\{lstlisting\}[^}]*\}?(.*?)\\end\{lstlisting\}', 
                     lstlisting_replacer, text, flags=re.DOTALL)
        
        # Convert verbatim
        text = re.sub(r'\\begin\{verbatim\}(.*?)\\end\{verbatim\}', 
                     r'```\n\1\n```', text, flags=re.DOTALL)
        
        # Handle inline code
        text = re.sub(r'\\verb\|([^|]*)\|', r'`\1`', text)
        
        return text
    
    def extract_title_info(self) -> tuple:
        """Extract title page information"""
        title_file = self.src_dir / "title.tex"
        if not title_file.exists():
            return "M.A.S.K.", "Machine-Learning Assisted Skeleton Kinect Tracking", "Marty Lauterbach"
        
        try:
            with open(title_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Extract title - look for M.A.S.K.
            title_match = re.search(r'\\textbf\{M\.A\.S\.K\.\}', content)
            title = "M.A.S.K." if title_match else "M.A.S.K."
            
            # Extract subtitle - hardcode the known subtitle
            subtitle = "Machine-Learning Assisted Skeleton Kinect Tracking"
            
            # Extract author
            author_match = re.search(r'(Marty Lauterbach)', content)
            author = author_match.group(1) if author_match else "Marty Lauterbach"
            
            return title, subtitle, author
        except Exception as e:
            print(f"Error extracting title info: {e}")
            return "M.A.S.K.", "Machine-Learning Assisted Skeleton Kinect Tracking", "Marty Lauterbach"
    
    def read_tex_file(self, filename: str) -> str:
        """Read and process a single .tex file"""
        filepath = self.src_dir / filename
        if not filepath.exists():
            print(f"Warning: File {filepath} not found")
            return ""
        
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            return self.clean_latex_commands(content)
        except Exception as e:
            print(f"Error reading {filepath}: {e}")
            return ""
    
    def parse_main_document(self) -> List[Tuple[str, str]]:
        """Parse the main document.tex file to extract section structure"""
        main_file = self.base_dir / "document.tex"
        sections = []
        
        try:
            with open(main_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Find all \input{src/filename} commands
            input_pattern = r'\\input\{src/([^}]*)\}'
            matches = re.findall(input_pattern, content)
            
            # Also extract section titles from the main document
            section_pattern = r'\\section\{([^}]*)\}.*?\\input\{src/([^}]*)\}'
            section_matches = re.findall(section_pattern, content, re.DOTALL)
            
            # Create mapping of files to section titles
            file_to_title = {match[1]: match[0] for match in section_matches}
            
            for filename in matches:
                title = file_to_title.get(filename, filename.replace('_', ' ').title())
                sections.append((title, filename))
                
        except Exception as e:
            print(f"Error parsing main document: {e}")
            # Fallback: include key files manually
            sections = [
                ("Introduction", "Einführung"),
                ("Requirements", "Requirements"),
                ("Development Process", "Entwicklungsprozess"),
                ("System Architecture", "Systemarchitektur_und_Ergebnisse"),
                ("Insights", "erkenntnisse"),
                ("Conclusion", "fazit"),
                ("Feasibility Study", "Feasibility"),
                ("Code Overview", "anhang_code_übersicht"),
                ("Acknowledgments", "danksagung")
            ]
        
        return sections
    
    def generate_readme(self) -> str:
        """Generate the complete README.md content"""
        readme_content = []
        
        # Extract title information
        title, subtitle, author = self.extract_title_info()
        
        # Header with title page information
        readme_content.append(f"# {title}")
        readme_content.append(f"## {subtitle}")
        readme_content.append("")
        readme_content.append(f"**Author:** {author}")
        readme_content.append("**Project:** MKI-Projekt SoSe 2025")
        readme_content.append("**Institution:** Reutlingen University in cooperation with Filmakademie Baden-Württemberg")
        readme_content.append("")
        readme_content.append("![FAWB Logo](_documentation/images/FAWB.svg)")
        readme_content.append("")
        readme_content.append("*Complete documentation automatically generated from LaTeX sources*")
        readme_content.append("")
        
        # Table of Contents
        readme_content.append("## Table of Contents")
        readme_content.append("")
        
        sections = self.parse_main_document()
        # Remove duplicates from sections list
        seen_titles = set()
        unique_sections = []
        for title, filename in sections:
            if title not in seen_titles and filename != 'title':
                seen_titles.add(title)
                unique_sections.append((title, filename))
        
        for title, _ in unique_sections:
            readme_content.append(f"- [{title}](#{title.lower().replace(' ', '-').replace('_', '-')})")
        readme_content.append("")
        
        # Process each section (skip title page as it's already handled in header)
        for title, filename in unique_sections:
                
            readme_content.append(f"## {title}")
            readme_content.append("")
            
            content = self.read_tex_file(f"{filename}.tex")
            if content:
                readme_content.append(content)
            else:
                readme_content.append(f"*Content from {filename}.tex could not be processed*")
            
            readme_content.append("")
            readme_content.append("---")
            readme_content.append("")
        
        # Add project structure
        readme_content.append("## Project Structure")
        readme_content.append("")
        readme_content.append("```")
        readme_content.append("MASK-main/")
        readme_content.append("├── *.toe                    # TouchDesigner project files")
        readme_content.append("├── *.py                     # Python DAT operators")
        readme_content.append("├── *.tox                    # TouchDesigner components")
        readme_content.append("├── Backup/                  # Project file versions")
        readme_content.append("├── _documentation/          # Complete LaTeX documentation")
        readme_content.append("│   ├── src/                # Individual section files")
        readme_content.append("│   ├── images/             # Figures and diagrams")
        readme_content.append("│   └── document.pdf        # Compiled documentation")
        readme_content.append("└── README.md               # This file")
        readme_content.append("```")
        readme_content.append("")
        
        # Footer
        readme_content.append("---")
        readme_content.append("")
        readme_content.append("*This README.md was automatically generated from the LaTeX documentation.")
        readme_content.append("For the complete formatted document, see `_documentation/document.pdf`.*")
        readme_content.append("")
        readme_content.append(f"*Generated on: {self.get_current_date()}*")
        
        content = "\n".join(readme_content)
        return self.beautify_markdown(content)
    
    def beautify_markdown(self, content: str) -> str:
        """Apply cosmetic improvements to generated markdown"""
        lines = content.split('\n')
        beautified_lines = []
        
        i = 0
        while i < len(lines):
            line = lines[i]
            
            # Add spacing around headers
            if line.startswith('#'):
                if i > 0 and beautified_lines and beautified_lines[-1].strip():
                    beautified_lines.append('')
                beautified_lines.append(line)
                if i < len(lines) - 1 and lines[i+1].strip():
                    beautified_lines.append('')
            
            # Add spacing around images
            elif line.startswith('!['):
                if i > 0 and beautified_lines and beautified_lines[-1].strip():
                    beautified_lines.append('')
                beautified_lines.append(line)
                if i < len(lines) - 1 and lines[i+1].strip():
                    beautified_lines.append('')
            
            # Add spacing around tables
            elif line.startswith('|'):
                if i > 0 and beautified_lines and beautified_lines[-1].strip() and not beautified_lines[-1].startswith('|'):
                    beautified_lines.append('')
                beautified_lines.append(line)
                # Look ahead for end of table
                if i < len(lines) - 1 and not lines[i+1].startswith('|') and lines[i+1].strip():
                    beautified_lines.append('')
            
            # Add spacing around code blocks
            elif line.startswith('```'):
                if i > 0 and beautified_lines and beautified_lines[-1].strip():
                    beautified_lines.append('')
                beautified_lines.append(line)
                # Find end of code block
                i += 1
                while i < len(lines) and not lines[i].startswith('```'):
                    beautified_lines.append(lines[i])
                    i += 1
                if i < len(lines):
                    beautified_lines.append(lines[i])  # Closing ```
                if i < len(lines) - 1 and lines[i+1].strip():
                    beautified_lines.append('')
            
            else:
                beautified_lines.append(line)
            
            i += 1
        
        # Final cleanup
        content = '\n'.join(beautified_lines)
        content = re.sub(r'\n\s*\n\s*\n+', '\n\n', content)
        
        return content
    
    def get_current_date(self) -> str:
        """Get current date in German format"""
        from datetime import datetime
        return datetime.now().strftime("%d.%m.%Y")
    
    def write_readme(self) -> None:
        """Write the generated README.md to the root directory"""
        readme_content = self.generate_readme()
        readme_path = self.root_dir / "README.md"
        
        try:
            with open(readme_path, 'w', encoding='utf-8') as f:
                f.write(readme_content)
            print(f"Successfully generated README.md at {readme_path}")
        except Exception as e:
            print(f"Error writing README.md: {e}")

def main():
    """Main function to run the converter"""
    converter = TexToReadmeConverter()
    converter.write_readme()

if __name__ == "__main__":
    main()