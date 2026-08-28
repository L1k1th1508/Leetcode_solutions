from pathlib import Path
import re


ROOT = Path(".")
README = ROOT / "README.md"


def get_solutions():
    """
    Find LeetCode problem folders.

    A LeetSync problem is normally represented by a directory
    whose name starts with a LeetCode problem number.
    """

    problems = []

    for folder in ROOT.iterdir():

        if not folder.is_dir():
            continue

        # Ignore GitHub configuration folders
        if folder.name.startswith("."):
            continue

        # Folder should start with a problem number
        match = re.match(r"^(\d+)-(.+)$", folder.name)

        if not match:
            continue

        number = int(match.group(1))
        slug = match.group(2)

        # Look for solution files
        solution_files = []

        for file in folder.rglob("*"):
            if file.is_file() and file.suffix.lower() in [".py", ".c"]:
                solution_files.append(file)

        if not solution_files:
            continue

        # Determine language
        extensions = {file.suffix.lower() for file in solution_files}

        if ".py" in extensions:
            language = "Python"
        elif ".c" in extensions:
            language = "C"
        else:
            language = "Other"

        problems.append({
            "number": number,
            "slug": slug,
            "language": language,
        })

    return sorted(problems, key=lambda x: x["number"])


def format_problem_name(slug):
    """
    Convert:
        two-sum
    into:
        Two Sum
    """

    return slug.replace("-", " ").title()


def generate_table(problems):

    lines = []

    lines.append("| # | Problem | Language |")
    lines.append("|---:|---|---|")

    for problem in problems:

        number = problem["number"]
        name = format_problem_name(problem["slug"])
        language = problem["language"]

        # Link directly to the solution folder
        link = f"[{name}](./{number}-{problem['slug']})"

        lines.append(
            f"| {number} | {link} | {language} |"
        )

    return "\n".join(lines)


def update_readme(problems):

    text = README.read_text(encoding="utf-8")

    total = len(problems)

    python_count = sum(
        p["language"] == "Python"
        for p in problems
    )

    c_count = sum(
        p["language"] == "C"
        for p in problems
    )

    stats = (
        f"**Problems Solved:** {total}\n\n"
        f"**Languages:** 🐍 Python ({python_count}) | "
        f"🔵 C ({c_count})"
    )

    table = generate_table(problems)

    # Replace statistics section
    text = re.sub(
        r"<!-- STATS_START -->.*?<!-- STATS_END -->",
        f"<!-- STATS_START -->\n{stats}\n<!-- STATS_END -->",
        text,
        flags=re.DOTALL,
    )

    # Replace problem table
    text = re.sub(
        r"<!-- PROBLEMS_START -->.*?<!-- PROBLEMS_END -->",
        f"<!-- PROBLEMS_START -->\n\n{table}\n\n<!-- PROBLEMS_END -->",
        text,
        flags=re.DOTALL,
    )

    README.write_text(text, encoding="utf-8")


if __name__ == "__main__":

    problems = get_solutions()

    print(f"Found {len(problems)} LeetCode problems.")

    update_readme(problems)

    print("README updated successfully.")