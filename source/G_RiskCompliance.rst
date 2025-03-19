.. _Risk_and_Compliance_Management:

Risk and Compliance Management
==============================

NIST SP 800-30 Revision 1, *Guide for Conducting Risk Assessments*,
:ref:`[9]<SP800_30>` states that risk is "a measure of the extent to
which an entity is threatened by a potential circumstance or event, and
typically a function of: (i) the adverse impacts that would arise if the
circumstance or event occurs; and (ii) the likelihood of occurrence."
The guide further defines risk assessment as "the process of
identifying, estimating, and prioritizing risks to organizational
operations (including mission, functions, image, reputation),
organizational assets, individuals, other organizations, and the Nation,
resulting from the operation of an information system. Part of risk
management incorporates threat and vulnerability analyses and considers
mitigations provided by security controls planned or in place."

The NCCoE recommends that any discussion of risk management—particularly
at the enterprise level— should begin by reviewing `NIST SP 800-37
Revision 2, Risk Management Framework for Information Systems and
Organizations <https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-37r2.pdf>`__  —material
that is publicly available. The `Risk Management Framework
(RMF) <http://csrc.nist.gov/groups/SMA/fisma/Risk-Management-Framework/>`__ 
guidance is invaluable and gave us a baseline to assess risks, from
which we developed the project, the security characteristics of the
build, and this guide.

Threats
-------

General threats to data exchanged over networks include eavesdropping,
tampering, and forgery. TLS uses cryptographic mechanisms to protect
data from being stolen, modified, or spoofed. This section describes
generic threats to the security of information that TLS mechanisms
protect.

- **Stolen keys.** If threat actors gain unauthorized access to
  symmetric keys used for data encryption or private keys used in public
  key cryptography, they can bypass authentication systems or gain
  access to other keys. If symmetric or private keys are stored without
  encryption, they are especially at risk of being exploited to
  undermine the security protections that TLS provides.

  - Inadequately protected keys are subject to unauthorized access by
    direct theft, hacking, or other means. The more data a key protects,
    the more severe the consequences typically are if a threat actor
    gains unauthorized access.

  - TLS 1.3 symmetric keys are used with Authenticated Encryption with
    Associated Data (AEAD) algorithms—providing confidentiality and
    integrity for the keys.

- **Certificate compromise.** Public keys used during authentication are
  often exchanged in certificates issued by a certificate authority
  (CA). A real threat exists if the issuing CA is compromised or if the
  registration system, persons, or process are used to obtain an
  unauthorized certificate in the name of a legitimate entity to
  compromise the clients.

- **Handshake data replay.** Parties to cryptographically protected
  communications exchange keys use protocols often called "handshakes,"
  which often include multiple steps. TLS 1.3 allows the client to send
  data (known as 0-RTT data) in the first flight of a handshake with a
  server that previously connected to the client. Replayable 0-RTT data
  presents several security threats to TLS-using applications unless
  those applications are specifically engineered to be safe under replay
  (minimally, this means idempotent, but could require stronger
  conditions, such as constant-time response). Many applications do not
  allow 0-RTT to avoid the replay concern (e.g.,
  draft-ietf-netconf-over-tls13).

- **Potential attacks include**:

  - Duplicating actions that cause side effects (e.g., purchasing an
    item or transferring money) to be duplicated, thus harming the site
    or the user.

  - Storing and replaying 0-RTT messages to reorder them with respect to
    other messages (e.g., moving a delete to after a create).

  - Exploiting cache timing behavior to discover the content of 0-RTT
    messages by replaying a message to a different cache node and then
    using a separate connection to measure request latency to see if the
    two requests address the same resource.

  - If data is replayed a large number of times, additional attacks
    become possible, e.g., repeated measurements of cryptographic
    operation speed. In addition, they can overload rate-limiting
    systems.

- **Misuse of client credentials** residing on the client machine.

- **Absence of support for endpoint solutions.** Not all server-type
  systems within an enterprise are supported by endpoint vendors.
  Enterprises commonly have old systems running custom operating system
  (OS) software for which there is limited or no support in endpoint
  solutions.

- **Systems compromised by running endpoint software.** When deployed,
  endpoint solutions may provide good security up to the point where the
  system running the endpoint or endpoint software is compromised. An
  endpoint solution may not detect an endpoint compromise if it relies
  on trusting what the endpoint software tells it—resulting in false
  trust in the endpoint. Alternate solutions that analyze network
  traffic can detect compromised or rogue endpoints and are resilient
  when used alongside endpoint solutions.

Vulnerabilities
---------------

Several vulnerabilities were found in both the TLS 1.2 protocol and in
the implementation of features permitted by TLS 1.2. While TLS 1.2 can
be made secure using extensions and careful configuration, TLS 1.3's
design avoids these vulnerabilities. Vendors are taking note and
focusing on TLS 1.3. Therefore, getting new algorithms or extensions for
TLS 1.2 for implementation by vendors is increasingly difficult. Below
are some examples of these challenges:

