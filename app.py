import re

def fix_linkedin_text(text):
    """
    Automates the insertion of invisible characters into empty lines to prevent linkedin parser from collapsing paragraphs.
    """
    # Pattern looks for empty lines or lines with only whitespace and replaces them with invisisble characters
    invisible_char = '\u2800' # Zero-width space character

    # regex: ^\s*$ matches a line that is empty or only has whitespace
    fixed_text = re.sub(r'^\s*$', invisible_char, text, flags=re.MULTILINE)

    return fixed_text

if __name__ == "__main__":
    linkedin_about_me = """software engineer with a passion for developing innovative programs that expedite the efficiency and effectiveness of organizational success.

Well-versed in technology and writing code to create systems that are reliable and user-friendly.

Skilled leader who has the proven ability to motivate, educate, and manage a team of professionals to build software programs and effectively track changes."""

    fixed_text = fix_linkedin_text(linkedin_about_me)

    print(f"Original Text:{repr(linkedin_about_me)}")
    print(f"Fixed Text:{repr(fixed_text)}")
    print(fixed_text)
