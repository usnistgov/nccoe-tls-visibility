**NIST SPECIAL PUBLICATION 1800-37**

.. _Root:

Addressing Visibility Challenges with TLS 1.3 within the Enterprise
###################################################################


.. toctree::
   :maxdepth: 5
   :titlesonly:
   :glob:
   :hidden:

   A_ExecutiveSummary.rst
   B_Introduction.rst
   C_ProjectOverview.rst
   D_Architecture.rst
   E_Builds.rst
   F_Demonstrations.rst
   G_RiskCompliance.rst
   H_GeneralFindings.rst
   L_Appendices.rst
   Z_ChangeLog.rst

+----------------------------+----------------------------+----------------------------+
| **Murugiah Souppaya** |br| | **David Wells** |br|       | **Murali Palamisamy** |br| |
| |br|                       | **Johann Tonsing** |br|    | |br|                       |
| National Institute of |br| | |br|                       | AppViewX |br|              |
| Standards and Technology   | Mira Security  |br|        | New York, NY               |
|                            | Cranberry Township, PA     |                            |
+----------------------------+----------------------------+----------------------------+
| **William Barker** |br|    | **Sean Turner** |br|       | **Dung Lam** |br|          |
| |br|                       | |br|                       | |br|                       |
| Dakota Consulting |br|     | sn3rd |br|                 | F5 |br|                    |
| Silver Spring, MD          | Washington, DC             | Seattle, WA                |
+----------------------------+----------------------------+----------------------------+
| **Karen Scarfone** |br|    | **Patrick Kelsey** |br|    | **Paul Barrett** |br|      |
| |br|                       | |br|                       | **Ray Jones** |br|         |  
| Scarfone Cybersecurity |br|| Not for Radio |br|         | **Sandeep Jha** |br|       |
| Clifton, VA                | Manheim, PA |br|           | |br|                       |
|                            |                            | NETSCOUT |br|              |
|                            |                            | Westford, MA               |
+----------------------------+----------------------------+----------------------------+
| **John Kent** |br|         | **Russ Housley** |br|      |                            |
| **Julian Sexton** |br|     | |br|                       |                            |
| **Michael Dimond** |br|    | |br|                       |                            |
| **Ryan Williams** |br|     | |br|                       |                            |
| The MITRE Corporation |br| | Vigil Security, LLC |br|   |                            |
| McLean, VA                 | Herndon, VA                |                            |
+----------------------------+----------------------------+----------------------------+



February 2025

PRELIMINARY DRAFT

..figure: 

|This graphic contains the logos for NIST and the NCCoE.|

**DISCLAIMER**

Certain commercial entities, equipment, products, or materials may be identified by name or company logo or other insignia in order to acknowledge their participation in this collaboration or to describe an experimental procedure or concept adequately. Such identification is not intended to imply special status or relationship with NIST or recommendation or endorsement by NIST or NCCoE; neither is it intended to imply that the entities, equipment, products, or materials are necessarily the best available for the purpose.

While NIST and the NCCoE address goals of improving management of cybersecurity and privacy risk through outreach and application of standards and best practices, it is the stakeholder's responsibility to fully perform a risk assessment to include the current threat, vulnerabilities, likelihood of a compromise, and the impact should the threat be realized before adopting cybersecurity measures such as this recommendation.

National Institute of Standards and Technology Special Publication 1800-37, Natl. Inst. Stand. Technol. Spec. Publ. 1800-37, (February 2025), CODEN: NSPUE2

**FEEDBACK**

You can view or download the initial public draft guide at the `NCCoE TLS Visibility project page <https://www.nccoe.nist.gov/addressing-visibility-challenges-tls-13>`__.

NIST used an agile process to make updates available as new example solutions were added. With this initial public draft, all example solutions are complete. We are now asking for feedback on this initial public draft.

Please submit comments by completing the comment template spreadsheet posted on the `NCCoE TLS Visibility project page <https://www.nccoe.nist.gov/addressing-visibility-challenges-tls-13>`__ and emailing it to applied-crypto-visibility@nist.gov.

.. note::
   TODO: Fill in the dates below.

Public comment period: xxx y, 2025 through Mmmmm dd, 2025

All comments are subject to release under the Freedom of Information Act.

NIST is particularly interested in your feedback on the following questions:

