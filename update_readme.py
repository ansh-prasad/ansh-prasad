import json

def generate_leetcode_stats_md(stats):
    return f"""
## LeetCode Stats

- **Total Problems Solved:** {stats['totalSolved']}
- **Easy Problems Solved:** {stats['easySolved']}
- **Medium Problems Solved:** {stats['mediumSolved']}
- **Hard Problems Solved:** {stats['hardSolved']}
- **Acceptance Rate:** {stats['acceptanceRate']}
- **Ranking:** {stats['ranking']}
"""

def generate_gfg_stats_md(stats):
    return f"""
## GeeksforGeeks Stats

- **Problems Solved:** {stats['problems_solved']}
- **Coding Score:** {stats['coding_score']}
- **Rank:** {stats['rank']}
"""

if __name__ == "__main__":
    with open("leetcode_stats.json", "r") as f:
        leetcode_stats = json.load(f)

    with open("gfg_stats.json", "r") as f:
        gfg_stats = json.load(f)

    leetcode_stats_md = generate_leetcode_stats_md(leetcode_stats)
    gfg_stats_md = generate_gfg_stats_md(gfg_stats)

    with open("README.md", "r") as f:
        readme = f.read()

    marker_start_leetcode = "<!-- LEETCODE-STATS-START -->"
    marker_end_leetcode = "<!-- LEETCODE-STATS-END -->"
    start_leetcode = readme.find(marker_start_leetcode) + len(marker_start_leetcode)
    end_leetcode = readme.find(marker_end_leetcode)

    marker_start_gfg = "<!-- GFG-STATS-START -->"
    marker_end_gfg = "<!-- GFG-STATS-END -->"
    start_gfg = readme.find(marker_start_gfg) + len(marker_start_gfg)
    end_gfg = readme.find(marker_end_gfg)

    new_readme = (readme[:start_leetcode] + leetcode_stats_md + readme[end_leetcode:start_gfg] + gfg_stats_md + readme[end_gfg:])

    with open("README.md", "w") as f:
        f.write(new_readme)
