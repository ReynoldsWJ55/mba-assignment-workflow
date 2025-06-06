# CLAUDE.md

This file provides guidance to Claude Code when working with the MBA Assignment Workflow system.

## Project Overview

**Purpose**: Automated MBA assignment completion using a 6-agent sequential workflow
**Output**: Publication-quality academic papers with proper research, framework application, and APA formatting
**Target Users**: MBA students requiring systematic, high-quality assignment completion

## Working with This Codebase

### Initial Setup Commands

```bash
# Install the MBA project setup script
rm ~/setup-mba-project.py
curl -s https://gist.githubusercontent.com/anthropic/claude-mba-workflow/main/setup-mba-project.py > ~/setup-mba-project.py
chmod +x ~/setup-mba-project.py

# Create convenient alias
echo 'alias mba-setup="python3 ~/setup-mba-project.py"' >> ~/.zshrc
source ~/.zshrc

# Create new project
mba-setup
```

### Project Creation Process

1. **Run setup script**: Detects existing courses in iCloud Drive/Stamford
2. **Configure assignment**: Enter course code, assignment details, frameworks
3. **Specify requirements**: Charts/graphs needed, data tables required
4. **Generate structure**: Creates complete folder hierarchy and agent prompts
5. **Auto-open option**: Opens project in VS Code automatically
6. **Ready for workflow**: All templates and guides generated automatically

## Architecture & Design Patterns

### Sequential Agent Pattern

The system implements a strict sequential workflow where each agent has specific responsibilities and dependencies:

```mermaid
graph LR
    A[Research Director] --> B[Collect Sources]
    B --> C[Academic Scout]
    C --> D[Research Analyst]
    D --> E[Framework Specialist]
    E --> F[Writing Coordinator]
    F --> G[Quality Controller]
    G --> H[Final Submission]
```

**Critical**: Each agent MUST complete before the next begins. Wait for completion messages.

### Simplified Folder Structure

```
assignment01-ProjectName/
├── 01-planning/
│   ├── instructions.md          # Assignment requirements
│   ├── CLAUDE.md               # Agent workflow prompts
│   └── research-strategy.md     # 🔍 USER REVIEW (Agent 1 output)
├── 02-sources/
│   ├── search-links.md         # 🔗 Direct + backup search URLs
│   ├── academic/
│   │   ├── files/              # 📁 USER PLACES PDFs HERE
│   │   └── analysis/           # 🤖 Summaries + evidence
│   └── industry/
│       ├── files/              # 📁 USER PLACES REPORTS HERE
│       └── analysis/           # 🤖 Summaries + evidence
├── 03-frameworks/
│   ├── individual/             # 🤖 PESTEL, Porter's, SWOT, VRIO
│   └── synthesis.md            # 🤖 Combined strategic insights
├── 04-writing/
│   ├── draft.md                # 🤖 Complete assignment
│   ├── references.md           # 🤖 APA citations
│   ├── visuals/                # 📊 Charts + tables (if required)
│   └── presentation.md         # 🤖 Executive summary
└── 05-final/
    └── submission.md           # 🎯 READY FOR SUBMISSION
```

**Key**: 📁 = User input required, 🤖 = Agent-generated, 🔗 = Clickable search links, 🔍 = User review required, 📊 = Charts/graphs, 📋 = Data tables, 🎯 = Final deliverable

## Agent Execution Guidelines

### Agent 1: Research Director

**Role**: Strategic planning and research design
**Dependencies**: Assignment instructions in `01-planning/instructions.md`
**Outputs**: Research plan, source requirements, collection strategy with direct search links, comprehensive planning document for user review
**Critical Actions**:

- Read and analyze assignment requirements thoroughly
- Map required frameworks to specific evidence needs
- Create comprehensive source collection strategy with clickable search URLs
- Generate Google Scholar and Google search links for each evidence category
- Generate Harvard Business Review, McKinsey, BCG, and other authoritative MBA source links
- Create database-specific search URLs (JSTOR, Business Source Premier, etc.)
- Generate backup Google search links for industry sources (in case direct links fail)
- Generate comprehensive planning document summarizing approach for user review
- Generate clear guidance for subsequent agents

### Agent 2: Academic Scout

**Role**: Source analysis and template creation
**Dependencies**: Sources placed in `source-files/` folders by user
**Outputs**: Analysis templates, quality assessment, extraction guides
**Critical Actions**:

- Scan both academic and industry source-files folders using LS tool
- Create individual templates for each source based on filename analysis
- Generate quality criteria and extraction roadmaps
- Prepare structured approach for evidence extraction
- **Important**: Do NOT attempt to read PDF files directly - use filename information only

### Agent 3: Research Analyst

**Role**: Evidence extraction and synthesis
**Dependencies**: Source files and templates from Agent 2
**Outputs**: Source summaries, evidence mapping, research synthesis
**Critical Actions**:

- Use Read tool to analyze ALL PDFs/documents in source-files folders
- Extract framework-specific evidence systematically using proper PDF reading capabilities
- Create detailed summaries maintaining academic rigor
- Map evidence to specific framework components
- **Important**: Use Read tool for PDF files - it can handle binary files including PDFs

### Agent 4: Framework Specialist

**Role**: Strategic framework application
**Dependencies**: Research synthesis and evidence mapping from Agent 3
**Outputs**: Individual framework analyses, integrated insights, recommendations
**Critical Actions**:

- Apply each required framework using extracted evidence
- Ensure proper theoretical grounding and application
- Generate integrated strategic insights
- Develop evidence-based recommendations

### Agent 5: Writing Coordinator

