import asyncio
from spade.agent import Agent
from spade.behaviour import CyclicBehaviour

class CoordinatorAgent(Agent):

    class DecisionLogic(CyclicBehaviour):

        async def run(self):
            msg = await self.receive(timeout=10)

            if msg:
                try:
                    a, b, m = map(int, msg.body.split(","))
                    await self.process_data(a, b, m)
                except ValueError:
                    print(f"[WARNING] Received invalid data: {msg.body}")

        async def process_data(self, a, b, m):

            if a > 85:
                print(f"[ALERT] Gate A is overcrowded ({a}% full). "
                      f"Fans are being redirected to Gate B for safety.")

            elif m < 30:
                print(f"[MAINTENANCE] The pitch is getting dry ({m}% moisture). "
                      f"Sprinklers are now turned on.")

            else:
                print(f"[STATUS] Stadium conditions are normal. "
                      f"Gate A: {a}% full, Pitch moisture: {m}%.")

    async def setup(self):
        print(f"[COORDINATOR AGENT] {self.jid} starting...")
        self.add_behaviour(self.DecisionLogic())


async def main():
    coordinator = CoordinatorAgent("stadium_ops@xmpp.jp", "password123")
    await coordinator.start()

    try:
        while True:
            await asyncio.sleep(1)
    except KeyboardInterrupt:
        await coordinator.stop()


if __name__ == "__main__":
    asyncio.run(main())