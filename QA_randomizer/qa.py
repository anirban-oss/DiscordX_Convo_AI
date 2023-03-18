import yaml
import time
import random
from textwrap import indent, fill

intro = (
    "#" * 78
    + "\n#"
    + f"{'MACHINE LEARNING INTERTVIEW PRACTICE QUESTIONS':^76}"
    + "#\n"
    + "#" * 78
    + "\n\nYou have 10 seconds to read each question and think up an "
    + "appropriate answer.\nEnter 'no' to stop."
)

with open("data.yaml") as f:
    data = yaml.safe_load(f)


def ask_question():
    question_info = random.choice(data)
    print(f"\nQuestion:\n{indent(question_info['question'], '   ')}\n")

    # Countdown
    for i in range(10, 0, -1):
        print(f"{i}", end=" \r", flush=True)
        time.sleep(1)

    print("Answers:")
    for ans in question_info["answers"]:
        print(
            indent(fill(f"@{ans['name']} -> {ans['content']}"), "   ") + "\n"
        )
        time.sleep(2)
    return input("Do you want to try again? ")


if __name__ == "__main__":
    print(intro)
    time.sleep(2)
    response = ask_question()

    while response.lower() not in {"no", "no."}:
        response = ask_question()
