function solution(video_len, pos, op_start, op_end, commands) {
    let video_len_real = video_len.split(':')
    let pos_real = pos.split(':')
    let op_start_real = op_start.split(':')
    let op_end_real = op_end.split(':')
    
    video_len_real = (parseInt(video_len_real[0]) * 60) + parseInt(video_len_real[1]);
    pos_real = (parseInt(pos_real[0]) * 60) + parseInt(pos_real[1]);
    op_start_real = (parseInt(op_start_real[0]) * 60) + parseInt(op_start_real[1]);
    op_end_real = (parseInt(op_end_real[0]) * 60) + parseInt(op_end_real[1]);
    
    commands.forEach(function(command) {
        if (pos_real >= op_start_real && pos_real <= op_end_real) {
                pos_real = op_end_real
        }
        
        if (command === 'prev') {
            pos_real = Math.max(0, pos_real - 10)
        }  else if (command === 'next') {
            pos_real += 10
            if (pos_real >= op_start_real && pos_real <= op_end_real) {
                pos_real = op_end_real
            } else if (pos_real > video_len_real) {
                pos_real = video_len_real       
            }
        }
        
        if (pos_real >= op_start_real && pos_real <= op_end_real) {
            pos_real = op_end_real
        }
    })
    
    const forward = Math.floor(pos_real / 60)
    const backward = pos_real % 60
    
    const minutes = String(forward).padStart(2, '0')
    const seconds = String(backward).padStart(2, '0') 
    return `${minutes}:${seconds}`;
}