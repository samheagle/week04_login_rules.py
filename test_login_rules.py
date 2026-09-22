from login_rules import is_locked_out, session_expired, risk_level

assert is_locked_out(5, 5) == True
print("PASS: Account locks after 5 attempts")
assert is_locked_out(4, 5) == False
print("PASS: Account isn't locked before 5 attempts")
assert session_expired(10, 5) == True
print("PASS: Account times out after >5 minutes")
assert session_expired(5, 5) == False
print("PASS: Account isn't timed out until >5 minutes have passed")
assert risk_level(6)=="HIGH"
print("PASS: 6 or more attempts provides HIGH rating")
assert risk_level(3)=="MEDIUM"
print("PASS: >3 attempts provides MEDIUM rating")
assert risk_level(0)=="LOW"
print("PASS: <=2 attempts provides LOW rating")