- Unlike TLS 1.3, TLS 1.2 offers some cipher suites, such as those that
  use RSA key exchange, that do not provide forward secrecy. Where
  forward secrecy is not provided, if a TLS-enabled server is
  compromised, the contents of its previous TLS communications are
  vulnerable to exposure. The ephemeral key exchange mechanisms that
  provide forward secrecy also protect future TLS communication against
  passive attackers.

- Enterprises widely use passive decryption techniques to achieve
  visibility into their internal TLS 1.2 enterprise traffic. These
  techniques only work with the cipher suites that use RSA key exchange.
  The RSA key exchange used in TLS 1.2 does not provide forward
  secrecy—making it vulnerable to a number of implementation flaws. As a
  result, its use has been deprecated. (See SP 800-131A Rev. 2
  :ref:`[10]<SP800_131A>`, SP 800-52 Rev. 2 :ref:`[11]<SP800_52>`, IETF
  draft *Deprecating Obsolete Key Exchange Methods in TLS 1.2*
  :ref:`[12]<deprecating>`, and *TLS 1.2 Is Frozen* :ref:`[13]<frozen>`.)

- Reusing keys outside the protected data center creates vulnerabilities
  around the comparison of key shares in different handshakes. These
  vulnerabilities may enable an attacker to track an endpoint or reveal
  the identity of the TLS server to which a user is connected. On the
  public internet, this is a violation of user privacy. The current TLS
  1.3 specification contains a new normative requirement stating that to
  prevent tracking and identification, "Clients SHOULD NOT reuse a
  ticket for multiple connections." Further, as of this writing, the
  revised TLS 1.3 draft specification contains an additional normative
  requirement for the same purpose, "Clients and Servers SHOULD NOT
  reuse a key share for multiple connections. Reuse of a key share
  allows passive observers to correlate different connections." This
  specification discourages client and server reuse of a key share for
  multiple internet connections. Reusing key shares outside protected
  facilities can also expand the impact of security breaches.

- Except in cases of exclusively symmetric key management environments,
  sharing symmetric keys should be restricted to data center
  environments. A node with access to the symmetric traffic keys can
  view all traffic and impersonate the endpoints by modifying and
  injecting traffic.

- The TLS 1.2 visibility mechanisms that are based on RSA private key
  sharing allow middleboxes to masquerade as servers. The TLS 1.3
  mechanisms prevent this because you don't need to share the signature
  private key to gain visibility.

Risk
----

TLS 1.3 significantly reduces risks associated with TLS 1.2. Its
approach to achieving forward secrecy creates a risk to systems and
enterprises whose IT security teams need visibility into traffic
exchanges. From a cryptographic point of view, enterprises implementing
TLS 1.3 might effectively mandate reliance on endpoint solutions to
achieve their operational security requirements. However, this can be
impractical for many enterprises.

For instance, if an enterprise relied entirely upon endpoint
security—without any visibility by middleboxes—they would need the items
listed below. This would require time and resources and could
potentially impact the migration to TLS 1.3.

A frequent first step taken by a sophisticated attacker on a target is
to modify, disable, or evade endpoint security tools. This is an
enduring reality faced by "blue team security practitioners" (e.g.,
security operations or incident response teams) for decades. Researchers
continue to publish results of successful evasion and neutering
techniques for all endpoint controls, including the most sophisticated
tools available on the market. Nonetheless, if malware has detonated on
a computer, the only thing between it and the endpoint security tool is
the OS. To combat this risk, organizations should budget for and perform
the following steps:

- Follow OS hardening requirements to limit the ability of
  software-accessible accounts to control endpoint security tools.

- Implement strategies that can help identify missing, fraudulent, or
  anomalous status or log data from the endpoint tool(s).

- Upgrade, modernize, or replace all legacy applications that leverage
  insecure libraries, protocols, applications, and subsystems throughout
  the endpoint state.

- Ensure that remote access to all endpoint agent management tools
  adheres to the most stringent authentication/authorization strategies.

- Implement strategies to persistently refresh endpoint agent policy or
  accurately detect policy drift.

- Implement a credible application allowlist solution to prevent
  execution/reading of applications and libraries.

- Endpoint control techniques such as enhanced logging can be effective
  detective controls where the following conditions are met:

  - Secure adequate funding to maintain a robust security information
    and event management (SIEM) infrastructure

  - Make trained personnel available to manage an SIEM or similar tool
    to create and administer correlation rules to produce timely,
    accurate alerts related to anomalous activity.

- Implement appropriate configuration of all cogent log-generating
  agents on the endpoint (e.g., instant log transfer to SIEM vs.
  periodic transfer of batched logs that can be deleted by an attacker
  to hide their activity).

See NIST SP 800-92 Revision 1, `Cybersecurity Log Management Planning
Guide <https://csrc.nist.gov/pubs/sp/800/92/r1/ipd>`__, for more
information on logging and log protection.

