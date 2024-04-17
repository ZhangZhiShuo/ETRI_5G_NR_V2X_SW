# 📌: ETRI_5G_NR_V2X_SW
> 차세대 차량에 장착될 5G_NR 장비의 통신 성능 검증 SW

</br>

## 1. 제작 기간 & 참여 인원 & 프로젝트 기여도
- 2023년 4월 ~ 11월 (8개월)
- 연구실 용역 프로젝트
- BE 2명/ PM 1명
- BE 기여도 20%

</br>

## 2. 사용 기술
#### 'Back-end'
  - Python 
  - socket
  - numpy
  - serial
#### 'Front-end'
  - PyQT5

</br>

## 3. SW 설계
![시뮬레이터 설계도2](https://github.com/havingforlunch/ETRI_5G_NR_V2X_SW/assets/105187310/76a78bc3-f9f8-4994-915c-923a2239198b)

## 4. 핵심 기능 및 상세 역할
이 SW의 핵심 기능은 Sender의 비디오 데이터와 GPS 정보들을 전송하여 Receiver에서 Sender의 상황을 Receiver가 알 수 있는 것입니다.
또한, T-map API를 사용하여 현 위치의 도로 정보와 날씨 정보에 따른 악조건을 탐지할 수 있습니다.
마지막으로, 통신 장비의 Latency, Throughput, PDR, 차량간 Distance를 실시간으로 확인할 수 있습니다.

### 4.1 GPS 데이터 처리 🛰️
  - GPS 센서를 통해 수신된 데이터에서 위치 정보를 가져오는 코드를 작성했습니다.
![gps 데이터 처리](https://github.com/havingforlunch/ETRI_5G_NR_V2X_SW/assets/105187310/ac887cfc-68bf-4280-bd4a-2e4627281165)

### 4.2 T-map API 데이터 처리 ⛅
  - T-map API에 현재 위치를 기반으로 날씨 정보와 도로 혼잡도 여부를 가져오는 코드를 작성했습니다.
![t-map api 1](https://github.com/havingforlunch/ETRI_5G_NR_V2X_SW/assets/105187310/7954f881-c577-4a7d-bf48-562e8200d458)
  - API로부터 수신된 데이터에서 현재 날씨를 SW에 보이도록 했습니다.
![날씨 정보](https://github.com/havingforlunch/ETRI_5G_NR_V2X_SW/assets/105187310/90859860-368e-49be-beab-5122cd5395eb)

### 4.3 통신 Latency 측정
  - 장비 간 통신 속도를 측정하기 위해 작업을 진행했습니다.
  - 커다란 동영상 데이터, T-map API 데이터 등 다양한 데이터들이 주고받기 때문에, Latency 측정을 위한 매직 넘버를 따로 부여했습니다.
  - 장비 내부에서의 접근이 불가했기 때문에, 외부적으로 연결된 PC에서 측정했습니다.
  - 작동 원리는 Receiver에서 Sender에게 전송하고, Receiver가 Sender로부터 받은 시간들을 통해 Latency를 계산했습니다.
  - 왕복 Latency이기 때문에 최종적으로는 2로 나누었습니다.
  - 또한, 작성한 코드를 일반적으로 바로 보여드리지 않고 문제와 데이터 분석을 통해 자료를 남겨놓습니다.
![슬라이드7](https://github.com/havingforlunch/ETRI_5G_NR_V2X_SW/assets/105187310/e16023b2-01ca-4a07-a3b4-2f8c436d3d47)
![슬라이드8](https://github.com/havingforlunch/ETRI_5G_NR_V2X_SW/assets/105187310/bfb3c6ab-0705-4934-9e02-27c60297b017)
 
## 5. 프로젝트 결과
![SW 결과](https://github.com/havingforlunch/ETRI_5G_NR_V2X_SW/assets/105187310/d134f1e9-fd2a-4b39-bcd9-b03388cdb175)
