# 🔐 Snort-Based IDS/IPS Project

## 📘 Project Overview

This project demonstrates the deployment and configuration of **Snort**, a signature-based Network Intrusion Detection and Prevention System (IDS/IPS), to monitor and secure a Linux-based environment. The system is designed to detect, alert, and prevent common network attacks by implementing custom Snort rules across all supported action types:

- **Intrusion Detection System (IDS) mode**
- **Inline Intrusion Prevention System (IPS) mode**

The system captures and analyzes network traffic using both passive (IDS) and active (IPS) modes, triggered via simulated attack traffic such as port scans, unauthorized access attempts, and exploit patterns.

---

## 🧰 Tools & Technologies

| Tool            | Purpose                             |
|-----------------|-------------------------------------|
| Snort 2.x       | Packet inspection and rule engine   |
| Ubuntu Linux    | Host OS for Snort and testing       |
| Python          | Log parsing and reporting           |
| Netcat / Curl   | Trigger HTTP, TCP traffic           |
| Nmap / FTP      | Trigger scan and brute-force tests  |
| IPTables        | Route packets to Snort via NFQUEUE  |
| Python HTTP Server | Simulated vulnerable service     |

---

## 🛡️ Rule Action Types Implemented

The project includes **18 custom Snort rules**, categorized into **6 rule action types**, each with 3 distinct detection or blocking scenarios.

| Action  | Description                              | Behavior                                           |
|---------|------------------------------------------|----------------------------------------------------|
| `alert` | Passive detection + alert                | Detects suspicious activity (e.g., FTP, `/admin`)  |
| `log`   | Packet logging                           | Saves full packet data for forensic analysis       |
| `drop`  | IPS blocking with logging                | Blocks threats silently (e.g., SSH/Telnet)         |
| `reject`| IPS blocking + notify attacker           | Sends RST/ICMP reply when blocking (e.g., ping)    |
| `pass`  | Allow listed traffic to bypass rules     | Whitelist trusted IPs or DNS traffic              |
| `sdrop` | Silently block without logging           | Ultra-stealth block (e.g., RDP, SNMP, DCOM)        |

---




