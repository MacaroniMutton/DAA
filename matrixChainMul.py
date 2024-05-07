def matrix_chain_order(p):
    n = len(p)-1
    m = [[0]*(n+1) for _ in range(n+1)]
    s = [[0]*(n+1) for _ in range(n+1)]
    for l in range(2, n+1):
        for i in range(1, n-l+2):
            j = i+l-1
            m[i][j] = float('inf')
            for k in range(i,j):
                q = m[i][k] + m[k+1][j] + p[i-1]*p[k]*p[j]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k
    return m, s

def print_opt_parens(s, i, j):
    if i==j:
        print(f"A{i}", end="")
    else:
        print("(", end="")
        print_opt_parens(s, i, s[i][j])
        print_opt_parens(s, s[i][j]+1, j)
        print(")", end="")

def main():
    p = [10, 20, 15, 12, 5, 25, 13]
    m, s = matrix_chain_order(p)
    for row in m:
        print(row)
    print("\n")
    for row in s:
        print(row)
    print("\n")
    print_opt_parens(s, 1, len(p)-1)

if __name__=='__main__':
    main()