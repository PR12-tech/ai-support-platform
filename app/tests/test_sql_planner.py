from app.agent.planner import choose_tool


def main():

    tool, arguments = choose_tool(

        question="How many shipped orders are there?",

        observations=[],

        tool_history=[],

        context={}

    )

    print("\n========== SQL PLANNER TEST ==========\n")

    print(tool)

    print(arguments)

    print("\n======================================\n")


if __name__ == "__main__":

    main()