Different types of malware execute with different intentions.
Destructive malware often doesn't require the instantiation of
command-and-control (C2) communication with attacker infrastructure.
However, the goals of the most sophisticated adversaries (e.g.,
financial gain, data exfiltration) are best achieved by maintaining
persistence via a C2 channel over a network to the attacker. To counter
this action, organizations should make security controls surrounding
outbound network communications from organizational endpoints maximally
restrictive.

The above concepts are beneficial to any organization. Yet, some IT and
security practitioners outside of highly targeted enterprises view these
concepts as ''nice to haves' rather than 'must haves.' Experience shows
that when network visibility is lost, network controls are also
lost—elevating "nice to haves" to the utmost imperatives.

As stated previously, re-architecting networks is difficult, expensive,
and time-consuming. Even if viable, it is not a practical short-term
solution for any organization, including large data centers. To mitigate
risk, organizations must make their endpoint solutions stable, capable,
and effective. To meet these goals, endpoint solutions must become
consistent and reliable recorders of all related events (enhanced
logging). In addition, producing, collecting, storing, and parsing
terabytes (or more) of data requires building a completely separate
infrastructure. This is not a simple proposition. Building this
infrastructure requires DPI for certain data, as well as for management
activities. Furthermore, if the true root cause of a compromise or other
network problem is occurring at a middlebox device, endpoints will not
see this information. Using intermediate proxies between all tiers adds
cost, latency, and potential points of failure. It also becomes less
viable as the number of tiers per given application increases; costs and
complexity arise, too, in many cases. Finally, situations will occur
where intermediate proxies are not possible, such as secure subnets and
virtual environments.

When adopting any visibility solution, it's imperative to protect stored
session keys from being accessed by external entities to the data
center. This requires implementing access controls that enforce least
privilege within the data center. Consequently, management's risk
assessment involves trading off the relative consequences of delaying
TLS 1.3 implementation or replacing enterprise data centers against the
cost of protecting stored session keys from access by processes other
than those that require or are approved for specific continuous
monitoring or forensics functions. While implementing visibility
solutions, enterprises must focus on supporting least privilege
principles, compliance with zero trust, and supply chain security
requirements. See NIST SP 800-207 :ref:`[14].<SP207>` Ideally,
implementations will provide network owners with control over what
information is actually shared with monitoring systems. Cryptographic
protection of all keys, whether at rest or in transit, is essential
except where the keys are being employed in a cryptographic process or
approved compensating controls are employed.

Standardized open interfaces for endpoint interception are needed but
are not currently available in applications that scale to the
requirements of large data centers. As a result, organizations may
determine that acceptance of some cryptographic security risks
associated with the visibility solutions described herein is acceptable
in the face of the consequences of delaying TLS 1.3 implementation and
of loss of visibility into information exchanges by the IT security
staff responsible for security monitoring and forensics. One of the
visibility approaches demonstrated in this project involves middlebox
solutions. The risks associated with introducing in-house middleboxes
having man-in-the-middle capabilities and/or caching or otherwise
storing session keys may be weighed against the consequences of losing
security monitoring and forensics capabilities.

Security Control Map
--------------------

Mappings between cybersecurity functions performed by the reference
design's logical components and the security characteristics enumerated
in relevant cybersecurity documents are available at :mark:`[provide
link]`.

Any organization can use these mappings to implement or refine TLS 1.3
visibility solutions. The mappings explain how cybersecurity functions
from the reference design relate to NIST-recommended security outcomes
and controls. See the security outcome subcategories from the NIST
Cybersecurity Framework (*Framework for Improving Critical
Infrastructure Cybersecurity* [CSF] 2.0) :ref:`[15]<csf>` and security
controls identified in NIST SP 800-53r5 (*Security and Privacy Controls
for Information Systems and Organizations*) :ref:`[16]<SP800_53>` for
more details. All of the elements in these mappings—the TLS 1.3
visibility cybersecurity functions, CSF Subcategories, and SP 800-53
controls—are concepts involving ways to reduce cybersecurity risk. The
mapping methodology is described in NIST IR 8477 *Mapping Relationships
Between Documentary Standards, Regulations, Frameworks, and Guidelines:
Developing Cybersecurity and Privacy Concept Mappings* [add this
reference].

The two primary use cases for this mapping (below) are not intended to
be comprehensive.

1. **Why should organizations implement TLS 1.3 visibility solutions?**
   This use case identifies how implementing TLS 1.3 visibility
   solutions can help organizations achieve CSF Subcategories and SP
   800-53 controls. Communicating to those individuals who expend
   resources to implement TLS 1.3 visibility, e.g., chief information
   security officers and security teams, can help fulfill other security
   requirements.

2. **How can organizations implement TLS 1.3 visibility solutions?**
   This use case identifies how an organization's existing
   implementations of CSF Subcategories and SP 800-53 controls can help
   support the trusted implementation of TLS 1.3 visibility solutions.
   An organization looking to implement TLS 1.3 visibility solutions
   might first assess its current security capabilities so that it can
   plan how to add missing capabilities and enhance existing
   capabilities. Organizations can leverage their existing security
   investments and prioritize future security technology deployment to
   address the gaps.




