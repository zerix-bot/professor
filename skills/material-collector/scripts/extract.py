#!/usr/bin/env python3
"""Extract text content from various file formats."""

import sys
import os
import subprocess
import zipfile
import xml.etree.ElementTree as ET
import re

def extract_pdf(path):
    """Extract text from PDF using pdftotext."""
    try:
        result = subprocess.run(['pdftotext', '-layout', path, '-'], 
                               capture_output=True, text=True, timeout=30)
        if result.returncode == 0 and result.stdout.strip():
            return result.stdout
        return "[PDF sem texto extraível ou vazio]"
    except Exception as e:
        return f"[Erro ao extrair PDF: {e}]"

def extract_image(path):
    """Extract text from image using OCR (pytesseract)."""
    try:
        import pytesseract
        from PIL import Image
        img = Image.open(path)
        text = pytesseract.image_to_string(img, lang='por')
        if text.strip():
            return text
        return "[Imagem sem texto detectável por OCR]"
    except ImportError:
        return "[OCR não disponível - pytesseract não instalado]"
    except Exception as e:
        return f"[Erro OCR: {e}]"

def extract_docx(path):
    """Extract text from DOCX using unzip + XML parsing."""
    try:
        with zipfile.ZipFile(path, 'r') as z:
            with z.open('word/document.xml') as f:
                tree = ET.parse(f)
                root = tree.getroot()
                ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
                texts = []
                for para in root.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}p'):
                    para_text = ''
                    for t in para.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t'):
                        if t.text:
                            para_text += t.text
                    if para_text.strip():
                        texts.append(para_text)
                if texts:
                    return '\n\n'.join(texts)
        return "[DOCX vazio]"
    except Exception as e:
        return f"[Erro ao extrair DOCX: {e}]"

def extract_pptx(path):
    """Extract text from PPTX using unzip + XML parsing."""
    try:
        texts = []
        with zipfile.ZipFile(path, 'r') as z:
            for name in z.namelist():
                if name.startswith('ppt/slides/slide') and name.endswith('.xml'):
                    with z.open(name) as f:
                        tree = ET.parse(f)
                        root = tree.getroot()
                        for elem in root.iter():
                            if elem.text and elem.text.strip():
                                texts.append(elem.text.strip())
        if texts:
            return '\n\n'.join(texts)
        return "[PPTX sem texto]"
    except Exception as e:
        return f"[Erro ao extrair PPTX: {e}]"

def main():
    if len(sys.argv) < 2:
        print("Uso: extract.py <caminho-do-arquivo>")
        sys.exit(1)
    
    path = sys.argv[1]
    if not os.path.exists(path):
        print(f"[Arquivo não encontrado: {path}]")
        sys.exit(1)
    
    ext = os.path.splitext(path)[1].lower()
    
    extractors = {
        '.pdf': extract_pdf,
        '.png': extract_image,
        '.jpg': extract_image,
        '.jpeg': extract_image,
        '.docx': extract_docx,
        '.pptx': extract_pptx,
    }
    
    extractor = extractors.get(ext)
    if not extractor:
        print(f"[Formato não suportado: {ext}]")
        sys.exit(1)
    
    result = extractor(path)
    print(result)

if __name__ == "__main__":
    main()