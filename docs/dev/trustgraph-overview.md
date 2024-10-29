
# Overview of the TrustGraph architecture

The TrustGraph mission is to make the experience of building LLM-based
applications resilient and straightforward.

This is achieved by:

## Adopting a pub/sub architecture

Also known as an enterprise bus, this provides a fabric to easily connect
parts of the system.  If you're used to complex enterprise architectures,
don't worry - we've used the simplest architecture decisions.
  
In TrustGraph, Apache Pulsar is used as the pub/sub framework.  The pub/sub
framework allows different disparate processing units to send messages to each
other.
  
There are two kinds of interaction:
- **flows**: These are asynchronous interactions which allow processing units
  to be chained together.  Once a processing unit has processed something
  data is delivered to the next processing item on a queue.
- **request/response**: The system uses two queues, one for delivery of
  requests, and the other for delivery of responses to those requests.
  
Pulsar takes care of a whole heap of features which are useful for making
systems resilient, such as load-sharing across multiple processors,
queueing data and retry on failure.

## Using message schemas

Pulsar supports associating message schemas with queues which helps to make
it easy to share message formats, but also spot issues if the wrong
components are connected inappropriately.  Using the wrong schema
on a queue causes an immediate error.

## Service discovery

The business of finding out which processing item to send information to
is called "service discovery" which can be a complex issue in itself.
With Pulsar managing queues, in TrustGraph service discovery is just a case
of known the name of the queue you want to deliver to.

The only issue to take care of is ensuring all the processing units know
where to find the Pulsar service.

## Scaling

Pulsar queues can deliver to multiple processing services to allow load to
scale up.  Scaling is just a case of running more processing items.

## Metrication and observability

TrustGraph processing components all provide a Prometheus service
to share metrics data, and TrustGraph integrates Prometheus and Grafana
out-of-the-box for instant LLM dashboarding.

## Pluggable procesing units

There are sometimes more than implementation of a processing component.
One example is LLM invocation.  TrustGraph supports many SLM/LLM options.

TrustGraph uses the same interface and queue names regardless of which
LLM processor is in use.  So all that's needed is to enable one LLM module
and the system is then equipped to provide LLM services through a standard
queue.

The set of pluggable interfaces include:
- An LLM interface to allow a wide set of LLM services to be used.
- An embedding interface to allow different embedding services to to be used.
- Graph query/store interfaces to support different graph stores.
- Vector query/store interfaces to support different vector stores.
- A prompt service which constructs prompts from structured invocations.
  This allows prompts to be tailored for different LLMs or for different
  problems.

# Software stack

At the time of writing, everything in TrustGraph is written in Python.

The Python code is published as Python libraries on PyPi.  It is also
built into a container which can be pulled from Docker Hub.

To interact with TrustGraph services you can download a Python client
which interacts with the services through Pulsar.

In fact, if you want, you don't need to use Python at all.  You could
take a look at the schemas we provide and invoke the services using
a Pulsar client in any language.

> In the future, we may migrate some services to use a different language
> if performance demands require that.

TrustGraph processors can run from any environment where you can
install a Python package, however the deployment configurations we
publish run processors as separate containers.  This allows deployment
in Docker Compose and Kubernetes environments.

# Running TrustGraph

When interacting with TrustGraph you will want to access internal services.
It is important to understand where those services exist.

## Docker Compose / Podman Compose

This is the simplest deployment and suitable for standalone execution
on a Linux machine, Linux VM or Macbook.  It is the simplest way to
learn about TrustGraph and also develop for TrustGraph.

When run in Docker or Podman Compose, each processor runs in a container in
a virtual environment.  In such an environment, each container has its
own internal IP address.  However, the Compose environments also expose
some of the TrustGraph services so that they look like they're running
on the basic Linux machine or Macbook, and this exposure lets you interact
directly with the services.

## Kubernetes

This is a more complex deployment from a point of interacting with services.
Different Kubernetes implementations manage exposure of services in a
different way, and we need to catch up on documenting how you would interact
with Kubernetes.

> FIXME: Document Kubernetes network invocation

# Essential points to take away

- TrustGraph is deployed using a set of containers
- One critical component is Pulsar - TrustGraph services are exposed as APIs
  though Pulsar.
- To interact with TrustGraph services you need to interact with Pulsar
  service, and so the Pulsar service needs to be accessible.

