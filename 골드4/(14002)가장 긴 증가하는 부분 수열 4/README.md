<h2>14002번: 가장 긴 증가하는 부분 수열 4</h2>
<ul>
  <li>랭크: 골드 4</li>
  <li>참고사항: 가장 긴 증가하는 부분 수열 응용</li>
</ul>
<h2>문제</h2>
<ul>
  <li>수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.</li>
  <li>입력: 첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000)이 주어진다. 둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (1 ≤ Ai ≤ 1,000)</li>
  <li>출력: 첫째 줄에 수열 A의 가장 긴 증가하는 부분 수열의 길이를 출력한다. 둘째 줄에는 가장 긴 증가하는 부분 수열을 출력한다. 그러한 수열이 여러가지인 경우 아무거나 출력한다.</li>
</ul>
<h2>풀이</h2>
<ul>
  <li>가장 긴 증가하는 부분 수열과 동일한 DP를 만든다.</li>
  <li>DP에서 가장 큰 숫자를 찾고, num_list 뒤에서 출발해서 가장 큰 숫자부터 가장 낮은 숫자 순으로 수열을 찾아준다.</li>
</ul>
<h2>팁</h2>
<ul>
  <li>뒤에서부터 카운팅을 하면 숫자가 엉키지 않는다.</li>
</ul>
