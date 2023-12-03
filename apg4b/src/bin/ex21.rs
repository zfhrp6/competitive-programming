use proconio::input;

fn main() {
    input! {
        a:usize,
        op:char,
        b:usize,
    }

    println!("{}", calc(&a, op, &b));
}

fn calc(a: &usize, op: char, b: &usize) -> String {
    match op {
        '+' => (a + b).to_string(),
        '−' => (a - b).to_string(),
        '∗' => (a * b).to_string(),
        '/' => (a / b).to_string(),
        '?' => "error".to_owned(),
        '=' => "error".to_owned(),
        '!' => "error".to_owned(),
        _ => unimplemented!()
    }
}
