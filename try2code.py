import itertools

def evaluate_policy(osa, osb, osc, xdqp, awvp, niqn, wigq, gusq, rtoy):
    if osa and not osb and not osc and not xdqp and not awvp and not (niqn or wigq) and gusq and not (rtoy):
        return True
    else:
        return False

def main():
    attributes = ['OSA', 'OSB', 'OSC', 'XDGP', 'AWVP', 'NIQN', 'WIGQ', 'GUSQ', 'RTOY']
    values = [True, False]
    for combination in itertools.product(values, repeat=len(attributes)):
        evaluated = evaluate_policy(*combination)
        if evaluated:
            print('Found a combination that evaluates to true:')
            print(combination)
            break

if __name__ == '__main__':
    main()
