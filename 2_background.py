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


# 이벤트 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # QUIT : 나가기
            running = False

    screen.fill((100, 100, 245))  # 화면을 같은 색으로 채우기
    # screen.blit(background, (0, 0))  # 배경 그리기(이미지, 이미지의 위치)
    pygame.display.update()  # 화면이 계속해서 나타나게 함. 화면 업데이트

# pygame 종료
pygame.quit()
