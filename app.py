import streamlit as st
import tempfile
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
import os
from neo4j import GraphDatabase
from langchain_community.vectorstores import Neo4jVector
from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
from langchain_community.graphs import Neo4jGraph
from langchain_experimental.graph_transformers import LLMGraphTransformer
# from neo4j.debug import watch


# watch("neo4j")

os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]
os.environ["NEO4J_URI"] = st.secrets["NEO4J_URI"]
os.environ["NEO4J_USERNAME"] = st.secrets["NEO4J_USERNAME"]
os.environ["NEO4J_PASSWORD"] = st.secrets["NEO4J_PASSWORD"]
os.environ["GROQ_API_KEY"] = st.secrets["GROQ_API_KEY"]
#driver = GraphDatabase.driver("neo4j+s://705bba1f.databases.neo4j.io", auth=("neo4j", "0CcPxCi2GEDHJw2dzJ11YsmPR15FyNqd1BX_v0v7ccs"))
st.set_page_config(
    page_title="Knowledge Graph builder",
    page_icon="📈"
)
st.title("Knowledge Graph builder📈")
uploaded_files = st.file_uploader("Upload files", accept_multiple_files=True)
if uploaded_files:
    text = []
    for file in uploaded_files:
        file_extension = os.path.splitext(file.name)[1]
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_file.write(file.read())
            temp_file_path = temp_file.name

        loader = None
        if file_extension == ".pdf":
            loader = PyPDFLoader(temp_file_path)

        if loader:
            text.extend(loader.load())
            os.remove(temp_file_path)

    # text_splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=10)
    # text_chunks = text_splitter.split_documents(text)



    llm=ChatOpenAI(model_name="gpt-3.5-turbo-0125", temperature=0)
    #llm=ChatGroq(model_name="llama3-8b-8192", temperature=0)
    graph = Neo4jGraph()
    llm_transformer = LLMGraphTransformer(llm=llm)
    with st.spinner("Generating graph..."):
        graph_documents = llm_transformer.convert_to_graph_documents(text)
    graph.add_graph_documents(
        graph_documents,
        baseEntityLabel=True,
        include_source=True
    )
    st.write(graph_documents)
    st.write(graph)