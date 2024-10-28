PromptClient Documentation

This document explains the PromptClient class used to interact with a TrustGraph Prompt service through Pulsar message queues. The Prompt service can be used to extract information from text chunks, including definitions, relationships, topics, and data rows based on a schema.
Class: PromptClient

The PromptClient class provides a simplified interface for sending various prompt requests to a TrustGraph Prompt service and receiving the corresponding responses.

Initialization:

    __init__(self, log_level=ERROR, subscriber=None, input_queue=None, output_queue=None, pulsar_host="pulsar://pulsar:6650")
        log_level (Optional[int]): Sets the logging level for the client. Defaults to ERROR.
        subscriber (Optional[str]): Pulsar subscriber name for receiving responses. Defaults to a system-generated name.
        input_queue (Optional[str]): Pulsar queue name for sending requests. Defaults to prompt_request_queue.
        output_queue (Optional[str]): Pulsar queue name for receiving responses. Defaults to prompt_response_queue.
        pulsar_host (Optional[str]): Pulsar service hostname and port. Defaults to "pulsar://pulsar:6650".

Methods:

    request(self, id, terms, timeout=300) -> PromptResponse
        Sends a prompt request to the service and returns the response.
            id (str): Unique identifier for the prompt type (e.g., "extract-definitions").
            terms (dict): Dictionary containing prompt-specific parameters.
            timeout (Optional[int]): Timeout in milliseconds for waiting for a response. Defaults to 300ms.
            Returns: A PromptResponse object containing the response from the Prompt service.

Prompt-Specific Request Methods:

The PromptClient class offers various helper methods for common prompt types:

    request_definitions(self, chunk, timeout=300) -> List[Definition]
        Extracts definitions for entities mentioned in the text chunk.
        chunk (str): Text chunk to analyze.
        timeout (Optional[int]): Timeout for waiting for the response. Defaults to 300ms.
        Returns: A list of Definition objects containing extracted entity names and definitions.

    request_relationships(self, chunk, timeout=300) -> List[Relationship]
        Extracts relationships between entities in the text chunk.
        chunk (str): Text chunk to analyze.
        timeout (Optional[int]): Timeout for waiting for the response. Defaults to 300ms.
        Returns: A list of Relationship objects containing subject, predicate, object, and optional object entity information.

    request_topics(self, chunk, timeout=300) -> List[Topic]
        Extracts topics discussed in the text chunk.
        chunk (str): Text chunk to analyze.
        timeout (Optional[int]): Timeout for waiting for the response. Defaults to 300ms.
        Returns: A list of Topic objects containing extracted topics and their definitions (if available).

    request_rows(self, schema, chunk, timeout=300) -> PromptResponse
        Extracts data rows from the text chunk based on a provided schema.
        schema (Object): Schema object defining the expected data structure.
        chunk (str): Text chunk to analyze.
        timeout (Optional[int]): Timeout for waiting for the response. Defaults to 300ms.
        Returns: A PromptResponse object containing the extracted data rows (format depends on the service implementation).

    request_kg_prompt(self, query, kg, timeout=300) -> PromptResponse
        Executes a prompt query using a provided knowledge graph (KG) as additional context.
        query (str): The prompt query to be executed.
        kg (List[List]): List of triples representing the knowledge graph (subject, predicate, object).
        timeout (Optional[int]): Timeout for waiting for the response. Defaults to 300ms.
        Returns: A PromptResponse object containing the response from the Prompt service based on the query and KG.

    request_document_prompt(self, query, documents, timeout=300) -> PromptResponse
        Executes a prompt query using a set of documents as additional context.
        query (

