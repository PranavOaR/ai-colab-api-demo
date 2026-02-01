#!/usr/bin/env python3
import json

notebook = {
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "# 🤖 Gemini Text Generation Demo\\n",
        "\\n",
        "Welcome! This notebook shows you how to use Google's Gemini AI to generate text.\\n",
        "\\n",
        "**What you'll learn:**\\n",
        "- How to set up the Gemini API in Colab\\n",
        "- How to generate text using AI\\n",
        "- How to use AI for summarization and code explanation\\n",
        "\\n",
        "---"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "## Step 1: Install the NEW Gemini SDK\\n",
        "\\n",
        "⚠️ **Important:** We're using the NEW `google-genai` package (not the old `google-generativeai`).\\n",
        "\\n",
        "First, let's clean up old packages and install the correct one."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": None,
      "metadata": {},
      "outputs": [],
      "source": [
        "# Remove old Gemini packages that cause 404 errors\\n",
        "!pip uninstall -y google-generativeai google-ai-generativelanguage 2>/dev/null\\n",
        "\\n",
        "# Install the NEW official Gemini SDK\\n",
        "!pip install -U -q google-genai\\n",
        "\\n",
        "print(\\\"✅ New Gemini SDK installed!\\\")"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "⚠️ **IMPORTANT: After running the cell above, you MUST:**\\n",
        "\\n",
        "1. Click **Runtime → Restart runtime** in the top menu\\n",
        "2. This clears cached imports and prevents errors\\n",
        "3. Then continue running the cells below\\n",
        "\\n",
        "Without restarting, you'll get import errors!"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "## Step 2: Import Libraries\\n",
        "\\n",
        "Now let's import the NEW Gemini SDK."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": None,
      "metadata": {},
      "outputs": [],
      "source": [
        "# Import the NEW Gemini SDK (not google.generativeai!)\\n",
        "from google import genai\\n",
        "from google.colab import userdata\\n",
        "\\n",
        "print(\\\"✅ Libraries imported successfully!\\\")"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "## Step 3: Set Up Your API Key (Securely!)\\n",
        "\\n",
        "**How to get your Gemini API key:**\\n",
        "1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)\\n",
        "2. Click \\\"Get API Key\\\" or \\\"Create API Key\\\"\\n",
        "3. Copy your API key\\n",
        "\\n",
        "**How to add it securely in Colab:**\\n",
        "1. Click the 🔑 key icon on the left sidebar (Secrets)\\n",
        "2. Click \\\"+ Add new secret\\\"\\n",
        "3. Name it: `GEMINI_API_KEY`\\n",
        "4. Paste your API key as the value\\n",
        "5. Toggle on \\\"Notebook access\\\"\\n",
        "\\n",
        "⚠️ **Never hardcode your API key directly in the notebook!**"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": None,
      "metadata": {},
      "outputs": [],
      "source": [
        "# Retrieve the API key securely from Colab Secrets\\n",
        "api_key = userdata.get('GEMINI_API_KEY')\\n",
        "\\n",
        "# Create the NEW Gemini client (not genai.configure!)\\n",
        "client = genai.Client(api_key=api_key)\\n",
        "\\n",
        "print(\\\"✅ Gemini client configured successfully!\\\")"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "## Step 4: Create a Safe AI Helper Function\\n",
        "\\n",
        "Let's create a helper function that calls Gemini and handles errors gracefully."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": None,
      "metadata": {},
      "outputs": [],
      "source": [
        "def ask_gemini(prompt, fallback_text=\\\"AI is temporarily unavailable.\\\"):\\n",
        "    \\\"\\\"\\\"\\n",
        "    Safe wrapper to call Gemini AI.\\n",
        "    If Gemini fails, returns fallback text instead of crashing.\\n",
        "    \\n",
        "    Args:\\n",
        "        prompt: The question or task for Gemini\\n",
        "        fallback_text: Text to return if Gemini fails\\n",
        "    \\n",
        "    Returns:\\n",
        "        AI response text or fallback text\\n",
        "    \\\"\\\"\\\"\\n",
        "    try:\\n",
        "        # Call the NEW Gemini API\\n",
        "        response = client.models.generate_content(\\n",
        "            model='gemini-1.5-flash',  # Stable, supported model\\n",
        "            contents=prompt\\n",
        "        )\\n",
        "        return response.text\\n",
        "    \\n",
        "    except Exception as e:\\n",
        "        # Never crash - return fallback instead\\n",
        "        print(f\\\"⚠️ Gemini unavailable: {str(e)}\\\")\\n",
        "        return fallback_text\\n",
        "\\n",
        "print(\\\"✅ Helper function ready!\\\")"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "## Step 5: Example 1 - Summarize a Paragraph\\n",
        "\\n",
        "Let's use Gemini to summarize a long paragraph into a short, simple explanation."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": None,
      "metadata": {},
      "outputs": [],
      "source": [
        "# Sample paragraph to summarize\\n",
        "paragraph = \\\"\\\"\\\"\\n",
        "Artificial intelligence (AI) is intelligence demonstrated by machines, \\n",
        "in contrast to the natural intelligence displayed by humans and animals. \\n",
        "Leading AI textbooks define the field as the study of \\\\\\\"intelligent agents\\\\\\\": \\n",
        "any device that perceives its environment and takes actions that maximize its \\n",
        "chance of successfully achieving its goals. Colloquially, the term \\\\\\\"artificial \\n",
        "intelligence\\\\\\\" is often used to describe machines that mimic \\\\\\\"cognitive\\\\\\\" functions \\n",
        "that humans associate with the human mind, such as \\\\\\\"learning\\\\\\\" and \\\\\\\"problem solving\\\\\\\".\\n",
        "\\\"\\\"\\\"\\n",
        "\\n",
        "# Create the prompt\\n",
        "prompt = f\\\"Summarize this paragraph in 2 simple sentences:\\\\n\\\\n{paragraph}\\\"\\n",
        "\\n",
        "# Call Gemini using our safe wrapper\\n",
        "fallback = \\\"AI can understand and process language to perform tasks like summarization. It mimics human thinking to solve problems.\\\"\\n",
        "summary = ask_gemini(prompt, fallback)\\n",
        "\\n",
        "# Display the results\\n",
        "print(\\\"📝 Original Paragraph:\\\")\\n",
        "print(paragraph)\\n",
        "print(\\\"\\\\n\\\" + \\\"=\\\"*50 + \\\"\\\\n\\\")\\n",
        "print(\\\"✨ AI Summary:\\\")\\n",
        "print(summary)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "## Step 6: Example 2 - Explain Code\\n",
        "\\n",
        "Let's ask Gemini to explain what a piece of code does."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": None,
      "metadata": {},
      "outputs": [],
      "source": [
        "# Sample code to explain\\n",
        "code = \\\"\\\"\\\"\\n",
        "def bubble_sort(arr):\\n",
        "    n = len(arr)\\n",
        "    for i in range(n):\\n",
        "        for j in range(0, n-i-1):\\n",
        "            if arr[j] > arr[j+1]:\\n",
        "                arr[j], arr[j+1] = arr[j+1], arr[j]\\n",
        "    return arr\\n",
        "\\\"\\\"\\\"\\n",
        "\\n",
        "# Create the prompt\\n",
        "prompt = f\\\"Explain what this Python code does in simple terms:\\\\n\\\\n{code}\\\"\\n",
        "\\n",
        "# Call Gemini using our safe wrapper\\n",
        "fallback = \\\"This code implements bubble sort, which repeatedly compares adjacent elements and swaps them if they're in wrong order to sort the array.\\\"\\n",
        "explanation = ask_gemini(prompt, fallback)\\n",
        "\\n",
        "# Display the results\\n",
        "print(\\\"💻 Code:\\\")\\n",
        "print(code)\\n",
        "print(\\\"\\\\n\\\" + \\\"=\\\"*50 + \\\"\\\\n\\\")\\n",
        "print(\\\"✨ AI Explanation:\\\")\\n",
        "print(explanation)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "## Step 7: Try Your Own Prompt!\\n",
        "\\n",
        "Now it's your turn! Modify the prompt below and see what Gemini generates."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": None,
      "metadata": {},
      "outputs": [],
      "source": [
        "# Try your own prompt here!\\n",
        "your_prompt = \\\"Write a short poem about machine learning.\\\"\\n",
        "\\n",
        "# Call Gemini using our safe wrapper\\n",
        "fallback = \\\"Machine learning, so bright and keen, Teaching computers what you've seen...\\\"\\n",
        "response_text = ask_gemini(your_prompt, fallback)\\n",
        "\\n",
        "# Display the result\\n",
        "print(\\\"✨ AI Response:\\\")\\n",
        "print(response_text)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "## 🎉 Congratulations!\\n",
        "\\n",
        "You've successfully learned how to:\\n",
        "- Set up the NEW Gemini SDK in Google Colab\\n",
        "- Use AI to generate text safely with error handling\\n",
        "- Summarize paragraphs and explain code with AI\\n",
        "\\n",
        "### What's Next?\\n",
        "- Try different prompts and see how the AI responds\\n",
        "- Check the [Gemini documentation](https://ai.google.dev/)\\n",
        "- Build your own AI-powered projects!\\n",
        "\\n",
        "---\\n",
        "\\n",
        "**Questions or issues?** Check the [GitHub repository](https://github.com/PranavOaR/ai-colab-api-demo) for more information."
      ]
    }
  ],
  "metadata": {
    "kernelspec": {
      "display_name": "Python 3",
      "language": "python",
      "name": "python3"
    },
    "language_info": {
      "codemirror_mode": {
        "name": "ipython",
        "version": 3
      },
      "file_extension": ".py",
      "mimetype": "text/x-python",
      "name": "python",
      "nbconvert_exporter": "python",
      "pygments_lexer": "ipython3",
      "version": "3.10.0"
    },
    "colab": {
      "provenance": []
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}

with open('notebooks/gemini_text_generation_demo.ipynb', 'w') as f:
    json.dump(notebook, f, indent=2)

print("✅ Successfully created NEW gemini SDK notebook!")
print("📦 Package: google-genai")
print("🔧 API: genai.Client + client.models.generate_content")  
print("🚀 Model: gemini-1.5-flash")
