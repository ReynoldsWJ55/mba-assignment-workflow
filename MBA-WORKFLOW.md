# MBA Assignment Workflow with Claude Code

## Overview

An automated, AI-powered system for completing MBA assignments using Claude Code with a sequential 6-agent workflow. Creates publication-quality academic work with proper research, framework application, and APA formatting.

## Initial Setup

### Installation

```bash
# Install the setup script
rm ~/setup-mba-project.py
curl -s https://gist.githubusercontent.com/anthropic/claude-mba-workflow/main/setup-mba-project.py > ~/setup-mba-project.py || cat > ~/setup-mba-project.py << 'EOF'
[Complete script content]
EOF
chmod +x ~/setup-mba-project.py

# Create alias for easy access
echo 'alias mba-setup="python3 ~/setup-mba-project.py"' >> ~/.zshrc
source ~/.zshrc
```

### Project Creation

```bash
mba-setup
```

- Detects existing MBA courses in iCloud Drive/Stamford
- Creates standardized folder structure
- Generates agent prompts and templates
- Sets up file organization system

## Folder Structure

```
assignment01-ProjectName/
├── 01-planning/
│   ├── instructions.md          # Assignment requirements
│   └── CLAUDE.md               # Agent workflow prompts
├── 02-research/
│   ├── academic-sources/
│   │   ├── source-files/       # 📁 PUT ACADEMIC PDFs HERE
│   │   └── summaries/          # Agent-generated summaries
│   └── industry-sources/
│       ├── source-files/       # 📁 PUT INDUSTRY REPORTS HERE
│       └── summaries/          # Agent-generated summaries
├── 03-analysis/
│   ├── framework-applications/
│   │   ├── individual-frameworks/  # Each framework analysis
│   │   └── synthesis/              # Combined insights
│   └── evidence-mapping/           # Source-to-framework links
├── 04-writing/
│   ├── outlines/               # Detailed writing plans
│   ├── drafts/                 # Version-controlled drafts
│   └── citations/              # APA reference management
└── 05-final/
    ├── submission/             # 🎯 FINAL ASSIGNMENT FILES
    └── supporting-materials/   # Quality reports
```

## Sequential Agent Workflow

### AGENT 1: Research Director

**Purpose**: Creates comprehensive research strategy

**Input**: Assignment instructions

**Actions**:

- Analyzes assignment requirements
- Maps frameworks to evidence needs
- Creates source collection strategy
- Generates research plan

**Output Files**:

- `02-research/planning-summary.md` (comprehensive approach for user review)
- `02-research/research-plan.md` (includes direct search links)
- `02-research/source-requirements.md` (with clickable URLs)
- `02-research/search-links.md` (Google Scholar & Google search URLs)

**Completion**: "Research Director Complete. REVIEW planning-summary.md and approve before collecting sources. Then run AGENT 2."

### AGENT 2: Academic Scout

**Purpose**: Analyzes collected sources and creates templates

**Input**: Sources placed in source-files folders

**Actions**:

- Scans for collected academic and industry sources
- Creates analysis templates for each source
- Generates quality assessment criteria
- Creates extraction guides

**Output Files**:

- Templates in summaries/ folders for each source
- `02-research/source-quality-assessment.md`

**Completion**: "Academic Scout Complete. Run AGENT 3 to extract evidence."

### AGENT 3: Research Analyst

**Purpose**: Extracts and organizes evidence from sources

**Input**: All collected source files

**Actions**:

- Reads and analyzes all PDFs/documents
- Extracts evidence relevant to each framework
- Creates detailed source summaries
- Maps evidence to framework requirements
- Generates research synthesis

**Output Files**:

- Individual source summaries
- `03-analysis/evidence-mapping/framework-evidence.md`
- `03-analysis/research-synthesis.md`

**Completion**: "Research Analyst Complete. Run AGENT 4 for framework analysis."

### AGENT 4: Framework Specialist

**Purpose**: Applies strategic frameworks using extracted evidence

**Input**: Research synthesis and evidence mapping

**Actions**:

- Applies each required framework systematically
- Creates comprehensive framework analyses
- Generates integrated strategic insights
- Develops evidence-based recommendations

**Output Files**:

- Individual framework analysis files
- `03-analysis/framework-applications/synthesis/integrated-analysis.md`
- `03-analysis/strategic-recommendations.md`

**Completion**: "Framework Specialist Complete. Run AGENT 5 for writing."

### AGENT 5: Writing Coordinator

**Purpose**: Creates complete academic draft

**Input**: All framework analyses and insights

**Actions**:

- Creates detailed section-by-section outline
- Writes complete first draft
- Integrates all framework analyses
- Generates proper APA citations
- Creates executive summary

**Output Files**:

