\# Signup Page Test Cases



\*\*Module:\*\* Signup

\*\*Precondition (all cases):\*\* User is on the signup page and does not already have an account.



| ID | Test Scenario | Test Steps | Expected Result | Priority |

|----|---------------|------------|-----------------|----------|

| TC01 | Signup with valid details |

&#x20;1. Enter a valid name<br>

2\. Enter a valid, unused email<br>

3\. Enter a valid password<br>

4\. Click Sign Up | Account is created and the user is redirected to the dashboard or login page | High |

| TC02 | Signup with an already registered email | 

1\. Enter an email that is already registered<br> 

2\. Fill in other valid details<br>

3\. Click Sign Up | An error message "Email already exists" is displayed and no new account is created | High |

| TC03 | Signup with empty fields |

&#x20;1. Leave all fields empty<br>

2\. Click Sign Up | "Required field" validation messages are displayed | Medium |

| TC04 | Signup with an invalid email format |

&#x20;1. Enter "abc" in the email field (no @)<br>

2\. Fill in other valid details<br>3. Click Sign Up | An invalid email format error is displayed | Medium |

| TC05 | Signup with a weak password |

&#x20;1. Enter a valid email<br>

2\. Enter a short password (e.g., "123")<br>

3\. Click Sign Up | A password strength or minimum length error is displayed | High |

| TC06 | Password and confirm password mismatch |

&#x20;1. Enter a password<br>

2\. Enter a different value in Confirm Password<br>

3\. Click Sign Up | An error message "Passwords do not match" is displayed | Medium |

| TC07 | Password field masking | 

1\. Type any text in the password field | Characters are masked (shown as dots) | Low |

