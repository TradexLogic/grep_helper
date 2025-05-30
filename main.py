#!/usr/bin/env python3
"""
╔════════════════════════════════════════════════════╗
║  🔍 GREP COMMAND GENERATOR SCRIPT                  ║
║  🛠️  Created by: TradexLogic                      ║
║  🌐 GitHub: https://github.com/TradexLogic         ║
║                                                    ║
║  📜 License: For personal or educational use only  ║
║  ❌ Unauthorized reproduction or distribution is   ║
║     strictly prohibited without written consent.   ║
╚════════════════════════════════════════════════════╝
"""

def generate_grep_commands(filename: str, search_term: str) -> list:
    """
    Generate 30 powerful and practical grep commands.
    Developed and curated by TradexLogic.
    """
    return [
        f"grep '{search_term}' {filename}",
        f"grep -i '{search_term}' {filename}  # Case-insensitive search",
        f"grep -n '{search_term}' {filename}  # Show line numbers",
        f"grep -v '{search_term}' {filename}  # Invert match (not matching)",
        f"grep -w '{search_term}' {filename}  # Match whole word",
        f"grep -x '{search_term}' {filename}  # Match whole line",
        f"grep -c '{search_term}' {filename}  # Count of matching lines",
        f"grep -l '{search_term}' {filename}  # Filenames with matches",
        f"grep -L '{search_term}' {filename}  # Filenames without matches",
        f"grep -r '{search_term}' {filename}  # Recursive search",
        f"grep -r -i '{search_term}' {filename}  # Recursive + case-insensitive",
        f"grep -A 3 '{search_term}' {filename}  # 3 lines After match",
        f"grep -B 3 '{search_term}' {filename}  # 3 lines Before match",
        f"grep -C 3 '{search_term}' {filename}  # 3 lines Before & After",
        f"grep --color=auto '{search_term}' {filename}  # Highlight match",
        f"grep -E '{search_term}|anotherword' {filename}  # Extended regex OR",
        f"grep -F '{search_term}' {filename}  # Fixed string",
        f"grep -P '{search_term}' {filename}  # Perl regex (if supported)",
        f"grep --include='*.txt' -r '{search_term}' {filename}  # Only .txt",
        f"grep --exclude='*.log' -r '{search_term}' {filename}  # Skip .log",
        f"grep -R '{search_term}' {filename}  # Recursive (same as -r)",
        f"grep -H '{search_term}' {filename}  # Force filename in output",
        f"grep -h '{search_term}' {filename}  # Hide filename in output",
        f"grep -s '{search_term}' {filename}  # Suppress error messages",
        f"grep -q '{search_term}' {filename}  # Quiet mode (no output)",
        f"grep -Z '{search_term}' {filename}  # Null-separated output",
        f"grep -o '{search_term}' {filename}  # Show only matching parts",
        f"grep -m 5 '{search_term}' {filename}  # Max 5 matches",
        f"grep -b '{search_term}' {filename}  # Show byte offset",
        f"grep --binary-files=text '{search_term}' {filename}  # Binary as text",
    ]

def main():
    print("📁 Welcome to the Grep Command Generator!")
    print("🔧 Developed with ❤️ by TradexLogic (https://github.com/TradexLogic)\n")

    filename = input("📂 Enter the filename or directory to search in: ").strip()
    search_term = input("🔍 What do you want to search for? ").strip()

    commands = generate_grep_commands(filename, search_term)

    print("\n📜 Here are 30 useful grep commands for your search:\n")
    for i, cmd in enumerate(commands, 1):
        print(f"{i:2d}. {cmd}")

    print("\n✅ Copy any command and use it in your terminal.")
    print("🔒 This tool is protected under author rights © TradexLogic\n")

if __name__ == "__main__":
    main()
