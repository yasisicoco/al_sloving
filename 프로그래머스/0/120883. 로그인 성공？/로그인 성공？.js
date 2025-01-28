function solution(id_pw, db) {
    const [id, pw] = [...id_pw]
    let id_check = false
    let pw_check = false
    for (let idpw of db) {
        const [db_id, db_pw] = [...idpw]
        if (id === db_id) {
            id_check = true
            if (pw === db_pw) {
            pw_check = true
            }
        }
    }
    
    if (id_check === true) {
        if (pw_check === true) {
            return 'login'
        } else {
            return 'wrong pw'
        }
    } else {
        return 'fail'
    }
}