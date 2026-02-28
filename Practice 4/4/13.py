import json, re

data = json.loads(input())
q = int(input())

token_re = re.compile(r'([A-Za-z_]\w*)|\[(\d+)\]')

for _ in range(q):
    query = input().strip()
    cur = data
    ok = True

    for key, idx in token_re.findall(query):
        if key:  # .key
            if isinstance(cur, dict) and key in cur:
                cur = cur[key]
            else:
                ok = False
                break
        else:    # [index]
            i = int(idx)
            if isinstance(cur, list) and 0 <= i < len(cur):
                cur = cur[i]
            else:
                ok = False
                break

    if ok:
        print(json.dumps(cur, separators=(",", ":"), ensure_ascii=False))
    else:
        print("NOT_FOUND")