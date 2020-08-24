import pygame

####################################
# 0. 기본 초기화 (반드시 해야하는 것들)
pygame.init()

# 화면 크기 설정
screen_width = 480  # 가로
screen_height = 640  # 세로
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 제목 설정
pygame.display.set_caption("HelloWorld")

# FPS
clock = pygame.time.Clock()  # 시간
#####################################
# 1. 사용자 게임 초기화 (배경화면, 게임 이미지, 좌표, 속도, 폰트 등)
# 배경이미지를 담은 자료형
background = pygame.image.load("C:/Users/user/PycharmProjects/Pygame/backGround.png")
# 플레이어
player = pygame.image.load("C:/Users/user/PycharmProjects/Pygame/player.png")
player_size = player.get_rect().size  # 이미지의 크기를 구해옴
player_width = player_size[0]  # 캐릭터의 가로 크기
player_height = player_size[1]  # 캐릭터의 세로 크기
player_x_pos = int(screen_width / 2 - player_width / 2)  # 캐릭터위치, x좌표. 화면 가로의 중앙
player_y_pos = int(screen_height - player_height)  # 화면 세로의 가정 아래
# 이동할 좌표
to_x = 0
to_y = 0
# 이동 속도
player_speed = 1

# 적(enemy)
enemy = pygame.image.load("C:/Users/user/PycharmProjects/Pygame/enemy.png")
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = int(screen_width / 2 - enemy_width / 2)
enemy_y_pos = int(screen_height / 2 - enemy_height / 2)

# 폰트 정의
game_font = pygame.font.Font(None, 40)  # 폰트 객체 생성 (폰트, 크기)
# 총 시간
total_time = 10
# 시간 계산
start_ticks = pygame.time.get_ticks()  # 현재 시작 tick 을 받아줌

# 이벤트 루프
running = True
while running:
    delta = clock.tick(60)  # 게임화면의 초당 프레임 수 지정
    print("fps : " + str(clock.get_fps()))  # get_fps() clock 에서 fps 를 가져오는 함수
    # 10 fps : 1초 동안 10번 동작, 20 fps : 1초 동안 20번 동작

    # 2. 이벤트 처리(키보드 함수)
    for event in pygame.event.get():  # 이벤트루프 : 반복 유지, 사용자가 누른 키를 인식
        if event.type == pygame.QUIT:  # QUIT : 나가기
            running = False

        if event.type == pygame.KEYDOWN:  # 키보드 키를 눌렀을때
            if event.key == pygame.K_LEFT:
                to_x -= player_speed
            elif event.key == pygame.K_RIGHT:
                to_x += player_speed
            elif event.key == pygame.K_UP:
                to_y -= player_speed
            elif event.key == pygame.K_DOWN:
                to_y += player_speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    # 3. 게임 캐릭터 위치 정의
    player_x_pos += to_x * delta
    player_y_pos += to_y * delta

    # 경계를 넘어가지 않도록 함
    if player_x_pos < 0:
        player_x_pos = 0
    elif player_x_pos > screen_width - player_width:
        player_x_pos = screen_width - player_width

    if player_y_pos < 0:
        player_y_pos = 0
    elif player_y_pos > screen_height - player_height:
        player_y_pos = screen_height - player_height

    # 4. 충돌 처리
    # 충돌 처리를위한 rect 정보 업데이트 // 이해 조금 안됨
    player_rect = player.get_rect()  # player 가 가진 충돌 정보(좌표, 크기)를 가져와 변수에 담음
    player_rect.left = player_x_pos
    player_rect.top = player_y_pos
    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos
    # 충돌 체크
    if player_rect.colliderect(enemy_rect):  # 충돌을 확인하는 함수
        print("충돌")
        running = False

    # 5. 화면에 그리기
    # 화면 표시
    screen.fill((100, 100, 245))  # 화면을 같은 색으로 채우기
    # screen.blit(background, (0, 0))  # 배경 그리기(이미지, 이미지의 위치)
    screen.blit(player, (player_x_pos, player_y_pos))  # 캐릭터 그리기
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))  # 적 그리기
    # 타이머 집어넣기
    # 경과 시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000  # 경과시간(ms)을 1000으로 나누어서 초(s)단위로 표시
    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255, 255, 255))  # render(출력할거, True, 색상)
    screen.blit(timer, (10, 10))
    # 시간이 0 이하면 게임종료
    if total_time - elapsed_time <= 0:
        print("타임아웃")
        running = False

    pygame.display.update()  # 화면이 계속해서 나타나게 함. 화면 업데이트
# 종료 전 대기
pygame.time.dalay(2000)  # 2초 대기(ms)
# pygame 종료
pygame.quit()
