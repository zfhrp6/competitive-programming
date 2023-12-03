use proconio::input;

fn main() {
    input! {
        n: usize,
        p: [usize; n],
    }

    let pc_vec = create_children_list(n, &p);
    for i in 0..n {
        println!("{}", calc_number_of_paper(&i, &pc_vec));
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

fn calc_number_of_paper(idx: &usize, vec: &Vec<Vec<usize>>) -> usize {
    if vec[*idx].is_empty() {
        return 1;
    }

    let mut num = 1;
    for child in &vec[*idx] {
        num += calc_number_of_paper(&child, vec);
    }
    num
}
