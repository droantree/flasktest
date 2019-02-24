import json
import random
import string

def do_process(user_query):
    result = {"uq": str(user_query)}
    result_lines = []

    #Enter some random string into first resuilt so we can see a difference
    rand_str = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
    result_lines.append({"type": "doc", "result": rand_str})
    
    for i in range(3):
        result_lines.append({"type": "doc", "result": ("result" + str(i+1))})
    
    result["lines"] = result_lines
    
    return json.dumps(result)

