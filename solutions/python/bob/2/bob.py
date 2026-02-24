def response(hey_bob):
    responses = ["Sure.", 
                 "Whoa, chill out!",
                 "Calm down, I know what I'm doing!",
                 "Fine. Be that way!",
                 "Whatever."]
    if is_silence(hey_bob):
        return responses[3]
    if is_question(hey_bob) and not is_yelling(hey_bob):
        return responses[0]
    if is_yelling(hey_bob) and not is_question(hey_bob):
        return responses[1]
    if is_yelling(hey_bob) and is_question(hey_bob):
        return responses[2]
    return responses[4]


#A few test functions
def is_silence(hey_bob):
    return hey_bob.isspace() or hey_bob == ""

def is_yelling(hey_bob):
    return hey_bob.isupper()

def is_question(hey_bob):
    return hey_bob.rstrip()[-1] == '?'