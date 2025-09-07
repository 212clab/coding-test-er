def acmicpc11659(datas):
    def solution(N, M, Nrr, Msrr, cnt):
        print(N, M, Nrr, Msrr)
        S = [0]* (N+1)
        for i in range(N):
            S[i+1] = S[i]+Nrr[i]
        # print(S)

        answer = list(map(int, outputs[cnt].split('\n')))
        for i in range(M):
            s, e = list(map(int, Msrr[i].split()))
            my = S[e]-S[s-1]
            print(f"{my} {"CORRECT! " if answer[i]== my else "INCORRECT"}")

    inputs = [datas[i] for i in datas.keys() if i.startswith('input')]
    outputs = [datas[i] for i in datas.keys() if i.startswith('output')]

    # print(inputs)
    cnt = 0
    for inp in inputs:
        lines =  list(inp.split('\n'))
        # print(lines)
        N, M = map(int, lines[0].split())
        Nrr = list(map(int, lines[1].split()))
        Msrr = list(lines[2:])
        solution(N,M,Nrr,Msrr,cnt)
        cnt += 1






def acmicpc2():
    print("Problem 2 solved")
    return "Result 2"