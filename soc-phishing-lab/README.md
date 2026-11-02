# SOC Phishing Investigation Lab

A defensive security operations exercise designed around a simulated phishing-related endpoint alert. The analyst takes the role of a Tier 1 Security Operations Center (SOC) analyst and investigates the supplied event records.

## Scenario

During routine monitoring, a security alert indicates a possible incident involving an employee in the finance department. The task is to reconstruct the sequence of events from the available logs, identify relevant indicators of compromise (IOCs), and determine what action the endpoint protection tool took.

The scenario is an investigation exercise. Findings must be supported by the supplied evidence; do not assume that every suspected attack stage occurred.

## Available files

- `logs/splunk_events.log` — event records exported from a SIEM-style environment, arranged chronologically.
- `iocs/iocs.txt` — workspace for recording identified indicators of compromise.

## Investigation questions

1. What are the sender's email address and the subject of the suspicious message?
2. What archive file did the user download, and from which URL?
3. Which child process was created on the endpoint after the file was executed?
4. Which external destination IP address did the script attempt to contact?
5. What action did the endpoint detection and response (EDR) or antivirus system take?

## Suggested workflow

1. Build a timeline from the available events.
2. Identify the phishing message and the user's interaction with it.
3. Trace downloaded files and process creation events.
4. Extract relevant network indicators.
5. Determine the endpoint protection outcome.
6. Record each conclusion with its supporting event or log reference, and distinguish confirmed facts from hypotheses.

## Scope and safety

This is a defensive, educational investigation. Analyze the supplied logs in a controlled environment. Do not execute unknown payloads or interact with external infrastructure identified in the logs.

## Author

Ruan Molinari — [GitHub](https://github.com/RuanMolinari)
