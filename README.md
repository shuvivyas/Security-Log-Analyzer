# Security Log Analyzer

A lightweight Python-based Security Log Analyzer that detects suspicious authentication activities such as Brute Force and Password Spraying attacks from log files.

## Features

- Parses authentication logs
- Detects Brute Force Attacks
- Detects Password Spraying Attacks
- Generates security alerts with attacker IP details
- Simple and modular Python code structure
- Includes sample log data for testing

## Attack Detection

### Brute Force Attack
Identifies IP addresses with 3 or more failed login attempts.

Example:
```text
2026-01-01 login failed user=admin ip=6.3.5.8
2026-01-01 login failed user=test ip=6.3.5.8
2026-01-01 login failed user=root ip=6.3.5.8
```

### Password Spraying Attack
Detects an IP address attempting logins against multiple user accounts.

Example:
```text
2026-01-01 login failed user=admin ip=6.3.5.8
2026-01-01 login failed user=test ip=6.3.5.8
2026-01-01 login failed user=root ip=6.3.5.8
2026-01-01 login failed user=guest ip=6.3.5.8
```

## Project Structure

```text
Security-Log-Analyzer/
│
├── logs/
│   └── sample.log
│
├── analyzer.py
├── parser.py
├── detector.py
├── alerts_triage.json
└── README.md
```

## How It Works

1. Read authentication logs.
2. Parse each log entry into structured data.
3. Analyze login events.
4. Detect suspicious patterns.
5. Generate alerts for potential attacks.

## Sample Output

```python
[
    {
        "Alert Type": "Brute Force Attack",
        "IP": "1.2.3.4",
        "Attempts": 6
    },
    {
        "Alert Type": "Password Spraying Attack",
        "IP": "6.3.5.8",
        "User Accounts": {
            "admin",
            "test",
            "root",
            "guest"
        }
    }
]
```

## Technologies Used

- Python
- Dictionaries
- Sets
- Collections (defaultdict)
- Log Analysis
- Cybersecurity Fundamentals


## Outcomes

This project demonstrates:

- Log parsing and analysis
- Security event detection
- Basic SOC alerting concepts
- Python data processing
- Threat detection fundamentals
