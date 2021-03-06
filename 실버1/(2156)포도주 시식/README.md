<h2>2156번: 포도주 시식</h2>
<ul>
  <li>랭크: 실버1</li>
  <li>참고사항: RGB 문제를 풀 때와 비슷한 접근 방식을 사용한다.</li>
</ul>
<h2>문제</h2>
<ul>
  <li>효주는 포도주 시식회에 갔다. 그 곳에 갔더니, 테이블 위에 다양한 포도주가 들어있는 포도주 잔이 일렬로 놓여 있었다. 효주는 포도주 시식을 하려고 하는데, 여기에는 다음과 같은 두 가지 규칙이 있다.<br>
    포도주 잔을 선택하면 그 잔에 들어있는 포도주는 모두 마셔야 하고, 마신 후에는 원래 위치에 다시 놓아야 한다.<br>
    연속으로 놓여 있는 3잔을 모두 마실 수는 없다.<br>
    효주는 될 수 있는 대로 많은 양의 포도주를 맛보기 위해서 어떤 포도주 잔을 선택해야 할지 고민하고 있다. 1부터 n까지의 번호가 붙어 있는 n개의 포도주 잔이 순서대로 테이블 위에 놓여 있고, 각 포도주 잔에 들어있는 포도주의 양이 주어졌을 때, 효주를 도와 가장 많은 양의 포도주를 마실 수 있도록 하는 프로그램을 작성하시오.</li>
  <li>입력: 첫째 줄에 포도주 잔의 개수 n이 주어진다. (1 ≤ n ≤ 10,000) 둘째 줄부터 n+1번째 줄까지 포도주 잔에 들어있는 포도주의 양이 순서대로 주어진다. 포도주의 양은 1,000 이하의 음이 아닌 정수이다.</li>
  <li>출력: 첫째 줄에 최대로 마실 수 있는 포도주의 양을 출력한다.</li>
</ul>
<h2>풀이</h2>
<ul>
  <li>n=1 또는 n=2일 때는 나온 수를 모두 더한다.</li>
  <li>
    n이 3이상일 때<br>
    i(i>=3)번째 포도주는 마실 수도 있고 안 마실 수도 있다. 마시는 경우는 3가지다. i-2번째는 마시고 i-1번째는 안 마시는 경우, i-2번째는 안 마시고 i-1번째는 마시는 경우, i-2번째와 i-1번째 모두 안 마시는 경우이다. 
    안 마시는 경우도 3가지다. i-2번째는 마시고 i-1번째는 안 마시는 경우, i-2번째는 안 마시고 i-1번째는 마시는 경우, i-2번째와 i-1번째 모두 마시는 경우이다. 이 6가지 경우의 수를 순서대로 dp에 담자.
  </li> 
  <li>i+1번째의 dp를 생각해보자<br>
  dp[0]은 i번째 dp[4]와 dp[5] 중 큰 값에 자신의 값을 더한 것이다.<br>
  dp[1]은 i번째 dp[0]과 dp[2] 중 큰 값에 자신의 값을 더한 것이다.<br>
  dp[2]는 i번째 dp[3]에 자신의 값을 더한 것이다.<br>
  dp[3]은 dp[4]와 dp[5] 중 큰 값이다.<br>
  dp[4]는 dp[0]과 dp[2] 중 큰 값이다.<br>
  dp[5]는 dp[1]이다.
  </li> 
  <li>dp에 있는 값 중 가장 큰 값이 정답이다.</li> 
</ul>
<h2>팁</h2>
<ul>
  <li>단계별로 나올 수 있는 모든 경우의 수로 dp를 만든다.</li>
</ul>