1.	How well do the practices in this guide relate to existing practices leveraged by your organization? Are there significant gaps between the sets of practices that this guide should address?

2.	How do you expect this guide to influence your future practices and processes?

3.	How do you envision using this guide? What changes would you like to see to increase/improve that use?

4.	What suggestions do you have on changing the format of the provided information?


| National Cybersecurity Center of Excellence
| National Institute of Standards and Technology
| 100 Bureau Drive
| Mailstop 2002
| Gaithersburg, MD 20899
| Email: nccoe@nist.gov

**NATIONAL CYBERSECURITY CENTER OF EXCELLENCE**

The National Cybersecurity Center of Excellence (NCCoE), a part of the National Institute of Standards and Technology (NIST), is a collaborative hub where industry organizations, government agencies, and academic institutions work together to address businesses ' most pressing cybersecurity issues. This public-private partnership enables the creation of practical cybersecurity solutions for specific industries, as well as for broad, cross-sector technology challenges. Through consortia under Cooperative Research and Development Agreements (CRADAs), including technology partners—from Fortune 50 market leaders to smaller companies specializing in information technology security—the NCCoE applies standards and best practices to develop modular, adaptable example cybersecurity solutions using commercially available technology. The NCCoE documents these example solutions in the NIST Special Publication 1800 series, which maps capabilities to the NIST Cybersecurity Framework and details the steps needed for another entity to re-create the example solution. The NCCoE was established in 2012 by NIST in partnership with the State of Maryland and Montgomery County, Maryland.

To learn more about the NCCoE, visit https://www.nccoe.nist.gov/. To learn more about NIST, visit https://www.nist.gov.

**NIST CYBERSECURITY PRACTICE GUIDES**

NIST Cybersecurity Practice Guides (Special Publication 1800 series) target specific cybersecurity challenges in the public and private sectors. They are practical, user-friendly guides that facilitate the adoption of standards-based approaches to cybersecurity. They show members of the information security community how to implement example solutions that help them align with relevant standards and best practices, and provide users with the materials lists, configuration files, and other information they need to implement a similar approach.

The documents in this series describe example implementations of cybersecurity practices that businesses and other organizations may voluntarily adopt. These documents do not describe regulations or mandatory practices, nor do they carry statutory authority.

**ABSTRACT**

The Transport Layer Security (TLS) protocol is widely deployed to secure network traffic. The latest version, TLS 1.3, has been strengthened so that even if a TLS-enabled server is compromised, the contents of its previous TLS communications are still protected—better known as forward secrecy. The approach used to achieve forward secrecy interferes with passive decryption techniques that are widely used by enterprises to achieve visibility into their own TLS 1.2 traffic. Many enterprises depend on that visibility to permit their authorized network security staff to implement controls needed to conform to cybersecurity, operational, and regulatory requirements. This forces enterprises to choose between using the old TLS 1.2 protocol or adopting TLS 1.3 with some alternative method for internal traffic visibility. The NCCoE has, in collaboration with technology providers and enterprise customers, initiated a project demonstrating options for maintaining visibility within the TLS 1.3 protocol within an enterprise to overcome these impediments. The project demonstrates several standards-compliant builds that can be used within enterprises to provide both real-time and post-facto systems monitoring and analytics capabilities. This publication describes the motivation, approach, architecture, build implementation, demonstration scenarios, results, and risk and compliance management characteristics for the demonstrated proofs of concept. Links to detailed technical information on implementation of each build resident on GitHub can serve as a valuable resource for your technology implementers by providing models they can emulate. The lessons learned from the implementations and integrations can benefit your organization by saving time and resources. This guide also includes links to mappings of TLS 1.3 visibility principles to commonly used security standards and guidance.

**KEYWORDS**

*bounded lifetime; break and inspect; ephemeral; key management; middlebox; passive decryption; passive inspection; protocol; Transport Layer Security (TLS); visibility*

**ACKNOWLEDGMENTS**

We are grateful to the following individuals for their generous contributions of expertise and time.

