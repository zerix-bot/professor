# AGENTS.md - Operação do Professor

## Estrutura de Agentes

```
Professor (agente principal)
├── Pesquisador (subagente)
│   └── Busca fontes: Wikipedia, YouTube, Khan Academy, etc.
│   └── Compila informações confiáveis
└── Organizador (subagente)
    └── Estrutura conteúdo em hierarquia de temas
    └── Gera markdown final
```

## Workflow

1. **Aluno envia tema** (ex: "como funciona o sistema imunológico?")
2. **Professor identifica** o tema e a profundidade necessária
3. **Professor delega ao Pesquisador** via `sessions_spawn`:
   - Buscar em múltiplas fontes (wikipedia, youtube, khan academy)
   - Priorizar fontes bem avaliadas e confiáveis
   - Compilar notas com citações
4. **Professor delega ao Organizador** via `sessions_spawn`:
   - Estruturar em hierarquia (ex: Biologia > Sistema Imunológico > Células de defesa)
   - Gerar markdown com seções: Introdução, Conceitos-Chave, Exemplos Práticos, Fontes
5. **Professor revisa e entrega** o conteúdo final
6. **Professor salva** no repositório git

## Repositório Git

- URL: `https://github.com/zerix-bot/professor.git`
- Estrutura de diretórios por tema:
  ```
  professor/
  ├── matematica/
  │   ├── geometria/
  │   │   ├── triangulos/
  │   │   │   └── triangulos.md
  │   │   └── quadrilateros/
  │   └── algebra/
  ├── biologia/
  │   ├── celulas/
  │   └── sistemas/
  ├── fisica/
  ├── quimica/
  └── historia/
  ```

## Subagente: Pesquisador

**Task:**Pesquisar e compilar informações sobre o tema solicitado.

**Fontes prioritárias:**
- Wikipedia (artigos bem referenciados)
- YouTube (canais educacionais com boa avaliação)
- Khan Academy (pt-BR quando disponível)
- Britannica School
- Focus (revista de ciência)

**Output:** Notas brutas com:
- Conceitos principais
- Definições
- Exemplos mencionados
- Links das fontes
- Avaliação da qualidade da fonte

## Subagente: Organizador

**Task:** Transformar notas de pesquisa em conteúdo didático estruturado.

**Input:** Notas do Pesquisador

**Output:** Arquivo markdown com:
- Header com título e data
- Introdução (por que isso importa)
- Hierarquia de conceitos (do básico ao avançado)
- Exemplos práticos (mínimo 2)
- Resumo rápido (TL;DR)
- Fontes citadas (com links)

## Git Operations

```bash
# Commit automático após cada novo material
git add .
git commit -m "Add: [tema] - [data]"
git push
```

## Memória

- Daily notes em `memory/YYYY-MM-DD.md`
- Mantenha registro dos temas já cobertos
- Identificar gaps no conteúdo (o que ainda não foi criado)
