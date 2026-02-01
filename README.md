# 🤖 AI Colab API Demo

A student-friendly project demonstrating how to use Google's Gemini AI API inside Google Colab for text generation tasks.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/PranavOaR/ai-colab-api-demo/blob/main/notebooks/gemini_text_generation_demo.ipynb)

## 📌 What This Project Does

This project teaches students how to integrate AI into their Colab notebooks. It demonstrates:

- How to securely set up API keys in Google Colab
- How to use Google's Gemini API for text generation
- Practical examples like paragraph summarization and code explanation
- Best practices for working with AI APIs in educational settings

## 🚀 How to Use

### Option 1: Open in Google Colab (Recommended)
1. Click the "Open in Colab" badge above
2. The notebook will open directly in Google Colab
3. Follow the instructions in the notebook to set up your API key
4. Run each cell step-by-step

### Option 2: Clone and Upload
1. Clone this repository:
   ```bash
   git clone https://github.com/PranavOaR/ai-colab-api-demo.git
   ```
2. Open [Google Colab](https://colab.research.google.com/)
3. Click File → Upload Notebook
4. Upload `notebooks/gemini_text_generation_demo.ipynb`

## 🔑 Getting Your API Key

1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Click "Get API Key" or "Create API Key"
3. Copy your API key
4. In Colab, click the 🔑 key icon (Secrets) in the left sidebar
5. Add a new secret named `GEMINI_API_KEY` with your API key as the value
6. Enable "Notebook access"

⚠️ **Important:** Never share your API key publicly or hardcode it in notebooks!

## 🤖 Where AI is Being Used

This project uses **Google Gemini AI** for natural language processing tasks:

- **Text Summarization**: The AI condenses long paragraphs into concise summaries
- **Code Explanation**: The AI analyzes and explains what code does in simple terms
- **Creative Text Generation**: The AI generates poems, stories, or custom responses
- **Educational Support**: Students can ask questions and get instant explanations

The AI model used is `gemini-pro`, which is designed for text-based tasks and conversations.

## 📝 Workflow Summary

1. **Install Dependencies**: Install the Google Generative AI package in Colab
2. **Configure API**: Securely retrieve the Gemini API key from Colab Secrets
3. **Initialize Model**: Create a Gemini Pro model instance for text generation
4. **Create Prompts**: Write clear instructions telling the AI what to generate
5. **Generate Responses**: Call the API and receive AI-generated text
6. **Display Results**: Show the outputs and experiment with different prompts

## 📂 Project Structure

```
ai-colab-api-demo/
│
├── notebooks/
│   └── gemini_text_generation_demo.ipynb    # Main demo notebook
│
├── assets/                                   # Store images or resources
│
└── README.md                                 # Project documentation
```

## 🎓 Learning Objectives

After completing this project, students will understand:

- How to integrate external APIs into Colab notebooks
- The importance of API key security
- How to structure prompts for better AI responses
- Practical applications of AI in education and coding
- How to debug and troubleshoot API connections

## 🛠️ Requirements

- A Google account (for Colab access)
- A Gemini API key (free tier available)
- Basic Python knowledge (helpful but not required)

## 💡 Ideas for Extension

- Add more examples (translation, question answering, etc.)
- Create a chatbot interface
- Compare responses from different AI models
- Build a study assistant that explains difficult concepts
- Generate practice problems and solutions

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