.. csv-table::
   :header: "Name", "Organization"

   "Ravishankar Chamarajnagar",  "AppViewX"
   "Michael Ackerman",           "Blue Cross Blue Shield"
   "Tim Cahill",                 "JPMorgan Chase & Company"
   "Dean Coclin",                "DigiCert"
   "Avesta Hojjati",             "DigiCert"
   "Jonathan Chen",              "F5"
   "Ryan Johnson",               "F5"
   "Brad Otlin*",                "F5"
   "Kevin Stewart",              "F5"
   "Joshua Klosterman",          "The MITRE Corporation"
   "Michael Dimond",             "The MITRE Corporation"
   "Julian Sexton",              "The MITRE Corporation"
   "Nanjaiah Vijayalakshmi",     "NETSCOUT"
   "David Cooper",               "NIST"
   "William Polk*",               "NIST (former employee)"
   "Gina Scinta",                "Thales Trusted Cyber Technologies"
   "Steven Fenter",              "U.S. Bank Corporation"
   "Jake Wills",                 "U.S. Bank Corporation"


*\* Former employee; all work for this publication was done while at that organization*

Special thanks to all who reviewed and provided feedback on this document.

The collaborators who have or will participate in this project's current or upcoming builds submitted their capabilities in response to a notice in the Federal Register. Respondents with relevant capabilities or product components were invited to sign a Cooperative Research and Development Agreement (CRADA) with NIST, allowing them to participate in a consortium to build this example solution. We are working with the following list of collaborators. 

.. csv-table:: Technology Partners/Collaborators

   "`AppViewX <https://www.appviewx.com/>`__ ", "`JPMorgan Chase & Company <https://www.jpmorganchase.com/>`__ ", "`Not for Radio, LLC <https://www.notforadio.com/>`__ "
   "`DigiCert <https://www.digicert.com/>`__ ", "`Mira Security, Inc. <https://mirasecurity.com/>`__ ", "`Thales Trusted Cyber Technologies <https://www.thalestct.com/>`__ "
   "`F5 <https://www.f5.com/>`__ ", "`NETSCOUT Corporation <https://www.netscout.com/>`__ ", "`U.S. Bank Corporation <https://usbank.com/>`__ "


**DOCUMENT CONVENTIONS**

The terms "shall" and "shall not" indicate requirements to be followed strictly to conform to the publication and from which no deviation is permitted. The terms "should" and "should not" indicate that among several possibilities, one is recommended as particularly suitable without mentioning or excluding others, or that a certain course of action is preferred but not necessarily required, or that (in the negative form) a certain possibility or course of action is discouraged but not prohibited. The terms "may" and "need not" indicate a course of action permissible within the limits of the publication. The terms "can" and "cannot" indicate a possibility and capability, whether material, physical, or causal.

**CALL FOR PATENT CLAIMS**

This public review includes a call for information on essential patent claims (claims whose use would be required for compliance with the guidance or requirements in this Information Technology Laboratory (ITL) draft publication). Such guidance and/or requirements may be directly stated in this ITL Publication or by reference to another publication. This call also includes disclosure, where known, of the existence of pending U.S. or foreign patent applications relating to this ITL draft publication and of any relevant unexpired U.S. or foreign patents.

ITL may require from the patent holder, or a party authorized to make assurances on its behalf, in written or electronic form, either:

a) assurance in the form of a general disclaimer to the effect that such party does not hold and does not currently intend holding any essential patent claim(s); or

b) assurance that a license to such essential patent claim(s) will be made available to applicants desiring to utilize the license for the purpose of complying with the guidance or requirements in this ITL draft publication either:

   1. under reasonable terms and conditions that are demonstrably free of any unfair discrimination; or 

   2. without compensation and under reasonable terms and conditions that are demonstrably free of any unfair discrimination. 

Such assurance shall indicate that the patent holder (or third party authorized to make assurances on its behalf) will include in any documents transferring ownership of patents subject to the assurance, provisions sufficient to ensure that the commitments in the assurance are binding on the transferee, and that the transferee will similarly include appropriate provisions in the event of future transfers with the goal of binding each successor-in-interest. 

The assurance shall also indicate that it is intended to be binding on successors-in-interest regardless of whether such provisions are included in the relevant transfer documents. 

Such statements should be addressed to: applied-crypto-visibility@nist.gov

.. |This graphic contains the logos for NIST and the NCCoE.| image:: images/Figure1.png
   :alt: This graphic contains the logos for NIST and the NCCoE.

.. # define a hard line break for HTML
.. |br| raw:: html

   <br />