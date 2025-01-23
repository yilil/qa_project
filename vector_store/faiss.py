from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document

from qa_project.settings import vectorstore_path
from resource_manager import resource_manager


def init():
    print("Creating a new FAISS vectorstore...")

    documents = [
        Document(page_content="INFO1110 is one of the USYD computer science core units.", metadata={"source": "file1.txt", "author": "Alice"}),
        Document(page_content="INFO1113 is one of the USYD computer science core units.", metadata={"source": "file2.txt", "author": "Bob"}),
        Document(page_content="USYD is located in Sydney.", metadata={"source": "file3.txt", "author": "Charlie"}),
        Document(page_content="The 2022 ABCD conference was held in Shanghai.", metadata={"source": "file4.txt", "author": "David"}),
    ]

    vector_store = FAISS.from_documents(documents, resource_manager.get_embedding_model())
    vector_store.save_local(vectorstore_path)
    print(f"A new FAISS vectorstore saved to {vectorstore_path}!")
