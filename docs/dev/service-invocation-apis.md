
# Service Invocation APIs

This document describes interaction with service APIs.

## APIs

APIs exist for the following use-cases:

- `GraphRagClient`: This performs a GraphRAG query.  The input is a query
  string in natural language, the output is a natural language response.
  This hides the complexity of the GraphRAG pipeline as a simple
  call.
- `DocumentRagClient`: This performs a Document RAG query.  The input is a
  query string in natural language, the output is a natural language response.
  This hides the complexity of the Document RAG pipeline as a simple
  call.
- `DocumentEmbeddingsClient`: This provides a client API which
  interacts with the document embedding service to fetch documents which
  match an embedding.  This is a low-level API useful for custom
  applications.

> FIXME: Complete

EmbeddingsClient
GraphEmbeddingsClient
LlmClient
PromptClient
TriplesQueryClient

