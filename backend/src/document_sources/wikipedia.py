import logging
from langchain_community.document_loaders import WikipediaLoader
from src.shared.llm_graph_builder_exception import LLMGraphBuilderException

def get_documents_from_Wikipedia(wiki_query:str, language:str):
  try:
    pages = WikipediaLoader(query=wiki_query.strip(), lang=language, load_all_available_meta=False, load_max_docs=1, doc_content_chars_max=120000).load()
    print("\n\n\n\n\n\nNumber of pages:", len(pages))
    print("Page content size:", len(pages[0].page_content))
    file_name = wiki_query.strip()
    logging.info(f"Total Pages from Wikipedia = {len(pages)}") 
    return file_name, pages
  except Exception as e:
    message="Failed To Process Wikipedia Query"
    error_message = str(e)
    logging.exception(f'Failed To Process Wikipedia Query: {file_name}, Exception Stack trace: {error_message}')
    raise LLMGraphBuilderException(error_message+' '+message)
