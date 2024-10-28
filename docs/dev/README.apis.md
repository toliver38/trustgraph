
# Developing with TrustGraph

This guide is for developers who want to interact with, or develop services
for TrustGraph.  You are in one of 2 camps:

- You want to work with the services that TrustGraph already provides
  as a system and want to interact with those services from your
  application.
- You want to add processing services to TrustGraph to extend what the
  system can do.
  
You need to understand:
- Everyone should read an [Overview](trustgraph-overview.md) of how the
  TrustGraph system hangs together.
- Everyone should understand how the
  [service invocation APIs](service-invocation-apis.md) hang
  together, and which bits of software implement those APIs.
- If you want to build components to run within TrustGraph you need to
  understand the [processing component API](process-apis.md)
  which are the foundation for components.
- If you want to build components, you should probably read how we 
  [package and deploy](packaging.md) because, you can go your own way on
  this, but it may save you a lot of time.
- Finally, having written new components, if you want the deployment to be
  slick it's worth understanding how the
  [templating system](templating.md) works, because
  this means you can create configurations for your system in the same way
  we do.

