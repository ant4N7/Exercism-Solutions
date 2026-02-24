def response(hey_bob):
    if is_silence(hey_bob):
        return "Fine. Be that way!"
    if is_question(hey_bob) and not is_yelling(hey_bob):
        return "Sure."
    if is_yelling(hey_bob) and not is_question(hey_bob):
        return "Whoa, chill out!"
    if is_yelling(hey_bob) and is_question(hey_bob):
        return "Calm down, I know what I'm doing!"
    return "Whatever."


#A few test functions
def is_silence(hey_bob):
    return hey_bob.isspace() or hey_bob == ""

def is_yelling(hey_bob):
    return hey_bob.isupper()

def is_question(hey_bob):
    return hey_bob.rstrip()[-1] == '?'