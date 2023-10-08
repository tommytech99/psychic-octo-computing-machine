# Find this code here: https://medium.com/@vikastiwari708409/how-to-use-gpt4all-llms-with-langchain-to-work-with-pdf-files-f0f0becadcb6

from langchain.document_loaders import PyPDFLoader
from langchain import PromptTemplate, LLMChain
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.llms import GPT4All
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores.faiss import FAISS
from langchain.callbacks.base import BaseCallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

# If you do not want to create indexes all the time
# comment out everything except "embeddings = HuggingFace...."
# after one run
documents = PyPDFLoader('data.pdf').load_and_split()
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1024,chunk_overlap=64)
texts = text_splitter.split_documents(documents)
embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')
faiss_index = FAISS.from_documents(texts, embeddings)
faiss_index.save_local("faiss_indexes")

# load vector store
print("loading indexes")
faiss_index = FAISS.load_local("faiss_indexes", embeddings)
print("index loaded")
gpt4all_path = './gpt4Models/ggml-model-gpt4all-falcon-q4_0.bin'

# # Set your query here manually
question = "Exactly how old is Tom?"
matched_docs = faiss_index.similarity_search(question, 4)
context = ""
for doc in matched_docs:
    context = context + doc.page_content + " \n\n "

template = """
Please use the following context to answer questions.
Context: {context}
 - -
Question: {question}
Answer: Let's think step by step."""

callback_manager = BaseCallbackManager([StreamingStdOutCallbackHandler()])
llm = GPT4All(model=gpt4all_path,callback_manager=callback_manager,verbose=True,repeat_last_n=0)
prompt = PromptTemplate(template=template, input_variables=["context", "question"]).partial(context=context)
llm_chain = LLMChain(prompt=prompt, llm=llm)

print(llm_chain.run(question))