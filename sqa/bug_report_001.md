\# Bug Report



| Field | Details |

|-------|---------|

| \*\*Bug ID\*\* | BUG-001 |

| \*\*Title\*\* | Login succeeds with a wrong password after 3 failed attempts |

| \*\*Module\*\* | Login |

| \*\*Severity\*\* | High |

| \*\*Priority\*\* | High |

| \*\*Status\*\* | Open |

| \*\*Environment\*\* | Windows 11, Chrome 120, Staging server |

| \*\*Reported By\*\* | Your Name |

| \*\*Date\*\* | 2026-11-13 |



\## Description

After three consecutive failed login attempts, the application accepts an incorrect password on the fourth attempt and logs the user in.



\## Preconditions

\- User has a registered account.

\- User is on the login page.



\## Steps to Reproduce

1\. Enter a valid email.

2\. Enter an incorrect password and click Login. Repeat this 3 times.

3\. On the 4th attempt, enter an incorrect password again and click Login.



\## Expected Result

Login is denied and an error message is displayed. The account is temporarily locked after repeated failed attempts.



\## Actual Result

The user is logged in and redirected to the dashboard.



\## Attachments

Screenshot or screen recording (to be added).

