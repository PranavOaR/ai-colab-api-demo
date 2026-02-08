# 🤖 AI Colab API Demo

A comprehensive, student-friendly project demonstrating how to use Google's Gemini AI API inside Google Colab for real-world applications including text generation and data analysis.

## 📚 Available Notebooks - Description 

### 1. Text Generation Demo
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/PranavOaR/ai-colab-api-demo/blob/main/notebooks/gemini_text_generation_demo.ipynb)

Learn the fundamentals of AI text generation, summarization, and code explanation.

### 2. Data Analysis Demo - Recommended
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/PranavOaR/ai-colab-api-demo/blob/main/notebooks/ai_data_analysis_demo.ipynb)

Discover how AI can analyze datasets, generate insights, and create automated reports.

## 📌 What This Project Does

This project teaches students how to integrate AI into their Colab notebooks with two practical demonstrations:

**Notebook 1: Text Generation**
- Secure API key setup in Google Colab
- Using Gemini for text summarization
- AI-powered code explanation
- Error handling and fallback strategies

**Notebook 2: Data Analysis**
- Creating and visualizing datasets
- Using AI to analyze data patterns
- Generating automated reports
- Asking AI specific questions about data

## 🚀 How to Use

### Option 1: Open Directly in Google Colab (Recommended)
1. Click any "Open in Colab" badge above
2. The notebook will open directly in Google Colab
3. Follow the instructions in the notebook to set up your API key
4. Run each cell step-by-step to see AI in action

### Option 2: Clone and Upload
1. Clone this repository:
   ```bash
   git clone https://github.com/PranavOaR/ai-colab-api-demo.git
   ```
2. Open [Google Colab](https://colab.research.google.com/)
3. Click File → Upload Notebook
4. Upload any notebook from the `notebooks/` folder

## 🔑 Getting Your API Key

1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Click "Get API Key" or "Create API Key"
3. Copy your API key
4. In Colab, click the 🔑 key icon (Secrets) in the left sidebar
5. Add a new secret named `GEMINI_API_KEY` with your API key as the value
6. Enable "Notebook access"

⚠️ **Important:** Never share your API key publicly or hardcode it in notebooks!

## 🤖 Where AI is Being Used

This project uses **Google Gemini AI** (`gemini-1.5-flash` model) for multiple practical applications:

### In Text Generation Notebook:
- **Text Summarization**: Condenses long paragraphs into concise summaries
- **Code Explanation**: Analyzes and explains code functionality in simple terms
- **Creative Generation**: Creates poems, stories, or custom text responses
- **Educational Support**: Provides instant explanations for learning

### In Data Analysis Notebook:
- **Data Interpretation**: Analyzes statistical summaries and identifies patterns
- **Insight Generation**: Extracts meaningful insights from datasets
- **Report Automation**: Generates professional reports from raw data
- **Q&A System**: Answers specific questions about data trends

All notebooks include error handling and fallback strategies to ensure reliability.

## 📝 Workflow Summary

**How This Project Works:**
1. **Install Dependencies**: Install the Google Generative AI package in Colab
2. **Configure API**: Securely retrieve the Gemini API key from Colab Secrets
3. **Initialize Model**: Create a Gemini client instance for AI operations
4. **Create Prompts**: Write clear instructions telling the AI what to generate/analyze
5. **Generate Responses**: Call the API and receive AI-generated outputs
6. **Display Results**: Show outputs with visualizations (for data analysis)

**Technical Stack:**
- **Platform**: Google Colab (cloud-based Jupyter notebooks)
- **AI Model**: Google Gemini 1.5 Flash
- **Languages**: Python
- **Key Libraries**: `google-genai`, `pandas`, `matplotlib`

## 📂 Project Structure

```
ai-colab-api-demo/
│
├── notebooks/
│   ├── gemini_text_generation_demo.ipynb    # Text generation & summarization
│   ├── ai_data_analysis_demo.ipynb          # Data analysis with AI
│   └── template.ipynb                       # Blank template for projects
│
├── assets/                                   # Images and resources
│
├── create_new_notebook.py                   # Script to generate notebooks
│
└── README.md                                 # Project documentation
```

## 🎓 Learning Objectives

After completing this project, students will understand:

- How to integrate external APIs into Colab notebooks
- The importance of API key security and best practices
- How to structure effective prompts for better AI responses
- Practical applications of AI in education, data science, and coding
- How to debug and troubleshoot API connections
- Combining AI with data visualization for insights
- Creating automated reports and analysis workflows

## 🛠️ Requirements

- A Google account (for Colab access)
- A Gemini API key (free tier available)
- Basic Python knowledge (helpful but not required)

## 💡 Ideas for Extension

**Text Generation:**
- Add language translation features
- Create a chatbot interface
- Build a study assistant for specific subjects
- Generate practice problems and solutions

**Data Analysis:**
- Analyze real-world datasets (weather, sports, finance)
- Create predictive models with AI insights
- Build interactive dashboards
- Compare multiple AI model responses
- Implement sentiment analysis on text data

## 📚 Resources

- [Google AI Studio](https://ai.google.dev/)
- [Gemini API Documentation](https://ai.google.dev/docs)
- [Google Colab Tutorial](https://colab.research.google.com/)

## 🤝 Contributing

Feel free to fork this project and add your own examples! Students are encouraged to:
- Add new use cases
- Improve documentation
- Share interesting prompts
- Report issues or bugs

## 📄 License

This project is open source and available for educational purposes.

---

**Made with ❤️ for students learning AI**
