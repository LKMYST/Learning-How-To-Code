import json
import re

input_file = open(r"D:\VSCode Workplace\CND3101\projects\redo_activity6\data\people.txt", "r")
output_file = open(r"D:\VSCode Workplace\CND3101\projects\redo_activity6\data\people.json", "w")

read_pattern = r"(\w+):\s*(.*)"
# (\w+) -> name
# \s*   -> possible spaces
# (.*)  -> friends

result = []

while True:
    line = input_file.readline()    # read a line
    if not line.strip():    # if not has next (line == "")
        break               # break from loop

    match_object = re.match(read_pattern, line)

    if match_object:
        name = match_object.group(1)
        friends = match_object.group(2)

        friend_list = [f.strip() for f in friends.split(',') if f.strip()]
        # same as below
        # friend_list = []
        # for f in friends.split(','):
        #     f = f.strip()
        #     if f:
        #         friend_list.append(f)
        
        # write_pattern = f'{{"name": "{name}", "knows": {json.dumps(friend_list)}}}'
        
        result.append({
            "name": name,
            "knows": friend_list
        })

output_file.writelines(json.dumps(result, indent=2))

input_file.close()
output_file.close()