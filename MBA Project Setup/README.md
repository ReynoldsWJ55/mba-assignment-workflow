# MBA Assignment Workflow System

An automated MBA assignment completion system using a 6-agent sequential workflow with Claude Code. Creates publication-quality academic papers with systematic research, strategic framework application, and proper APA formatting.

## Features

### Core Capabilities
- **Sequential 6-Agent Workflow**: Systematic progression from research planning to final submission
- **Automated Source Discovery**: Pre-generated search links for academic and industry sources
- **Strategic Framework Integration**: Built-in support for major business analysis frameworks
- **Streamlined Project Structure**: Optimized folder organization with 43% fewer directories
- **Privacy-First Design**: Personal information stored in environment variables

### Academic Standards
- **APA 7th Edition Formatting**: Automatic citation generation and reference management
- **MBA-Level Analysis**: Professional academic writing standards throughout
- **Quality Assurance**: Built-in compliance checking and review processes
- **Source Verification**: Academic rigor with peer-reviewed and authoritative sources

## Quick Start

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd mba-assignment-workflow
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment**
   ```bash
   cp .env.example .env
   # Edit .env file with your personal directory paths
   ```

4. **Create your first project**
   ```bash
   python setup-mba-project.py
   ```

## Configuration

### Environment Variables

The system uses environment variables to keep personal information secure. Copy `.env.example` to `.env` and customize:

```bash
# Your MBA courses directory (optional)
MBA_COURSES_DIR="/Users/yourname/Library/Mobile Documents/com~apple~CloudDocs/YourUniversity"

# University name for folder detection
UNIVERSITY_NAME="YourUniversity" 

# Default working directory (optional)
DEFAULT_WORK_DIR="/Users/yourname/Documents/MBA"
```

### Project Structure

Each assignment creates a standardized directory structure optimized for the 6-agent workflow:

```
assignment01-ProjectName/
├── 01-planning/
│   ├── instructions.md          # Assignment requirements and specifications
│   ├── CLAUDE.md               # Complete agent workflow prompts
│   └── research-strategy.md     # Strategic research plan (requires user review)
├── 02-sources/
│   ├── search-links.md         # Direct and backup search URLs
│   ├── academic/
│   │   ├── files/              # Academic PDFs and papers
│   │   └── analysis/           # Source summaries and evidence extraction
│   └── industry/
│       ├── files/              # Industry reports and company documents
│       └── analysis/           # Professional source analysis
├── 03-frameworks/
│   ├── individual/             # Individual framework applications
│   └── synthesis.md            # Integrated strategic analysis
├── 04-writing/
│   ├── draft.md                # Complete assignment draft
│   ├── references.md           # APA 7th Edition citations
│   ├── visuals/                # Charts, graphs, and data tables
│   └── presentation.md         # Executive summary and key findings
└── 05-final/
    └── submission.md           # Final submission-ready document
```

## Workflow Process

### Step 1: Project Setup

Execute the setup script to create your assignment structure:

```bash
python setup-mba-project.py
```

The interactive setup will guide you through:
- **Directory Selection**: Choose course folder or create custom location
- **Assignment Configuration**: Enter details, due dates, and requirements
- **Framework Selection**: Choose from supported strategic frameworks
- **Visual Requirements**: Specify needs for charts, graphs, or data tables
- **Development Environment**: Option to auto-open in VS Code

### Step 2: Sequential Agent Execution

The system operates through six specialized agents that must be executed in order:

1. **Agent 1 (Research Director)**
   - Analyzes assignment requirements
   - Creates comprehensive research strategy
   - Generates automated search links for source collection

2. **Planning Review Phase**
   - User reviews and approves `research-strategy.md`
   - Ensures correct interpretation of assignment requirements

3. **Source Collection Phase**
   - Use generated search links to gather academic and industry sources
   - Place PDFs in designated folders for agent processing

4. **Agent 2 (Academic Scout)**
   - Analyzes collected sources
   - Creates structured templates for evidence extraction

5. **Agent 3 (Research Analyst)**
   - Extracts evidence from all source documents
   - Maps findings to strategic framework requirements

6. **Agent 4 (Framework Specialist)**
   - Applies each selected strategic framework systematically
   - Generates framework-specific analysis and insights

7. **Agent 5 (Writing Coordinator)**
   - Creates complete academic draft
   - Integrates all framework analyses
   - Generates APA citations and executive summary

