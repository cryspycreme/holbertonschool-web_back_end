import asyncio

async def task(name, delay):
    print(f"{name}: start")

    await asyncio.sleep(delay)
    print(f"{name}: resumed after first await")

    await asyncio.sleep(delay)
    print(f"{name}: resumed after second await")

    print(f"{name}: finished")


async def main():
    # Schedule multiple tasks running "concurrently"
    t1 = asyncio.create_task(task("Task A", 1))
    t2 = asyncio.create_task(task("Task B", 0.5))

    print("Main coroutine: awaiting both tasks")
    await t1
    await t2

asyncio.run(main())
