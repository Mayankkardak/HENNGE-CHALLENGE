def main():
    def read_input():
        lines = []
        try:
            n = int(input())
            if n < 1 or n > 100:
                print("Number of test cases must be between 1 and 100.")
                return []
            lines.append(str(n))
            for i in range(n):
                x = input()
                y = input()
                lines.append(x)
                lines.append(y)
        except ValueError:
            print("Invalid input format.")
        return lines

    def process_test_cases(lines, index, remaining, acc):
        if remaining == 0 or index + 1 >= len(lines):
            return acc
        x_line = lines[index]
        y_line = lines[index + 1]
        if not x_line.isdigit():
            return process_test_cases(lines, index + 2, remaining - 1, acc + ["-1"])
        x = int(x_line)
        y_values = y_line.strip().split()
        if len(y_values) != x:
            return process_test_cases(lines, index + 2, remaining - 1, acc + ["-1"])
        result = compute_sum(y_values, 0, 0)
        acc.append(str(result))
        return process_test_cases(lines, index + 2, remaining - 1, acc)

    def compute_sum(vals, i, total):
        if i >= len(vals):
            return total
        try:
            n = int(vals[i])
            if n <= 0:
                total += n ** 4
        except:
            return -1
        return compute_sum(vals, i + 1, total)

    lines = read_input()
    if not lines or not lines[0].isdigit():
        return
    n = int(lines[0])
    output = process_test_cases(lines[1:], 0, n, [])
    
		print('\n')
    print('\n'.join(output))


if __name__ == "__main__":
    main()
