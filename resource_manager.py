from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from qa_project.settings import vectorstore_path, llm_name, embedding_model_name


class ResourceManager:
    """
    Singleton: ensure there is only one instance of resource manager throughout the program lifecycle.
    """
    _instance = None

    def __init__(self):
        # Prevent reinitialisation in case `__init__` is accidentally called
        if hasattr(self, "initialised") and self.initialised:
            return
        self.llm = None
        self.embedding_model = None
        self.vectorstore = None
        self.initialised = True

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(ResourceManager, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def get_llm(self):
        if self.llm is None:
            self.llm = ChatGoogleGenerativeAI(model=llm_name)
        return self.llm

    def get_embedding_model(self):
        if self.embedding_model is None:
            self.embedding_model = GoogleGenerativeAIEmbeddings(model=embedding_model_name)
        return self.embedding_model

    def get_vector_store(self):
        if self.vectorstore is None:
            self.vectorstore = FAISS.load_local(vectorstore_path, self.get_embedding_model(), allow_dangerous_deserialization=True)
        return self.vectorstore


resource_manager = ResourceManager()
