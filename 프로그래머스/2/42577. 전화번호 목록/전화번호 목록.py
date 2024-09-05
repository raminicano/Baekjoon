def solution(phone_book):
    # 전화번호 목록을 사전순으로 정렬
    phone_book.sort() # 이렇게 되면 접두어 관계에 있는 전화번호들을 서로 인접하게됨
    
    # 정렬된 리스트에서 인접한 두 번호만 비교
    for i in range(len(phone_book) - 1):
        # 앞 번호가 뒷 번호의 접두어인지 확인
        if phone_book[i] == phone_book[i + 1][:len(phone_book[i])]:
            return False
    
    return True
