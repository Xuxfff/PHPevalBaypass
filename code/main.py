import sys

chars_table = {}
for i in range(10):
    chars_table[str(i)] = f"[{str(i)}...0][0][0]" 
chars_table["."] = "[112345678111111...8][0][20]"
chars_table["E"] = "[112345678111111...8][0][15]"
for i in range(2):
    tmp = chars_table.copy()
    for i in tmp.keys():
        for j in tmp.keys():
            if ord(i)^ord(j) > 32 and chr(ord(i)^ord(j)) not in tmp.keys():
                m = chars_table[i]
                n = chars_table[j]
                chars_table[chr(ord(i)^ord(j))] =  f"{m}^{n}"
def find(s):
    for i in chars_table.keys():
        for j in chars_table.keys():
            if ord(i)^ord(j) == ord(s):
                m = chars_table[i]
                n = chars_table[j]
                return f"[{m}^{n}][0]"
    return None

def exp(command):
    result = []
    for s in command:
        if s in chars_table.keys():
            result.append("[" + chars_table[s] + "][0]")
            continue
        elif s.isalpha() and s.upper() in chars_table.keys():
            result.append("[" + chars_table[s.upper()] + "][0]")
            continue
        else:
            res = find(s)
            if res:
                result.append(res)
                continue
            elif s.isalpha():
                res = find(s.upper())
                if res:
                    result.append(res)
                    continue
            else:
                exit(f"{s} not found!")
    print(".".join(result))

if __name__ == '__main__':
    if(len(sys.argv) < 2):
        exit("[+]Usage: python main.py command")
    command = sys.argv[1]
    exp(command)