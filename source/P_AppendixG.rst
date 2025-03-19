.. _AppendixG:

G. Mappings of TLS 1.3 Visibility Capabilities to Risk Framework Documents
###################################################################################

Mappings between cybersecurity functions performed by the reference design's logical components and the security characteristics enumerated in relevant cybersecurity documents are provided in this appendix. These mappings are intended for any organization that is interested in implementing TLS 1.3 visibility solutions or that has begun or completed an implementation.
The mappings provide information on how cybersecurity functions from the reference design are related to NIST-recommended security outcomes and controls: the security outcome subcategories from the NIST Cybersecurity Framework (Framework for Improving Critical Infrastructure Cybersecurity [CSF] 2.0) and security controls identified in NIST SP 800-53r5 (Security and Privacy Controls for Information Systems and Organizations). All of the elements in these mappings—the TLS 1.3 visibility cybersecurity functions, CSF Subcategories, and SP 800-53 controls—are concepts involving ways to reduce cybersecurity risk.

Return to :ref:`Risk_and_Compliance_Management`.

.. _G.1:

G.1 Use Cases
*************

There are two primary use cases for this mapping. They are not intended to be comprehensive.

1.	**Why should organizations implement TLS 1.3 visibility solutions?** This use case identifies how implementing TLS 1.3 visibility solutions can support organizations in achieving CSF Subcategories and SP 800-53 controls. This helps communicate to an organization's chief information security officer, security team, and senior management that expending resources to implement TLS 1.3 visibility solutions can also aid in fulfilling other security requirements.

2.	**How can organizations implement TLS 1.3 visibility solutions?** This use case identifies how an organization's existing implementations of CSF Subcategories and SP 800-53 controls can help support trusted implementation of TLS 1.3 visibility solutions. An organization wanting to implement TLS 1.3 visibility solutions might first assess its current security capabilities so that it can plan how to add missing capabilities and enhance existing capabilities. Organizations can leverage their existing security investments and prioritize future security technology deployment to address the gaps.

.. _G.2:

G.2 Mapping Terminology
***********************


In this publication, we use the following relationship types from NIST IR 8477 to describe how the functions in our reference design are related to the NIST reference documents. Note that the Supports relationship applies only to use case 1 in Section D.1 and the Is Supported By relationship applies only to use case 2. 

•	Supports: TLS 1.3 Visibility function X supports security control/Subcategory/capability/requirement Y when X can be applied alone or in combination with one or more other functions to achieve Y in whole or in part.

•	Is Supported By: TLS 1.3 Visibility function X is supported by security control/Subcategory/capability/requirement Y when Y can be applied alone or in combination with one or more other security controls/Subcategories/capabilities/requirements to achieve X in whole or in part. 

Each Supports and Is Supported By relationship has one of the following properties assigned to it:

•	Example of: The supporting concept X is one way (an example) of achieving the supported concept Y in whole or in part. However, Y could also be achieved without applying X.

•	 Integral to: The supporting concept X is integral to and a component of the supported concept Y. X must be applied as part of achieving Y.

•	Precedes: The supporting concept X precedes the supported concept Y when X must be achieved before applying Y. In other words, X is a prerequisite for Y. 

When determining whether a reference design function's support for a given CSF Subcategory or SP 800- 53 control is integral to that support versus an example of that support, we do not consider how that function may in general be used to support the Subcategory, control, capability, or requirement. Rather, we consider only how that function is intended to support that Subcategory, control, capability, or requirement within the context of our reference design. 

Also, when determining whether a function is supported by a CSF Subcategory, SP 800-53 control, capability, etc. with the relationship property of precedes, we do not consider whether it is possible to apply the function without first achieving the Subcategory, control, capability, or requirement. Rather, we consider whether, according to our reference design, the Subcategory, control, capability, or requirement. Rather, 434 we consider whether, according to our reference design, the Subcategory, control, capability, or 435 requirement is to be achieved prior to applying that function.

.. _G.3:

G.3 Cybersecurity Framework (CSF) Mapping
*****************************************

This section provides a mapping of system architectural elements to the CSF. It includes both CSF objectives that need to be met for secure operation of the platform for visibility into TLS 1.3-protected traffic and CSF objectives that the platform supports.

.. nccoe-mapping-table::
   :header: Logical Architecture Component, Component's Function, Function's Relationship to CSF Subcategories, Relationship Explanation
   :widths: 10 30 30 30
   :file: ./csv/csf.csv

.. _G.4:

G.4 Special Publication (SP) 800-53 Mapping
*******************************************

While SP 800-53 identifies a broad range of controls that are applicable to the TLS 1.3 visibility platform that is described in this publication, a number of the controls are particularly needed to implement the demonstrated configuration securely. The following table identifies these controls using the "is supported by" designation. The table also identifies SP 800-53 controls that are supported by the demonstrated platform.

.. nccoe-mapping-table::
   :header: Logical Architecture Component, Component's Function, Function's Relationship to SP 800-53 Controls, Relationship Explanation
   :widths: 10 30 30 30
   :file: ./csv/800-53.csv
 