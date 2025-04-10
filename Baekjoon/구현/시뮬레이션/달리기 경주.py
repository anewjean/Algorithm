def solution(players, callings):
    player_rank =  {player: rank for rank, player in enumerate(players)}

    for called_player in callings:
        # 호명된 선수의 현재 순위
        current_rank = player_rank[called_player]

        # 앞 선수랑 위치 바꾸기
        players[current_rank], players[current_rank - 1] = players[current_rank - 1], players[current_rank]

        # 선수 순위 업데이트
        player_rank[called_player] = current_rank - 1
        player_rank[player_rank[current_rank]] = current_rank

    return  players

def solution(players, callings):
    for called_player in callings:
        rank = players.index(called_player)
        players.remove(called_player)
        players.insert(rank - 1, called_player)
    return players