---
name: material-collector
description: Subagente do Professor para coletar e extrair conteúdo de arquivos anexados (PDF, imagens, DOCX, PPTX). Use quando o aluno enviar um arquivo como anexo junto com um pedido de explicação ou aula. O skill extrai o texto/conteúdo do arquivo e retorna para o Professor usar como base. Extensões suportadas: .pdf, .png, .jpg, .jpeg, .docx, .pptx.
---

# Material Collector

Extrai conteúdo de arquivos anexados para o Professor usar como base em explicações.

## Como usar

Quando receber um arquivo anexo:

```bash
# Identificar tipo e extrair
python3 /home/umbrel/.openclaw/workspace-professor/skills/material-collector/scripts/extract.py <caminho-do-arquivo>
```

## Formatos suportados

| Extensão | Método | Notas |
|----------|--------|-------|
| `.pdf` | `pdftotext` | Extrai texto direto |
| `.png`, `.jpg`, `.jpeg` | OCR (pytesseract) ou descrição | Tenta OCR primeiro |
| `.docx` | `python-docx` | Requer biblioteca |
| `.pptx` | `python-pptx` | Requer biblioteca |

## Output

Retorna texto extraído em markdown, pronto para o Professor usar como base.

## Notas

- Imagens: tenta pytesseract (OCR), fallback para descrição genérica
- DOCX/PPTX: instala bibliotecas com `pip install python-docx python-pptx` se necessário
- Arquivos grandes: processa e resume se preciso