.. _ProjectOverview:

Project Overview
################

Background
----------

The NCCoE hosted an industry roundtable in 2018 to assess the scope of
the visibility challenges faced by enterprises. NCCoE staff participated
in the Center for Cybersecurity Policy's 2019 workshop
:ref:`[4]<ccpl_workshop>` on enterprise visibility and helped identify a
set of baseline criteria for acceptability of
solutions for visibility challenges. The NCCoE adopted the criteria
without change and hosted a virtual workshop focused on TLS 1.3 in
September 2020 :ref:`[5]<workshop>`. We identified the options below to
maintain visibility:

- Endpoint mechanisms that establish visibility, such as enhanced
  logging

- Network architectures that inherently provide visibility, e.g., using
  overlays or incorporating middleboxes

- Key management mechanisms that defer forward secrecy to maintain
  current levels of network visibility

- Innovative tools that analyze network traffic without decryption

- Deploying alternative standards-based network security protocols where
  forward secrecy is optional or unsupported.

In May 2021, the NCCoE published a project description for a TLS 1.3
visibility project that featured use case scenarios for the
implementation of potential solutions, as discussed in the workshops.
Collaborators participating in this project submitted their capabilities
in response to NIST's open call in the *Federal Register* for all
sources of relevant security capabilities from academia and industry
(vendors and integrators). Those respondents with relevant capabilities
or product components were selected as collaborators and signed a
Cooperative Research and Development Agreement (CRADA) to participate
with NIST in a consortium to build the example solution and to develop
the architectures and demonstration scenarios featured in this practice
guide.

Solution
--------

The project demonstrates approaches and practices that meet common
compliance, operations, and security requirements while gaining the
performance and capability benefits that TLS 1.3 deployment offers.

We focus on enterprise data center environments. This includes
on-premises data centers and hybrid cloud deployments hosted by a
third-party data center or public cloud provider. We use real-world
visibility approaches that utilize current or emerging components,
proprietary vendor products, and commercially viable open-source
solutions. We include approaches that restore visibility into encrypted
data in transit, such as alternative key establishment mechanisms and
how to manage NIST's and industry's standards. The following are out of
scope and not impacted by our proposed solutions:

- Information transmitted over the public internet (e.g., connections
  between enterprise users and services on the public internet).

- Emerging deployment models leveraging encrypted transport to protect
  protocols that were previously in the clear, such as DoT (Domain Name
  System [DNS] over TLS) :ref:`[6]<rfc7858>`, DoH (DNS over Hypertext
  Transfer Protocol Secure [HTTPS]) :ref:`[7]<rfc8484>`, and DoQ (DNS
  over QUIC) :ref:`[8]<rfc9250>`. DoT, DoH, and DoQ may be the subject of
  future NCCoE work.

This project does not change or replace the RFC 8446 standard. Our
proposed solutions provide secure management of servers' cryptographic
keys, securely manage recorded traffic, and consider privacy via a broad
set of options, including:

- **Key-management mechanisms** that defer forward secrecy until all
  copies of keying material needed to maintain current levels of network
  visibility are deleted (such as copies retained to support passive
  decryption and inspection, referred to throughout this document as
  passive inspection).

- **Network architectures** that provide visibility, such as using
  overlays or incorporating middleboxes (see RFC 3234: Middleboxes:
  Taxonomy and Issues :ref:`[3]<rfc3234>`).

The TLS 1.3 visibility project focuses on passive inspection and
middlebox solutions to avoid losing TLS 1.3 visibility characteristics
and vulnerabilities identified in TLS 1.2.

To achieve visibility through key management (via passive inspection),
we demonstrate two technical mechanisms for servers whose traffic is of
interest to the enterprise, as follows:

- The enterprise provisions bounded-lifetime Diffie-Hellman (DH) key
  pairs for TLS 1.3 servers and are used in ephemeral key exchanges.
  This approach includes a purely static deployment that can also use
  key pairs for a short period of time.

- The enterprise collects and retains the per-session symmetric session
  keys used to encrypt the connections instead of provisioning DH key
  pairs.

  Some aspects of analytics functions need enterprise visibility into
  their encrypted traffic. This may require combining network
  architecture and key-management techniques to achieve operational
  visibility. Therefore, this project demonstrates an architecture that
  achieves visibility inside the data center using tools that break and
  inspect traffic. These middleboxes are commonly used at the enterprise
  edge to achieve real-time visibility. We also demonstrate how an
  enterprise can access historical data through key management-based
  solutions.

With passive inspection solutions, a key distribution function manages
DH keys and symmetric traffic keys. Both are retained by a key
distribution function while corresponding encrypted traffic is either
decrypted, destroyed, or no longer available.

Authorized systems that examine traffic obtain the appropriate keys
from the key distribution function. The solution incorporates
components to retain traffic for retrospective applications, e.g.,
troubleshooting and cybersecurity forensics. Stored traffic is
retained in encrypted form until policy conditions (e.g., retention
time limits) are met. The data is then deleted by the storage
function. The resulting solutions protect keys and data against misuse
or compromise, and they don't leave recorded traffic at risk of
compromise indefinitely. The solutions include mechanisms and
procedures used to transmit, store, provide access to, and use
cryptographic keys that can perform comprehensive deletion of
decryption keys when defined temporal or data protection limits are
met.

Since TLS 1.3 is designed to allow client/server communication in a way
that prevents eavesdropping, the solutions also assume out-of-band
notification of the visibility policy.
