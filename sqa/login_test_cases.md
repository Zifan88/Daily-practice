\# Login Page Test Cases



\*\*Module:\*\* Login

\*\*Precondition (all cases):\*\* User is on the login page and has a registered account.



| ID | Test Scenario | Test Steps | Expected Result | Priority |

|----|---------------|------------|-----------------|----------|

| TC01 | Login with valid credentials | 

1\. Enter a valid email<br>

2\. Enter a valid password<br>

3\. Click Login | User is redirected to the dashboard | High |

| TC02 | Login with a wrong password |

&#x20;1. Enter a valid email<br>

2\. Enter an incorrect password<br>

3\. Click Login | An error message is displayed and the user stays on the login page | High |

| TC03 | Login with an unregistered email | 

1\. Enter an unregistered email<br>

2\. Enter any password<br>

3\. Click Login | An error message is displayed and login is denied | High |

| TC04 | Login with empty fields | 

1\. Leave email and password empty<br>

2\. Click Login | "Required field" validation messages are displayed | Medium |

| TC05 | Login with an invalid email format |

&#x20;1. Enter "abc" in the email field (no @)<br>

2\. Enter any password<br>3. Click Login | An invalid email format error is displayed | Medium |

| TC06 | Password field masking |

&#x20;1. Type any text in the password field | Characters are masked (shown as dots) | Low |

