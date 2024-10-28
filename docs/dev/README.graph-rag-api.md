
# GraphRagClient Documentation

This document details the GraphRagClient class used to interact with a
GraphRAG service through Pulsar message queues.

Class: GraphRagClient

The GraphRagClient class provides a simplified interface for sending
retrieval-augmented generation (RAG) queries to a GraphRAG service. It
handles communication via Pulsar message queues, including sending
requests and receiving responses.

Initialization:

  __init__(
      self, log_level=ERROR, subscriber=None, input_queue=None,
      output_queue=None, pulsar_host="pulsar://pulsar:6650")

  - `log_level (Optional[int])`: Sets the logging level for the
    client. Defaults to ERROR.

  - `subscriber (Optional[str])`: Pulsar subscriber name for receiving
    responses. Defaults to a system-generated name.

  - `input_queue (Optional[str])`: Pulsar queue name for sending
    requests. Defaults to graph_rag_request_queue.

  - `output_queue (Optional[str])`: Pulsar queue name for receiving
    responses. Defaults to graph_rag_response_queue.

  - `pulsar_host (Optional[str])`: Pulsar service hostname and
    port. Defaults to "pulsar://pulsar:6650".

Methods:

  `request(self, query, user="trustgraph", collection="default", timeout=500)
      -> GraphRagResponse`

  Sends a RAG query to the GraphRAG service and returns the response.
  
  - `query (str)`: The RAG query to be executed.

  - `user (Optional[str])`: User associated with the request. Defaults
    to "trustgraph".

  - `collection (Optional[str])`: Collection associated with the
    request. Defaults to "default".

  - `timeout (Optional[int])`: Timeout in milliseconds for waiting for a
    response. Defaults to 500ms.

  Returns: A `GraphRagResponse` object containing the response from the
  GraphRAG service.

Usage:

- Create a GraphRagClient instance with desired configuration (optional).
- Call the request method with your RAG query, specifying any
  additional parameters like user, collection, or timeout.
- The request method returns a GraphRagResponse object containing the
  response from the GraphRAG service.

Example:

```python

from graphrag_client import GraphRagClient

# Set log level to INFO for more details
client = GraphRagClient(log_level=INFO)

query = "What is the capital of France?"

response = client.request(query)

if response.status == "SUCCESS":
  print(f"Answer: {response.answer}")
else:
  print(f"Error: {response.error}")

```

Note: This documentation focuses on the functionalities of the
GraphRagClient class. Refer to the specific GraphRAG implementation
for details on the query format and response structure.

