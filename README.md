# prj_ros2_td

### 과제 목적
- ROS2 Humble 실전 활용 능력 평가
- 개발과정에서 ChatGPT 등 AI Agent 활용 가능
- 문서화 및 컨테이너 실행환경 구축 역량 확인

### 필수 기능
- 실시간 센서 데이터 처리
- 장애물 감지 경고
- 설정 가능한 퍼플리시 주기
- Docker 배포지원

### 개발 내용
- 개발환경
  - Ubuntu 22.04
  - visusal studio code
- 기술 스택 :  [![ROS2](https://img.shields.io/badge/ROS2-Humble-blue)]()
[![Python](https://img.shields.io/badge/Python-3.8+-green)]()
[![Docker](https://img.shields.io/badge/Docker-Ready-blue)]()

- 프로젝트 구조 및 설명
  ```
  src/
  ├── sensor_system/                            # ROS2 PKG ROOT
  │   ├── sensor_node.py                        # 센서 데이터 publish 노드
  │   ├── control_node.py                       # 장애물 감지 및 제어 노드
  │   └── launch/
  │      └── sensor_system.launch.py             # 통합 실행 launch 파일 
  ├── Package.xml                                # ROS2 pkg metadata
  ├── setup.py                                   # python package 설정
  └── README.md
  ```

- 실행 방법
  ```bash
  # 기본 실행
  ros2 launch sensor_system sensor_system.launch.py
  
  # 퍼블리시 주기 변경 실행
  ros2 launch sensor_system sensor_system.launch.py publish_interval:=0.5
  ```

### 실행 결과
- 기본실행
<img width="1291" height="759" alt="화면 캡처 2025-07-15 214414" src="https://github.com/user-attachments/assets/ac85f02e-72c1-4982-ac51-46a5383fcd31" />

- 퍼블리시 주기 0.5s 변경하여 실행
<img width="1718" height="838" alt="화면 캡처 2025-07-15 214433" src="https://github.com/user-attachments/assets/1f887d58-8d77-4418-951c-1a125e91e930" />

### Docker 배포 환경
**현재 상태**: 용량 제약으로 실행 테스트 불가 |
**임의 구현 상태**: 배포용 Docker 환경

<details>
<summary>📋 Docker 구성 파일</summary>

#### Dockerfile
```dockerfile
FROM ros:humble-ros-base-jammy

WORKDIR /workspace
COPY src/ /workspace/src/

# 의존성 설치
RUN apt-get update && apt-get install -y \
    python3-colcon-common-extensions \
    && rm -rf /var/lib/apt/lists/*

# 빌드 및 환경 설정
RUN /bin/bash -c "source /opt/ros/humble/setup.bash && colcon build"
ENV ROS_DOMAIN_ID=0

CMD ["ros2", "launch", "sensor_system", "sensor_system.launch.py"]

```

#### docker-compose.yml
```yaml
version: '3.8'
services:
  sensor-system:
    build: .
    environment:
      - ROS_DOMAIN_ID=0
      - PUBLISH_INTERVAL=1.0
    command: >
      bash -c "source /opt/ros/humble/setup.bash && 
               source /workspace/install/setup.bash &&
               ros2 launch sensor_system sensor_system.launch.py 
               publish_interval:=$${PUBLISH_INTERVAL}"
```

#### 배포 실행 방법
```bash# 단일 컨테이너 실행
docker build -t autonomous-robot:latest .
docker run -it --rm autonomous-robot:latest

# Docker Compose 실행
docker-compose up -d
docker-compose logs -f
```
</details>


### AI 도구 활용 내용
#### ChatGPT 활용 부분
- **Launch 파일 작성** (60%): LaunchDescription 문법 및 argument 전달 구조
- **Docker 환경 구성** (80%): 환경 구성 불가로 멀티스테이지 빌 드 및 docker-compose.yml 설정 참고

#### 직접 구현 영역
- **ubuntu 22.04기반 ros2 환경 구성 설정**
- **sensor_node/control_node 생성 로직**
- **pub/sub 메시지 처리**
- **디버깅 및 테스트**
 