8. **Agent 6 (Quality Controller)**
   - Performs comprehensive quality review
   - Ensures academic standards and compliance
   - Prepares final submission package

### Step 3: Automated Source Discovery

Agent 1 generates comprehensive search links for efficient source collection:

- **Academic Databases**: Google Scholar, JSTOR, Business Source Premier
- **Professional Publications**: Harvard Business Review, MIT Sloan Management Review
- **Consulting Insights**: McKinsey Quarterly, BCG Insights, Bain & Company
- **Industry Sources**: Company reports, annual statements, industry analyses
- **Backup Options**: Google fallback searches when direct links are unavailable

## Supported Strategic Frameworks

The system provides built-in support for major strategic analysis frameworks used in MBA programs:

### Core Frameworks
- **Porter's Five Forces**: Comprehensive industry competitive analysis examining supplier power, buyer power, competitive rivalry, threat of substitutes, and threat of new entrants
- **SWOT Analysis**: Strategic planning tool analyzing internal strengths and weaknesses alongside external opportunities and threats
- **VRIO Framework**: Resource-based view analysis evaluating Value, Rarity, Imitability, and Organizational factors for competitive advantage

### Advanced Frameworks
- **PESTEL Analysis**: Macro-environmental analysis covering Political, Economic, Social, Technological, Environmental, and Legal factors
- **Value Chain Analysis**: Systematic examination of primary and support activities that create competitive advantage
- **Business Model Canvas**: Nine building blocks framework for business model design and innovation
- **McKinsey 7S**: Organizational effectiveness model analyzing Strategy, Structure, Systems, Shared Values, Style, Staff, and Skills

## System Requirements

### Technical Dependencies
- **Python 3.7 or higher**: Core runtime environment
- **Claude Code**: VS Code extension for AI-assisted development
- **python-dotenv**: Environment variable management (installed via requirements.txt)

### Recommended Access
- **University Library Databases**: For access to academic journals and research papers
- **Google Scholar**: Free access to academic literature
- **Professional Publications**: Subscriptions to Harvard Business Review, McKinsey Quarterly (optional but beneficial)

## Benefits and Advantages

### Efficiency Improvements
- **Automated Research Pipeline**: Streamlined process from source discovery to final submission
- **Template-Based Analysis**: Consistent structure across all assignments
- **Integrated Citations**: Automatic APA 7th Edition formatting
- **Quality Assurance**: Built-in review processes and academic standards checking

### Academic Excellence
- **Professional Standards**: MBA-level analysis and writing throughout
- **Source Diversity**: Balanced mix of academic and industry perspectives
- **Framework Rigor**: Systematic application of strategic analysis tools
- **Comprehensive Output**: Complete packages ready for submission

## Privacy and Security

### Data Protection
- **Environment Variables**: All personal information stored in local `.env` files
- **Repository Safety**: No hardcoded personal data in source code
- **Configurable Paths**: University and personal directory information kept private
- **Public Repository Safe**: Designed for open-source sharing without privacy concerns

### Security Best Practices
- **Local Configuration**: Personal settings remain on your machine
- **No Data Transmission**: All processing occurs locally
- **Version Control Safe**: `.gitignore` prevents accidental personal data commits

## Contributing

We welcome contributions to improve the MBA Assignment Workflow System:

### Development Process
1. **Fork the Repository**: Create your own copy for development
2. **Create Feature Branch**: Isolate new features or improvements
3. **Maintain Privacy**: Ensure no personal information in commits
4. **Test Thoroughly**: Verify functionality across different environments
5. **Submit Pull Request**: Detailed description of changes and benefits

### Areas for Contribution
- Additional strategic frameworks
- Enhanced source discovery mechanisms
- Improved output formatting
- Documentation and examples
- Bug fixes and performance improvements

## License and Usage

This project is released under the MIT License, providing broad permissions for use, modification, and distribution.

### Academic Integrity Notice

This system is designed to enhance and streamline academic work while maintaining the highest standards of academic integrity. Users are responsible for:

- **Proper Attribution**: All sources must be correctly cited and referenced
- **Original Analysis**: Framework applications and insights must be your own work
- **Institutional Compliance**: Adherence to your university's academic policies
- **Quality Standards**: Maintaining the academic rigor expected in MBA programs

The system automates research organization and formatting but requires original thinking, analysis, and interpretation from the user.