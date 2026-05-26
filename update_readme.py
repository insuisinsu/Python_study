# update_readme.py
import subprocess
import os

def get_git_logs():
    try:
        # 1. git log를 통해 커밋 해시, 날짜, 커밋 메시지를 가져옵니다.
        log_output = subprocess.check_output(
            ["git", "log", "--pretty=format:%h|%ad|%s", "--date=short"],
            text=True, encoding="utf-8"
        )
        commits = []
        for line in log_output.strip().split("\n"):
            if not line:
                continue
            parts = line.split("|", 2)
            if len(parts) == 3:
                commit_hash, date, subject = parts
                
                # 2. 각 커밋에서 변경된 파일 목록을 가져옵니다.
                files_output = subprocess.check_output(
                    ["git", "diff-tree", "--no-commit-id", "--name-only", "-r", commit_hash],
                    text=True, encoding="utf-8"
                )
                # README.md 자체나 스크립트 파일은 변경 목록에서 제외하여 깔끔하게 만듭니다.
                files = []
                for f in files_output.strip().split("\n"):
                    f = f.strip()
                    if f and f != "README.md" and f != "update_readme.py":
                        files.append(f)
                
                commits.append((date, subject, files))
        return commits
    except Exception as e:
        print(f"Git 로그를 읽는 중 오류 발생: {e}")
        return []

def update_readme():
    readme_path = "README.md"
    if not os.path.exists(readme_path):
        print("README.md 파일이 존재하지 않습니다.")
        return

    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()

    # 특정 마커를 기준으로 윗부분(학습 목차 및 실행법)만 남기고 하단을 자릅니다.
    marker = "## 📅 학습 기록 (Update History)"
    if marker in content:
        content = content.split(marker)[0].strip()
    else:
        content = content.strip() + "\n\n---"

    logs = get_git_logs()
    
    # 새 학습 기록 테이블 생성
    table_lines = [
        f"\n\n{marker}\n",
        "| 날짜 (Date) | 커밋 메시지 (Commit Message) | 변경된 파일 (Modified Files) |",
        "| :--- | :--- | :--- |"
    ]
    
    for date, subject, files in logs:
        # 파일명을 링크나 가독성 좋은 텍스트로 가공
        if files:
            files_str = ", ".join([f"`{f}`" for f in files])
        else:
            files_str = "-"
            
        table_lines.append(f"| {date} | **{subject}** | {files_str} |")

    table_lines.append("\n---\n\n열심히 공부해서 파이썬 마스터가 되어봅시다! 화이팅! 💪🔥\n")
    
    new_content = content + "\n".join(table_lines)
    
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(new_content)
    
    print("README.md 학습 기록이 자동으로 업데이트되었습니다!")

if __name__ == "__main__":
    update_readme()
