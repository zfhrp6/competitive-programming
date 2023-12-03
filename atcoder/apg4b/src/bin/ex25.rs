use proconio::input;
use std::collections::HashSet;

fn main() {
    input! {
        n: usize,
        a: [usize;n],
        m: usize,
        b: [usize;m],
        com: String,
    }
    let mut xx = 0;

    if com == "subtract" {
        input! {
            x: usize,
        }
        xx = x;
    }

    let a: HashSet<usize> = a.iter().cloned().collect();
    let b: HashSet<usize> = b.iter().cloned().collect();
    match &com as &str {
        "intersection" => to_string(&intersection(&a, &b)),
        "union_set" => to_string(&union_set(&a, &b)),
        "symmetric_diff" => to_string(&symmetric_diff(&a, &b)),
        "subtract" => to_string(&subtract(&a, &xx)),
        "increment" => to_string(&increment(a)),
        "decrement" => to_string(&decrement(a)),
        _ => unimplemented!(),
    }
}

fn to_string(a: &HashSet<usize>) {
    let n = &a.len();
    let mut v: Vec<usize> = a.iter().clone().map(|x| *x).collect();
    eprintln!("{:?}", v);
    v.sort();
    eprintln!("{:?}", v);
    let mut idx = 0;
    if v.len() == 0{
        println!("");
        return;
    }
    for c in v {
        print!("{}", c);
        if idx != n - 1 {
            print!(" ");
        }
        idx += 1;
    }
    println!("");
}

fn intersection(a: &HashSet<usize>, b: &HashSet<usize>) -> HashSet<usize> {
    a.intersection(b).cloned().collect()
}

fn union_set(a: &HashSet<usize>, b: &HashSet<usize>) -> HashSet<usize> {
    a.union(b).cloned().collect()
}
fn symmetric_diff(a: &HashSet<usize>, b: &HashSet<usize>) -> HashSet<usize> {
    a.symmetric_difference(b).cloned().collect()
}
fn subtract(a: &HashSet<usize>, x: &usize) -> HashSet<usize> {
    let mut r = a.clone();
    r.remove(x);
    r
}

fn increment(a: HashSet<usize>) -> HashSet<usize> {
    let mut r: HashSet<usize> = HashSet::new();
    fn inner_inc(n: &usize) -> usize {
        if n == &49 {
            0
        } else {
            n + 1
        }
    }
    for e in a {
        r.insert(inner_inc(&e));
    }
    r
}
fn decrement(a: HashSet<usize>) -> HashSet<usize> {
    let mut r: HashSet<usize> = HashSet::new();
    fn inner_dec(n: &usize) -> usize {
        if n == &0 {
            49
        } else {
            n - 1
        }
    }
    for e in a {
        r.insert(inner_dec(&e));
    }
    r
}
