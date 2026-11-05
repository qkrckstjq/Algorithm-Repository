answer = []

def solution(n):

    def hanoi(n, A, B, C):
        global answer; 
        
        if n == 1:
            answer.append([A, C])
        else:
            hanoi(n - 1, A, C, B) #1단계 현재 가장 큰 원반을 움직이기 위한 사전 작업, 목적 = n-1개 원반을 B로
            answer.append([A, C]) #2단계 1단계 완료 후 가장 원반 움직임 A -> C
            hanoi(n - 1, B, A, C) #다시 현재 가장 큰 원반을 움직이기 위해 기둥 조정, 목적 = B를 C로
            
    hanoi(n, 1, 2, 3)
    
    return answer