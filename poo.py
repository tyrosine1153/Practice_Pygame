import pygame
#####################################
# 0. 기본 초기화 (반드시 해야하는 것들)
pygame.init()

# 화면 크기 설정
screen_width = 480  # 가로
screen_height = 640  # 세로
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 제목 설정
pygame.display.set_caption("게임이름")

# FPS
clock = pygame.time.Clock()  # 시간

background = pygame.image.load("C:/Users/user/PycharmProjects/Pygame/backGround.png")
player = pygame.image.load("C:/Users/user/PycharmProjects/Pygame/player.png")
player_size = player.get_rect().size
player_width = player_size[0]
player_height = player_size[1]
player_x_pos = int(screen_width / 2 - player_width / 2)
player_y_pos = int(screen_height - player_height)


######################################
# 1. 사용자 게임 초기화 (배경화면, 게임 이미지, 좌표, 속도, 폰트 등)


running = True
while running:
    delta = clock.tick(30)  # 게임화면의 초당 프레임 수 지정

    # 2. 이벤트 처리(키보드 함수)
    for event in pygame.event.get():  # 이벤트루프 : 반복 유지, 사용자가 누른 키를 인식
        if event.type == pygame.QUIT:  # QUIT : 나가기
            running = False

        if event.type == pygame.KEYDOWN:
            pass

    # 3. 게임 캐릭터 위치 정의

    # 4. 충돌 처리

    # 5. 화면에 그리기
    screen.blit(background, (0, 0))
    screen.blit(player, (player_x_pos, player_y_pos))

    pygame.display.update()  # 화면이 계속해서 나타나게 함. 화면 업데이트


pygame.quit()