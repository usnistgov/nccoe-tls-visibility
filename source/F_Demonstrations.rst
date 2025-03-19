.. _Functional_Demonstrations:


Functional Demonstrations 
==========================

Usage Scenarios Supported
-------------------------

The TLS 1.3 visibility project demonstrates how to enable a variety of
security monitoring and analysis activities that support enterprise
compliance, security, and operational requirements. Representative
scenarios described in this section involve enterprise data center
environments that may include on-premises and hybrid cloud deployments
hosted by a third-party data center or a public cloud provider.
Organizations may need access to plaintext traffic entering their
systems for reasons ranging from fraud detection to enforcement of
system use policies to cybersecurity monitoring and analysis. Examples
of scenarios where visibility into traffic content for security
compliance and continuity of operations is required include outbound
traffic, connections across the internet to the enterprise network
boundary, and communications within the enterprise network between
internal systems. This project focuses on communications within the
enterprise network and does not focus on outbound connections or
communications across the public internet. Some example scenarios
requiring visibility into TLS 1.3-protected traffic include
troubleshooting, performance monitoring, cybersecurity threat triage,
and cybersecurity forensics. Individual enterprises may apply the
visibility techniques outlined in this project to selected
representative scenarios or to additional scenarios tailored to their
specific operations.

Troubleshooting Scenario
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If availability and operational problems occur, enterprises that provide
these services to customers, partners, and employees need to rapidly
troubleshoot and fix these issues. Operations troubleshooting scenarios
demonstrate the enterprise tracing transactions through all tiers of an
application, including the collection of detailed information such as
transaction identifiers, data payload, and the results of operations
performed by each application tier. Because operational issues can be
intermittent and difficult to replicate, troubleshooting scenarios
include the ability to proactively collect and view detailed historical
data that may or may not appear in logs. Examples of troubleshooting
situations include application unavailability and intermittent system
failures. Visibility into enterprise elements such as communications for
network-attached storage (NAS), identity management systems, databases,
routers and switches, application servers, web servers, load balancers,
and firewalls can help provide a complete picture of the end-to-end
session across the enterprise. The troubleshooting scenario includes
these elements:

- Demonstrating the ability to trace transactions across multiple tiers
  of applications and communications infrastructure, such as load
  balancers, firewalls, routers, and switches.

- Collecting detailed information that shows the outcomes of operations
  performed (which may or may not be recorded in logs).

- Accessing detailed historical data (which may or may not be available
  in logs).

Performance Monitoring Scenario
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Application performance and response times are critical to customer
service and time-sensitive mission-critical applications. Performance
issues may range from application-specific response degradation to
malicious distributed denial of service attacks. Enterprises must
proactively detect and isolate performance issues for multi-tier
applications.

The performance monitoring scenario includes the following elements:

- Rapidly and accurately detect user performance issues.

- Predict and resolve customer performance issues based on upstream
  degradation.

- Ability to rapidly identify the source of performance issues.

- Monitor across all mission-critical applications/platforms.

- Minimize performance load on applications/platforms.

Cybersecurity Threat Triage and Forensics Scenario
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

With the widespread threat of cyber-attacks, enterprises must rapidly
triage indicators of compromise (IOCs)—separating false positives from
real attacks. The threat triage scenario includes triage,
identification, and response to IOCs that may arise in a variety of
enterprise elements. Examples include network-attached storage, identity
management systems, databases, routers and switches, application
servers, web servers, load balancers, and firewalls. IOCs may appear in
processes, open ports, and logs. The cybersecurity threat triage
scenario includes the following elements:

- Rapidly get a clear picture of the system state.

- Reduce triage time with an accurate, detailed picture of current and
  historical communications.

- Minimize reliance on data sources that can be manipulated by attackers
  (including end-point devices).

After a major compromise, enterprises must quickly identify how the
attack occurred. This includes pinpointing each compromised system, the
exploited vulnerabilities, the attack methods used, and the data
exfiltrated. To be effective, obtain accurate information about all
operations performed by attackers (even if the attacker manipulated the
logs) from independent data sources. The security forensics scenario
includes the ability to trace paths of attacks as they pivot laterally
across the internal network of compromised systems. Affected systems may
involve network-attached storage, identity management systems,
databases, routers and switches, application servers, web servers, load
balancers, client systems, and firewalls.

The cybersecurity forensics component of this scenario includes the
following elements:

- Ability to trace the path of attack across a network of compromised
  systems.

- Accurate information about all operations performed by attackers.

- Facilitate the creation of updated and improved operations and
  security policies to prevent or mitigate the success of future
  attacks.

Monitoring for Compliance and Hygiene Scenario
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Enterprises that conduct proactive traffic assessments can compare the
attributes of the traffic being monitored against their forward-looking
expectations for cybersecurity. The compliance and hygiene scenario
shows how to verify that the observed traffic profile complies with
current cybersecurity standards and objectives. This includes verifying
that updates are implemented according to enterprise policies and
detecting instances where disallowed security components, outdated
protocols, systems, hardware, or software versions are in use.

.. _demonstration_examples:
Example Demonstration Events 
-----------------------------

Twelve events were chosen to demonstrate the scenarios outlined in
The table below lists these demonstration events.

.. table:: Demonstration Events

   +-----------------------------------------------------------------------+
   | **Troubleshooting Examples**                                          |
   +=======================================================================+
   | Identification of Failed Network Traffic Due to Expired TLS PKI       |
   | Certificates (Layer 4)                                                |
   +-----------------------------------------------------------------------+
   | Protocol-Specific Service Utilization and Consumption Characteristics |
   | Identification and Logging                                            |
   +-----------------------------------------------------------------------+
   | Identification of and Reporting Protocol-Specific Error Status Codes  |
   +-----------------------------------------------------------------------+
   | **Performance Monitoring Examples**                                   |
   +-----------------------------------------------------------------------+
   | Identification of, Collection of, and Reporting on Protocol-specific  |
   | Error Status Codes for Services                                       |
   +-----------------------------------------------------------------------+
   | Identification of Propagation of Performance Issues Throughout a      |
   | System by Correlating Error Status Codes Across Component Services    |
   | from TLS Connections on Either Side of a Proxy                        |
   +-----------------------------------------------------------------------+
   | Develop Baselines for Traffic Performance Characteristics for         |
   | Individual Servers                                                    |
   +-----------------------------------------------------------------------+
   | **Threat Triage and Forensics Examples**                              |
   +-----------------------------------------------------------------------+
   | Scan for Suspicious/Malicious Content                                 |
   +-----------------------------------------------------------------------+
   | Detection of Unanticipated Inability to Decrypt Traffic               |
   +-----------------------------------------------------------------------+
   | Detection of Command-and-Control and Exfiltration Activity            |
   +-----------------------------------------------------------------------+
   | Scanning of Network Traffic for Un-sanitized User Input               |
   +-----------------------------------------------------------------------+
   | **Monitoring for Compliance and Hygiene Examples**                    |
   +-----------------------------------------------------------------------+
   | Detection of the Use of Outdated Protocols                            |
   +-----------------------------------------------------------------------+
   | Detection of, Identification of, and Reporting on the Use of Outdated |
   | Software                                                              |
   +-----------------------------------------------------------------------+

These events illustrate a build's capability to demonstrate each
scenario. Specific product configurations for the examples are included
in :ref:`Appendix E<AppendixE>`. Demonstration input and output information, traffic generated,
results, and screenshots associated with the validation of examples are
posted in :ref:`Appendix F<AppendixF>`.

