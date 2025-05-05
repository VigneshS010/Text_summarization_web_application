# Text Summarization App

A Streamlit-based application that generates summaries from URLs, PDFs, or manual text input using the Long-T5 summarization model.

## Installation

1. **Prerequisites**:  
   - Python 3.7+  
   - pip package manager  

2. **Install dependencies**:  
   ```bash
   pip install streamlit newspaper3k PyPDF2 transformers torch
   ```

## Usage

1. **Run the app**:  
   ```bash
   streamlit run app.py
   ```

2. **Select a text source**:  
   - **URL**: Enter a valid article URL.  
   - **PDF**: Upload a PDF file.  
   - **Manual Input**: Paste text directly.  

3. Click the **Summarize** button to generate a condensed summary (50-250 words).  

## Contributing

1. Fork the repository.  
2. Create a feature branch:  
   ```bash
   git checkout -b feature/your-feature
   ```  
3. Commit changes and push to your fork.  
4. Open a Pull Request.  

**Guidelines**:  
- Report bugs via GitHub Issues.  
- Suggest features/enhancements through Discussions.  

## License

MIT License  
Permission is granted for free use, modification, and distribution. See LICENSE file for full terms.
