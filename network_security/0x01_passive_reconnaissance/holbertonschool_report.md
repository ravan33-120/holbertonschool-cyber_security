Passive Reconnaissance Summary
Target Domain: holbertonschool.com
1. Overview

This document presents the results of a passive reconnaissance study
conducted on holbertonschool.com.
All data was gathered using the Shodan search engine, without performing
any direct interaction, probing, or active scanning against the target
infrastructure.

2. Identified IP Information

According to publicly available Shodan data, the following IP addresses
are linked to holbertonschool.com and related services:

35.180.27.154

52.47.143.83

Network and Hosting Details

Cloud Provider: Amazon Web Services (AWS)

Platform: EC2

Geographic Location: Paris, France

This suggests that the target domain is deployed on AWS cloud-based
infrastructure.

3. Observed Subdomains

Passive analysis revealed several subdomains associated with the main
domain:

holbertonschool.com

www.holbertonschool.com

yriry.holbertonschool.com

The yriry.holbertonschool.com subdomain appears to be related to a
Level 2 discussion forum or internal platform.

4. Detected Technologies

Information obtained from Shodan indicates the use of the following
technologies and services:

Web Server

Nginx running on Ubuntu

Hosting Environment

Amazon EC2 (AWS)

Security Features

Support for TLS 1.2 and TLS 1.3

SSL/TLS certificates issued by Let’s Encrypt

Network Behavior

HTTP 301 redirection enabled

Open ports:

80 (HTTP)

443 (HTTPS)

5. Assessment

The passive reconnaissance process provided a clear picture of the
target’s hosting and security setup.
Holbertonschool.com operates on AWS infrastructure, implements modern
encryption protocols, and enforces secure HTTPS connections.
Several subdomains were identified, each likely serving a distinct
function.
