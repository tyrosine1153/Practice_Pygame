import pygame

pygame.init()

# 화면 크기 설정
screen_width = 480  # 가로
screen_height = 640  # 세로
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 제목 설정
pygame.display.set_caption("HelloWorld")

# 배경이미지를 담은 자료형
background = pygame.image.load("C:/Users/user/PycharmProjects/Pygame/backGround.png")
# 플레이어
player = pygame.image.load("C:/Users/user/PycharmProjects/Pygame/player.png")
player_size = player.get_rect().size  # 이미지의 크기를 구해옴
player_width = player_size[0]  # 캐릭터의 가로 크기
player_height = player_size[1]  # 캐릭터의 세로 크기
player_x_pos = int(screen_width / 2 - player_width / 2)  # 캐릭터위치, x좌표. 화면 가로의 중앙
player_y_pos = int(screen_height - player_height)  # 화면 세로의 가정 아래


# 이벤트 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # QUIT : 나가기
            running = False

    screen.fill((100, 100, 245))  # 화면을 같은 색으로 채우기
    # screen.blit(background, (0, 0))  # 배경 그리기(이미지, 이미지의 위치)
    screen.blit(player, (player_x_pos, player_y_pos))  # 캐릭터 그리기
    pygame.display.update()  # 화면이 계속해서 나타나게 함. 화면 업데이트

# pygame 종료
pygame.quit()
