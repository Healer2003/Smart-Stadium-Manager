
# Smart Stadium Manager (SSM)

This project implements an **Intelligent Multi-Agent System (MAS)** for a Smart Stadium environment. It follows the **Prometheus methodology** and utilizes the **SPADE framework** for agent development and **XMPP** for communication.

## 1. Environment Setup
The system is designed to run in **GitHub Codespaces**. Ensure you have the SPADE framework installed:

```bash
pip install spade
```
## 2. XMPP Configuration
This project uses the public xmpp.jp server for inter-agent communication. You must have two registered accounts on the server:

    Coordinator: stadium_ops@xmpp.jp

    Sensor: pitch_monitor@xmpp.jp

    [!IMPORTANT]
    Update the password field in both sensor_agent.py and coordinator_agent.py with your specific account credentials before running.

## 3. Project Structure
File	Description
stadium_env.py	Standalone Python module simulating physical stadium dynamics (gate occupancy and pitch moisture).
sensor_agent.py	Perceives the stadium state and transmits data via FIPA-ACL inform messages.
coordinator_agent.py	The decision-making brain. Processes data and executes safety or maintenance protocols.

## 4. How to Run the System

To see the agents in action, open two separate terminals in your Codespace:
Step 1: Start the Coordinator

The Coordinator must be running first to listen for messages.

``` bash

python coordinator_agent.py
```
Step 2: Start the Sensor

In a new terminal, start the Sensor to begin data transmission.

``` bash

python sensor_agent.py
```
## 5. Agent Logic & Capabilities
Crowd Management (Safety Goal)

If the sensor reports Gate A occupancy > 85%, the Coordinator triggers a safety plan to reroute fans to Gate B and updates digital signage.
Pitch Maintenance (Longevity Goal)

If soil moisture levels drop below 30%, the Coordinator triggers the irrigation system. It employs utility-based logic to balance resource use against turf health.

## 6. Communication Protocol

All interactions adhere to the FIPA-ACL standard. The Sensor agent uses the inform performative to share state data, ensuring a low-latency, decoupled architecture.