use proconio::input;

fn debug_iv(v: &Vec<isize>) {
    for c in v {
        eprint!("{} ", c);
    }
    eprintln!("");
}

fn debug_uv(v: &Vec<usize>) {
    for c in v {
        eprint!("{} ", c);
    }
    eprintln!("");
}

fn debug(v: &Vec<Vec<usize>>){
    for c in v {
        debug_uv(&c);
        eprintln!("");
    }
    eprintln!("");
}

fn main() {
    input! {
        n: usize,
        p: [usize; n-1],
    }

    let pc_vec = create_children_list(n, &p);
    debug(&pc_vec);
    let mut number_memo: Vec<isize> = vec![-1; n];
    debug_iv(&number_memo);
    for i in 0..n {
        println!("{}", calc_number_of_paper(&i, &pc_vec, &mut number_memo));
    }
}

fn create_children_list(n: usize, p: &[usize]) -> Vec<Vec<usize>> {
    let mut v: Vec<Vec<usize>> = Vec::new();
    for _ in 0..n {
        v.push(Vec::new());
    }
    for (idx, p_id) in p.iter().enumerate() {
        v[*p_id].push(idx);
    }
    v
}

fn calc_number_of_paper(idx: &usize, vec: &Vec<Vec<usize>>, memo: &mut Vec<isize>) -> usize {
    if vec[*idx].is_empty() {
        memo[*idx] = 1;
        return 1;
    }

    if memo[*idx] != -1 {
        return memo[*idx] as usize;
    }

    let mut num = 1;
    for child in &vec[*idx] {
        num += calc_number_of_paper(&child, &vec, memo);
    }
    memo[*idx] = num as isize;
    num
}
