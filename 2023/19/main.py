from operator import lt, gt
from copy import deepcopy
from functools import reduce


def parse_data(filename):
    with open(filename) as f:
        rules, input = f.read().split('\n\n')
        rs = {}
        for rule in rules.splitlines():
            name, rule = rule.split('{')
            rule = rule.replace('}', '')
            r = []
            for step in rule.split(','):
                if '<' in step:
                    n, v = step.split('<')
                    v, d = v.split(':')
                    r.append({
                        'name': n,
                        'op': lt,
                        'value': int(v),
                        'dest': d,
                    })
                elif '>' in step:
                    n, v = step.split('>')
                    v, d = v.split(':')
                    r.append({
                        'name': n,
                        'op': gt,
                        'value': int(v),
                        'dest': d,
                    })
                else:
                    r.append(step)
            rs[name] = r

        parts = []
        for part in input.splitlines():
            part = part.replace('{', '').replace('}', '')
            l = {}
            for p in part.split(','):
                k, v = p.split('=')
                l[k] = int(v)

            parts.append(l)

    return rs, parts


def parse_rules(rules, parts, start):
    valid = []
    for part in parts:
        if is_valid_part(part, start, rules):
            valid.append(part)

    return sum(sum(p.values()) for p in valid)


def is_valid_part(part, rulename, rules):
    if rulename == 'A':
        return True
    if rulename == 'R':
        return False
    rule = rules[rulename]
    for r in rule:
        if not isinstance(r, dict):
            continue

        if r['op'](part[r['name']], r['value']):
            return is_valid_part(part, r['dest'], rules)

    return is_valid_part(part, rule[-1], rules)

def eval_rules_recursive(rules):
    intervals = get_intervals('in', rules, {k: [1, 4000] for k in 'xmas'})
    return sum(reduce(lambda x, y: x * y, (j - i + 1 for i, j in interval.values())) for interval in intervals)


def get_intervals(rulename, rules, intervals):
    valid = []
    if rulename == 'A':
        return [intervals]
    if rulename == 'R':
        return valid

    rule = rules[rulename]
    for r in rule:
        if not isinstance(r, dict):
            valid += get_intervals(rule[-1], rules, intervals)
            break

        if r['op'] == gt:
            if intervals[r['name']][0] > r['value']:
                valid += get_intervals(r['dest'], rules, intervals)
                break

            new_intervals = deepcopy(intervals)
            new_intervals[r['name']][0] = r['value'] + 1
            valid += get_intervals(r['dest'], rules, new_intervals)
            intervals[r['name']][1] = r['value']

        if r['op'] == lt:
            if intervals[r['name']][1] < r['value']:
                valid += get_intervals(r['dest'], rules, intervals)
                break

            new_intervals = deepcopy(intervals)
            new_intervals[r['name']][1] = r['value'] - 1
            valid += get_intervals(r['dest'], rules, new_intervals)
            intervals[r['name']][0] = r['value']

    return valid


def eval_rules(rules):
    queue = [('in', {k: [1, 4000] for k in 'xmas'})]
    valid = []
    while queue:
        rulename, intervals = queue.pop(0)
        if rulename == 'A':
            valid.append(intervals)
            continue
        if rulename == 'R':
            continue

        rule = rules[rulename]
        for r in rule:
            if not isinstance(r, dict):
                queue.append((rule[-1], intervals))
                continue

            if r['op'] == gt:
                if intervals[r['name']][0] > r['value']:
                    queue.append((r['dest'], intervals))
                    break

                new_intervals = deepcopy(intervals)
                new_intervals[r['name']][0] = r['value'] + 1
                queue.append((r['dest'], new_intervals))
                intervals[r['name']][1] = r['value']

            if r['op'] == lt:
                if intervals[r['name']][1] < r['value']:
                    queue.append((r['dest'], intervals))
                    break

                new_intervals = deepcopy(intervals)
                new_intervals[r['name']][1] = r['value'] - 1
                queue.append((r['dest'], new_intervals))
                intervals[r['name']][0] = r['value']

    return sum(reduce(lambda x, y: x * y, (j - i + 1 for i, j in interval.values())) for interval in valid)


rules, parts = parse_data('example.txt')
result = parse_rules(rules, parts, 'in')
print(result)
assert result == 19114
result = eval_rules(rules)
print(result)
assert result == 167409079868000
rules, parts = parse_data('input.txt')
result = parse_rules(rules, parts, 'in')
print(result)
result = eval_rules(rules)
print(result)
result = eval_rules_recursive(rules)
print(result)
