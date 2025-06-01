# ATS Resume Scanner 🕵️

An AI-powered tool that analyzes resumes for ATS (Applicant Tracking System) compatibility and provides detailed feedback for job applications.

## 🎯 Features

- **ATS Compatibility Analysis**: Evaluates how well your resume will perform with ATS systems
- **Skills Detection**: Identifies and extracts key skills from your resume
- **Job Matching**: Analyzes resume compatibility with specific job descriptions
- **Format Review**: Checks resume structure and formatting
- **Keyword Optimization**: Suggests improvements for better keyword matching
- **Actionable Recommendations**: Provides specific suggestions for improvement

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- OpenAI API key
- uv package manager (for dependency management)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/ats-cv.git
cd ats-cv
```

2. Install uv if you haven't already:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

3. Create virtual environment and install dependencies:
```bash
uv venv
uv pip install streamlit openai python-dotenv PyPDF2
```

4. Create a `.env` file in the project root and add your OpenAI API key:
```env
OPENAI_API_KEY=your_api_key_here
HR_ASSISTANT_ID=your_assistant_id_here
```

### Running the Application

1. Start the Streamlit server:
```bash
streamlit run main.py
```

2. Open your browser and navigate to `http://localhost:8501`

## 📝 How to Use

1. **Upload Resume**: Click "Upload your CV" and select a PDF file
2. **Enter Job Details**: 
   - Input the target job position (optional)
   - Paste the job description (optional)
3. **Analyze**: Click "Analyze Resume" to get detailed feedback

## 🛠️ Technical Stack

- **Frontend**: Streamlit
- **Backend**: Python
- **AI/ML**: OpenAI API
- **File Processing**: PyPDF2
- **Environment**: python-dotenv

## 📋 Analysis Components

The tool provides analysis in six key areas:
1. ATS Readability Score
2. Key Skills Detection
3. Job Match Analysis
4. Format and Structure Review
5. Keyword Optimization
6. Recommendations for Improvement

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- OpenAI for providing the API
- Streamlit for the wonderful web framework
- All contributors and users of this tool

