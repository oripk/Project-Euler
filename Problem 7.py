"""
ArrayList<Integer> getPrimes(int n){
  ArrayList<Integer> memo = new ArrayList<>();
  memo.add(2);

  for(int i = 2 ; i <= n ; ++i){
    for(int j = 0 ; j < memo.size() ; ++j){
      if(i % memo.get(j) == 0) break; // 소수로 나누어 떨어지면 소수가 아니다.
      if((j + 1) == memo.size()) memo.add(i); // 이전까지의 모든 소수로 나누어 떨어지지 않으면 소수다.
    }
  }
} 시간복잡도 쩜!
"""

def get(num):
    for i in range(2, num):
        if(num % i == 0):
            return False
    return True

array = [2, ]
num = 3
count = 1
while count != 10005:
    if get(num):
        array.append(num)
        print(array.pop(0), count)
        count += 1
    num += 1
