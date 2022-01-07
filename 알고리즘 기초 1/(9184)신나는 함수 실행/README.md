<h2>9184번: 신나는 함수 실행</h2>
<ul>
  <li>랭크: 실버2</li>
  <li>참고사항: Recursive DP를 활용할 수 있어야 함.</li>
</ul>
<h2>문제</h2>
<ul>
  <li>if a <= 0 or b <= 0 or c <= 0, then w(a, b, c) returns:
    1

if a > 20 or b > 20 or c > 20, then w(a, b, c) returns:
    w(20, 20, 20)

if a < b and b < c, then w(a, b, c) returns:
    w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)

otherwise it returns:
    w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)</li>
  <li>다음과 같은 재귀 함수가 있을 때, a, b, c가 주어지면 w(a, b, c)를 출력하는 프로그램을 작성하라.</li>
  <li>입력: 입력은 세 정수 a, b, c로 이루어져 있으며, 한 줄에 하나씩 주어진다. 입력의 마지막은 -1 -1 -1로 나타내며, 세 정수가 모두 -1인 경우는 입력의 마지막을 제외하면 없다.</li>
  <li>출력: 입력으로 주어진 각각의 a, b, c에 대해서, w(a, b, c)를 출력한다.</li>
  <li>제한: -50 ≤ a, b, c ≤ 50</li>
</ul>
<h2>풀이</h2>
<ul>
  <li>중복 계산을 방지하기 위해 배열에 값을 저장시키고 이를 활용하는 것이 중요하다.</li>
  <li>3차원 배열에 W(a, b, c)의 값을 저장시킨다.</li>
</ul>
<h2>팁</h2>
<ul>
  <li>recursive DP로 피보나치 수열을 푸는 방법과 거의 동일하다.</li>
</ul>
