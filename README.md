## Knowledge Graph Builder

This project allows you to build a knowledge graph from uploaded documents using large language models (LLMs) and Neo4j.

### Features

* Upload documents (currently supports PDFs)
* Process text with LLMs (currently supports OpenAI API and Groq)
* Generate knowledge graph based on LLM output
* Visualize the generated knowledge graph in Streamlit

### Requirements

* Python 3.x
* Streamlit
* langchain
* langchain-community
* langchain-openai (or langchain-groq)
* neo4j
* PyPDF2 (for PDF support)

### Installation

1. Install required libraries:
   ```bash
   pip install streamlit langchain langchain-community langchain-openai (or langchain-groq) neo4j PyPDF2
   ```
2. Create a `.env` file in your project directory and set the following environment variables:
   * `OPENAI_API_KEY`: Your OpenAI API key (if using OpenAI)
   * `NEO4J_URI`: Your Neo4j connection URI
   * `NEO4J_USERNAME`: Your Neo4j username
   * `NEO4J_PASSWORD`: Your Neo4j password
   * `GROQ_API_KEY`: Your Groq API key (if using Groq)

### Usage

1. Clone this repository.
2. Run the script:
   ```bash
   streamlit run main.py
   ```
3. Upload your documents in the Streamlit app.
4. The app will process the documents, generate a knowledge graph, and display it.
