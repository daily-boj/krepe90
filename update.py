import datetime as dt
import argparse
import requests
import os

LEVEL_NAME = [
    "UNRATED",

    "Bronze V",
    "Bronze IV",
    "Bronze III",
    "Bronze II",
    "Bronze I",

    "Silver V",
    "Silver IV",
    "Silver III",
    "Silver II",
    "Silver I",

    "Gold V",
    "Gold IV",
    "Gold III",
    "Gold II",
    "Gold I",

    "Platinum V",
    "Platinum IV",
    "Platinum III",
    "Platinum II",
    "Platinum I",

    "Diamond V",
    "Diamond IV",
    "Diamond III",
    "Diamond II",
    "Diamond I",

    "Ruby V",
    "Ruby IV",
    "Ruby III",
    "Ruby II",
    "Ruby I",
]


def get_problem(p_id: int) -> str:
    resp = requests.get(f"https://api.solved.ac/v2/search/problems.json?query={p_id}&page=1")
    resp.raise_for_status()

    data = resp.json()
    if not data.get("success"):
        return "???"
    p = data.get("result", {}).get("problems", [])
    if len(p) < 1:
        return "???"
    else:
        return p[0]


def append_readme(*args):
    with open("README.md", "a", encoding="utf-8") as f:
        for code in args:
            p = get_problem(code)
            title = p.get("title")
            level = p.get("level")

            t_date = dt.date.today()
            t_date_str = str(t_date) if t_date.weekday() < 5 else f"**{t_date}**"
            t_tier_img = f"<img src=\"https://static.solved.ac/tier_small/{level}.svg\" height=\"18px\" alt=\"{LEVEL_NAME[level]}\" title=\"{LEVEL_NAME[level]}\"/>"
            t_problem = f"[{code}. {title}](https://www.acmicpc.net/problem/{code})"
            t_code = "[python](P{code}.py)"
            t_note = ""
            f.write(f"|{t_date_str}|{t_tier_img}|{t_problem}|⬛|{t_code}|{t_note}|\n")
            if os.path.exists(f"P{code}.py"):
                print(f"{LEVEL_NAME[level]:12s} - [{code}. {title}] / code file already exists!!")
                continue
            else:
                with open(f"P{code}.py", "w", encoding="utf-8") as f2:
                    f2.write(f"# https://www.acmicpc.net/problem/{code}\n# {dt.date.today()} / {code}. {title} / {LEVEL_NAME[level]}\n")
                print(f"{LEVEL_NAME[level]:12s} - [{code}. {title}] added!!")


def main():
    pass


if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("number", help="BOJ problem code numbers", type=int, nargs="+")
    args = arg_parser.parse_args()
    append_readme(*args.number)