**Role**: Academic writing and document creation
**Dependencies**: All framework analyses from Agent 4
**Outputs**: Complete draft, outline, citations, executive summary, charts/graphs, data tables
**Critical Actions**:

- Create MBA-level academic writing
- Integrate all framework analyses coherently
- Generate proper APA 7th Edition citations
- Create charts/graphs and data tables (if required)
- Maintain professional academic standards throughout

### Agent 6: Quality Controller

**Role**: Final review and submission preparation
**Dependencies**: Complete draft from Agent 5
**Outputs**: Final submission package, quality reports, compliance verification
**Critical Actions**:

- Comprehensive quality review against academic standards
- Verify framework applications are complete and accurate
- Ensure APA compliance and citation accuracy
- Create submission-ready package with documentation

## Supported Strategic Frameworks

### Primary Frameworks

- **Porter's Five Forces**: Industry competitive analysis
- **SWOT Analysis**: Internal/external strategic factors
- **VRIO Framework**: Resource-based competitive advantage
- **PESTEL Analysis**: Macro-environmental factors
- **Value Chain Analysis**: Activity-based competitive advantage

### Advanced Frameworks

- **Business Model Canvas**: Business model innovation
- **McKinsey 7S**: Organizational effectiveness

## Authoritative MBA Sources (Auto-Generated Links)

### Academic & Professional Publications

- **Harvard Business Review**: Case studies, strategy articles, leadership insights
- **MIT Sloan Management Review**: Research-based management insights
- **Stanford Business**: Innovation and entrepreneurship focus
- **McKinsey Quarterly**: Strategy consulting insights and research
- **BCG Insights**: Management consulting perspectives
- **Bain & Company**: Strategic consulting reports
- **Deloitte Insights**: Industry analysis and trends

### Academic Databases

- **JSTOR**: Peer-reviewed academic journals
- **Business Source Premier**: Comprehensive business database
- **ProQuest**: Academic research and dissertations
- **SAGE Business Cases**: Real-world case studies
- **Emerald Insight**: Business and management research

## File Management Rules

### Critical File Locations

```bash
# User must place sources here:
02-research/academic-sources/source-files/     # Academic PDFs
02-research/industry-sources/source-files/    # Industry reports

# Agent 1 generates search links here:
02-research/search-links.md                    # Direct + backup Google search URLs

# Agents generate analysis here:
02-research/*/summaries/                       # Source summaries
03-analysis/framework-applications/            # Framework analyses
04-writing/drafts/                            # Writing outputs

# Final deliverables appear here:
05-final/submission/                          # Ready for submission
```

### Search Links Format (Generated by Agent 1)

```markdown
## Industry Sources

### McKinsey Quarterly
- Direct: https://mckinsey.com/search?q=netflix+strategy
- **Backup Google**: https://google.com/search?q=site:mckinsey.com+"netflix+strategy"

### Harvard Business Review  
- Direct: https://hbr.org/search?term=streaming+industry
- **Backup Google**: https://google.com/search?q=site:hbr.org+"streaming+industry"
```

### File Naming Conventions

- **Academic sources**: `author-year-title.pdf`
- **Industry sources**: `organization-year-report-title.pdf`
- **Draft versions**: `draft-v1-complete.md`, `draft-v2-revised.md`
- **Framework files**: `porter-five-forces-analysis.md`, `swot-analysis.md`

### Quality Standards

- **APA 7th Edition**: All citations and references
- **MBA-level writing**: Professional academic standards
- **Source verification**: Quality assessment for all sources
- **Version control**: Tracked changes and improvements
- **Submission package**: Complete, compliant, ready-to-submit

## Best Practices for Claude Code

### When Working with This System

1. **Read the full project structure** before starting any agent
2. **Check for existing files** that agents should build upon
3. **Follow the sequential order** - never skip ahead in the workflow
4. **Wait for completion messages** before proceeding to next agent
5. **Verify file placement** - ensure sources are in correct locations

### PDF File Handling

**Agent 2 (Academic Scout)**:
- Use LS tool to scan source-files folders
- Create templates based on filename analysis only
- Do NOT attempt to read PDF content directly

**Agent 3 (Research Analyst)**:
- Use Read tool for all PDF analysis - it handles binary files including PDFs
- Do NOT use basic file reading commands like cat or head
- Read tool will display PDF content in readable format

### Error Prevention

- **Source placement**: Always check source-files folders exist and contain files
- **Template completion**: Ensure each agent completes all required outputs
- **Framework coverage**: Verify all required frameworks are properly applied
- **Citation accuracy**: Maintain APA 7th Edition standards throughout
- **File organization**: Never modify the established folder structure

### Output Quality

- **Academic rigor**: Maintain MBA-level analysis throughout
- **Evidence-based**: All conclusions must be supported by source evidence
- **Professional presentation**: Error-free, well-formatted documents
- **Comprehensive coverage**: Address all assignment requirements thoroughly
- **Integration**: Seamlessly connect research, analysis, and writing phases

## Common Troubleshooting

### Agent Not Finding Sources

- Verify PDFs are in correct `source-files/` folders
- Check file permissions and accessibility
- Ensure files are not corrupted or password-protected

### Incomplete Framework Analysis

- Confirm all required frameworks are specified in instructions
- Verify evidence extraction completed successfully
- Check that research synthesis contains sufficient data

### Citation or Formatting Issues

- Review APA 7th Edition requirements
- Verify all sources have complete bibliographic information
- Check that in-text citations match reference list

### Quality Control Failures

- Ensure all previous agents completed successfully
- Verify assignment requirements are fully addressed
- Check that academic writing standards are maintained

This system transforms manual assignment completion into a systematic, AI-enhanced academic production pipeline that consistently delivers publication-quality results.
