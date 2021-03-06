T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    weights = list(map(int, input().split()))
    weights.sort()
    
    dad_sum_1 = sum(weights[:K])
    child_sum_1 = sum(weights[K:])
    sum_1 = abs(child_sum_1- dad_sum_1)
    
    dad_sum_2 = sum(weights[0:N-K])
    child_sum_2 = sum(weights[N-K:])
    sum_2 = abs(child_sum_2-dad_sum_2)
    
    print(max(sum_1, sum_2))