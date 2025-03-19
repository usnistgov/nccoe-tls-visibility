
.. _AppendixF:

F. Details of the Functional Demonstrations and Results
################################################################



.. _F.1:

F.1 Traffic Visibility to Support Troubleshooting
*************************************************

Enterprises providing services to customers, partners, and employees must have the ability to rapidly troubleshoot and fix issues when availability and operational issues occur. Operations troubleshooting scenarios demonstrate the enterprise tracing transactions through all tiers of an application, including collection of detailed information such as transaction identifiers, data payload, and the results of operations performed by each application tier. Because operational issues can be intermittent and difficult to replicate, troubleshooting scenarios include the ability to proactively collect and view detailed historical data that may or may not be available in logs. Examples of troubleshooting situations include application unavailability and intermittent system failures. Visibility may be required into enterprise elements such as communications for network-attached storage (NAS), identity management systems, databases, routers and switches, application servers, web servers, load balancers, and firewalls in order to build a complete picture of the end-to-end session across the enterprise. The troubleshooting scenario includes the following elements:

* Show ability to trace transactions through multiple tiers of applications and communications infrastructure (load-balancers, firewalls, routers, switches, etc.)
* Collect detailed information showing result of operations performed (may or may not be available in logs)
* Ability to view detailed historical data (may or may not be available in logs)



.. _C.2:

F.2 Traffic Visibility to Support Performance Monitoring
********************************************************

Application performance and response times are critical to customer service and time-sensitive mission-critical applications. Performance issues may range from application-specific response degradation to occurrences of malicious distributed denial of service attacks. Enterprises must be able to proactively detect and isolate performance issues for multi-tier applications. The performance monitoring scenario involves rapidly and accurately detecting user performance issues, predicting and resolving customer performance issues based on upstream degradation, maintaining the ability to rapidly identify sources of performance issues, monitoring across all mission-critical applications and platforms, and minimizing performance loads on applications and platforms. The performance monitoring scenario includes the following elements:

* Rapidly and accurately detect user performance issues
* Predict and resolve customer performance issues based on upstream degradation
* Ability to rapidly identify source of performance issues
* Monitor across all mission-critical applications/platforms
* Minimize performance load on applications/platforms


.. _F.3:

F.3 Traffic Visibility to Support Cybersecurity Threat Triage and Forensics
***************************************************************************

With the widespread threat of cyber-attacks, enterprises must be able to rapidly triage indicators of compromise (IOCs), quickly distinguishing false positives from real attacks. The threat triage scenario includes triage, identification, and response to IOCs. IOCs may arise in a variety of enterprise elements. Examples include network-attached storage, identity management systems, databases, routers and switches, application servers, web servers, load balancers, and firewalls. They may be found in processes, open ports, and logs. Performing threat triage may require visibility into current and historical inbound and outbound communications. Effective performance of threat triage requires rapidly obtaining a clear picture of system state, reducing triage time with an accurate and detailed picture of current and historical communications, minimizing reliance on data sources that can be manipulated by attackers, and using independent data sources for verification. The cybersecurity threat triage scenario includes the following elements:

* Rapidly get clear picture of system state
* Reduce triage time with an accurate, detailed picture of current and historical communications
* Minimize reliance on data sources that can be manipulated by attackers (including end-point devices)


.. _F.4:

F.4 Traffic Visibility to Support Monitoring for Compliance and Hygiene
***********************************************************************

Following a major compromise, enterprises must be able to establish a clear picture of how the attack occurred, including each system that was compromised, vulnerabilities that were exploited, attack methods that were used, and data that was exfiltrated. To be effective, accurate information must be obtained about all operations performed by attackers (even if logs were manipulated) from independent data sources. The security forensics scenario includes the ability to trace paths of attacks as they pivot laterally across the internal network of compromised systems. Affected systems may involve network-attached storage, identity management systems, databases, routers and switches, application servers, web servers, load balancers, client systems, and firewalls. The cybersecurity forensics scenario includes the following elements:

* Ability to trace path of attack across network of compromised systems
* Accurate information about all operations performed by attackers (even if logs were manipulated)
* Facilitate the creation of updated and improved operations and security policies to prevent or mitigate the success of future attacks



.. _F.5:

F.5 Functional Demonstration Scripts and Results
************************************************

.. toctree::
   :maxdepth: 2
   :hidden:

   AppCScenarios/ds-1.rst
   AppCScenarios/ds-2.rst
   AppCScenarios/ds-3.rst
   AppCScenarios/ds-4.rst
   AppCScenarios/ds-5.rst
   AppCScenarios/ds-6.rst
   AppCScenarios/ds-7.rst
   AppCScenarios/ds-8.rst
   AppCScenarios/ds-9.rst
   AppCScenarios/ds-10.rst
   AppCScenarios/ds-11.rst
   AppCScenarios/ds-12.rst
   AppCScenarios/ds-13.rst


* :ref:`scenario-1.1`
* :ref:`scenario-1.2`
* :ref:`scenario-1.3`
* :ref:`scenario-2.1`
* :ref:`scenario-2.2`
* :ref:`scenario-2.3`
* :ref:`scenario-3.1a`
* :ref:`scenario-3.1b`
* :ref:`scenario-3.2`
* :ref:`scenario-3.3`
* :ref:`scenario-3.4`
* :ref:`scenario-4.1`
* :ref:`scenario-4.2`