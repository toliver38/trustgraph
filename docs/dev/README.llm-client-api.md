LlmClient Documentation

This document details the 

LlmClient class used to interact with a Large Language Model (LLM) service through Pulsar message queues. The LLM service can be used to generate text completions or continuations based on a provided prompt.
Class: LlmClient

The LlmClient class offers a simplified interface for sending text completion requests to an LLM service and receiving the generated responses.

Initialization:

    __init__(self, log_level=ERROR, subscriber=None, input_queue=None, output_queue=None, pulsar_host="pulsar://pulsar:6650")
        log_level (Optional[int]): Sets the logging level for the client. Defaults to ERROR.
        subscriber (Optional[str]): Pulsar subscriber name for receiving responses. Defaults to a system-generated name.
        input_queue (Optional[str]): Pulsar queue name for sending requests. Defaults to text_completion_request_queue.
        output_queue (Optional[str]): Pulsar queue name for receiving responses. Defaults to text_completion_response_queue.
        pulsar_host (Optional[str]): Pulsar service hostname and port. Defaults to "pulsar://pulsar:6650".

Method:

    request(self, prompt, timeout=300) -> TextCompletionResponse
        Sends a text completion request to the LLM service and returns the response.
            prompt (str): The text prompt for which to generate a completion.
            timeout (Optional[int]): Timeout in milliseconds for waiting for a response. Defaults to 300ms.
            Returns: A TextCompletionResponse object containing the generated text completion from the LLM service.