- `04-writing/outlines/detailed-outline.md`
- `04-writing/drafts/complete-draft.md`
- `04-writing/citations/apa-references.md`
- `04-writing/drafts/executive-summary.md`

**Completion**: "Writing Coordinator Complete. Run AGENT 6 for final review."

### AGENT 6: Quality Controller

**Purpose**: Final review and submission preparation

**Input**: Complete draft and all supporting materials

**Actions**:

- Reviews complete assignment for quality
- Verifies framework applications
- Checks APA citation compliance
- Assesses academic writing standards
- Creates final submission package

**Output Files**:

- `05-final/submission/final-assignment.md`
- `05-final/supporting-materials/quality-report.md`
- `05-final/supporting-materials/submission-checklist.md`

**Completion**: "Quality Controller Complete. Assignment ready in 05-final/submission/"

## Usage Process

### Step 1: Project Setup

```bash
mba-setup
```

- Select existing course or create new
- Enter assignment details
- Choose required frameworks
- Charts/graphs required?: y/n
- Data tables required?: y/n
- Open project in VS Code?: y/n
- System creates complete structure

### Step 2: Assignment Configuration

- Edit `01-planning/instructions.md` with specific requirements
- Review framework selections
- Confirm source requirements

### Step 3: Sequential Agent Execution

1. **Project auto-opens** in VS Code (if selected)
2. **Open CLAUDE.md** for agent prompts
3. **Copy AGENT 1** prompt to Claude Code
4. **Wait for completion** message
5. **REVIEW** `02-research/planning-summary.md` - approve or request changes
6. **Collect sources** and place in source-files folders
7. **Run AGENT 2** through **AGENT 6** sequentially
8. **Final assignment** appears in `05-final/submission/`

### Step 4: Planning Review (After Agent 1)

- **Review** `02-research/planning-summary.md` thoroughly
- **Verify** assignment interpretation is correct
- **Check** framework approach is appropriate
- **Confirm** source strategy will meet requirements
- **Approve** or request modifications before proceeding

### Step 5: Source Collection (After Planning Approval)

- **Use generated search links**: Click direct URLs from `02-research/search-links.md`
- **Google Scholar links**: Pre-formatted academic search queries
- **Harvard Business Review**: Direct HBR case study and article searches
- **McKinsey/BCG/Bain**: Consulting firm insight searches (with Google backup)
- **Academic databases**: JSTOR, Business Source Premier, ProQuest links
- **Google search links**: Industry reports and company document searches
- **Backup searches**: Google fallback links when industry sites are blocked/paywalled
- **Download sources**: Save PDFs from search results
- Place files in appropriate source-files folders:
  - Academic PDFs → `02-research/academic-sources/source-files/`
  - Industry reports → `02-research/industry-sources/source-files/`

## Key Features

### Automation

- **Auto-extraction** of evidence from PDFs
- **Auto-application** of strategic frameworks
- **Auto-generation** of APA citations
- **Auto-creation** of complete academic drafts
- **Auto-quality** checking and compliance

### Framework Support

- Porter's Five Forces
- SWOT Analysis
- VRIO Framework
- PESTEL Analysis
- Value Chain Analysis
- Business Model Canvas
- McKinsey 7S

### Academic Standards

- **APA 7th Edition** formatting
- **MBA-level** academic writing
- **Peer-reviewed** source integration
- **Professional** presentation
- **Publication-quality** output

### File Management

- **Organized** folder structure
- **Version control** for drafts
- **Source separation** from analysis
- **Clear submission** package
- **Quality documentation**

## Benefits

### For Students

- **Time Efficiency**: Automated research extraction and framework application
- **Quality Assurance**: Built-in academic standards and compliance checking
- **Consistency**: Standardized approach across all assignments
- **Learning**: Proper framework application and academic writing

### For Academic Work

- **Rigorous Research**: Systematic source analysis and evidence extraction
- **Framework Mastery**: Proper application of strategic frameworks
- **Professional Output**: Publication-quality academic documents
- **Compliance**: APA formatting and citation standards

## Requirements

### Software

- **Claude Code** (VS Code extension)
- **Python 3.x** (for setup script)
- **macOS/Windows** with iCloud Drive (optional)

### Access

- **University library databases** for academic sources
- **Google Scholar** for research
- **Industry report** access
- **Claude Opus 4** recommended for writing tasks

## Troubleshooting

### Common Issues

- **Missing sources**: Ensure PDFs are in correct source-files folders
- **Agent not reading files**: Check file permissions and locations
- **Incomplete output**: Wait for full completion messages
- **Citation errors**: Review APA 7th edition requirements

### File Organization

- Keep raw sources separate from analysis
- Use clear naming conventions
- Follow folder structure exactly
- Don't modify agent-generated file locations

---

This workflow transforms MBA assignment completion from manual coordination to systematic, AI-enhanced academic production with professional quality outcomes.
