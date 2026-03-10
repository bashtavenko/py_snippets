def process_commands(commands):
    db = {}
    value_count = {}
    result = []

    for command in commands:
        parts = command.split()


        if not parts:
            continue

        action = parts[0]

        try:
            if action == "SET":
                key, value = parts[1], parts[2]
                # Decrease the count if the key existed
                if key in db:
                    old_value = db[key]
                    value_count[old_value] -= 1
                    if value_count[old_value] == 0:
                        del value_count[old_value]
                db[key] = value
                value_count[value] = value_count.get(value, 0) + 1
            elif action == "GET":
                key = parts[1]
                result.append(db.get(key, "null"))
            elif action == "DELETE":
                key = parts[1]
                if key in db:
                    value = db[key]
                    value_count[value] -= 1
                    if value_count[value] == 0:
                        del value_count[value]
                    del db[key]
            elif action == "COUNT":
                value = parts[1]
                result.append(str(value_count.get(value, 0)))
            else:
                raise ValueError("Invalid command")

        except ValueError:
            result.append("error")

    return result


if __name__ == "__main__":
    print(process_commands([
        "SET a 10",
        "SET b 20",
        "GET a",
        "COUNT 10",
        "DELETE a",
        "INVALID x",
        "GET a"
    ]))
