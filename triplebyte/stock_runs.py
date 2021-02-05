
def stock_runs(prices):
    diff = [ y - x for x, y in zip(prices[:-1], prices[1:])]
    print(diff)
    max_run = 0
    current_run = 0
    prev = 'same'
    for d in diff:
        print(current_run)
        if d < 0:
            if prev == 'fell':
                current_run += 1
            else:
                prev = 'fell'
                current_run = 2
        elif d > 0:
            if prev == 'rose':
                current_run += 1
            else:
                prev = 'rose'
                current_run = 2
        else:
            prev = 'same'
            current_run = 0
        
        if current_run > max_run:
            max_run = current_run
    return max_run
        

if __name__ == '__main__':
    print(stock_runs([1,2,3]))
    print(stock_runs([2,3,4,3,2,1]))
    print(stock_runs([1]))