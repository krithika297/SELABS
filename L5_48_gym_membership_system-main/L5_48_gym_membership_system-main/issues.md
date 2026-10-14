# Lab 5: Static Code Analysis — Issues and Fixes

The original gym membership program was analyzed using Pylint, Bandit, and Flake8. The following table lists the main issues found and how I fixed them. Line numbers refer to the original program.

| Issue | Type | Line(s) | Description | Fix Approach |
|-------|------|---------|-------------|--------------|
| Shell command execution | Security - High | 58 | os.system() executes a shell command and may introduce command-injection risks. | Removed the shell command and used print() to display the export message. |
| Weak MD5 hash | Security - High | 47 | MD5 is not suitable for security-sensitive hashing. | Replaced MD5 with SHA-256. |
| Unsafe eval() | Security - Medium | 42 | eval() can execute arbitrary Python expressions. | Replaced the expression with a direct renewal-fee calculation and discount validation. |
| Mutable default argument | Code quality | 15 | Using member_log=[] shares the same list between calls. | Changed the default to None and created a new list when needed. |
| Broad exception handling | Security / Code quality | 26 | A bare except hides errors and makes debugging difficult. | Used members.pop(m_id, None) to handle a missing member safely. |
| Hardcoded secret | Security | 70 | A secret stored directly in source code can be exposed. | Read the secret from the GYM_API_SECRET environment variable. |
| Insecure random PIN | Security | 51 | random.randint() is not designed for security-sensitive random values. | Used secrets.randbelow() to generate the PIN. |
| Unused import | Code quality | 6 | The math module was imported but never used. | Removed the unused import. |
| Unused variables | Code quality | 31, 41, 63 | Variables were assigned but not meaningfully used. | Removed unnecessary variables and simplified the active-member count. |
| Incorrect None comparison | Code quality | 32 | Comparing a value to None with == is not the recommended style. | Used is not None through a direct membership-status check. |
| Missing docstrings | Code quality | Multiple | Functions lacked descriptions of their purpose. | Added docstrings to the functions. |
| Function naming | Style | 15, 23, 30, 40 | Function names did not follow snake_case naming conventions. | Renamed the functions to snake_case. |
| File handling | Code quality | 55-57 | The file was opened and closed manually without specifying an encoding. | Used with open(..., encoding="utf-8") for safe file handling. |
| Long lines and indentation | Style | Multiple | Some lines exceeded the style limit and tabs were mixed with spaces. | Reformatted long lines and used consistent spaces for indentation. |
| Missing final newline | Style | 82 | The original file did not end with a newline. | Added a final newline. |

## Final verification

- Pylint: 10.00/10
- Bandit: No issues identified
- Flake8: No issues reported
- Python syntax check: Passed
- Program execution: Passed
