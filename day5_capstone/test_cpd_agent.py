# day5_capstone/test_cpd_agent.py

import asyncio
from pprint import pprint

from runner_setup import runner  # uses the file we just created


async def ask_cpd_agent(
    message: str,
    user_id: str = "demo_user",
    session_id: str = "cpd_demo",
):
    print(f"\nUser > {message}")
    response = await runner.run_debug(
        [message],
        user_id=user_id,
        session_id=session_id,
        verbose=True,
    )
    return response


async def main():
    # You can change these test queries to whatever you want
    queries = [
        "What is the overall training completion rate?",
        "Which staff are underperforming below 70% completion?",
        "Please generate a reminder email for staff_id: 101",
    ]

    for q in queries:
        resp = await ask_cpd_agent(q)
        print("\nAssistant response:")
        pprint(resp)
        print("\n" + "=" * 80)


if __name__ == "__main__":
    asyncio.run(main())
