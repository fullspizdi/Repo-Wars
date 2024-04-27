import json
import os
from github import Github

# Load configuration
with open('config/test_config.json') as config_file:
    config = json.load(config_file)

# Initialize GitHub client
g = Github(config['github_token'])

# Repository where the competition is taking place
repo = g.get_repo(config['repository_name'])

def update_leaderboard():
    leaderboard = {}
    
    # Fetch all pull requests merged into the main branch
    pulls = repo.get_pulls(state='closed', base='main', sort='created')
    
    for pull in pulls:
        if pull.merged:
            user = pull.user.login
            if user not in leaderboard:
                leaderboard[user] = 0
            # Points for merged pull requests
            leaderboard[user] += config['points']['merged_pull_request']
            
            # Additional points for passing tests
            commits = pull.get_commits()
            for commit in commits:
                statuses = commit.get_statuses()
                for status in statuses:
                    if status.state == 'success':
                        leaderboard[user] += config['points']['passing_tests']
                        break

    # Sort leaderboard by points
    sorted_leaderboard = sorted(leaderboard.items(), key=lambda item: item[1], reverse=True)

    # Update README.md with the new leaderboard
    content_file = repo.get_contents("README.md")
    readme_content = content_file.decoded_content.decode()
    
    # Locate the leaderboard section in the README
    start_marker = "## Leaderboard\n"
    end_marker = "\n##"
    start_idx = readme_content.find(start_marker) + len(start_marker)
    end_idx = readme_content.find(end_marker, start_idx)
    
    # Prepare the new leaderboard content
    leaderboard_content = start_marker
    for user, points in sorted_leaderboard:
        leaderboard_content += f"- {user}: {points} points\n"
    
    # Replace the old leaderboard section with the new one
    new_readme_content = readme_content[:start_idx] + leaderboard_content + readme_content[end_idx:]
    
    # Commit the updated README to the repository
    repo.update_file(content_file.path, "Update leaderboard", new_readme_content, content_file.sha)

if __name__ == "__main__":
    update_leaderboard()
