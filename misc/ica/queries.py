"""
Simple container of integer numbers with queries.
"""
import bisect


def solution(queries):
    container = {}  # Value, Count
    result = []
    for query in queries:
        op = query[0]
        value = int(query[1])  # Always integer
        if op == "ADD":
            container[value] = container.get(value, 0) + 1
            result.append("")
        elif op == "EXISTS":
            result.append("true" if value in container else "false")
        elif op == "REMOVE":
            if value in container:
                container[value] -= 1
                if container[value] == 0:
                    container.pop(value)
                result.append("true")
            else:
                result.append("false")
        else:
            # GET_NEXT
            arr = []
            for v, _ in container.items():
                arr.append(v)
            arr.sort()

            index = bisect.bisect(arr, value)
            if index < len(arr):
                result.append(str(arr[index]))
            else:
                result.append("")

    return result
