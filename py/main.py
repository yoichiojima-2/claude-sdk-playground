from argparse import ArgumentParser

import asyncio

import claude_agent_sdk as claude
from claude_agent_sdk import query, ClaudeAgentOptions


ALLOWED_TOOLS = [
    "Read",
    "Write",
    "Edit",
    "Bash",
    "Glob",
    "Grep",
    "WebSearch",
    "WebFetch",
    "AskUserQuestion",
]


def parse_args():
    parser = ArgumentParser()
    parser.add_argument("-p", "--prompt", type=str)
    return parser.parse_args()


async def query(prompt, allowed_tools):
    messages = claude.query(
        prompt="hello",
        options=claude.ClaudeAgentOptions(allowed_tools=allowed_tools)
    )
    async for message in messages:
        yield message


async def main():
    args = parse_args()
    async for message in query(args.prompt, ALLOWED_TOOLS):
        print(message)


if __name__ == "__main__":
    asyncio.run(main())

