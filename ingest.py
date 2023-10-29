from haystack.nodes import EmbeddingRetriever, PreProcessor, AnswerParser
from haystack.document_stores import WeaviateDocumentStore
from haystack.preview.components.file_converters.pypdf import PyPDFToDocument
from haystack import Pipeline
print("import succes")

path = ["data/doc.pdf"]