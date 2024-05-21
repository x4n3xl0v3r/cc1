import sys
import subprocess as sp

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('provide filename with test cases')
        sys.exit(1)

    test_cases_fn = sys.argv[1]
    with open(test_cases_fn, 'r', encoding='utf8') as hf:
        cases: list[str] = list(filter(lambda x: len(x) > 0, map(lambda x: x.strip(), hf.readlines())))

    with open('result.txt', 'w', encoding='utf8') as hf:
        for e, case in enumerate(cases):
            case_parts = case.split(' ')

            args = []
            expected = ''
            for cp_e, cp in enumerate(case_parts):
                if cp.startswith(':'):
                    args = case_parts[:cp_e]
                    expected = ' '.join(case_parts[cp_e:]).replace(':', '')
                    break

            args_string = ' '.join(args)
            try:
                output = sp.check_output(f'triangle {args_string}').decode('1251').strip()
            except sp.CalledProcessError as e:
                output = e.output.decode('1251').strip()

            print(output, expected)
            if output != expected:
                hf.write('error;\n')
            else:
                hf.write('success;\n')
