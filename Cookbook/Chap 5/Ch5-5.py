##########################################################################################################
# 5.5] 존재하지 않는 파일에 쓰기
#   * 파일이 파일 시스템에 존재하지 않을 때만, 데이터를 파일에 쓰고 싶다.
#    : open()에 w 대신 x 모드를 사용하여 해결할 수 있다.
#
# * 실수로 파일을 덮어쓰는 등의 문제를 우아하게 피해갈 수 있는 좋은 방법이다 ! (파이썬 3 이후 지원)
##########################################################################################################

# s라는 파일이 이미 존재할 경우 에러가 발생한다.
with open('s', 'xt') as f:
    f.write('Hello\n')