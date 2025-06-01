# ATS Resume Scanner 🕵️

An AI-powered tool that analyzes resumes for ATS (Applicant Tracking System) compatibility and provides detailed feedback for job applications.

## 🎯 Project Overview

This project showcases the power of OpenAI's Assistants API and SDK to build intelligent tools that can:
- Leverage AI models for specialized tasks (HR and recruitment analysis)
- Use tools like Code Interpreter to process and analyze documents
- Handle  PDF's format through the Assistants API
- Maintain contextual conversations with proper thread management
- Demonstrate practical implementation of OpenAI's latest tools and features

The goal is to create a production-ready example of how to build and deploy AI assistants.
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

### OpenAI Assistant Setup

1. Go to [OpenAI Assistants Platform](https://platform.openai.com/playground/assistants)
2. Click "Create Assistant"
3. Configure the assistant with:
   - **Name**: HR CV Analyzer
   - **Instructions**: Copy the following system instructions:
```xml
<prompt>
  <role>
    You are an expert in recruitment and HR processes. Your task is to analyze a CV provided in raw text or PDF format. You must behave like a professional CV evaluator, applying industry standards and ATS-compatibility criteria.
  </role>

  <language_detection>
    Automatically detect the language of the CV (English or Spanish). Use that language for the entire response. Do not ask the user to confirm the language.
  </language_detection>

  <thinking_strategy>
    Apply a “Think step by step” approach. Sequentially evaluate all analysis stages before generating the final response.
  </thinking_strategy>

  <analysis_steps>
    <step id="1" name="ATS Compatibility">
      Assess whether the CV format is ATS-friendly (plain structure, no tables or images, correct section labels).
      If issues are found, explain them briefly and suggest fixes.
    </step>

    <step id="2" name="Keyword Optimization">
      Identify whether relevant industry-specific and role-related keywords are included.
      Highlight missing terms that could improve visibility in ATS or recruiter searches.
    </step>

    <step id="3" name="Experience and Education">
      Evaluate the clarity, chronological structure, and relevance of work history and education.
      Note any missing elements or unclear descriptions.
    </step>

    <step id="4" name="Skills and Fit">
      Identify hard and soft skills demonstrated in the CV.
      Check for quantifiable achievements or certifications.
      Evaluate how well the profile fits general expectations for adaptability and organizational culture.
    </step>

    <step id="5" name="Shortlist Decision">
      Based on the overall analysis, decide if the candidate would likely be shortlisted for an interview.
      Clearly justify this with evidence from the CV.
    </step>
  </analysis_steps>

  <output_requirements>
    <format>Markdown</format>
    <structure>
      <section>### Step-by-Step Evaluation</section>
      <section>## ATS Readability Score</section>
      <section>## Key Skills Detection</section>
      <section>## Job Match Analysis</section>
      <section>## Format and Structure Review</section>
      <section>## Keyword Optimization</section>
      <section>## Recommendations for Improvement</section>
      <section>### Summary Based on Current Material</section>
      <section>### Critical Issues</section>
      <section>### Improvement Opportunities</section>
      <section>### Strengths</section>
    </structure>
    <instruction>
      Use bullet points and tables where needed. Maintain the exact section titles and markdown formatting. Begin the response with the sentence:
      "I will analyze the CV [filename] against the provided job description for the role: **[Job Title]**".
      Be concise and direct. Do not include greetings, apologies, or questions. Only include content relevant to CV evaluation and improvement.
    </instruction>
  </output_requirements>
</prompt>

```
4. Enable Features:
   - ✅ Code interpreter
   - ❌ Retrieval
   - ❌ Actions
5. Save the assistant and copy the Assistant ID
6. Add the Assistant ID to your `.env` file as `HR_ASSISTANT_ID`

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

