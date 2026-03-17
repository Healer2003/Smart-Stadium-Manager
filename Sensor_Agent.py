import asyncio
from spade.agent import Agent
from spade.behaviour import PeriodicBehaviour
from spade.message import Message
from Stadium_Environment import StadiumEnvironment 

class SensorAgent(Agent):
    def __init__(self, jid, password):
        super().__init__(jid, password)
        self.env = StadiumEnvironment()

    class MonitorBehaviour(PeriodicBehaviour):
        async def run(self):
            # Update the environment
            self.agent.env.update()
            a, b, m = self.agent.env.get_data()
            weather = self.agent.env.weather_condition

            # Prepare message for coordinator
            msg = Message(to="stadium_ops@xmpp.jp")
            msg.set_metadata("performative", "inform")
            msg.body = f"{a},{b},{m}"

            await self.send(msg)

            # Human-friendly log
            print(f"[SENSOR] Crowd levels checked: Gate A is {a}% full, "
                  f"Gate B is {b}% full. Pitch moisture: {m}%. Weather: {weather}.")

    async def setup(self):
        print(f"[SENSOR AGENT] {self.jid} starting...")
        self.add_behaviour(self.MonitorBehaviour(period=5))


async def main():
    sensor = SensorAgent("pitch_monitor@xmpp.jp", "password123")
    await sensor.start()

    try:
        while True:
            await asyncio.sleep(1)
    except KeyboardInterrupt:
        await sensor.stop()


if __name__ == "__main__":
    asyncio.run(main())