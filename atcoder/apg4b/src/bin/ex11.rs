use proconio::input;

fn main() {
    input! {
        n: isize,
        a: isize,
    }
    let mut idx = 1;
    let mut calced = a;
    for _ in 0..n {
        input! {
            op: char,
            b: isize,
        }
        let tmp = calc(&calced, op, &b);
        if tmp == "error" {
            println!("{}", tmp);
            std::process::exit(0);
        }
        calced = tmp.parse().unwrap();
        println!("{}:{}", idx, calced);
        idx += 1;
    }
}

fn calc(a: &isize, op: char, b: &isize) -> String {
    match op {
        '+' => (a + b).to_string(),
        '-' => (a - b).to_string(),
        '*' => (a * b).to_string(),
        '/' => {
            if b != &0 {
                (a / b).to_string()
            } else {
                "error".to_owned()
            }
        }
        '?' => "error".to_owned(),
        '=' => "error".to_owned(),
        '!' => "error".to_owned(),
        _ => unimplemented!(),
    }
}
