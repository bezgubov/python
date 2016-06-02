#!/usr/bin/env python

fl_dict = {
    "name": {
        "first": "One",
        "last": "Drone"
    },
    "job": "scout",
    "recent": {},
    "additional": {
        "place": {
            "zone": "1",
            "cell": "2"}
    }
}

def flatten(dictionary):
    stack = [((), dictionary)]
    # print 'stack type - ' + str(type(stack))
    # print 'stack data - ' + str(stack)
    result = {}
    while stack:
        path, current = stack.pop()
        for k, v in current.items():
            print 'v - ' + str(type(v))
            print v
            if isinstance(v, dict) and len(v) > 0:
                stack.append((path + (k,), (v)))
            elif isinstance(v, dict) and len(v) == 0:
                result["/".join((path + (k,)))] = ""
            else:
                result["/".join((path + (k,)))] = v
    return result

def main():
    print flatten(fl_dict)

if __name__ == '__main__':
    main()
