# -*- coding: utf-8 -*-
import sys

if len(sys.argv) is 1:
	print >> sys.stderr, '읽을 파일명을 입력해 주세요'
	exit(1)

# 명령행 옵션으로 지정한 파일명 얻기
fname = sys.argv[1]



# 파일 내용을, 일 바이트씩 읽어서 화면에 16진수로 출력하기
try:
  FH = open(fname, 'rb')  # 파일 열기

  while True:
    s = FH.read(128)
    if s == '': break
    print '%02X' % int(ord(s)),  # 1바이트씩 출력


  FH.close()  # 파일 닫기
except IOError:
  print >> sys.stderr, '파일을 열 수 없습니다.'
