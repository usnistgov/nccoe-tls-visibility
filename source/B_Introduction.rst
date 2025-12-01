.. _Introduction:

Introduction to This TLS 1.3 Visibility Practice Guide 
=======================================================

Enterprise cybersecurity depends on identification, protection,
detection, and response, as well as recovery policies, mechanisms, and
processes. Cryptography—a critical component of cybersecurity—is an
important mechanism for protecting enterprise information and processes.
Network and system monitoring and analysis of encrypted traffic and the
underlying plaintext is often necessary for detecting cyber-attacks and
anomalous behavior, understanding their nature, and responding to and
recovering from an incident. *Transport Layer Security (TLS)* is a
cryptographic protocol that is widely deployed to secure internal
enterprise traffic within traditional office networks and enterprise
data centers, and connections across the public internet.

*The Transport Layer Security (TLS) Protocol Version 1.3* (RFC 8446
:ref:`[2]<tls1_3rfc>`), always provides *forward secrecy*.
In the legacy TLS 1.2 implementations, forward secrecy is optional, but
in TLS 1.3, every session is compatible with forward secrecy, and it is
achieved when compatible key management practices are employed, such as
deleting keys when they are no longer needed.

Many enterprises have regulatory requirements for visibility into network
traffic and stored data. The approach used in TLS 1.3 to achieve forward 
secrecy conflicts with the passive decryption techniques that are widely used by
enterprises to gain visibility into their internal enterprise
TLS-protected traffic. The use of forward secrecy conflicts with the passive
decryption techniques used today for visibility, resulting in 
enterprises choosing between using the TLS 1.2 protocol without forward 
secrecy or adopting TLS 1.3 together with some alternative method for 
achieving visibility into internal traffic. If an enterprise opts for TLS 1.2, 
it misses out on the performance enhancements in TLS 1.3 and faces additional
risks by relying on increasingly out-of-date protocol implementations. Further,
TLS 1.2 will not be updated to support post-quantum cryptographic (PQC) algorithms.

Loss of visibility into received network traffic can impair critical
functions such as network and application performance monitoring,
security logging, and diagnostics, which undermines the effectiveness of
network and security operations and engineering teams. Without the 
ability to decrypt network data for deep packet inspection (DPI), 
monitoring, or diagnostics, enterprises will rely on endpoint devices 
for performance and security information. The incoming network data 
stream can contain information or perspectives that individual endpoint 
devices, like workstations, servers, etc., that support a security 
client are not capable of providing. Reliance on endpoints in the 
absence of visibility into network traffic introduces security 
and operational risks for network and data center operations in the 
following ways:

- Visibility into network data is even more critical when the endpoints
  are having problems or are in any way compromised. A degraded or
  compromised endpoint device may fail to report incidents that can be
  detected within the incoming network data stream.

- Visibility into network data is essential to enable the ability to
  discover issues that involve multiple platforms or multiple
  organizations within the enterprise.

- Visibility into network data is required when sessions span across devices that do
  not log information well or at all. Even with devices that do logging
  well, it is frequently necessary to augment that logging by having
  visibility to related network data. Even where endpoint data is
  adequate, it still needs to be collected, consolidated, centralized,
  and correlated. Where sessions span domains of control, network data
  is the only common point at which multiple operators can establish
  common ground for monitoring, security, and diagnostics.

- When logging of network traffic is turned off or reduced, which is
  often the case, visibility into network data may be the only alternative
  to see anomalies. Visibility into network data is preferable when 
  the endpoint (or a middlebox, a network device that often intercepts 
  and manipulates network traffic for security, optimization, or content 
  filtering) platform is incapable of adequate logging without causing 
  utilization or performance issues on the platform. 

- There are many security threats that are more easily identifiable or only
  visible with visibility into network data. Where and how the
  network data is identified and collected can reveal key information
  about security threats.

- Staff can analyze network data to ensure that endpoint security agents
  are operating properly. If an endpoint is compromised or its security
  agent is not running properly, network data is the only line of
  defense and the most critical tool for performing related triage and
  forensics to quickly resolve related issues.

- If network data cannot be decrypted, a security breach, malware, or
  other compromise can more easily spread throughout the entire
  organization via a single platform.

- Nearly all attacks occur over the network—leaving behind traces or
  tracks. To understand questionable traffic, it is necessary to understand 
  the source of the traffic.  Without decryption, you cannot gain such 
  insights, nor can you detect, trace, or eliminate malicious actions.

- Root cause analysis is critical to most large organizations. Forensics
  performed after a breach or other security exposure event depends
  heavily on DPI and network data to figure out what happened, why, and
  what can be done about it. Alternatives to DPI require significant
  time and effort and are generally prohibitively disruptive and
  expensive. Alternatives to DPI monitoring and analysis of decrypted
  incoming network data streams include:

- Re-architecting the enterprise network\ **:** This is difficult,
  expensive, and time-consuming, and, even where feasible, is not a
  short-term solution.

- Depending on endpoints for management and logging\ **:** Even if the
  available endpoint solutions selected are stable, capable, and
  effective, and are consistent and reliable recorders of all events
  related to incidents (enhanced logging), this would require building a
  completely separate infrastructure capable of collecting, storing, and
  parsing terabytes (or more) of data. None of this is a simple
  proposition, and such an infrastructure would require both DPI for
  certain data and significantly enhanced infrastructure management.
  Furthermore, if the true root cause is occurring at a middlebox
  device, endpoints will not see essential information at all.

- Use of intermediate proxies between application tiers: This approach
  would add cost, latency, and potential points of failure. The more
  tiers that a given application has makes proxies less viable and more
  expensive than enabling visibility of network traffic, as described in
  this publication. The cost and complexity increases could be enormous
  in many cases. There may also be situations where intermediate proxies
  are not possible, such as secure subnets and virtual environments.

A significant constraint in meeting the visibility challenges attendant
on TLS 1.3 is the lack of workable approaches that don't change the current TLS 1.3
standard or require the development or adoption of additional or
alternative standards.

Our goal is to demonstrate a standards-based reference design and 
provide users with the information they need to replicate tested 
TLS 1.3 implementations that permit visibility into network traffic. 
The demonstration allows an enterprise to benefit from the performance 
and capability benefits that TLS 1.3 deployment offers and gain 
visibility into network traffic. 

This project addresses known technical and management challenges:

- Secure management of servers' cryptographic keys

- Management of recorded traffic

- Managing expectations of privacy

