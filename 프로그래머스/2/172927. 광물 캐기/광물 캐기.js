function solution(picks, minerals) {
    let depth = 0;
    let min = Number.MAX_SAFE_INTEGER;
    let calc = 0;
    const pickList = [];
    
    // 곡괭이 리스트 생성
    for (let i = 0; i < picks.length; i++) {
        for (let j = 0; j < picks[i]; j++) {
            if (picks[i] > 0) {
                pickList.push(i);
            }
        }
    }

    // 깊이 계산 (광물 그룹 수 또는 사용 가능한 곡괭이 수)
    depth = Math.min(Math.ceil(minerals.length / 5), pickList.length);
    
    // 방문 배열 초기화
    const visit = new Array(pickList.length).fill(false);

    // DFS 함수
    function dfs(idx) {
        // 현재 계산값이 최소값 이상이면 중단
        if (calc >= min) return;

        // 깊이에 도달하면 최소값 갱신
        if (idx === depth) {
            min = Math.min(min, calc);
            return;
        }

        // 각 곡괭이 시도
        for (let i = 0; i < pickList.length; i++) {
            if (!visit[i]) {
                // 곡괭이 사용 표시
                visit[i] = true;
                
                // 피로도 계산
                const tmp = fatigue(pickList[i], idx, minerals);
                
                // 피로도 더하고 재귀 호출
                calc += tmp;
                dfs(idx + 1);
                
                // 백트래킹
                visit[i] = false;
                calc -= tmp;
            }
        }
    }

    // 피로도 계산 함수
    function fatigue(num, st, minerals) {
        st = st * 5;
        const range = Math.min(st + 5, minerals.length);
        let sum = 0;

        // 광물별 피로도 계산
        for (let i = st; i < range; i++) {
            switch (minerals[i]) {
                case 'diamond':
                    sum += num === 0 ? 1 : (num === 1 ? 5 : 25);
                    break;
                case 'iron':
                    sum += num === 0 ? 1 : (num === 1 ? 1 : 5);
                    break;
                case 'stone':
                    sum += 1;
                    break;
            }
        }
        return sum;
    }

    // DFS 시작
    dfs(0);
    
    return min;
}