
from . clients.document_embeddings_client import DocumentEmbeddingsClient
from . clients.triples_query_client import TriplesQueryClient
from . clients.embeddings_client import EmbeddingsClient
from . clients.prompt_client import PromptClient

from . schema import DocumentEmbeddingsRequest, DocumentEmbeddingsResponse
from . schema import TriplesQueryRequest, TriplesQueryResponse
from . schema import prompt_request_queue
from . schema import prompt_response_queue
from . schema import embeddings_request_queue
from . schema import embeddings_response_queue
from . schema import document_embeddings_request_queue
from . schema import document_embeddings_response_queue

LABEL="http://www.w3.org/2000/01/rdf-schema#label"
DEFINITION="http://www.w3.org/2004/02/skos/core#definition"

class Query:

    def __init__(
            self, rag, user, collection, verbose,
            doc_limit=20
    ):
        self.rag = rag
        self.user = user
        self.collection = collection
        self.verbose = verbose
        self.doc_limit = doc_limit

    def get_vector(self, query):

        if self.verbose:
            print("Compute embeddings...", flush=True)

        qembeds = self.rag.embeddings.request(query)

        if self.verbose:
            print("Done.", flush=True)

        return qembeds

    def get_docs(self, query):

        vectors = self.get_vector(query)

        if self.verbose:
            print("Get entities...", flush=True)

        docs = self.rag.de_client.request(
            vectors, limit=self.doc_limit
        )

        if self.verbose:
            print("Docs:", flush=True)
            for doc in docs:
                print(doc, flush=True)

        return docs

class DocumentRag:

    def __init__(
            self,
            pulsar_host="pulsar://pulsar:6650",
            pulsar_api_key=None,
            pr_request_queue=None,
            pr_response_queue=None,
            emb_request_queue=None,
            emb_response_queue=None,
            de_request_queue=None,
            de_response_queue=None,
            verbose=False,
            module="test",
    ):

        self.verbose=verbose

        if pr_request_queue is None:
            pr_request_queue = prompt_request_queue

        if pr_response_queue is None:
            pr_response_queue = prompt_response_queue

        if emb_request_queue is None:
            emb_request_queue = embeddings_request_queue

        if emb_response_queue is None:
            emb_response_queue = embeddings_response_queue

        if de_request_queue is None:
            de_request_queue = document_embeddings_request_queue

        if de_response_queue is None:
            de_response_queue = document_embeddings_response_queue

        if self.verbose:
            print("Initialising...", flush=True)

        self.de_client = DocumentEmbeddingsClient(
            pulsar_host=pulsar_host,
            subscriber=module + "-de",
            input_queue=de_request_queue,
            output_queue=de_response_queue,
            pulsar_api_key=pulsar_api_key,
        )            

        self.embeddings = EmbeddingsClient(
            pulsar_host=pulsar_host,
            input_queue=emb_request_queue,
            output_queue=emb_response_queue,
            subscriber=module + "-emb",
            pulsar_api_key=pulsar_api_key,
        )

        self.lang = PromptClient(
            pulsar_host=pulsar_host,
            input_queue=pr_request_queue,
            output_queue=pr_response_queue,
            subscriber=module + "-de-prompt",
            pulsar_api_key=pulsar_api_key,
        )

        if self.verbose:
            print("Initialised", flush=True)

    def query(
            self, query, user="trustgraph", collection="default",
            doc_limit=20,
    ):

        if self.verbose:
            print("Construct prompt...", flush=True)

        q = Query(
            rag=self, user=user, collection=collection, verbose=self.verbose,
            doc_limit=doc_limit
        )

        docs = q.get_docs(query)

        if self.verbose:
            print("Invoke LLM...", flush=True)
            print(docs)
            print(query)

        resp = self.lang.request_document_prompt(query, docs)

        if self.verbose:
            print("Done", flush=True)

        return resp

