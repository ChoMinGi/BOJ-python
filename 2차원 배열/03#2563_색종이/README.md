총 100*100의 도화지에 10*10인 검은 사각형들이 놓여지는 경우이므로 for문을 이중으로 여러번 반복해도 지연시간이나 소요되는 시간이 적다.

따라서 100을 두번 이중 리스트를 통해 2차원의 표를 만들어놓고 검은색 색종이가 놓이는 부분을 =1 로 표현을 하여 나중에 전체합을 구하게 하였다.

이때 이중 리스트문에서의 안쪽 리스트까지의 전체합의 표현법은 sum(map(sum, 리스트명)) 형태로 표기한다.
